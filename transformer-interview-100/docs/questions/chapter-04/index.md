# 第 4 章 · Norm、Residual 与 FFN

> 理解深层 Transformer 为什么能稳定训练，以及 FFN 为什么承担大量参数与非线性计算。

## 本章完成标准

- Pre/Post-LN 对比
- LayerNorm/RMSNorm 维度
- SwiGLU 参数预算
- 初始化/activation RMS 诊断

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q036 为什么现代 LLM 普遍偏向 Pre-Norm？](Q036.md) | normalization |
| [Q037 LayerNorm 到底沿哪个维度计算？](Q037.md) | normalization |
| [Q038 RMSNorm 与 LayerNorm 有什么区别？](Q038.md) | normalization |
| [Q039 FFN 为什么不可缺少？](Q039.md) | ffn |
| [Q040 为什么经典 Transformer 常用 d_ff≈4d_model？](Q040.md) | transformer |
| [Q041 GELU 为什么比 ReLU 常见？](Q041.md) | ffn |
| [Q042 SwiGLU 是什么，为什么现代 LLM 常用？](Q042.md) | ffn |
| [Q043 为什么深层 Transformer 对初始化特别敏感？](Q043.md) | training |
| [Q044 为什么 Input Embedding 与 LM Head 经常 Weight Tying？](Q044.md) | transformer |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-03/index.md) · [下一学习节点](../chapter-05/index.md)
