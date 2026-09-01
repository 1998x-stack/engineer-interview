---
id: Q029
title: "GloVe 与 Word2Vec 的差异"
chapter: "表示学习与序列模型"
difficulty: "★★"
frequency: "★★★"
tags:
  - representation-sequence
  - word2vec
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q029 GloVe 与 Word2Vec 的差异

[← Q028](Q028-sgns-pmi.md) | **第 3 章 · 表示学习与序列模型** | [Q030 →](Q030-contextual-embeddings.md)

> **难度**：★★  ·  **频率**：★★★  ·  **标签**：`representation-sequence`, `word2vec`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q029.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

GloVe 为什么强调 global co-occurrence？与 Word2Vec 的训练视角有什么不同？

## 2. 面试官到底在考什么

理解 count-based 与 predictive 两类方法。

### 评分维度

- 先给训练目标或状态转移，再解释它解决上一代方法什么问题。
- 理解梯度、表示与上下文依赖。
- 能把历史模型与 Transformer 的演进关系讲清楚。

## 3. 30-60 秒标准回答

GloVe 显式使用词共现矩阵并拟合 log co-occurrence；Word2Vec 从局部窗口采样训练预测任务。 二者都将统计结构压入低维向量。

## 4. 白板核心公式

- $J=\sum_{ij}f(X_{ij})(w_i^\top\tilde w_j+b_i+\tilde b_j-\log X_{ij})^2$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：GloVe 的 weighting function 抑制极少或极高共现带来的不稳定。
- **PDF 基线要点**：Word2Vec 更像在线采样优化，GloVe 更显式依赖预统计。
- **PDF 基线要点**：今天两者主要作为理解 embedding 的经典基础。
- **扩展理解**：GloVe 显式拟合全局共现统计，word2vec 通过预测任务隐式学习。
- **扩展理解**：二者都利用局部窗口共现，只是优化形式不同。
- **扩展理解**：面试可继续比较稀有词、训练并行性和静态 embedding 的共同局限。

## 6. 专业深挖：原理、边界与工程

### GloVe 与 Word2Vec 的差别不止“全局 vs 局部”
- Word2Vec 通过预测任务从 center-context pair 学表示；GloVe 先统计全局共现矩阵，再拟合 $w_i^T\tilde w_j+b_i+\tilde b_j\approx\log X_{ij}$。
- GloVe 的 weighting function 控制罕见 noisy pair 和超高频 pair 的贡献；取 log 则压缩跨多个数量级的计数动态范围。
- SGNS 与 PMI factorization 的理论关系说明二者其实都在压缩词-上下文统计，只是优化形式与数据管线不同。
### 边界与工程
- GloVe 需要构建/存储稀疏共现矩阵，大语料 I/O 和内存成本高；Word2Vec 更适合在线流式 pair 训练。
- 两者都属于静态词向量，无法根据当前句子改变词义表示。
- 公平比较要固定 corpus、window、vocab、subsampling 等预处理，否则差异未必来自算法本身。

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

- 只说“GloVe 是全局、Word2Vec 是局部”但不解释目标函数。

## 9. 追问树

1. 为什么词向量能出现线性类比？
2. 静态 embedding 的根本限制？

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

- [Q028 SGNS 为什么与 PMI Matrix Factorization 有关系？](Q028-sgns-pmi.md)
- [Q030 静态词向量为什么解决不了一词多义？](Q030-contextual-embeddings.md)
- [Q031 RNN 为什么梯度消失/爆炸？](Q031-rnn-gradient.md)
- [Q034 Seq2Seq 为什么需要 Attention？](Q034-seq2seq-attention.md)

## 13. 一句话收束

> **GloVe 与 Word2Vec 的差别不止“全局 vs 局部”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
