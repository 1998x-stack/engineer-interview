---
id: Q082
title: "RAG 的 Chunk Size 应该怎么选？"
chapter: 8
chapter_title: "Hybrid Search、Neural Reranking 与 RAG"
difficulty: 4
frequency: "S"
roles: "RAG Retrieval"
tags:
  - hybrid-search
  - reranking
  - rag
source: "搜索引擎算法岗面试宝典 PDF, 2026 Edition"
status: "expanded-v2"
last_updated: "2026-09-02"
---

# Q082 · RAG 的 Chunk Size 应该怎么选？

[← 上一题](Q081-colbert-late-interaction.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q083-high-recall-rag-still-wrong.md)

> 本题“30 秒回答 / 深度拆解 / 原始追问 / Gotcha / 一句话记忆”来自配套 PDF；“工程化补充 / 推导 / 练习 / 追问参考回答”等为仓库扩展内容。

## 题目画像

| 维度 | 内容 |
|---|---|
| 难度 | 4/5 |
| 频率 | S |
| 适用岗位 | RAG Retrieval |
| 所属章节 | [Hybrid Search、Neural Reranking 与 RAG](README.md) |
| 核心标签 | `hybrid-search`, `reranking`, `rag` |

## 面试官到底在考什么

这道题表面在问“RAG 的 Chunk Size 应该怎么选？”，实际主要看三件事：**是否掌握核心定义/机制、是否能说明边界与 trade-off、是否能把算法落到可观测的线上系统**。回答建议采用“结论 → 原理 → 极限/反例 → 工业实现 → 指标”的顺序。

## 30 秒回答

没有通用最优值。Chunk 太小会丢上下文、跨句关系和表格结构；太大则 embedding 主题混杂、检索 精度下降，并浪费生成上下文。需要结合文档结构、retriever、reranker 与最终 QA 做端到端选择。

## 5 分钟深度回答

- 优先结构感知 chunk：heading/paragraph/table/code block，而不是固定字符硬切。
- Overlap 能缓解边界信息丢失，但会制造重复候选和 token 浪费。
- 可使用 parent-child retrieval：小 chunk 检索，返回更大的 parent context。
- 对事实型 QA 与长篇解释型 QA，最佳 chunk 粒度通常不同。
- 评价至少要同时看 retrieval recall、context precision、answer quality、latency/token cost。

## 进一步深挖：从“会答”到“能做”

#### Hybrid / RAG 的诊断矩阵

把失败分成四格：① lexical miss / dense hit；② lexical hit / dense miss；③两路都 hit 但 fusion/rerank 错；④候选正确但生成器未利用。只有第 1/2 类应该优先改 retriever；第 3 类改 fusion/rerank；第 4 类要改 context packing、prompt 或 generator。

### 本章高级视角

Hybrid 不是 `BM25 + vector` 两个 API 调用。高质量系统需要 query routing、candidate budget、fusion、dedup、rerank、context packing 与 fallback。RAG 还应追加 answer-level evaluation，避免只优化 retrieval 指标而生成质量不升。

### 工业落地时必须补充的 6 个问题

1. **数据从哪里来？** 标签/统计量/embedding/点击信号如何生成，是否存在偏差或版本漂移？
2. **线上预算是多少？** candidate 数、CPU/GPU、内存、网络 fan-out 与 p99 latency 分别是多少？
3. **离线怎么验证？** 需要什么 golden set、oracle analysis、slice 与 counterfactual/ablation？
4. **线上看什么？** 除主指标外，至少准备 latency、zero-result/timeout、quality guardrail 与成本指标。
5. **失败如何降级？** 模型、向量服务、feature store 或 shard 异常时是否能回退到 lexical / cache / static rule？
6. **如何回滚和复现？** index、model、feature schema、query rewrite policy 是否版本化并可灰度？

### 追问链：参考回答
**追问 1：Overlap 设太大有什么问题？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 2：表格应该如何 chunk？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 3：是否可以 query-aware dynamic chunking？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

## 第二轮专业扩展（v2）

> 本节是在第一版题解之上新增的工程与研究视角，目标是让回答达到高级搜索算法 / Relevance / Retrieval 面试的深度。

### 核心机制再拆一层

chunk 是 retrieval unit 不是固定字符切片；需考虑语义边界、overlap、metadata、parent-child；通过 answer utility 而非只看 retrieval metric 选 size。

不要停留在名词解释。面试时建议主动回答三个问题：**它改变了哪一个概率/排序/数据结构？它用什么近似换来了什么成本？它最容易在哪类 query 或数据分布上失败？**

### 数据链路与可复现性

Hybrid/RAG 链路要保留每个候选来自哪个 retriever、原始 score/rank、fusion score、rerank score、chunk→document lineage 和最终送入生成模型的 context 顺序。

建议把所有可能影响结果的资产版本化：`data/index snapshot → analyzer/feature schema → model/config → serving policy → evaluation set`。只有这样，线上 bad case 才能被可靠重放。

### 复杂度、成本与规模感

端到端成本是 lexical + dense + fusion + rerank + generation 的总和。很多 RAG 系统真正昂贵的不是 ANN，而是过大的 rerank depth 和冗余 context token。

回答复杂度时不要只写 Big-O；至少再补一个真实工程维度：**内存/字节、候选数、网络 fan-out、模型调用数、cache locality、p99 或更新成本**。算法岗高级面试非常看这种规模感。

### 白板公式 / 伪代码 / 实验抓手

实验矩阵至少同时扫描 `chunk_size × overlap × top_k × rerank_k`，并记录：retrieval recall、context precision、duplicate-token ratio、最终 answer score、prompt tokens。单独最大化 chunk-level Recall 很容易选出过大的 chunk。

### 失败模式与线上诊断

分离 retrieval miss、fusion miss、rerank miss、context packing miss、generation miss；只有这样才能知道 Recall 已高时为什么答案仍错。

诊断时优先问：“**正确答案在哪一步第一次消失？**”如果到当前阶段输入里就没有正确候选，这一阶段再复杂也无法修复；如果候选存在但顺序错，才进入评分、特征、模型或融合分析。

### 可观测性：上线后必须能回答什么

至少记录 source-wise Recall、union oracle、RRF/fusion contribution、rerank NDCG、context precision/recall、duplicate ratio、answer groundedness 与 token cost。

最少保留按 query slice 的指标，而不是只看全局均值。常见 slice 包括 head/tail、navigational/informational、rare entity、语言/地区、长短 query、长短文档、新老内容、filter selectivity 与设备。

### Senior / Staff 级追问

1. **怎样用 oracle fusion/rerank/generation 分析端到端瓶颈？**
   - 回答应先定义目标与约束，再给实验设计；不要只给“换某算法”的结论。
2. **如果只能保留一个 fallback channel，你选 lexical 还是 dense，为什么？**
   - 回答应包含可观测信号、对照/消融、上线 guardrail 和失败回退。

Staff 级回答要做 end-to-end attribution：为每个 stage 设计 oracle replacement，估算若该阶段完美时最终答案能提升多少，从而决定下一笔工程预算投哪里。

### 面试回答分层标准

- **及格（60 分）**：定义正确，能说明输入/输出与一个核心优缺点。
- **较强（75 分）**：能写关键公式/流程，说明至少两个 trade-off，并指出适用与失败场景。
- **高级（85 分）**：能给数量级或复杂度，说明数据如何构建、线上如何观测、如何用实验验证。
- **Senior/Staff（90+）**：能把该技术放进完整搜索链路，讨论 SLO、成本、bias、降级、版本化、回滚和优先级，并能用 oracle/ablation 证明为什么要做这项改动。

### 复习时建议做的最小实验

把本题做成一个可复现小实验：固定一组 20–100 个 query 和 golden relevance，改变**一个**关键变量，记录质量、延迟/成本和失败样本。最终产出一张 `quality–cost` 曲线和 5 个 bad cases。这样面试时就不再只是“背知识”，而是能讲出自己的工程判断。

## PDF 原始追问链

- Overlap 设太大有什么问题？
- 表格应该如何 chunk？
- 是否可以 query-aware dynamic chunking？

## 高频失分点 / Gotcha

“512 tokens 是最佳实践”不是结论，只是常见起点。

### 加强版 Gotchas

- 不要把“算法名字”当作系统答案：面试官通常会继续问数据、参数、SLO、更新与失败恢复。
- 不要只报全局平均指标：至少按 head/tail query、语言/类目、文档长度、新老用户或 filter selectivity 做 slice。
- 不要把 offline gain 直接等价为 online gain：线上还有曝光偏差、延迟、缓存、展示和反馈环。
- 数学题至少检查一个极限情况；系统题至少做一次数量级估算。

## 实战练习

> **练习：** 对同一文档尝试 128/256/512/1024 token chunk，并比较 retrieval 与 answer quality。

完成标准：能在不看答案的情况下，先用 30 秒给结论，再用 5 分钟白板说明原理、至少两个 trade-off、一个 failure case 和验证指标。

## 一句话记忆

Chunk size 是检索与生成共同的超参数。

## 参考资料

- **R13** [BEIR benchmark](https://arxiv.org/abs/2104.08663)

[← 上一题](Q081-colbert-late-interaction.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q083-high-recall-rag-still-wrong.md)
