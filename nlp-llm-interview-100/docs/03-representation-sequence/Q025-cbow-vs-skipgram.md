---
id: Q025
title: "CBOW 与 Skip‑Gram：输入输出正好相反吗？"
chapter: "表示学习与序列模型"
difficulty: "★★"
frequency: "★★★★"
tags:
  - representation-sequence
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q025 CBOW 与 Skip‑Gram：输入输出正好相反吗？

[← Q024](../02-classical-nlp/Q024-nlp-data-augmentation.md) | **第 3 章 · 表示学习与序列模型** | [Q026 →](Q026-negative-sampling.md)

> **难度**：★★  ·  **频率**：★★★★  ·  **标签**：`representation-sequence`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q025.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

CBOW 和 Skip-Gram 的训练目标、速度与低频词表现有何差异？

## 2. 面试官到底在考什么

掌握经典表示学习目标。

### 评分维度

- 先给训练目标或状态转移，再解释它解决上一代方法什么问题。
- 理解梯度、表示与上下文依赖。
- 能把历史模型与 Transformer 的演进关系讲清楚。

## 3. 30-60 秒标准回答

CBOW 用上下文预测中心词，更新更聚合、训练快；Skip-Gram 用中心词预测上下文，一词产生 多个训练对，对低频词通常更友好但计算更重。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：二者都基于 distributional hypothesis。
- **PDF 基线要点**：窗口大小决定更偏句法还是主题语义。
- **PDF 基线要点**：真正大词表训练还需要 hierarchical softmax 或 negative sampling。
- **扩展理解**：CBOW 用上下文预测中心词，Skip-Gram 用中心词预测上下文；目标方向不同导致稀有词学习特性不同。
- **扩展理解**：两者最终都在学习 word-context compatibility。
- **扩展理解**：面试可进一步比较训练速度、窗口采样和 subsampling 高频词。

## 6. 专业深挖：原理、边界与工程

### CBOW / Skip-Gram 的训练信号差异
- CBOW 把上下文向量聚合后预测中心词；Skip-Gram 用中心词分别预测窗口中的多个上下文词。二者不只是“输入输出反过来”，还改变每个词获得的监督次数。
- Skip-Gram 对每个 center-context pair 单独训练，低频词每次出现可获得多个更新，因此常对 rare words 更友好；CBOW 聚合上下文，训练更平滑、更快。
- 窗口大小决定语义偏好：小窗口更偏局部句法，大窗口更偏主题/语义共现。
### 边界与工程
- 两者在大词表下都需要 Negative Sampling 或 Hierarchical Softmax 等输出近似。
- 高频词 subsampling 用来减少 “the/的” 等词产生的海量低信息 pair，与 Negative Sampling 是两个独立机制。
- 静态 Word2Vec 最终仍是一词一个向量，无法根据上下文消解 polysemy，这会自然连接到 BERT/ELMo。

## 7. 实现、复杂度与工程验证

- 把表示学习与共现统计、上下文依赖和梯度路径联系起来。
- 比较时同时讨论参数量、并行性、长期依赖和数据效率。
- 用小型可控任务验证“长依赖/低频词/一词多义”等具体假设。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 只说“一个正一个反”不谈优化特点。

## 9. 追问树

1. window size 怎么选？
2. subsampling 高频词有什么作用？

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

## 10. 面试现场自检

- [ ] 30-60 秒能给出结论，不绕弯。
- [ ] 能写出关键公式、shape 或状态转移。
- [ ] 至少能解释一个 Why 和一个 trade-off。
- [ ] 能举出一个失败模式或反例。
- [ ] 能回答两层追问。
- [ ] 能把答案连接到真实训练/检索/服务系统。

## 11. 参考资料

- [word2vec](https://arxiv.org/abs/1301.3781)
- [GloVe](https://aclanthology.org/D14-1162/)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q024 NLP 数据增强：怎么保证不破坏标签？](../02-classical-nlp/Q024-nlp-data-augmentation.md)
- [Q026 Word2Vec 为什么需要 Negative Sampling？](Q026-negative-sampling.md)
- [Q031 RNN 为什么梯度消失/爆炸？](Q031-rnn-gradient.md)
- [Q034 Seq2Seq 为什么需要 Attention？](Q034-seq2seq-attention.md)

## 13. 一句话收束

> **CBOW / Skip-Gram 的训练信号差异**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
