"""Transparent PyTorch baselines for Q003/Q012/Q016/Q055/Q069/Q100.

Educational reference implementations, not optimized production kernels.
Tensor shapes and rejection policies are part of the exercise contract.
"""
from __future__ import annotations

import math
import torch
import torch.nn.functional as F


def cross_entropy_logits(logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
    """Mean categorical NLL from logits, with logsumexp and no explicit softmax."""
    if (not isinstance(logits, torch.Tensor) or logits.ndim != 2 or
            not logits.is_floating_point() or logits.shape[0] < 1 or logits.shape[1] < 2 or
            not isinstance(targets, torch.Tensor) or targets.shape != (logits.shape[0],) or
            targets.dtype != torch.long or targets.device != logits.device):
        raise ValueError("logits must be nonempty float [B,C>=2]; targets int64 [B]")
    if not bool(torch.isfinite(logits).all()) or not bool(((targets >= 0) & (targets < logits.shape[1])).all()):
        raise ValueError("logits must be finite and target indices must be valid")
    x = logits.float() if logits.dtype in (torch.float16, torch.bfloat16) else logits
    selected = x.gather(1, targets[:, None]).squeeze(1)
    return (torch.logsumexp(x, dim=-1) - selected).mean()


def _bn_args(x, gamma, beta, eps):
    if (not isinstance(x, torch.Tensor) or x.ndim != 4 or
            not x.is_floating_point() or x.numel() == 0):
        raise ValueError("x must be nonempty float tensor [B,C,H,W]")
    if not isinstance(eps, (float, int)) or isinstance(eps, bool) or eps <= 0 or not math.isfinite(eps):
        raise ValueError("eps must be finite and positive")
    for v in (gamma, beta):
        if (not isinstance(v, torch.Tensor) or v.shape != (x.shape[1],) or
                v.dtype != x.dtype or v.device != x.device):
            raise ValueError("gamma/beta must be [C] and share dtype/device with x")
    if not all(bool(torch.isfinite(t).all()) for t in (x, gamma, beta)):
        raise ValueError("x/gamma/beta must be finite")


def batchnorm2d_train(x: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5):
    """Train-mode BN forward: variance uses biased estimator across (B,H,W).

    Does not update running statistics; PyTorch running variance uses the unbiased
    estimator, distinct from the variance used in normalization.
    """
    _bn_args(x, gamma, beta, eps)
    if x.shape[0] * x.shape[2] * x.shape[3] <= 1:
        raise ValueError("train-mode BatchNorm requires >1 values per channel")
    axes = (0, 2, 3)
    mean = x.mean(axes, keepdim=True)
    variance = ((x - mean) ** 2).mean(axes, keepdim=True)
    y = (x - mean) / torch.sqrt(variance + eps)
    return y * gamma[None, :, None, None] + beta[None, :, None, None]


def batchnorm2d_eval(x, gamma, beta, running_mean, running_var, eps: float = 1e-5):
    """Eval-mode BN uses frozen running stats, independent of inference batch."""
    _bn_args(x, gamma, beta, eps)
    for stat in (running_mean, running_var):
        if (not isinstance(stat, torch.Tensor) or stat.shape != (x.shape[1],) or
                stat.device != x.device or stat.dtype != x.dtype or not bool(torch.isfinite(stat).all())):
            raise ValueError("running statistics must be finite [C] tensors")
    if not bool((running_var >= 0).all()):
        raise ValueError("running variance must be nonnegative")
    return ((x - running_mean[None, :, None, None]) /
            torch.sqrt(running_var[None, :, None, None] + eps) *
            gamma[None, :, None, None] + beta[None, :, None, None])


def adamw_step(p, grad, m, v, *, step: int, lr: float, weight_decay: float = 0.,
               beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8):
    """Functional AdamW update with bias-corrected moments, no in-place mutation."""
    if not all(isinstance(z, torch.Tensor) for z in (p, grad, m, v)):
        raise ValueError("p, grad, m, v must be tensors")
    if not p.is_floating_point() or any(z.shape != p.shape or z.dtype != p.dtype or z.device != p.device for z in (grad, m, v)):
        raise ValueError("all AdamW tensors must share floating shape/dtype/device")
    if not all(bool(torch.isfinite(z).all()) for z in (p, grad, m, v)) or not bool((v >= 0).all()):
        raise ValueError("moments must be finite, and v must be nonnegative")
    if (not isinstance(step, int) or isinstance(step, bool) or step < 1 or
            not (0 <= beta1 < 1 and 0 <= beta2 < 1) or
            not all(math.isfinite(x) for x in (lr, weight_decay, eps)) or
            lr < 0 or weight_decay < 0 or eps <= 0):
        raise ValueError("invalid optimizer hyperparameters")
    new_m = beta1 * m + (1 - beta1) * grad
    new_v = beta2 * v + (1 - beta2) * grad.square()
    corrected_m = new_m / (1 - beta1 ** step)
    corrected_v = new_v / (1 - beta2 ** step)
    new_p = p * (1 - lr * weight_decay) - lr * corrected_m / (corrected_v.sqrt() + eps)
    return new_p, new_m, new_v


def reference_attention(q, k, v, *, causal: bool = False, padding_keep=None):
    """Q/K/V [B,H,T,D]; padding_keep [B,Tk] bool, True=visible.

    For causal suffix decoding, Tq queries occupy the final Tq positions of Tk.
    Completely masked query rows fail closed rather than returning uniform weights.
    """
    if not all(isinstance(z, torch.Tensor) and z.ndim == 4 for z in (q, k, v)):
        raise ValueError("q/k/v must have shape [B,H,T,D]")
    b, h, tq, d = q.shape
    tk = k.shape[2]
    if (min(b, h, tq, d, tk) <= 0 or k.shape != (b, h, tk, d) or
            v.shape[:3] != (b, h, tk) or v.shape[3] < 1 or
            not q.is_floating_point() or
            any(z.dtype != q.dtype or z.device != q.device for z in (k, v))):
        raise ValueError("incompatible q/k/v shapes, dtype or device")
    if causal and tq > tk:
        raise ValueError("causal suffix query requires Tq<=Tk")
    if not all(bool(torch.isfinite(z).all()) for z in (q, k, v)):
        raise ValueError("q/k/v must be finite")
    keep = torch.ones(b, 1, tq, tk, dtype=torch.bool, device=q.device)
    if padding_keep is not None:
        if (not isinstance(padding_keep, torch.Tensor) or
                padding_keep.shape != (b, tk) or padding_keep.dtype != torch.bool or
                padding_keep.device != q.device):
            raise ValueError("padding_keep must be bool [B,Tk] on input device")
        keep = keep & padding_keep[:, None, None, :]
    if causal:
        q_positions = torch.arange(tq, device=q.device) + tk - tq
        k_positions = torch.arange(tk, device=q.device)
        keep = keep & (k_positions[None, None, None, :] <= q_positions[None, None, :, None])
    if not bool(keep.any(dim=-1).all()):
        raise ValueError("all-masked query: no visible key")
    dtype = torch.float32 if q.dtype in (torch.float16, torch.bfloat16) else q.dtype
    score = (q.to(dtype) @ k.to(dtype).transpose(-2, -1)) / math.sqrt(d)
    probs = torch.softmax(score.masked_fill(~keep, float("-inf")), dim=-1)
    return (probs @ v.to(dtype)).to(v.dtype)


def symmetric_infonce(q, k, temperature: float = 0.07, symmetric: bool = True):
    """CLIP-like InfoNCE with diagonal positives, L2-normalized embeddings."""
    if (not isinstance(q, torch.Tensor) or not isinstance(k, torch.Tensor) or
            q.ndim != 2 or k.shape != q.shape or q.shape[0] < 2 or q.shape[1] < 1 or
            not q.is_floating_point() or q.dtype != k.dtype or q.device != k.device):
        raise ValueError("q and k must share nonempty float shape [B>=2,D]")
    if (not isinstance(temperature, (float, int)) or isinstance(temperature, bool) or
            not math.isfinite(temperature) or temperature <= 0):
        raise ValueError("temperature must be finite and >0")
    if not all(bool(torch.isfinite(z).all()) for z in (q, k)) or not bool((q.norm(dim=-1) > 0).all()) or not bool((k.norm(dim=-1) > 0).all()):
        raise ValueError("embeddings must be finite and have nonzero norm")
    logits = F.normalize(q.float() if q.dtype in (torch.float16, torch.bfloat16) else q, dim=-1) @ (
        F.normalize(k.float() if k.dtype in (torch.float16, torch.bfloat16) else k, dim=-1).T
    ) / temperature
    labels = torch.arange(q.shape[0], device=q.device)
    loss = F.cross_entropy(logits, labels)
    return (loss + F.cross_entropy(logits.T, labels)) * 0.5 if symmetric else loss
