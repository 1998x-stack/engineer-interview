---
id: Q013
title: "HMM：三个基本问题与两条核心假设"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★★"
frequency: "★★★★"
tags:
  - classical-nlp
  - hmm
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q013 HMM：三个基本问题与两条核心假设

[← Q012](../01-ml-foundations/Q012-adam-vs-adamw.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q014 →](Q014-crf-vs-hmm.md)

> **难度**：★★★  ·  **频率**：★★★★  ·  **标签**：`classical-nlp`, `hmm`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q013.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

HMM 的状态、观测、转移、发射分别是什么？三个基本问题如何求解？

## 2. 面试官到底在考什么

从概率图角度理解早期序列标注。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

HMM 是生成式序列模型，假设隐藏状态满足一阶马尔可夫，当前观测只依赖当前隐藏状态。Eval- uation 用 Forward，Decoding 用 Viterbi，Learning 常用 Baum-Welch/EM。

## 4. 白板核心公式

- $P(x,z)=P(z_1)\prod_{t=2}^T P(z_t|z_{t-1})\prod_{t=1}^T P(x_t|z_t)$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：联合分布可分解为初始状态、状态转移和发射概率的乘积。
- **PDF 基线要点**：Forward 计算所有路径概率之和；Viterbi 只保留最优路径。
- **PDF 基线要点**：HMM 对特征依赖假设强，难以使用丰富重叠特征。
- **扩展理解**：HMM 的三类问题对应 Forward、Viterbi 与 Baum-Welch/EM，分别是求概率、求最优路径、估参数。
- **扩展理解**：生成式假设带来可解释性，也限制了特征表达能力。
- **扩展理解**：面试常追问前向算法与 Viterbi 的“sum-product vs max-product”差异。

## 6. 专业深挖：原理、边界与工程

### HMM 的所有算法来自同一个分解
- HMM 联合分布可写为 $P(z_1)\prod_tP(z_t|z_{t-1})\prod_tP(x_t|z_t)$，依赖一阶 Markov 和 emission 条件独立假设。
- Forward 是对所有隐状态路径求和，Viterbi 是对所有路径取 max；递推结构相似，只是聚合代数不同。
- Baum–Welch 是 EM：E 步用 forward-backward 计算状态/转移后验期望，M 步更新初始、转移和 emission 参数。
### 边界与工程
- 长序列概率连乘容易 underflow，应使用 log-space 或 scaling factors。
- K 个状态时训练/解码典型复杂度 $O(TK^2)$；稀疏转移可降低实际代价。
- HMM 的限制不是“传统”，而是观测生成假设和局部 Markov 结构使其难以利用任意上下文特征。

## 7. 实现、复杂度与工程验证

- 给出状态/标签空间、独立性假设和训练/解码复杂度。
- 区分局部 score、全局归一化与解码约束。
- 真实 NLP 数据要考虑 OOV、标注规范、领域词典和 span 对齐。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 把 Forward 与 Viterbi 混淆。
- 只背算法名称，不会写递推。

## 9. 追问树

1. Backward 算法作用？
2. 为什么 EM 能训练含隐变量模型？

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

- [CRF](https://repository.upenn.edu/cis_papers/159/)
- [BM25 overview (Stanford IR book)](https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q012 Adam 与 AdamW 到底差在哪？](../01-ml-foundations/Q012-adam-vs-adamw.md)
- [Q014 CRF 和 HMM 有什么根本区别？](Q014-crf-vs-hmm.md)
- [Q015 BERT 后为什么还要接 CRF？](Q015-bert-crf.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)

## 13. 一句话收束

> **HMM 的所有算法来自同一个分解**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
