# 07. Mixture-of-Experts

从 routing、负载均衡到 expert parallel 与 All-to-All 的系统瓶颈。

## 本章训练目标

- 不只会定义：能够写公式、画数据/通信流；
- 不只会 Why：能够说明代价、失效边界和等成本实验；
- 不只会小规模：能够把问题映射到真实预训练系统。

## 题目

- [Q061. MoE 为什么能“总参数很大、每 Token FLOPs 较小”？](./061.md) · B 类等价追问题 · ★★★★★ · 易
- [Q062. Top-1 与 Top-2 Routing 有什么 Trade-off？](./062.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q063. 为什么 MoE 会出现 Expert Collapse / Hot Expert？](./063.md) · A 类高频真题型 · ★★★★★ · 难
- [Q064. Load-Balancing Auxiliary Loss 怎么工作？为什么太强会伤模型？](./064.md) · B 类等价追问题 · ★★★★☆ · 难
- [Q065. DeepSeek-V3 的 Auxiliary-Loss-Free Load Balancing 为什么重要？](./065.md) · A 类高频真题型 · ★★★★★ · 难
- [Q066. Shared Expert 的意义是什么？](./066.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q067. Fine-Grained Experts 为什么可能优于少量大 Experts？](./067.md) · B 类等价追问题 · ★★★★☆ · 难
- [Q068. Expert Parallel 与 Tensor Parallel 如何相互影响？](./068.md) · B 类等价追问题 · ★★★★★ · 难
- [Q069. MoE 为什么特别容易 Communication-Bound？](./069.md) · A 类高频真题型 · ★★★★★ · 难
- [Q070. Qwen3 MoE 与 DeepSeek-V3 MoE 应该怎样专业比较？](./070.md) · A 类高频真题型 · ★★★★★ · 难
