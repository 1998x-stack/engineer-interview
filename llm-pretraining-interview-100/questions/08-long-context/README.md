# 08. 长上下文与高效 Attention

从 O(S²)、RoPE 外推到 continued pretraining、CP 与真实长上下文评测。

## 本章训练目标

- 不只会定义：能够写公式、画数据/通信流；
- 不只会 Why：能够说明代价、失效边界和等成本实验；
- 不只会小规模：能够把问题映射到真实预训练系统。

## 题目

- [Q071. Self-Attention 为什么是 O(S²)？](./071.md) · B 类等价追问题 · ★★★★☆ · 易
- [Q072. FlashAttention 解决的是计算复杂度还是 IO Complexity？](./072.md) · A 类高频真题型 · ★★★★★ · 易
- [Q073. RoPE 为什么会有 Length Extrapolation 问题？](./073.md) · B 类等价追问题 · ★★★★★ · 难
- [Q074. NTK-Aware Scaling / YaRN 本质上在做什么？](./074.md) · B 类等价追问题 · ★★★★☆ · 难
- [Q075. 为什么 Long-Context 通常还需要 Continued Pretraining？](./075.md) · B 类等价追问题 · ★★★★★ · 中
- [Q076. Context 从 4K 扩到 32K，为什么常采用阶段式训练？](./076.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q077. Sliding-Window Attention 的优缺点是什么？](./077.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q078. 用了 FlashAttention 为什么长上下文训练仍然 OOM？](./078.md) · A 类高频真题型 · ★★★★★ · 中
- [Q079. Context Parallel 下 Attention 是怎么计算的？](./079.md) · A 类高频真题型 · ★★★★★ · 难
- [Q080. 如何证明一个“128K 模型”真的有 128K 有效能力？](./080.md) · B 类等价追问题 · ★★★★☆ · 难
