# 第 9 章 · Coding / Debug / System Design

> 把知识转成可验证实现：先 invariant/reference，再优化；用行为测试捕捉能正常训练却语义错误的 bug。

## 本章完成标准

- MHA reference
- causal leakage
- KV parity
- stride/contiguous
- tiny overfit
- 系统设计闭环

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q091 Coding：下面的 Attention 有哪些 bug？](Q091.md) | attention, coding |
| [Q092 Coding：给 Transformer 加 KV Cache](Q092.md) | inference, coding |
| [Q093 给你几百行 Transformer 代码，如何系统 Debug？](Q093.md) | coding |
| [Q094 Coding：如何验证 causal mask 没有未来泄漏？](Q094.md) | attention, coding |
| [Q095 Coding：如何验证 KV Cache 实现正确？](Q095.md) | inference, coding |
| [Q096 Coding：为什么 transpose 后 view 经常报错或 silently 出问题？](Q096.md) | bert-gpt, coding |
| [Q097 Coding：如何处理全 Mask 行导致的 NaN？](Q097.md) | attention, coding |
| [Q098 Coding：如何做 Tiny Overfit Test？](Q098.md) | coding |
| [Q099 Coding：如何为 Attention 写 Shape Assertions？](Q099.md) | attention, coding |
| [Q100 System Design：用 Transformer 设计文本分类系统](Q100.md) | system-design |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-08/index.md) · [下一学习节点](../../system-design/SD01.md)
