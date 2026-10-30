# 高频手撕：IoU / NMS / BatchNorm

目标：**先正确，再向量化，再谈工程优化。**

本页是精简的手写版；模块根目录 `examples/geometry_ops.py` 提供带输入校验的可运行参考实现，`tests/test_geometry_ops.py` 使用标量 IoU oracle 和 PyTorch BatchNorm 做数值对齐。在模块目录执行 `python -m pytest -q tests` 可验证。下面三个代码块假设按顺序执行；实际工程应优先导入经过测试的实现。

## 1. Batch IoU

必须说清：

- 输入 `boxes1[N,4]`, `boxes2[M,4]`；
- 坐标格式 `xyxy`；
- 连续坐标还是像素闭区间；
- 退化框与空输入；
- `N×M` 中间矩阵的内存。

```python
import torch

def batch_iou(a, b):
    # a: [N,4], b: [M,4], xyxy continuous coordinates
    lt = torch.maximum(a[:, None, :2], b[None, :, :2])
    rb = torch.minimum(a[:, None, 2:], b[None, :, 2:])
    wh = (rb - lt).clamp(min=0)
    inter = wh[..., 0] * wh[..., 1]

    area_a = ((a[:, 2]-a[:, 0]).clamp(min=0) *
              (a[:, 3]-a[:, 1]).clamp(min=0))
    area_b = ((b[:, 2]-b[:, 0]).clamp(min=0) *
              (b[:, 3]-b[:, 1]).clamp(min=0))
    union = area_a[:, None] + area_b[None, :] - inter
    safe_union = torch.where(union > 0, union, torch.ones_like(union))
    return torch.where(union > 0, inter / safe_union, torch.zeros_like(union))
```

**追问**：N、M 很大导致 OOM？→ 按一侧 chunk 计算。

## 2. NMS

```python
def nms(boxes, scores, iou_thr=0.5):
    order = scores.argsort(descending=True, stable=True)  # 分数相同保持输入次序
    keep = []
    while order.numel() > 0:
        i = int(order[0].item())
        keep.append(i)
        if order.numel() == 1:
            break
        rest = order[1:]
        iou = batch_iou(boxes[i:i+1], boxes[rest])[0]
        order = rest[iou <= iou_thr]
    return keep
```

必须主动提：class-aware vs class-agnostic、confidence/top-k 预筛、密集目标失败、最坏 O(N²)。约定 score 相同时按输入顺序；IoU 严格大于阈值才抑制；零面积框的 IoU 定义为 0。上方精简代码未做输入合法性校验，完整校验见 `examples/geometry_ops.py`。

## 3. BatchNorm2d Forward（教学简化版）

```python
def bn2d_train(x, gamma, beta, eps=1e-5):
    # x [N,C,H,W], gamma/beta [C]
    mean = x.mean(dim=(0, 2, 3), keepdim=True)
    var = ((x - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)
    x_hat = (x - mean) / torch.sqrt(var + eps)
    y = x_hat * gamma.view(1,-1,1,1) + beta.view(1,-1,1,1)
    return y, mean, var
```

追问时说明：本例只演示训练 batch 的有偏方差（`unbiased=False`）和归一化，不提供 running stats、momentum 或 eval mode。训练时单通道样本数需至少为 2；真实 PyTorch BatchNorm 的 train/eval 与状态更新由 `nn.BatchNorm2d` 完成。

## 4. 手撕评分标准

- 40%：主逻辑正确；
- 20%：shape/broadcast 正确；
- 20%：边界条件；
- 10%：复杂度；
- 10%：能说出生产实现如何更快/更稳。
