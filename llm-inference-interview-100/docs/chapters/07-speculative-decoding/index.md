# 07 Speculative Decoding

用“proposal 成本 + verification 成本 + acceptance”而不是宣传 speedup 判断价值。

## 本章学习方法

- **问题范围**：Q061 - Q070
- **核心实验**：对不同 draft 长度/温度做 sweep，画 accepted tokens 与实际 speedup 曲线。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q061 Speculative Decoding 的基本原理是什么？](q061-speculative-decoding-draft.md) - ★★★★★ - `speculative-decoding, draft`
- [Q062 为什么标准 speculative sampling 可以保持输出分布不变？](q062-speculative-sampling-correctness.md) - ★★★★★ - `speculative-sampling, correctness`
- [Q063 Acceptance Rate 为什么是 Spec Decode 最关键指标之一？](q063-acceptance-spec-decode.md) - ★★★★★ - `acceptance, spec-decode`
- [Q064 Draft Model 为什么不能越小越好？](q064-draft-model-tradeoff.md) - ★★★★☆ - `draft-model, tradeoff`
- [Q065 N-gram / Suffix speculation 为什么不需要 Draft Model？](q065-ngram-speculation.md) - ★★★★☆ - `ngram, speculation`
- [Q066 Medusa 是什么？](q066-medusa-spec-decode.md) - ★★★★☆ - `Medusa, spec-decode`
- [Q067 EAGLE 与普通 Draft Model 的关键区别？](q067-eagle-speculation.md) - ★★★★★ - `EAGLE, speculation`
- [Q068 MTP 为什么既可以用于训练，也可以用于推理加速？](q068-mtp-deepseek.md) - ★★★★★ - `MTP, DeepSeek`
- [Q069 Tree Attention 为什么能加速 speculative verification？](q069-tree-attention-verification.md) - ★★★★☆ - `tree-attention, verification`
- [Q070 Speculative Decoding 在什么情况下反而变慢？](q070-spec-decode-negative-speedup.md) - ★★★★★ - `spec-decode, negative-speedup`
