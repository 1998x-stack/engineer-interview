"""Numerical oracle, invariance and input-contract tests for NLP interview references."""
import sys
from pathlib import Path

import pytest
import torch
import torch.nn.functional as F

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from examples.nlp_reference import (
    stable_softmax, reference_attention, nearest_neighbors,
    reciprocal_rank_fusion, recall_at_k, reciprocal_rank
)


@pytest.mark.parametrize("shape,dim", [((3, 5), -1), ((2, 3, 4), 1), ((4,), 0)])
def test_softmax_matches_torch(shape, dim):
    torch.manual_seed(4)
    x = torch.randn(shape, dtype=torch.float64, requires_grad=True) * 1200
    actual = stable_softmax(x, dim)
    oracle = torch.softmax(x, dim=dim)
    torch.testing.assert_close(actual, oracle, rtol=1e-12, atol=1e-12)
    grad_a = torch.autograd.grad(actual.square().sum(), x, retain_graph=True)[0]
    grad_b = torch.autograd.grad(oracle.square().sum(), x)[0]
    torch.testing.assert_close(grad_a, grad_b, atol=1e-12, rtol=1e-12)


def test_softmax_mask_and_extreme_logits():
    x = torch.tensor([[10000., -10000., 5.], [3., 3., 3.]], dtype=torch.float64)
    mask = torch.tensor([[True, False, True], [False, True, True]])
    actual = stable_softmax(x, keep=mask)
    expected = torch.softmax(x.masked_fill(~mask, float("-inf")), dim=-1)
    torch.testing.assert_close(actual, expected)
    assert torch.isfinite(actual).all()
    torch.testing.assert_close(actual.sum(-1), torch.ones(2, dtype=torch.float64))


@pytest.mark.parametrize("bad", [
    torch.tensor([[False, False]]),
    torch.tensor([[1, 0]]),
    torch.tensor([True, False]),
])
def test_softmax_invalid_masks(bad):
    with pytest.raises(ValueError):
        stable_softmax(torch.tensor([[1., 2.]]), keep=bad)


@pytest.mark.parametrize("bad", [
    torch.tensor([float("nan")]),
    torch.tensor([float("inf")]),
    torch.empty(0),
    torch.ones(2, dtype=torch.int64),
])
def test_softmax_bad_input(bad):
    with pytest.raises(ValueError):
        stable_softmax(bad)


@pytest.mark.parametrize("causal", [True, False])
def test_attention_matches_sdpa_and_gradients(causal):
    torch.manual_seed(17)
    q = torch.randn(2, 3, 4, 8, dtype=torch.float64, requires_grad=True)
    k = torch.randn(2, 3, 4, 8, dtype=torch.float64, requires_grad=True)
    v = torch.randn(2, 3, 4, 8, dtype=torch.float64, requires_grad=True)
    mask = torch.tensor([[True, True, True, True], [True, True, False, False]])
    visible = mask[:, None, None, :]
    if causal:
        visible = visible & torch.ones(4, 4, dtype=torch.bool).tril()[None, None, :, :]
    actual = reference_attention(q, k, v, causal=causal, key_padding_mask=mask)
    expected = F.scaled_dot_product_attention(q, k, v, attn_mask=visible, dropout_p=0.)
    torch.testing.assert_close(actual, expected, rtol=1e-11, atol=1e-11)
    ga = torch.autograd.grad(actual.square().sum(), (q, k, v), retain_graph=True)
    gb = torch.autograd.grad(expected.square().sum(), (q, k, v))
    for a, b in zip(ga, gb):
        torch.testing.assert_close(a, b, rtol=1e-10, atol=1e-10)


def test_attention_decode_suffix_matches_full_causal():
    torch.manual_seed(7)
    q, k, v = [torch.randn(1, 2, 6, 4) for _ in range(3)]
    full = reference_attention(q, k, v, causal=True)
    suffix = reference_attention(q[:, :, -2:, :], k, v, causal=True)
    torch.testing.assert_close(suffix, full[:, :, -2:, :])


def test_attention_future_leakage_is_blocked():
    torch.manual_seed(23)
    q, k, v = [torch.randn(1, 2, 5, 6) for _ in range(3)]
    original = reference_attention(q, k, v, causal=True)
    k[:, :, -1, :] += 100
    v[:, :, -1, :] -= 50
    changed = reference_attention(q, k, v, causal=True)
    torch.testing.assert_close(original[:, :, :-1], changed[:, :, :-1])


def test_attention_rejects_no_visible_key_and_invalid_shape():
    q = torch.zeros(1, 2, 3, 4)
    with pytest.raises(ValueError, match="no visible keys"):
        reference_attention(q, q, q, key_padding_mask=torch.zeros(1, 3, dtype=torch.bool))
    with pytest.raises(ValueError, match="key_padding_mask"):
        reference_attention(q, q, q, key_padding_mask=torch.ones(3, 3, dtype=torch.bool))
    with pytest.raises(ValueError, match="length"):
        reference_attention(q, q[:, :, :2], q[:, :, :2], causal=True)


def test_nearest_neighbors_scalar_oracle_and_blocking():
    torch.manual_seed(5)
    corpus = torch.randn(23, 6, dtype=torch.float64)
    queries = torch.randn(7, 6, dtype=torch.float64)
    brute = torch.stack([((corpus - row) ** 2).sum(-1).argmin() for row in queries])
    for block_size in (1, 3, 8, 1024):
        torch.testing.assert_close(nearest_neighbors(queries, corpus, block_size=block_size), brute)


def test_nearest_neighbors_ties_and_empty_queries():
    x = torch.tensor([[0., 0.], [0., 0.], [1., 1.]])
    q = torch.tensor([[0., 0.], [1., 1.]])
    assert nearest_neighbors(q, x, block_size=1).tolist() == [0, 2]
    assert nearest_neighbors(torch.empty(0, 2), x).numel() == 0


@pytest.mark.parametrize("queries,corpus", [
    (torch.zeros(2, 3), torch.zeros(1, 4)),
    (torch.zeros(2, 3), torch.zeros(0, 3)),
    (torch.ones(2, 3, dtype=torch.int32), torch.zeros(4, 3)),
])
def test_nearest_neighbors_invalid(queries, corpus):
    with pytest.raises(ValueError):
        nearest_neighbors(queries, corpus)


def test_rrf_rank_order_and_deduplication():
    result = reciprocal_rank_fusion([["A", "B", "A"], ["B", "A"]], k=1)
    assert [x[0] for x in result] == ["A", "B"]
    assert result[0][1] == pytest.approx(1 / 2 + 1 / 3)
    assert result[1][1] == pytest.approx(1 / 3 + 1 / 2)
    assert result == reciprocal_rank_fusion([["A", "B", "A"], ["B", "A"]], k=1)


def test_rrf_duplicate_within_single_list_not_double_counted():
    assert reciprocal_rank_fusion([["x", "x"]], k=60) == [("x", 1 / 61)]
    assert reciprocal_rank_fusion([], k=60) == []


def test_retrieval_metrics_known_values():
    relevant = {"a", "b", "c"}
    retrieved = ["x", "a", "a", "b"]
    assert recall_at_k(retrieved, relevant, 1) == 0.
    assert recall_at_k(retrieved, relevant, 4) == pytest.approx(2 / 3)
    assert reciprocal_rank(retrieved, relevant) == .5
    assert reciprocal_rank(["x", "y"], relevant) == 0.


def test_retrieval_metrics_reject_missing_ground_truth():
    with pytest.raises(ValueError):
        recall_at_k(["x"], set(), 2)
    with pytest.raises(ValueError):
        reciprocal_rank(["x"], set())
    with pytest.raises(ValueError):
        reciprocal_rank_fusion([["x"]], k=0)
