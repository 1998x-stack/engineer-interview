# 第 1 章 · Transformer 总体架构与设计动机

> 从 RNN 的串行依赖出发，建立 Transformer block、Residual、LayerNorm、Tensor Shape 与模块职责的统一计算图。

## 本章完成标准

- 能完整画 Encoder/Decoder block
- 能从 `[B,T,D]` 推到 MHA 全 shape
- 能区分 token mixing 与 channel mixing
- 能解释并行性与 O(T²) trade-off

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q001 为什么 Transformer 能取代 RNN/LSTM？](Q001.md) | transformer |
| [Q002 请完整描述一个 Transformer Encoder Layer](Q002.md) | transformer |
| [Q003 请完整描述 Transformer Decoder](Q003.md) | inference |
| [Q004 Residual Connection 到底解决什么问题？](Q004.md) | transformer |
| [Q005 为什么 Transformer 更常用 LayerNorm 而不是 BatchNorm？](Q005.md) | normalization |
| [Q006 手写 Transformer 时最重要的 Tensor Shape 链是什么？](Q006.md) | transformer |
| [Q007 标准 Multi-Head Attention 参数量如何估算？](Q007.md) | attention |
| [Q008 Self-Attention 与 Cross-Attention 的本质区别是什么？](Q008.md) | attention |
| [Q009 Attention 与 FFN 分别承担什么功能？](Q009.md) | attention, ffn |
| [Q010 如果完全删除 Position Encoding，会发生什么？](Q010.md) | position, coding |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../../guide/knowledge-map.md) · [下一学习节点](../chapter-02/index.md)
