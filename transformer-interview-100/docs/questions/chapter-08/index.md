# 第 8 章 · 长上下文、高性能 Attention 与 MoE

> 把 Attention 放进 GPU/IO/通信世界：online softmax、FlashAttention、sparse/linear、MoE、quantization。

## 本章完成标准

- exact vs approximate
- IO-aware 分析
- MoE all-to-all
- 长上下文瓶颈
- 量化质量回归

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q081 FlashAttention 为什么不需要存完整 Attention Matrix？](Q081.md) | attention, systems |
| [Q082 Online Softmax 如何分块仍保持精确？](Q082.md) | attention |
| [Q083 Sparse Attention 如何降低复杂度？](Q083.md) | attention, systems |
| [Q084 Linear Attention 与 FlashAttention 最大区别？](Q084.md) | attention, systems |
| [Q085 长上下文 Transformer 至少有哪些瓶颈？](Q085.md) | systems |
| [Q086 Sliding Window Attention 的优势与损失？](Q086.md) | attention, systems |
| [Q087 MoE 为什么能在相近每-token FLOPs 下增加参数量？](Q087.md) | training, systems |
| [Q088 MoE 最大训练难点是什么？](Q088.md) | systems |
| [Q089 Quantization 为什么对 Transformer 推理重要？](Q089.md) | systems |
| [Q090 Coding：从零实现 Multi-Head Attention](Q090.md) | attention, coding |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-07/index.md) · [下一学习节点](../chapter-09/index.md)
