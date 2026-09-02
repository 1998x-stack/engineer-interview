---
id: Q098
title: "系统设计：10 亿文档 Semantic Search"
chapter: 10
chapter_title: "综合系统设计与 0→1 方法论"
difficulty: 5
frequency: "S"
roles: "Vector Search"
tags:
  - system-design
  - search-architecture
  - staff-interview
  - semantic-search
source: "搜索引擎算法岗面试宝典 PDF, 2026 Edition"
status: "expanded-v2"
last_updated: "2026-09-02"
---

# Q098 · 系统设计：10 亿文档 Semantic Search

[← 上一题](Q097-system-design-query-autocomplete.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q099-system-design-hybrid-search.md)

> 本题“30 秒回答 / 深度拆解 / 原始追问 / Gotcha / 一句话记忆”来自配套 PDF；“工程化补充 / 推导 / 练习 / 追问参考回答”等为仓库扩展内容。

## 题目画像

| 维度 | 内容 |
|---|---|
| 难度 | 5/5 |
| 频率 | S |
| 适用岗位 | Vector Search |
| 所属章节 | [综合系统设计与 0→1 方法论](README.md) |
| 核心标签 | `system-design`, `search-architecture`, `staff-interview`, `semantic-search` |

## 面试官到底在考什么

这道题表面在问“系统设计：10 亿文档 Semantic Search”，实际主要看三件事：**是否掌握核心定义/机制、是否能说明边界与 trade-off、是否能把算法落到可观测的线上系统**。回答建议采用“结论 → 原理 → 极限/反例 → 工业实现 → 指标”的顺序。

## 30 秒回答

先做资源预算，再选索引。1B×768 float32 仅原始向量约 3.07TB，因此通常需要分片、压缩或降维；再 根据 recall/p99/QPS 选择 HNSW、IVF-PQ 或混合架构。

## 5 分钟深度回答

- 需求：metric、TopK、target Recall@K、QPS、p99、update rate、memory budget、GPU/CPU。
- Embedding pipeline：versioned model → batch encode → index build → shadow validation
→ atomic publish。
- Index：若内存充足且重 recall，可 HNSW；极大规模/强压缩偏 IVFPQ/OPQ；热点可用 HNSW、
冷数据用 IVF-PQ。
- Shard：hash/tenant/semantic routing；查询并发 fan-out，局部 ANN topK 后全局 merge。
- 更新：新向量增量层 + 周期性主索引 rebuild，避免分布漂移。
- 评估：ANN recall（相对 exact ground truth）与 retrieval relevance 分开测。

## 数学 / 白板推导

### 10 亿向量的第一性估算

假设 768 维 float32：

$$768\times4=3072\text{ bytes/vector}$$

$$10^9\times3072\approx3.07\text{ TB}$$

这还没有算 DocID、HNSW links、metadata、replica 与 allocator overhead。系统设计里必须先做这个数量级估算，再讨论 HNSW、IVF-PQ、SQ/PQ、分片和冷热分层。

## 进一步深挖：从“会答”到“能做”

#### Staff 级系统设计评分点

系统设计不是组件清单，而是**约束驱动的决策记录**。先报规模、QPS、update rate、freshness、p99 与 quality target；每选一个索引/模型，都说明它解决哪个瓶颈、付出什么代价、如何降级和如何验证收益。

### 本章高级视角

系统设计最终看优先级。最好的答案会先用 oracle/error analysis 找瓶颈，然后选择最低成本的改动，并定义 rollout、guardrail、rollback。不要把“上更大模型”当默认方案。

### 工业落地时必须补充的 6 个问题

1. **数据从哪里来？** 标签/统计量/embedding/点击信号如何生成，是否存在偏差或版本漂移？
2. **线上预算是多少？** candidate 数、CPU/GPU、内存、网络 fan-out 与 p99 latency 分别是多少？
3. **离线怎么验证？** 需要什么 golden set、oracle analysis、slice 与 counterfactual/ablation？
4. **线上看什么？** 除主指标外，至少准备 latency、zero-result/timeout、quality guardrail 与成本指标。
5. **失败如何降级？** 模型、向量服务、feature store 或 shard 异常时是否能回退到 lexical / cache / static rule？
6. **如何回滚和复现？** index、model、feature schema、query rewrite policy 是否版本化并可灰度？

### 追问链：参考回答
**追问 1：128GB/节点、32 节点够不够？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 2：PQ code 32 bytes 时 1B 需要多少空间？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 3：如何无停机切 embedding model？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

## 第二轮专业扩展（v2）

> 本节是在第一版题解之上新增的工程与研究视角，目标是让回答达到高级搜索算法 / Relevance / Retrieval 面试的深度。

### 核心机制再拆一层

先算 1B embeddings 的原始 3TB+ 存储，再选 HNSW/IVF-PQ/分片；讨论 metadata filter、更新、GPU/CPU、replica 与 exact-recall benchmark。

不要停留在名词解释。面试时建议主动回答三个问题：**它改变了哪一个概率/排序/数据结构？它用什么近似换来了什么成本？它最容易在哪类 query 或数据分布上失败？**

### 数据链路与可复现性

系统设计先定义 corpus、query traffic、update/freshness、label/logging、tenant/security，再画离线 indexing 与在线 serving 两条链路；否则很容易只画出“组件名拼图”。

建议把所有可能影响结果的资产版本化：`data/index snapshot → analyzer/feature schema → model/config → serving policy → evaluation set`。只有这样，线上 bad case 才能被可靠重放。

### 复杂度、成本与规模感

必须给数量级：文档数、平均文档大小、索引膨胀、embedding bytes、QPS、candidate depth、rerank cost、p99 SLA、峰值系数和副本数。数字可以假设，但要自洽。

回答复杂度时不要只写 Big-O；至少再补一个真实工程维度：**内存/字节、候选数、网络 fan-out、模型调用数、cache locality、p99 或更新成本**。算法岗高级面试非常看这种规模感。

### 白板公式 / 伪代码 / 实验抓手

容量估算至少写三行：`raw vectors ≈ 3.07 TB`（1B×768×fp32）；若保留 2 replicas 则仅原始向量约 6.1 TB；若用 PQ 96B/code，codes 约 96 GB/replica，再加 IDs、coarse index、metadata 与冗余。

### 失败模式与线上诊断

设计中必须明确 degraded mode：vector service 不可用、某 shard 超时、feature store 超时、LLM rewrite 超时、CDC 落后时分别返回什么。

诊断时优先问：“**正确答案在哪一步第一次消失？**”如果到当前阶段输入里就没有正确候选，这一阶段再复杂也无法修复；如果候选存在但顺序错，才进入评分、特征、模型或融合分析。

### 可观测性：上线后必须能回答什么

从业务 metric → retrieval/rank metric → stage latency → infra saturation 建立四层 dashboard，并保留 trace 能回放单个 query。

最少保留按 query slice 的指标，而不是只看全局均值。常见 slice 包括 head/tail、navigational/informational、rare entity、语言/地区、长短 query、长短文档、新老内容、filter selectivity 与设备。

### Senior / Staff 级追问

1. **先给出三项最关键的容量假设，并说明假设错 10× 时架构是否仍成立。**
   - 回答应先定义目标与约束，再给实验设计；不要只给“换某算法”的结论。
2. **如果预算砍半，你删掉哪个组件，如何量化损失？**
   - 回答应包含可观测信号、对照/消融、上线 guardrail 和失败回退。

Staff 级设计最重要的是决策顺序：先找瓶颈与 oracle 上限，再做最低成本实验；架构图必须同时包含 rollout、guardrail、rollback、capacity headroom 与长期数据飞轮。

### 面试回答分层标准

- **及格（60 分）**：定义正确，能说明输入/输出与一个核心优缺点。
- **较强（75 分）**：能写关键公式/流程，说明至少两个 trade-off，并指出适用与失败场景。
- **高级（85 分）**：能给数量级或复杂度，说明数据如何构建、线上如何观测、如何用实验验证。
- **Senior/Staff（90+）**：能把该技术放进完整搜索链路，讨论 SLO、成本、bias、降级、版本化、回滚和优先级，并能用 oracle/ablation 证明为什么要做这项改动。

### 复习时建议做的最小实验

把本题做成一个可复现小实验：固定一组 20–100 个 query 和 golden relevance，改变**一个**关键变量，记录质量、延迟/成本和失败样本。最终产出一张 `quality–cost` 曲线和 5 个 bad cases。这样面试时就不再只是“背知识”，而是能讲出自己的工程判断。

## PDF 原始追问链

- 128GB/节点、32 节点够不够？
- PQ code 32 bytes 时 1B 需要多少空间？
- 如何无停机切 embedding model？

## 高频失分点 / Gotcha

语义搜索设计不能只说“用 Milvus/FAISS”；真正考的是数量级与 trade-off。

### 加强版 Gotchas

- 不要把“算法名字”当作系统答案：面试官通常会继续问数据、参数、SLO、更新与失败恢复。
- 不要只报全局平均指标：至少按 head/tail query、语言/类目、文档长度、新老用户或 filter selectivity 做 slice。
- 不要把 offline gain 直接等价为 online gain：线上还有曝光偏差、延迟、缓存、展示和反馈环。
- 数学题至少检查一个极限情况；系统题至少做一次数量级估算。

## 实战练习

> **练习：** 分别估算 Flat、HNSW、IVF-PQ 的 1B×768 向量内存，并写出精度/延迟/构建时间 trade-off。

完成标准：能在不看答案的情况下，先用 30 秒给结论，再用 5 分钟白板说明原理、至少两个 trade-off、一个 failure case 和验证指标。

## 一句话记忆

先算 3TB，再谈索引。

## 参考资料

- **R6** [Faiss indexes wiki](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes)

[← 上一题](Q097-system-design-query-autocomplete.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q099-system-design-hybrid-search.md)
