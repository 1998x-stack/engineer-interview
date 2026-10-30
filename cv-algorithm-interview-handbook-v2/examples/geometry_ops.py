"""Runnable interview references for box IoU, greedy NMS and BN2d training.

This is educational PyTorch code, not a replacement for fused production ops.
Boxes use floating-point (x1,y1,x2,y2) continuous coordinates and nonnegative sizes.
NMS is class-agnostic, stable for tied scores, and suppresses boxes with IoU > threshold.
"""
from __future__ import annotations

import math
import torch


def _boxes(value: torch.Tensor, name: str) -> None:
    if not isinstance(value, torch.Tensor) or value.ndim != 2 or value.shape[1] != 4:
        raise ValueError(f"{name} must have shape (N,4)")
    if not value.is_floating_point():
        raise TypeError(f"{name} must be floating point")
    if not bool(torch.isfinite(value).all()):
        raise ValueError(f"{name} must contain only finite values")
    if not bool((value[:, 2:] >= value[:, :2]).all()):
        raise ValueError(f"{name} has reversed xyxy coordinates")


def batch_iou(boxes1: torch.Tensor, boxes2: torch.Tensor) -> torch.Tensor:
    """Return pairwise IoU of two (N,4)/(M,4) box arrays, shape (N,M).

    Zero-area boxes have zero IoU, including two identical zero-area boxes.
    Empty inputs return an appropriately shaped empty tensor.
    """
    _boxes(boxes1, "boxes1")
    _boxes(boxes2, "boxes2")
    if boxes1.device != boxes2.device or boxes1.dtype != boxes2.dtype:
        raise ValueError("box arrays must use the same device and dtype")
    lt = torch.maximum(boxes1[:, None, :2], boxes2[None, :, :2])
    rb = torch.minimum(boxes1[:, None, 2:], boxes2[None, :, 2:])
    wh = (rb - lt).clamp_min(0)
    intersection = wh[..., 0] * wh[..., 1]
    size1 = boxes1[:, 2:] - boxes1[:, :2]
    size2 = boxes2[:, 2:] - boxes2[:, :2]
    area1 = size1[:, 0] * size1[:, 1]
    area2 = size2[:, 0] * size2[:, 1]
    union = (area1[:, None] + area2[None, :] - intersection).clamp_min(0)
    safe_union = torch.where(union > 0, union, torch.ones_like(union))
    return torch.where(union > 0, intersection / safe_union, torch.zeros_like(union))


def nms(boxes: torch.Tensor, scores: torch.Tensor, iou_thr: float = 0.5) -> list[int]:
    """Return original row indices kept by greedy class-agnostic NMS.

    An overlap strictly greater than iou_thr is suppressed; equality is kept.
    Ties in scores use input order. Worst-case O(N^2) time.
    """
    _boxes(boxes, "boxes")
    if (not isinstance(scores, torch.Tensor) or scores.ndim != 1
            or scores.shape[0] != boxes.shape[0] or not scores.is_floating_point()):
        raise ValueError("scores must be a floating tensor of shape (N,)")
    if scores.device != boxes.device or not bool(torch.isfinite(scores).all()):
        raise ValueError("scores must be finite and use the boxes device")
    if not isinstance(iou_thr, (int, float)) or not math.isfinite(iou_thr) or not 0 <= iou_thr <= 1:
        raise ValueError("iou_thr must be finite and between 0 and 1")
    order = torch.argsort(scores, descending=True, stable=True)
    keep: list[int] = []
    while order.numel():
        i = int(order[0].item())
        keep.append(i)
        rest = order[1:]
        if rest.numel() == 0:
            break
        overlap = batch_iou(boxes[i:i + 1], boxes[rest])[0]
        order = rest[overlap <= iou_thr]
    return keep


def bn2d_train(
    x: torch.Tensor, gamma: torch.Tensor, beta: torch.Tensor, eps: float = 1e-5
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Simplified BN2d training step: returns (y, mean, biased_variance).

    Statistics have shape (1,C,1,1), reduce axes (0,2,3).
    Does NOT maintain running statistics or implement eval mode; see nn.BatchNorm2d.
    """
    if not isinstance(x, torch.Tensor) or x.ndim != 4 or not x.is_floating_point():
        raise ValueError("x must be a float tensor of shape (N,C,H,W)")
    n, c, h, w = x.shape
    if min(n, c, h, w) <= 0 or n * h * w < 2:
        raise ValueError("BN2d training requires at least two samples per channel")
    for name, value in (("gamma", gamma), ("beta", beta)):
        if (not isinstance(value, torch.Tensor) or value.shape != (c,)
                or value.device != x.device or value.dtype != x.dtype):
            raise ValueError(f"{name} must be shape (C,) with matching device and dtype")
    if not isinstance(eps, (float, int)) or not math.isfinite(eps) or eps <= 0:
        raise ValueError("eps must be a finite positive number")
    mean = x.mean(dim=(0, 2, 3), keepdim=True)
    var = ((x - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)
    normalized = (x - mean) * torch.rsqrt(var + eps)
    y = normalized * gamma.reshape(1, c, 1, 1) + beta.reshape(1, c, 1, 1)
    return y, mean, var
