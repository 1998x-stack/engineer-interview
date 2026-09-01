---
id: Q026
title: "Word2Vec 为什么需要 Negative Sampling？"
chapter: "表示学习与序列模型"
difficulty: "★★★"
frequency: "★★★★★"
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

# Q026 Word2Vec 为什么需要 Negative Sampling？

[← Q025](Q025-cbow-vs-skipgram.md) | **第 3 章 · 表示学习与序列模型** | [Q027 →](Q027-hierarchical-softmax.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`representation-sequence`, `word2vec`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q026.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

词表几十万时，Skip-Gram full softmax 为什么昂贵？Negative Sampling 如何改写目标？

## 2. 面试官到底在考什么

理解从 full softmax 到二分类近似。

### 评分维度

- 先给训练目标或状态转移，再解释它解决上一代方法什么问题。
- 理解梯度、表示与上下文依赖。
- 能把历史模型与 Transformer 的演进关系讲清楚。

## 3. 30-60 秒标准回答

full softmax 每次需对整个词表归一化。Negative Sampling 把一个正 word-context 对与 K 个 噪声负样本做二分类，使单步复杂度从 O(|V|) 降到 O(K)。

## 4. 白板核心公式

- $\log\sigma(v_o^\top v_i)+\sum_{k=1}^K\log\sigma(-v_k^\top v_i)$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：负样本分布经典做法与 unigram^0.75 有关。
- **PDF 基线要点**：Negative Sampling 的目标不是精确估计语言模型概率，而是学习好 embedding。
- **PDF 基线要点**：K 越大通常估计更好但计算更贵。
- **扩展理解**：Negative Sampling 把大词表 softmax 近似成若干二分类，使每步复杂度从 O(|V|) 降到 O(K)。
- **扩展理解**：负样本分布不是随便选，word2vec 使用 unigram^3/4 改善学习。
- **扩展理解**：它学习的是有用表示，不是严格归一化语言模型概率。

## 6. 专业深挖：原理、边界与工程

### Negative Sampling 把大词表问题改写成二分类
- 完整 Softmax 每个训练 pair 都要对 $|V|$ 个词归一化；Negative Sampling 只计算一个正 pair 和 K 个噪声负 pair，成本从词表级降到 $O(K)$。
- 目标 $\log\sigma(v_c^Tv_w)+\sum_k\log\sigma(-v_{n_k}^Tv_w)$ 的含义是让真实共现 dot product 变大、噪声 pair 变小，而不是直接学习严格归一化的 $P(w|c)$。
- 经典噪声分布使用 unigram$^{3/4}$：比原始 unigram 更平缓，避免最高频词垄断；比均匀采样又更容易得到“有信息的常见负例”。
### 边界与工程
- K 太少估计噪声大，太多计算线性上升且负例冗余；不是越多越好。
- 高频词 subsampling 发生在正 pair 构造阶段，Negative Sampling 发生在输出训练阶段，面试时不要混为一谈。
- 若任务需要真正的词概率而非 embedding 表示，Hierarchical/Adaptive/Full Softmax 的概率语义更直接。

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

- 误以为 negative sample 就是随机采句子。
- 不知道正负样本分别优化什么。

## 9. 追问树

1. 为什么高频词采样分布要平滑？
2. 与 Noise Contrastive Estimation 有何联系？

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

- [Q025 CBOW 与 Skip‑Gram：输入输出正好相反吗？](Q025-cbow-vs-skipgram.md)
- [Q027 Hierarchical Softmax 为什么是 O(log|V|)？](Q027-hierarchical-softmax.md)
- [Q031 RNN 为什么梯度消失/爆炸？](Q031-rnn-gradient.md)
- [Q034 Seq2Seq 为什么需要 Attention？](Q034-seq2seq-attention.md)

## 13. 一句话收束

> **Negative Sampling 把大词表问题改写成二分类**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
