---
id: Q077
title: "为什么搜索系统通常是多阶段 Retrieval→Rerank？"
chapter: "检索、搜索与 RAG"
difficulty: "★★"
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

# Q077 为什么搜索系统通常是多阶段 Retrieval→Rerank？

[← Q076](Q076-biencoder-vs-crossencoder.md) | **第 7 章 · 检索、搜索与 RAG** | [Q078 →](Q078-dense-retrieval-negatives.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`retrieval-rag`, `retrieval`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q077.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

为什么不直接用最强 Cross-Encoder 对全库搜索？

## 2. 面试官到底在考什么

考察系统级 recall/precision/cost 权衡。

### 评分维度

- 把 recall、precision、latency 分阶段分析。
- 能从 index/negative sampling/rerank 解释系统设计。
- 评价必须端到端可诊断。

## 3. 30-60 秒标准回答

大库中昂贵模型无法逐文档运行，因此先用高召回、低成本 retriever 把候选从百万/十亿缩到百/千， 再用更强 reranker 精排，最后给 LLM 少量高质量 context。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：每阶段的目标不同：召回阶段优先 Recall，排序阶段优先 top quality。
- **PDF 基线要点**：可继续加 rule/authority/freshness 重新排序。
- **PDF 基线要点**：端到端优化要避免某阶段指标提升却损伤最终回答。
- **扩展理解**：多阶段架构让廉价高召回模块先缩小候选，再用昂贵高精度模型精排。
- **扩展理解**：每一阶段都要有独立 recall budget 与 latency budget。
- **扩展理解**：系统优化目标是端到端 utility，而不是单模块最高分。

## 6. 专业深挖：原理、边界与工程

### 多阶段检索是计算预算分配问题
- 大规模语料不可能对百万/十亿文档逐一运行昂贵 Cross-Encoder/LLM，因此先用便宜 retriever 把候选压到几百/几千，再用更强模型逐级精排。
- 前级优化 recall，后级优化 precision；前级漏掉的相关文档后级无法恢复，所以每层的错误代价不对称。
- 典型链路可扩成 query understanding → lexical/dense retrieval → fusion → cross-encoder rerank → LLM context selection/generation。
### 边界与工程
- 每加一级都增加 latency、故障点和特征/版本同步成本，不能无限堆模型。
- Top-K 需要按 recall–latency 曲线调，不是固定“1000→100→10”的教条。
- 线上应记录每阶段 candidate set、score 和最终点击/答案贡献，才能定位回归发生在哪一级。

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

- 只说“为了快”。

## 9. 追问树

1. 候选 K 取多大怎么定？
2. cascade 如何做早退？

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

- [Q076 Bi‑Encoder 与 Cross‑Encoder：为什么一快一准？](Q076-biencoder-vs-crossencoder.md)
- [Q078 Dense Retrieval 的负样本怎么构造？](Q078-dense-retrieval-negatives.md)
- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](Q075-sparse-vs-dense-retrieval.md)
- [Q084 如何完整评估一个 RAG 系统？](Q084-rag-evaluation.md)

## 13. 一句话收束

> **多阶段检索是计算预算分配问题**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
