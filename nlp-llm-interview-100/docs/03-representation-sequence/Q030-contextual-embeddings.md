---
id: Q030
title: "静态词向量为什么解决不了一词多义？"
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

# Q030 静态词向量为什么解决不了一词多义？

[← Q029](Q029-glove-vs-word2vec.md) | **第 3 章 · 表示学习与序列模型** | [Q031 →](Q031-rnn-gradient.md)

> **难度**：★★  ·  **频率**：★★★★  ·  **标签**：`representation-sequence`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q030.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

“bank”在河岸与银行语境中为什么需要不同表示？ELMo/BERT 如何解决？

## 2. 面试官到底在考什么

从 Word2Vec 过渡 BERT 的关键逻辑。

### 评分维度

- 先给训练目标或状态转移，再解释它解决上一代方法什么问题。
- 理解梯度、表示与上下文依赖。
- 能把历史模型与 Transformer 的演进关系讲清楚。

## 3. 30-60 秒标准回答

静态 embedding 为词表中每个词给一个固定向量；contextual encoder 让 token 表示成为整个 上下文的函数，因此同一 token 在不同句子中可得到不同向量。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：ELMo 用双向语言模型的上下文状态；BERT 用双向 Transformer。
- **PDF 基线要点**：tokenization 后的 subword 还需通过上下文组合成词义。
- **PDF 基线要点**：contextual embedding 并不保证所有语义可线性分离。
- **扩展理解**：静态词向量把词型映射到单一向量，无法根据上下文动态消歧。
- **扩展理解**：ELMo/BERT 让 token representation 成为整个上下文的函数。
- **扩展理解**：要区分 lexical embedding 与 contextual hidden state。

## 6. 专业深挖：原理、边界与工程

### 静态 Embedding 的根本表达限制
- 静态词表把每个词映射到固定 $E[w]$，所以 “apple” 在公司语境和水果语境得到同一个向量；polysemy 被压在一个平均表示里。
- Contextual Encoder 则输出 $h_i=f(x_{1:n},i)$，同一 token 的表示依赖整句，从而可以编码词义、句法角色、实体指代等。
- 注意 BERT 的“输入 embedding table”仍是静态的；真正上下文化的是经过 Transformer 层后的 hidden state。
### 边界与工程
- Contextual 并不意味着词义自动完美分离；层选择、上下文长度和训练目标都会影响表示。
- 一个“词”可能被 tokenizer 拆成多个 subword，词级任务需要明确首 token、平均或其他 pooling 规则。
- 静态 embedding 仍有低内存、可缓存、低延迟优势，轻量系统不必一概淘汰。

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

- 把 contextual embedding 解释成“每个词有多个预存向量”。

## 9. 追问树

1. 句向量怎么从 BERT token 表示得到？
2. 为什么 [CLS] 不一定是最佳通用语义向量？

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

- [Q029 GloVe 与 Word2Vec 的差异](Q029-glove-vs-word2vec.md)
- [Q031 RNN 为什么梯度消失/爆炸？](Q031-rnn-gradient.md)
- [Q034 Seq2Seq 为什么需要 Attention？](Q034-seq2seq-attention.md)

## 13. 一句话收束

> **静态 Embedding 的根本表达限制**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
