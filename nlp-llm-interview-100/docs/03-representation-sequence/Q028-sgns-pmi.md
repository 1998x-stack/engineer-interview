---
id: Q028
title: "SGNS 为什么与 PMI Matrix Factorization 有关系？"
chapter: "表示学习与序列模型"
difficulty: "★★★★"
frequency: "★★★"
tags:
  - representation-sequence
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q028 SGNS 为什么与 PMI Matrix Factorization 有关系？

[← Q027](Q027-hierarchical-softmax.md) | **第 3 章 · 表示学习与序列模型** | [Q029 →](Q029-glove-vs-word2vec.md)

> **难度**：★★★★  ·  **频率**：★★★  ·  **标签**：`representation-sequence`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q028.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

为什么常说 Skip-Gram with Negative Sampling 隐式分解 shifted PMI matrix？

## 2. 面试官到底在考什么

考察理论深度。

### 评分维度

- 先给训练目标或状态转移，再解释它解决上一代方法什么问题。
- 理解梯度、表示与上下文依赖。
- 能把历史模型与 Transformer 的演进关系讲清楚。

## 3. 30-60 秒标准回答

在理想化最优条件下，word-context 内积近似 PMI(w,c)-log k。说明预测式 embedding 与共现 统计矩阵并非完全割裂。

## 4. 白板核心公式

- $\mathrm{SGNS}\;\approx\;\mathrm{PMI}(w,c)-\log k$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：PMI 衡量联合出现相对独立出现的提升。
- **PDF 基线要点**：负采样数量 k 引入 shift。
- **PDF 基线要点**：真实训练中低维约束、采样、subsampling 等使关系是近似而非精确。
- **扩展理解**：SGNS 与 shifted PMI factorization 的关系揭示了分布式词向量背后的统计结构。
- **扩展理解**：关键等式不是说 SGNS“等于 SVD”，而是其最优点与 PMI-shift 有对应关系。
- **扩展理解**：该联系帮助解释窗口、负采样数和频率分布对 embedding 的影响。

## 6. 专业深挖：原理、边界与工程

### SGNS 与 Shifted PMI 的连接
- SGNS 的二分类最优 log-odds 可推导为数据共现概率与噪声概率之比；在经典假设下得到 $v_w^Tv_c\approx PMI(w,c)-\log k$。
- 因此 Word2Vec 并非“完全神秘的神经方法”：它通过 SGD 隐式完成一个低秩共现矩阵因子化，只是不显式构造整张 PMI 矩阵。
- $PMI(w,c)=\log\frac{P(w,c)}{P(w)P(c)}$ 衡量词与上下文相对独立基线的超额共现，而不是简单共同出现次数。
### 边界与工程
- 该等价依赖特定噪声分布、充分优化和足够维度等理想条件，实际 embedding 只是近似。
- PMI 对稀有 pair 方差很大，常需 PPMI、频率阈值和平滑。
- window、方向、距离加权决定共现定义，也就决定最终 embedding 学到的关系类型。

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

- 把等式当成训练代码中显式计算 PMI。

## 9. 追问树

1. PPMI 为什么把负 PMI 截为 0？
2. SVD 与 embedding 有什么关系？

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

- [Q027 Hierarchical Softmax 为什么是 O(log|V|)？](Q027-hierarchical-softmax.md)
- [Q029 GloVe 与 Word2Vec 的差异](Q029-glove-vs-word2vec.md)
- [Q031 RNN 为什么梯度消失/爆炸？](Q031-rnn-gradient.md)
- [Q034 Seq2Seq 为什么需要 Attention？](Q034-seq2seq-attention.md)

## 13. 一句话收束

> **SGNS 与 Shifted PMI 的连接**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
