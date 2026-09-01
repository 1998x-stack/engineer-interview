# 第 7 章 · 自回归推理与 KV Cache

> 从 incremental computation 和 KV 生命周期推导 Serving：prefill/decode、GQA、PagedAttention、continuous batching 与 speculative decoding。

## 本章完成标准

- KV 公式手算
- full-vs-cache parity
- TTFT/TPOT
- GQA/MQA
- scheduler trade-off

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q068 KV Cache 缓存了什么，为什么不缓存 Q？](Q068.md) | inference |
| [Q069 KV Cache 内存如何估算？](Q069.md) | inference |
| [Q070 为什么训练不需要像 decode 一样使用 KV Cache？](Q070.md) | inference |
| [Q071 Prefill 与 Decode 的瓶颈有什么不同？](Q071.md) | inference |
| [Q072 MHA、MQA、GQA 的区别？](Q072.md) | inference |
| [Q073 Greedy、Beam Search 与 Sampling 如何选择？](Q073.md) | inference |
| [Q074 Temperature、Top-k、Top-p 分别做什么？](Q074.md) | inference |
| [Q075 为什么模型会陷入重复生成？](Q075.md) | transformer |
| [Q076 LLM Serving 的关键 latency 指标有哪些？](Q076.md) | inference |
| [Q077 Continuous Batching 为什么适合 LLM？](Q077.md) | inference |
| [Q078 PagedAttention 解决什么问题？](Q078.md) | attention, inference |
| [Q079 Speculative Decoding 为什么能加速且保持目标分布？](Q079.md) | inference, coding |
| [Q080 FlashAttention 到底优化了什么？](Q080.md) | attention, systems |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-06/index.md) · [下一学习节点](../chapter-08/index.md)
