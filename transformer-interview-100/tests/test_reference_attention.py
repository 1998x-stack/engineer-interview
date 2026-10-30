import sys
from pathlib import Path

import pytest
import torch
import torch.nn.functional as F

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from examples.reference_attention import ReferenceMHA, causal_mask


def test_shape_and_finite():
    model = ReferenceMHA(32, 4).eval()
    y = model(torch.randn(2, 7, 32), causal_mask(7))
    assert y.shape == (2, 7, 32)
    assert torch.isfinite(y).all()


def test_causal_prefix_invariance():
    torch.manual_seed(0)
    model = ReferenceMHA(32, 4).eval()
    original = torch.randn(1, 8, 32)
    changed = original.clone()
    changed[:, 5:] = torch.randn_like(changed[:, 5:])
    y1 = model(original, causal_mask(8))
    y2 = model(changed, causal_mask(8))
    torch.testing.assert_close(y1[:, :5], y2[:, :5], atol=1e-5, rtol=1e-5)


@pytest.mark.parametrize("mask_form", ["none", "2d", "3d", "4d_broadcast", "4d_heads"])
def test_matches_pytorch_sdpa(mask_form):
    torch.manual_seed(11)
    batch, length, width, heads = 2, 6, 24, 3
    model = ReferenceMHA(width, heads).eval()
    x = torch.randn(batch, length, width)
    keep = causal_mask(length)
    if mask_form == "none":
        supplied, expected_keep = None, None
    elif mask_form == "2d":
        supplied, expected_keep = keep[0, 0], keep
    elif mask_form == "3d":
        supplied, expected_keep = keep[0, 0].expand(batch, -1, -1), keep
    elif mask_form == "4d_broadcast":
        supplied, expected_keep = keep, keep
    else:
        supplied = keep.expand(batch, heads, -1, -1).clone()
        supplied[0, 0, 3:, 0] = False
        expected_keep = supplied

    q, k, v = model.qkv(x).chunk(3, -1)
    q, k, v = [z.reshape(batch, length, heads, width // heads).transpose(1, 2) for z in (q, k, v)]
    expected = F.scaled_dot_product_attention(q, k, v, attn_mask=expected_keep, dropout_p=0.0)
    expected = model.out(expected.transpose(1, 2).contiguous().reshape(batch, length, width))
    torch.testing.assert_close(model(x, supplied), expected, atol=2e-6, rtol=2e-6)


def test_gradients_finite():
    model = ReferenceMHA(16, 4)
    x = torch.randn(2, 4, 16, requires_grad=True)
    model(x, causal_mask(4)).square().mean().backward()
    assert x.grad is not None and torch.isfinite(x.grad).all()
    assert all(p.grad is not None and torch.isfinite(p.grad).all() for p in model.parameters())


def test_batch_specific_mask_controls_only_its_batch():
    model = ReferenceMHA(16, 4).eval()
    x = torch.randn(2, 4, 16)
    mask = causal_mask(4).expand(2, -1, -1, -1).clone()
    mask[1, :, -1, 0] = False
    baseline = model(x, causal_mask(4))
    changed = model(x, mask)
    torch.testing.assert_close(changed[0], baseline[0])
    torch.testing.assert_close(changed[1, :-1], baseline[1, :-1])
    assert not torch.allclose(changed[1, -1], baseline[1, -1])


@pytest.mark.parametrize("bad_mask", [
    torch.zeros((4, 4), dtype=torch.bool),
    torch.tensor([[True, False, False, False], [True, True, False, False], [False, False, False, False], [True, True, True, True]]),
])
def test_rejects_fully_masked_query_rows(bad_mask):
    with pytest.raises(ValueError, match="at least one unmasked key"):
        ReferenceMHA(16, 4)(torch.randn(2, 4, 16), bad_mask)


@pytest.mark.parametrize("bad_mask", [
    torch.ones(4, 4),
    torch.ones(1, 4, 4, 1, dtype=torch.bool),
    torch.ones(3, 4, 4, dtype=torch.bool),
    torch.ones(2, 2, 4, 4, dtype=torch.bool),
    torch.ones(2, 4, dtype=torch.bool),
])
def test_rejects_invalid_mask_shape_or_type(bad_mask):
    with pytest.raises((TypeError, ValueError)):
        ReferenceMHA(16, 4)(torch.randn(2, 4, 16), bad_mask)


@pytest.mark.parametrize("d_model,heads", [(0, 1), (8, 0), (8, 3), (-8, 2), (True, 1)])
def test_rejects_invalid_constructor_arguments(d_model, heads):
    with pytest.raises(ValueError):
        ReferenceMHA(d_model, heads)


@pytest.mark.parametrize("shape", [(2, 0, 16), (0, 3, 16), (2, 3, 17), (2, 16)])
def test_rejects_invalid_input_shape(shape):
    with pytest.raises(ValueError):
        ReferenceMHA(16, 4)(torch.randn(*shape))


@pytest.mark.parametrize("length", [0, -1, 2.2, True])
def test_causal_mask_rejects_invalid_length(length):
    with pytest.raises(ValueError):
        causal_mask(length)
