# 第 6 章 · 训练、优化与分布式

> 建立从 objective/loss mask 到数值精度、optimizer、scaling 和多 GPU 的系统训练故障树。

## 本章完成标准

- NaN 定位
- AdamW/Grad Clip
- BF16/FP16
- global batch
- DP/TP/PP/CP

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q055 Decoder LM 的 label 为什么必须 shift？](Q055.md) | training, inference |
| [Q056 Padding token 为什么不能参与 loss？](Q056.md) | training |
| [Q057 Transformer loss 变成 NaN，如何系统排查？](Q057.md) | training |
| [Q058 为什么训练早期常用 Learning Rate Warmup？](Q058.md) | training |
| [Q059 Adam 与 AdamW 的核心区别？](Q059.md) | training |
| [Q060 Gradient Clipping 为什么有用？](Q060.md) | training |
| [Q061 Gradient Accumulation 是否完全等价于大 Batch？](Q061.md) | training |
| [Q062 FP16 与 BF16 为什么训练表现不同？](Q062.md) | training |
| [Q063 训练正常但验证每次结果不同，先查什么？](Q063.md) | transformer |
| [Q064 Transformer 初始化不合理有哪些症状？](Q064.md) | training |
| [Q065 固定训练 FLOPs，模型更大还是 token 更多？](Q065.md) | training |
| [Q066 Transformer 多 GPU 有哪些并行方式？](Q066.md) | training |
| [Q067 Decoder-only LLM 的生成过程是什么？](Q067.md) | inference |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-05/index.md) · [下一学习节点](../chapter-07/index.md)
