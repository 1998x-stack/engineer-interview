# 05. 分布式训练

掌握 DP/TP/PP/CP/EP、ZeRO/FSDP、collective 与千卡拓扑设计。

## 本章训练目标

- 不只会定义：能够写公式、画数据/通信流；
- 不只会 Why：能够说明代价、失效边界和等成本实验；
- 不只会小规模：能够把问题映射到真实预训练系统。

## 题目

- [Q041. DDP 到底做了什么？](./041.md) · A 类高频真题型 · ★★★★★ · 易
- [Q042. Tensor Parallel 如何切 Transformer？](./042.md) · A 类高频真题型 · ★★★★★ · 难
- [Q043. 为什么 TP 通常限制在 NVLink/NVSwitch 高速域？](./043.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q044. Pipeline Parallel 为什么有 Bubble？1F1B 如何改善？](./044.md) · A 类高频真题型 · ★★★★★ · 中
- [Q045. 为什么 1F1B 比 All-Forward-Then-Backward 更省 Activation Memory？](./045.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q046. ZeRO-1、ZeRO-2、ZeRO-3 分别 Shard 什么？](./046.md) · A 类高频真题型 · ★★★★★ · 易
- [Q047. FSDP 与 ZeRO-3 有什么关系和区别？](./047.md) · A 类高频真题型 · ★★★★★ · 中
- [Q048. Sequence Parallel 与 Context Parallel 有什么区别？](./048.md) · A 类高频真题型 · ★★★★★ · 难
- [Q049. Expert Parallel 为什么需要 All-to-All？](./049.md) · A 类高频真题型 · ★★★★★ · 中
- [Q050. 给你 1024 张 GPU，TP/PP/DP/CP/EP 怎么设计？](./050.md) · A 类高频真题型 · ★★★★★ · 难
