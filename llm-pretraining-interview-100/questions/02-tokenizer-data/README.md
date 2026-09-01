# 02. Tokenizer 与预训练数据

从 tokenizer fertility 到清洗、去重、数据 mixture、污染检测和 synthetic data。

## 本章训练目标

- 不只会定义：能够写公式、画数据/通信流；
- 不只会 Why：能够说明代价、失效边界和等成本实验；
- 不只会小规模：能够把问题映射到真实预训练系统。

## 题目

- [Q011. BPE、WordPiece、SentencePiece 的本质区别？](./011.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q012. Vocabulary Size 应该怎么定？](./012.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q013. 什么是 Tokenizer Fertility？为什么中文/多语言必须看？](./013.md) · B 类等价追问题 · ★★★☆☆ · 中
- [Q014. 从 Common Crawl 到训练 Token：完整预训练数据 Pipeline 怎么设计？](./014.md) · A 类高频真题型 · ★★★★★ · 难
- [Q015. Exact Dedup、MinHash、SimHash、Semantic Dedup 分别解决什么？](./015.md) · B 类等价追问题 · ★★★★★ · 中
- [Q016. 预训练数据为什么不能简单追求“质量越高越好”？](./016.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q017. 预训练数据 Mixture 到底怎么调？](./017.md) · A 类高频真题型 · ★★★★★ · 难
- [Q018. 什么是 Benchmark Contamination？如何系统检测？](./018.md) · B 类等价追问题 · ★★★★★ · 难
- [Q019. Packing 与 Padding 有什么区别？为什么 Packing 不是简单拼接？](./019.md) · A 类高频真题型 · ★★★★★ · 中
- [Q020. Synthetic Data 在预训练阶段的价值与风险是什么？](./020.md) · B 类等价追问题 · ★★★★★ · 中
