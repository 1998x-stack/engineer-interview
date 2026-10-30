"""Independent correctness checks for the teaching examples in geometry_ops."""
import sys
from pathlib import Path

import pytest
import torch
import torch.nn.functional as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from examples.geometry_ops import batch_iou, bn2d_train, nms


def box(x1, y1, x2, y2):
    return [float(x1), float(y1), float(x2), float(y2)]


def scalar_iou(a, b):
    # Independent, scalar intersection/union oracle.
    width = max(0., min(a[2], b[2]) - max(a[0], b[0]))
    height = max(0., min(a[3], b[3]) - max(a[1], b[1]))
    intersection = width * height
    area1 = (a[2] - a[0]) * (a[3] - a[1])
    area2 = (b[2] - b[0]) * (b[3] - b[1])
    union = area1 + area2 - intersection
    return intersection / union if union > 0 else 0.


@pytest.mark.parametrize(("a", "b", "expected"), [
    (box(0, 0, 2, 2), box(0, 0, 2, 2), 1.0),
    (box(0, 0, 2, 2), box(1, 1, 3, 3), 1.0 / 7),
    (box(-2, -2, 0, 0), box(1, 1, 3, 3), 0.0),
    (box(0, 0, 0, 2), box(0, 0, 0, 2), 0.0),
    (box(0, 0, 2, 2), box(2, 0, 4, 2), 0.0),
])
def test_iou_known_cases(a, b, expected):
    actual = batch_iou(torch.tensor([a]), torch.tensor([b]))
    torch.testing.assert_close(actual, torch.tensor([[expected]]), atol=1e-7, rtol=1e-6)


def test_iou_empty_inputs():
    assert batch_iou(torch.empty(0, 4), torch.zeros(3, 4)).shape == (0, 3)
    assert batch_iou(torch.empty(3, 4), torch.empty(0, 4)).shape == (3, 0)
    assert batch_iou(torch.empty(0, 4), torch.empty(0, 4)).shape == (0, 0)


def test_iou_scalar_oracle_random():
    generator = torch.Generator().manual_seed(23)
    aa = torch.randn((9, 2), generator=generator, dtype=torch.float64)
    bb = torch.randn((7, 2), generator=generator, dtype=torch.float64)
    a = torch.cat([aa, aa + torch.rand((9, 2), generator=generator, dtype=torch.float64) * 3], 1)
    b = torch.cat([bb, bb + torch.rand((7, 2), generator=generator, dtype=torch.float64) * 3], 1)
    actual = batch_iou(a, b)
    oracle = torch.tensor([[scalar_iou(x.tolist(), y.tolist()) for y in b] for x in a], dtype=torch.float64)
    torch.testing.assert_close(actual, oracle, atol=1e-12, rtol=1e-12)
    torch.testing.assert_close(actual, batch_iou(b, a).T, atol=1e-12, rtol=1e-12)


def test_iou_small_boxes_do_not_lose_ratio_to_epsilon():
    tiny = torch.tensor([[0., 0., 1e-6, 1e-6]], dtype=torch.float64)
    torch.testing.assert_close(batch_iou(tiny, tiny), torch.ones(1, 1, dtype=torch.float64))


@pytest.mark.parametrize("wrong", [
    torch.tensor([[2., 0., 1., 1.]]),
    torch.tensor([[0., 0., float("nan"), 1.]]),
    torch.tensor([[0., 0., float("inf"), 1.]]),
    torch.zeros(2, 3),
    torch.zeros(2, 4, dtype=torch.int64),
])
def test_iou_rejects_invalid_boxes(wrong):
    with pytest.raises((ValueError, TypeError)):
        batch_iou(wrong, torch.zeros(1, 4))


def test_nms_suppression_and_ties():
    boxes = torch.tensor([
        box(0, 0, 2, 2), box(0, 0, 2, 2), box(3, 3, 5, 5), box(3, 3, 5, 5)
    ])
    scores = torch.tensor([0.8, 0.8, 0.9, 0.1])
    assert nms(boxes, scores) == [2, 0]
    assert nms(boxes, scores, iou_thr=1.0) == [2, 0, 1, 3]


def test_nms_empty_and_touching_boxes():
    assert nms(torch.empty(0, 4), torch.empty(0)) == []
    boxes = torch.tensor([box(0, 0, 2, 2), box(2, 0, 4, 2)])
    assert nms(boxes, torch.tensor([0.3, 0.2]), iou_thr=0.0) == [0, 1]


@pytest.mark.parametrize("invalid_thr", [-0.1, 1.1, float("nan"), float("inf")])
def test_nms_invalid_threshold(invalid_thr):
    with pytest.raises(ValueError):
        nms(torch.zeros(1, 4), torch.tensor([1.0]), invalid_thr)


def test_nms_invalid_scores():
    with pytest.raises(ValueError):
        nms(torch.zeros(1, 4), torch.tensor([float("nan")]))
    with pytest.raises(ValueError):
        nms(torch.zeros(2, 4), torch.tensor([1.0]))


def test_bn_matches_pytorch_functional_and_backprop():
    torch.manual_seed(7)
    x = torch.randn(4, 3, 3, 2, dtype=torch.float64, requires_grad=True)
    gamma = torch.randn(3, dtype=torch.float64, requires_grad=True)
    beta = torch.randn(3, dtype=torch.float64, requires_grad=True)
    y, mean, var = bn2d_train(x, gamma, beta)
    expected = F.batch_norm(x, None, None, gamma, beta, training=True, eps=1e-5)
    torch.testing.assert_close(y, expected, atol=1e-12, rtol=1e-12)
    torch.testing.assert_close(mean.flatten(), x.mean((0, 2, 3)), atol=1e-12, rtol=1e-12)
    torch.testing.assert_close(var.flatten(), x.var((0, 2, 3), unbiased=False), atol=1e-12, rtol=1e-12)
    g1 = torch.autograd.grad(y.square().sum(), (x, gamma, beta), retain_graph=True)
    g2 = torch.autograd.grad(expected.square().sum(), (x, gamma, beta))
    for a, b in zip(g1, g2):
        torch.testing.assert_close(a, b, atol=1e-10, rtol=1e-10)


def test_bn_rejects_unsupported_single_value_and_shape():
    with pytest.raises(ValueError):
        bn2d_train(torch.ones(1, 2, 1, 1), torch.ones(2), torch.zeros(2))
    with pytest.raises(ValueError):
        bn2d_train(torch.ones(2, 2, 1, 1), torch.ones(3), torch.zeros(2))
    with pytest.raises(ValueError):
        bn2d_train(torch.ones(2, 2, 1, 1), torch.ones(2), torch.zeros(2), 0.0)
