---
id: Q015
title: "BERT 后为什么还要接 CRF？"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - classical-nlp
  - bert
  - crf
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q015 BERT 后为什么还要接 CRF？

[← Q014](Q014-crf-vs-hmm.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q016 →](Q016-crf-emission-transition.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`classical-nlp`, `bert`, `crf`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q015.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

BERT 已经很强，NER 为什么仍有人在顶部加 CRF？

## 2. 面试官到底在考什么

理解 contextual feature 与 structured prediction 分工。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

BERT 提供上下文 token 表示与 emission score；若逐 token 独立 softmax，标签之间没有显式 转移约束。CRF 可学习 BIO/BIOES 等标签转移偏好并做全局最优解码。

## 4. 白板核心公式

- $s(x,y)=\sum_i E_{i,y_i}+\sum_i A_{y_{i-1},y_i}$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：BERT 解决“看上下文”，CRF 解决“标签序列结构”。
- **PDF 基线要点**：在数据量大、标签规则简单时，纯 token classifier 也可能足够。
- **PDF 基线要点**：生成式 LLM 做结构化抽取时，约束方式又发生变化。
- **扩展理解**：BERT 提供 contextual emission score，CRF 提供结构化标签转移约束，两者职责不同。
- **扩展理解**：CRF 的价值取决于标签间约束强度与数据量；某些任务上独立 softmax 已足够。
- **扩展理解**：不要回答成“BERT 不懂 BIO”，而要说它默认 loss 没显式建模全局标签路径。

## 6. 专业深挖：原理、边界与工程

### BERT 和 CRF 的分工
- BERT 提供上下文化 token hidden state，并通过 Linear 产生每个标签的 emission；独立 Softmax 默认每个 token 自己选标签，不显式建模标签之间的合法转移。
- CRF 把 emission 与 transition 相加形成整条序列分数，能够偏好/约束 BIO/BIOES 合法路径，并用 Viterbi 做全局最优解码。
- 因此不是“CRF 修正 BERT 错误”，而是“强表示 + 结构化预测”两层职责互补。
### 边界与工程
- 标签依赖弱、数据量大时 CRF 增益可能很小，独立 token classifier 更快更简单。
- 嵌套 NER、跨句实体不适合单一 BIO 链式标签，需要 span-based 或生成式方案。
- 比较模型时看 entity-level exact F1，而不是只看 token accuracy；后者会掩盖边界错误。

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

- 把 CRF 说成“纠正 BERT 错误”的万能模块。
- 没有说明训练/解码差异。

## 9. 追问树

1. 如何禁止 O→I-PER 之类非法转移？
2. Viterbi 的时间复杂度？

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

- [Q014 CRF 和 HMM 有什么根本区别？](Q014-crf-vs-hmm.md)
- [Q016 CRF 的 Emission 与 Transition Matrix 分别表示什么？](Q016-crf-emission-transition.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)

## 13. 一句话收束

> **BERT 和 CRF 的分工**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
