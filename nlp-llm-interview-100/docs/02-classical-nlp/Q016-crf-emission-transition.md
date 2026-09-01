---
id: Q016
title: "CRF 的 Emission 与 Transition Matrix 分别表示什么？"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★"
frequency: "★★★★"
tags:
  - classical-nlp
  - crf
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q016 CRF 的 Emission 与 Transition Matrix 分别表示什么？

[← Q015](Q015-bert-crf.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q017 →](Q017-chinese-word-segmentation.md)

> **难度**：★★  ·  **频率**：★★★★  ·  **标签**：`classical-nlp`, `crf`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q016.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

给定序列长度 T、标签数 K，emission 和 transition 分别是什么 shape？总分如何计算？

## 2. 面试官到底在考什么

是否真正理解 BERT-CRF 的张量。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

Emission 通常为 T×K，表示每个位置属于每个标签的局部分数；Transition 为 K×K，表示相邻 标签转移分数。序列总分是两者沿路径累加。

## 4. 白板核心公式

- $s(x,y)=\sum_i \mathrm{Emission}_i(y_i)+\sum_i\mathrm{Transition}(y_{i-1},y_i)$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：可以加入 START/STOP 状态。
- **PDF 基线要点**：训练计算 gold path score 与 log-partition 的差。
- **PDF 基线要点**：解码用 Viterbi，把 sum-product 换成 max-product/max-sum。
- **扩展理解**：Emission 是输入相关的局部证据，Transition 是标签结构先验；sequence score 是二者之和。
- **扩展理解**：训练用 log-partition function + dynamic programming，解码用 Viterbi。
- **扩展理解**：要能明确矩阵 shape，并解释 START/STOP state。

## 6. 专业深挖：原理、边界与工程

### Emission 与 Transition 的数学含义
- $E_{t,k}$ 是“位置 t 像标签 k 的局部证据”，常来自 encoder hidden 的 Linear 输出，不需要先 Softmax。
- $A_{i,j}$ 是从标签 i 到 j 的转移势能，标准一阶 CRF 在所有位置共享。序列分数为 emission 与 transition 之和。
- 训练时正确路径 score 要高，同时通过 partition function 与所有可能路径竞争；梯度可理解为 empirical feature count 减 model expected count。
### 边界与工程
- START/END transition 也属于模型的一部分，忘记它们会改变路径概率。
- Viterbi 把 forward 中的 logsumexp 换成 max，并保存 backpointer；二者是非常典型的“同一 DP，不同半环”。
- padding mask 不能只把 emission 置 0 后继续转移，应真正停止对应序列的状态更新。

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

- transition 不是“词之间转移”。
- 把概率和未归一化 score 混淆。

## 9. 追问树

1. 如何 batch 化 CRF？
2. padding mask 如何处理？

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

- [Q015 BERT 后为什么还要接 CRF？](Q015-bert-crf.md)
- [Q017 中文分词：传统方法与 LLM 时代如何看？](Q017-chinese-word-segmentation.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)

## 13. 一句话收束

> **Emission 与 Transition 的数学含义**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
