# 预训练 Debug Playbook

## Loss Spike / NaN 的共同原则

> **定位第一个异常事件，而不是修饰最终症状。**

```text
first bad step
→ first bad rank
→ first bad tensor/layer
→ forward or backward
→ deterministic replay
→ single-variable ablation
→ root cause
→ fix
→ regression + long-run validation
```

## 必存信息

- checkpoint + optimizer/scheduler state
- consumed tokens / global step
- RNG state
- dataloader/shard/sample IDs
- rank topology
- loss / grad norm / parameter norm
- selected activation/logit statistics
- NCCL / hardware error logs

## 快速分类

| 现象 | 第一批假设 |
|---|---|
| 同一 batch replay 必现 | 数据 / deterministic numerical path |
| 单 rank 先异常 | hardware / rank-specific data / distributed state |
| 所有 rank 同时异常 | optimizer / schedule / shared batch / model instability |
| MFU 突降但 loss 正常 | straggler / network / dataloader / kernel |
| expert load 极不均 | routing collapse / data skew / capacity setting |
