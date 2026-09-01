---
id: Q084
title: "如何完整评估一个 RAG 系统？"
chapter: "检索、搜索与 RAG"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - retrieval-rag
  - rag
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q084 如何完整评估一个 RAG 系统？

[← Q083](Q083-reranker.md) | **第 7 章 · 检索、搜索与 RAG** | [Q085 →](../08-data-evaluation/Q085-pretraining-data-pipeline.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`retrieval-rag`, `rag`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q084.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

设计 RAG 离线评测体系。

## 2. 面试官到底在考什么

必须拆检索与生成，不能只看答案。

### 评分维度

- 把 recall、precision、latency 分阶段分析。
- 能从 index/negative sampling/rerank 解释系统设计。
- 评价必须端到端可诊断。

## 3. 30-60 秒标准回答

至少分 retrieval 与 generation：检索看 Recall@K、MRR/NDCG、gold evidence coverage；生 成看 correctness、faithfulness/groundedness、citation accuracy；最终再看 end-to-end task success、latency、cost。

## 4. 白板核心公式

- $P(\mathrm{correct})\approx P(\mathrm{retrieve\ evidence})\times P(\mathrm{answer\ correct}|\mathrm{evidence})$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：若 gold doc 未召回，生成错应归因 retrieval。
- **PDF 基线要点**：答案正确但引用错，仍是 groundedness/citation failure。
- **PDF 基线要点**：LLM-as-judge 需用人工集/确定性验证校准。
- **扩展理解**：RAG 必须拆 retrieval quality、context quality、generation correctness/faithfulness 与端到端 success。
- **扩展理解**：只有 answer score 不能定位问题：错误可能来自没召回、召回噪声、上下文截断或生成幻觉。
- **扩展理解**：评估集应包含无答案、时效性、冲突文档和 long-tail query。

## 6. 专业深挖：原理、边界与工程

### RAG Evaluation 必须拆 Retrieval 与 Generation
- Retrieval 层看 Recall@K、MRR、NDCG、evidence coverage；Generation 层看 correctness、faithfulness/groundedness、citation accuracy、format/safety。
- 端到端错误要归因：答案错可能因为没召回、召回但排太后、context 被截断、模型忽略证据、证据本身矛盾。
- “LLM Judge 总分”不能替代分层指标，否则系统回归时无法定位是 Retriever 还是 Generator。
### 边界与工程
- 对多答案/多证据问题，单 gold passage Recall 会低估合理召回，需要 evidence set 或人工 adjudication。
- Faithfulness 与 correctness 不同：模型可以忠于错误文档，也可以凭参数知识答对但没有 grounded citation。
- 线上还要监控 latency、context token、empty/no-answer rate、用户反馈和 corpus freshness。

## 7. 实现、复杂度与工程验证

- 拆成 recall→rerank→generation，各层用不同指标和延迟预算。
- 检索系统必须同时考虑 index freshness、长尾实体、ANN recall 与线上 latency。
- 任何更强 reranker 都要回答每个 query 需要多少次模型前向。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 只看 BLEU/ROUGE。
- 只评价生成，不评价召回。

## 9. 追问树

1. 没有 gold evidence 时怎么评？
2. 线上如何做 failure taxonomy？

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

- [DPR](https://arxiv.org/abs/2004.04906)
- [Sentence-BERT](https://arxiv.org/abs/1908.10084)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q083 为什么 Reranker 通常比 Retriever 更准？](Q083-reranker.md)
- [Q085 预训练数据清洗 Pipeline 应如何设计？](../08-data-evaluation/Q085-pretraining-data-pipeline.md)
- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](Q075-sparse-vs-dense-retrieval.md)

## 13. 一句话收束

> **RAG Evaluation 必须拆 Retrieval 与 Generation**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
