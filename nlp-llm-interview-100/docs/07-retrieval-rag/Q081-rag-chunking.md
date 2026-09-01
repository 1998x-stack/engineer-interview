---
id: Q081
title: "RAG Chunking：为什么“固定 500 tokens”不是答案？"
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

# Q081 RAG Chunking：为什么“固定 500 tokens”不是答案？

[← Q080](Q080-ivf-pq.md) | **第 7 章 · 检索、搜索与 RAG** | [Q082 →](Q082-hybrid-search-rrf.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`retrieval-rag`, `rag`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q081.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

如何选择 chunk size、overlap 与边界？

## 2. 面试官到底在考什么

理解 retrieval unit 与 context trade-off。

### 评分维度

- 把 recall、precision、latency 分阶段分析。
- 能从 index/negative sampling/rerank 解释系统设计。
- 评价必须端到端可诊断。

## 3. 30-60 秒标准回答

chunk 太小会丢上下文和指代，太大降低检索精度并浪费 context。应结合文档结构、标题层级、 段落/语义边界、模型窗口与 query 粒度，通过 retrieval + end-to-end eval 调参。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：可做 parent-child retrieval：小块召回、大块返回。
- **PDF 基线要点**：overlap 能缓解边界切断，但增加重复与索引量。
- **PDF 基线要点**：表格、代码、FAQ、合同应使用不同结构感知切分。
- **扩展理解**：chunk 是 retrieval unit，不是纯文本切割问题；应与文档结构、query 类型和生成上下文共同优化。
- **扩展理解**：固定 token 长度是 baseline，结构感知/语义切分常更合理。
- **扩展理解**：chunk overlap 会提升召回也会增加重复与上下文浪费。

## 6. 专业深挖：原理、边界与工程

### Chunking 本质是在选择“检索单元”
- Chunk 太小：证据被切碎、标题/上下文丢失；Chunk 太大：一个向量混入多个主题，dense 表示被平均，BM25 也受长度归一化影响，并浪费 LLM context token。
- 固定 500 token 只是 baseline；更合理可按 heading、paragraph、HTML block、语义边界做 structure-aware chunk，再用 token budget 限制。
- Overlap 可以缓解边界切断，但也引入重复索引和重复召回，需要在 recall 与索引膨胀间权衡。
### 边界与工程
- 最优 chunk size 与任务相关：事实 QA 喜欢局部证据，摘要/合同比较需要更长结构。
- 可以 decouple retrieval chunk 与 generation context：先检索小 chunk，再扩展到父 section/邻近窗口送给 LLM。
- 评估应同时看 answer-containing recall、duplicate context rate、context token cost 和最终 answer correctness。

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

- 只按 token 数切，无结构意识。

## 9. 追问树

1. 如何处理超长表格？
2. query-aware chunking 是否值得？

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

- [Q080 IVF‑PQ：如何用聚类与乘积量化压缩十亿向量？](Q080-ivf-pq.md)
- [Q082 Hybrid Search 与 RRF：为什么排名融合常比 raw score 加权稳？](Q082-hybrid-search-rrf.md)
- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](Q075-sparse-vs-dense-retrieval.md)
- [Q084 如何完整评估一个 RAG 系统？](Q084-rag-evaluation.md)

## 13. 一句话收束

> **Chunking 本质是在选择“检索单元”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
