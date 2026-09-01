---
id: Q075
title: "Sparse Retrieval 与 Dense Retrieval 的核心差异"
chapter: "检索、搜索与 RAG"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - retrieval-rag
  - retrieval
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异

[← Q074](../06-alignment/Q074-ppo-dpo-grpo.md) | **第 7 章 · 检索、搜索与 RAG** | [Q076 →](Q076-biencoder-vs-crossencoder.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`retrieval-rag`, `retrieval`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q075.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

BM25 与 dense retriever 各擅长什么？为什么生产常混合？

## 2. 面试官到底在考什么

现代搜索必答。

### 评分维度

- 把 recall、precision、latency 分阶段分析。
- 能从 index/negative sampling/rerank 解释系统设计。
- 评价必须端到端可诊断。

## 3. 30-60 秒标准回答

Sparse 强于精确词面、稀有实体、数字与可解释性；Dense 把 query/document 映射到低维向量， 擅长语义匹配。二者错误模式互补，混合检索常提升 recall。

## 4. 白板核心公式

- $s(q,d)=e_q^\top e_d$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：Dense 需要 ANN 索引与 embedding 更新。
- **PDF 基线要点**：Sparse 对词汇不匹配弱，但对新实体常稳。
- **PDF 基线要点**：多语言/跨语言检索时 dense 优势可能更明显。
- **扩展理解**：Sparse 依赖 lexical overlap，Dense 学语义向量；二者错误模式互补。
- **扩展理解**：专名、数字、稀有实体常由 sparse 占优，语义改写由 dense 占优。
- **扩展理解**：现代检索常通过 hybrid + rerank 组合。

## 6. 专业深挖：原理、边界与工程

### Sparse 与 Dense 的错误模式互补
- BM25/Sparse 强在精确 term、数字、ID、稀有实体和可解释倒排；Dense 将 query/document 映射到向量空间，能处理同义改写、语义匹配和跨语言。
- Dense 的优势来自训练出的连续表示，但也会把新实体/数字等细粒度词面信息“平均化”；Sparse 则对词汇 mismatch 天然脆弱。
- Hybrid Retrieval 的核心不是“取平均”，而是利用两类模型的互补召回错误。
### 边界与工程
- Dense 需要 ANN index、embedding version 与文档更新重编码；Sparse 的索引更新通常更直接。
- 多语言 dense 可能更强，但要看训练对齐数据；Sparse 可通过多语分词/翻译索引扩展。
- 生产常先做 union/merge，再用 RRF 或 reranker，而不是简单把不可比的 raw score 相加。

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

- 把 dense 说成“永远比 BM25 好”。

## 9. 追问树

1. SPLADE 属于 sparse 还是 dense？
2. hybrid score 怎么融合？

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

- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](../06-alignment/Q074-ppo-dpo-grpo.md)
- [Q076 Bi‑Encoder 与 Cross‑Encoder：为什么一快一准？](Q076-biencoder-vs-crossencoder.md)
- [Q084 如何完整评估一个 RAG 系统？](Q084-rag-evaluation.md)

## 13. 一句话收束

> **Sparse 与 Dense 的错误模式互补**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
