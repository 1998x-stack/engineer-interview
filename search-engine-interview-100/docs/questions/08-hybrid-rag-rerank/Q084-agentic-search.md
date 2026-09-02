---
id: Q084
title: "什么是 Agentic / Iterative Search？"
chapter: 8
chapter_title: "Hybrid Search、Neural Reranking 与 RAG"
difficulty: 5
frequency: "A"
roles: "LLM Search"
tags:
  - hybrid-search
  - reranking
  - rag
  - agentic-search
source: "搜索引擎算法岗面试宝典 PDF, 2026 Edition"
status: "expanded-v2"
last_updated: "2026-09-02"
---

# Q084 · 什么是 Agentic / Iterative Search？

[← 上一题](Q083-high-recall-rag-still-wrong.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · 下一题：无 →

> 本题“30 秒回答 / 深度拆解 / 原始追问 / Gotcha / 一句话记忆”来自配套 PDF；“工程化补充 / 推导 / 练习 / 追问参考回答”等为仓库扩展内容。

## 题目画像

| 维度 | 内容 |
|---|---|
| 难度 | 5/5 |
| 频率 | A |
| 适用岗位 | LLM Search |
| 所属章节 | [Hybrid Search、Neural Reranking 与 RAG](README.md) |
| 核心标签 | `hybrid-search`, `reranking`, `rag`, `agentic-search` |

## 面试官到底在考什么

这道题表面在问“什么是 Agentic / Iterative Search？”，实际主要看三件事：**是否掌握核心定义/机制、是否能说明边界与 trade-off、是否能把算法落到可观测的线上系统**。回答建议采用“结论 → 原理 → 极限/反例 → 工业实现 → 指标”的顺序。

## 30 秒回答

传统 retrieval 一次 query 后就固定结果；Agentic Search 允许模型根据当前证据判断缺口、生成下一 轮 query、执行多跳检索和 sufficiency check，直到证据足够或预算耗尽。

## 5 分钟深度回答

- Plan：把复杂问题拆成子问题。
- Retrieve：针对子问题检索。
- Inspect：抽取证据并发现缺口。
- Rewrite/Next-hop：根据已知信息生成下一步 query。
- Sufficiency：判断证据是否足够，避免无限循环。
- 关键工程问题：tool latency、query explosion、重复检索、引用追踪与预算控制。

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
**追问 1：如何定义停止条件？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 2：如何防止 agent 被错误证据带偏？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 3：多跳检索如何去重和缓存？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

## 第二轮专业扩展（v2）

> 本节是在第一版题解之上新增的工程与研究视角，目标是让回答达到高级搜索算法 / Relevance / Retrieval 面试的深度。

### 核心机制再拆一层

iterative search 让模型根据当前证据产生下一 query并检查 sufficiency；收益在多跳/开放问题，风险是成本、循环、错误累积与不可控 query drift。

不要停留在名词解释。面试时建议主动回答三个问题：**它改变了哪一个概率/排序/数据结构？它用什么近似换来了什么成本？它最容易在哪类 query 或数据分布上失败？**

### 数据链路与可复现性

Hybrid/RAG 链路要保留每个候选来自哪个 retriever、原始 score/rank、fusion score、rerank score、chunk→document lineage 和最终送入生成模型的 context 顺序。

建议把所有可能影响结果的资产版本化：`data/index snapshot → analyzer/feature schema → model/config → serving policy → evaluation set`。只有这样，线上 bad case 才能被可靠重放。

### 复杂度、成本与规模感

端到端成本是 lexical + dense + fusion + rerank + generation 的总和。很多 RAG 系统真正昂贵的不是 ANN，而是过大的 rerank depth 和冗余 context token。

回答复杂度时不要只写 Big-O；至少再补一个真实工程维度：**内存/字节、候选数、网络 fan-out、模型调用数、cache locality、p99 或更新成本**。算法岗高级面试非常看这种规模感。

### 白板公式 / 伪代码 / 实验抓手

本题不要求为了“显得技术”而硬写代码。白板上更重要的是把 **输入 → 状态/统计量 → 决策 → 输出 → 复杂度 → 失败边界** 连起来，并给出一个可验证的反例或极限情况。

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

- 如何定义停止条件？
- 如何防止 agent 被错误证据带偏？
- 多跳检索如何去重和缓存？

## 高频失分点 / Gotcha

Agentic 不等于“让 LLM 自由搜索很多次”；必须有预算、状态、证据与可验证终止条件。

### 加强版 Gotchas

- 不要把“算法名字”当作系统答案：面试官通常会继续问数据、参数、SLO、更新与失败恢复。
- 不要只报全局平均指标：至少按 head/tail query、语言/类目、文档长度、新老用户或 filter selectivity 做 slice。
- 不要把 offline gain 直接等价为 online gain：线上还有曝光偏差、延迟、缓存、展示和反馈环。
- 数学题至少检查一个极限情况；系统题至少做一次数量级估算。

## 实战练习

> **练习：** 画出 multi-hop agentic search 状态机，明确每轮的 stop/sufficiency condition。

完成标准：能在不看答案的情况下，先用 30 秒给结论，再用 5 分钟白板说明原理、至少两个 trade-off、一个 failure case 和验证指标。

## 一句话记忆

一次检索找答案，多次检索补证据链。

第九章分布式搜索与工程系统

算法最终要跑在真实服务里：掌握分片、NRT、CDC、缓存、尾延迟和故障诊断。

题号 题目 难度 Q85 为什么 Search Index 要做 Sharding？ 2/5 Q86 分布式 Search Query 的 Scatter-Gather 怎么工作？ 3/5 Q87 为什么每个 Shard 只返回 Local TopK 可能有问题？ 4/5 Q88 Primary Shard 与 Replica 的区别是什么？ 2/5 Q89 Shard 越多是不是查询越快？什么是 Over-sharding？ 3/5 Q90 什么是 Near Real-Time（NRT）Search？ 3/5 Q91 Refresh Interval 为什么存在 Freshness-Throughput Trade-off？ Trade-off？ 3/5 Q92 搜索索引如何与 MySQL/业务数据库保持同步？ 4/5 Q93 搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？一定最有效？ 3/5 Q94 搜索延迟从 50ms 突然变成 2s，怎么系统排查？ 5/5

## 参考资料

- **R13** [BEIR benchmark](https://arxiv.org/abs/2104.08663)

[← 上一题](Q083-high-recall-rag-still-wrong.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · 下一题：无 →
