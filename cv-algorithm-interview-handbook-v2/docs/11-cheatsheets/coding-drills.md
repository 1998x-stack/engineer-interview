# 高频手撕：IoU / NMS / BatchNorm

目标：**先正确，再向量化，再谈工程优化。**

## 1. Batch IoU

必须说清：

- 输入 `boxes1[N,4]`, `boxes2[M,4]`；
- 坐标格式 `xyxy`；
- 连续坐标还是像素闭区间；
- 退化框与空输入；
- `N×M` 中间矩阵的内存。

```python
import torch

def batch_iou(a, b, eps=1e-7):
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
    return inter / union.clamp(min=eps)
```

**追问**：N、M 很大导致 OOM？→ 按一侧 chunk 计算。

## 2. NMS

```python
def nms(boxes, scores, iou_thr=0.5):
    order = scores.argsort(descending=True)
    keep = []
    while order.numel() > 0:
        i = order[0]
        keep.append(i.item())
        if order.numel() == 1:
            break
        rest = order[1:]
        iou = batch_iou(boxes[i:i+1], boxes[rest])[0]
        order = rest[iou <= iou_thr]
    return keep
```

必须主动提：class-aware vs class-agnostic、confidence/top-k 预筛、密集目标失败、最坏 O(N²)。

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

追问时说明：真实框架还涉及 running stats、momentum、方差估计口径、mixed precision 和 eval mode。

## 4. 手撕评分标准

- 40%：主逻辑正确；
- 20%：shape/broadcast 正确；
- 20%：边界条件；
- 10%：复杂度；
- 10%：能说出生产实现如何更快/更稳。
