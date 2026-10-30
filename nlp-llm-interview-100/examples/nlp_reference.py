"""Educational reference implementations for Q097-Q099 and RAG retrieval.

These are intentionally small correctness baselines, not optimized production kernels.
Attention boolean key masks use True=visible; all-masked queries are rejected.
"""
from __future__ import annotations

import math
from collections.abc import Hashable, Sequence

import torch


def stable_softmax(x: torch.Tensor, dim: int = -1, keep: torch.Tensor | None = None) -> torch.Tensor:
    """Normalize on dim using max subtraction and optional exact-shape keep mask."""
    if not isinstance(x, torch.Tensor) or not x.is_floating_point() or x.ndim == 0 or x.numel() == 0:
        raise ValueError("x must be a nonempty floating tensor with at least one axis")
    if not isinstance(dim, int) or isinstance(dim, bool) or not -x.ndim <= dim < x.ndim:
        raise ValueError("dim is outside tensor rank")
    if not bool(torch.isfinite(x).all()):
        raise ValueError("x must be finite")
    y = x.float() if x.dtype in (torch.float16, torch.bfloat16) else x
    if keep is not None:
        if not isinstance(keep, torch.Tensor) or keep.dtype != torch.bool or keep.shape != x.shape:
            raise ValueError("keep must be a boolean tensor with exactly x.shape")
        if keep.device != x.device or not bool(keep.any(dim=dim).all()):
            raise ValueError("keep must share x.device and every row must expose at least one key")
        y = y.masked_fill(~keep, float("-inf"))
    z = y - y.amax(dim=dim, keepdim=True)
    weights = torch.exp(z)
    result = weights / weights.sum(dim=dim, keepdim=True)
    return result.to(x.dtype)


def reference_attention(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    *,
    causal: bool = False,
    key_padding_mask: torch.Tensor | None = None,
) -> torch.Tensor:
    """Scaled-dot-product attention with q/k/v shapes (B,H,T,D).

    For causal suffix queries, q is the final Tq positions of k (Tq<=Tk).
    key_padding_mask has shape (B,Tk), True means available.
    Masked query positions are not implemented: strip/pad them at the caller.
    """
    if not all(isinstance(z, torch.Tensor) and z.ndim == 4 for z in (q, k, v)):
        raise ValueError("q, k, v must have rank 4 (B,H,T,D)")
    b, h, tq, d = q.shape
    if min(b, h, tq, d) < 1 or k.shape[:2] != (b, h) or v.shape[:2] != (b, h):
        raise ValueError("batch/head dimensions must agree and be nonempty")
    tk = k.shape[2]
    if tk < 1 or v.shape[2] != tk or k.shape[3] != d or v.shape[3] != d:
        raise ValueError("attention time and head dimensions mismatch")
    if any(z.dtype != q.dtype or z.device != q.device for z in (k, v)) or not q.is_floating_point():
        raise ValueError("q/k/v must use the same floating dtype and device")
    if not all(bool(torch.isfinite(z).all()) for z in (q, k, v)):
        raise ValueError("q/k/v must be finite")
    if causal and tq > tk:
        raise ValueError("causal suffix query length must be <= key length")
    visible = torch.ones((b, 1, tq, tk), device=q.device, dtype=torch.bool)
    if key_padding_mask is not None:
        if (not isinstance(key_padding_mask, torch.Tensor) or
                key_padding_mask.dtype != torch.bool or
                key_padding_mask.shape != (b, tk) or key_padding_mask.device != q.device):
            raise ValueError("key_padding_mask must be bool (B,Tk), True=visible")
        visible = visible & key_padding_mask[:, None, None, :]
    if causal:
        q_positions = torch.arange(tq, device=q.device) + tk - tq
        k_positions = torch.arange(tk, device=q.device)
        visible = visible & (k_positions[None, None, None, :] <= q_positions[None, None, :, None])
    if not bool(visible.any(dim=-1).all()):
        raise ValueError("an attention query has no visible keys")
    compute_dtype = torch.float32 if q.dtype in (torch.float16, torch.bfloat16) else q.dtype
    scores = (q.to(compute_dtype) @ k.to(compute_dtype).transpose(-2, -1)) / math.sqrt(d)
    scores = scores.masked_fill(~visible, float("-inf"))
    probabilities = torch.softmax(scores, dim=-1)
    return (probabilities @ v.to(compute_dtype)).to(v.dtype)


def nearest_neighbors(
    queries: torch.Tensor, corpus: torch.Tensor, *, block_size: int = 1024
) -> torch.Tensor:
    """Exact 1-NN indices using squared L2 and chunked matrix products.

    Uses O(M*block_size) scratch, not an (M,N,D) broadcast; tied minima
    select the lowest corpus index. For extremely close large vectors use float64.
    """
    if (not isinstance(queries, torch.Tensor) or not isinstance(corpus, torch.Tensor) or
            queries.ndim != 2 or corpus.ndim != 2 or queries.shape[1] != corpus.shape[1] or
            queries.shape[1] < 1 or corpus.shape[0] < 1 or
            not queries.is_floating_point() or
            queries.dtype != corpus.dtype or queries.device != corpus.device):
        raise ValueError("expected (M,D) and nonempty (N,D) float tensors with same dtype/device")
    if not isinstance(block_size, int) or isinstance(block_size, bool) or block_size <= 0:
        raise ValueError("block_size must be a positive integer")
    if not bool(torch.isfinite(queries).all()) or not bool(torch.isfinite(corpus).all()):
        raise ValueError("vectors must be finite")
    m, n = queries.shape[0], corpus.shape[0]
    if m == 0:
        return torch.empty(0, dtype=torch.long, device=queries.device)
    compute = torch.float64 if queries.dtype == torch.float64 else torch.float32
    qq = queries.to(compute)
    cc = corpus.to(compute)
    # Query squared norms are constant for the argmin over corpus indices.
    best = torch.full((m,), float("inf"), dtype=compute, device=qq.device)
    indices = torch.zeros(m, dtype=torch.long, device=qq.device)
    for start in range(0, n, block_size):
        chunk = cc[start:start + block_size]
        distance = (chunk * chunk).sum(dim=-1)[None, :] - 2 * (qq @ chunk.T)
        local_value, local_index = distance.min(dim=-1)
        improved = local_value < best  # strict preserves earliest index on ties
        best = torch.where(improved, local_value, best)
        indices = torch.where(improved, local_index + start, indices)
    return indices


def reciprocal_rank_fusion(rankings: Sequence[Sequence[Hashable]], k: int = 60) -> list[tuple[Hashable, float]]:
    """Deterministic RRF scores: sum 1/(k+rank), ranks start at 1.

    Repeated document IDs inside a single ranking count only at first appearance.
    Ties use first appearance across rank lists.
    """
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k must be a positive integer")
    scores: dict[Hashable, float] = {}
    order: dict[Hashable, int] = {}
    for ranking in rankings:
        seen: set[Hashable] = set()
        for rank, doc in enumerate(ranking, 1):
            if doc in seen:
                continue
            seen.add(doc)
            if doc not in order:
                order[doc] = len(order)
            scores[doc] = scores.get(doc, 0.0) + 1.0 / (k + rank)
    return sorted(scores.items(), key=lambda pair: (-pair[1], order[pair[0]]))


def recall_at_k(retrieved: Sequence[Hashable], relevant: set[Hashable], k: int) -> float:
    """Unique relevant documents in first k results divided by total relevant docs."""
    if not relevant or not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("relevant must be nonempty and k must be a positive integer")
    return len(set(retrieved[:k]) & relevant) / len(relevant)


def reciprocal_rank(retrieved: Sequence[Hashable], relevant: set[Hashable]) -> float:
    """1 / rank of first relevant item; 0 if not found."""
    if not relevant:
        raise ValueError("relevant must be nonempty")
    return next((1.0 / i for i, doc in enumerate(retrieved, 1) if doc in relevant), 0.0)
