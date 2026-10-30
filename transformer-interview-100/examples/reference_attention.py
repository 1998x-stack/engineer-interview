"""Readable multi-head self-attention reference for educational validation.

This intentionally materializes the attention matrix and is not a production
replacement for PyTorch SDPA or FlashAttention.

A boolean mask uses True for a permitted key and False for a masked key.
Accepted masks: (T,T), (B,T,T), or (B|1,H|1,T,T). Every query row must
retain at least one key; all-masked rows are rejected rather than producing
NaN softmax output.
"""

import math

import torch
from torch import nn


class ReferenceMHA(nn.Module):
    """Self-attention over (batch, sequence, model_width)."""

    def __init__(self, d_model: int, num_heads: int):
        super().__init__()
        if (
            not isinstance(d_model, int)
            or isinstance(d_model, bool)
            or not isinstance(num_heads, int)
            or isinstance(num_heads, bool)
            or d_model <= 0
            or num_heads <= 0
            or d_model % num_heads != 0
        ):
            raise ValueError("d_model and num_heads must be positive integers; d_model must be divisible by num_heads")
        self.h = num_heads
        self.dh = d_model // num_heads
        self.qkv = nn.Linear(d_model, 3 * d_model, bias=False)
        self.out = nn.Linear(d_model, d_model, bias=False)

    def _attention_mask(self, mask: torch.Tensor, batch: int, length: int, device: torch.device) -> torch.Tensor:
        if not isinstance(mask, torch.Tensor) or mask.dtype != torch.bool:
            raise TypeError("mask must be a boolean torch.Tensor (True means allowed)")
        if mask.device != device:
            raise ValueError("mask and input must be on the same device")
        if mask.ndim == 2 and mask.shape == (length, length):
            mask = mask[None, None, :, :]
        elif mask.ndim == 3 and mask.shape == (batch, length, length):
            mask = mask[:, None, :, :]
        elif mask.ndim == 4 and (
            mask.shape[0] in (1, batch)
            and mask.shape[1] in (1, self.h)
            and mask.shape[2:] == (length, length)
        ):
            pass
        else:
            raise ValueError(
                f"invalid mask shape {tuple(mask.shape)}; expected (T,T), "
                f"(B,T,T), or (B|1,H|1,T,T), with B={batch}, H={self.h}, T={length}"
            )
        mask = mask.expand(batch, self.h, length, length)
        if not bool(mask.any(dim=-1).all()):
            raise ValueError("every attention query must have at least one unmasked key")
        return mask

    def forward(self, x: torch.Tensor, mask: torch.Tensor | None = None) -> torch.Tensor:
        if not isinstance(x, torch.Tensor) or x.ndim != 3:
            raise ValueError("x must be a tensor with shape (B,T,D)")
        batch, length, width = x.shape
        if length == 0 or batch == 0 or width != self.h * self.dh:
            raise ValueError(f"expected nonempty (B,T,{self.h * self.dh}) input, got {tuple(x.shape)}")

        keep = None if mask is None else self._attention_mask(mask, batch, length, x.device)
        q, k, v = self.qkv(x).chunk(3, dim=-1)

        def split_heads(z: torch.Tensor) -> torch.Tensor:
            return z.reshape(batch, length, self.h, self.dh).transpose(1, 2)

        q, k, v = (split_heads(z) for z in (q, k, v))
        scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.dh)
        if keep is not None:
            scores = scores.masked_fill(~keep, float("-inf"))
        probabilities = torch.softmax(scores, dim=-1)
        attended = probabilities @ v
        attended = attended.transpose(1, 2).contiguous().reshape(batch, length, width)
        return self.out(attended)


def causal_mask(T: int, device=None) -> torch.Tensor:
    """Return a (1,1,T,T) boolean causal keep-mask."""
    if not isinstance(T, int) or isinstance(T, bool) or T <= 0:
        raise ValueError("T must be a positive integer")
    return torch.ones(T, T, dtype=torch.bool, device=device).tril()[None, None]
