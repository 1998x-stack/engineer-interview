---
id: Q093
title: "搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？"
chapter: 9
chapter_title: "分布式搜索与工程"
difficulty: 3
frequency: "A"
roles: "性能"
tags:
  - distributed-search
  - infra
  - latency
  - cache
source: "搜索引擎算法岗面试宝典 PDF, 2026 Edition"
status: "expanded-v2"
last_updated: "2026-09-02"
---

# Q093 · 搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？

[← 上一题](Q092-mysql-search-cdc-sync.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q094-search-tail-latency-debugging.md)

> 本题“30 秒回答 / 深度拆解 / 原始追问 / Gotcha / 一句话记忆”来自配套 PDF；“工程化补充 / 推导 / 练习 / 追问参考回答”等为仓库扩展内容。

## 题目画像

| 维度 | 内容 |
|---|---|
| 难度 | 3/5 |
| 频率 | A |
| 适用岗位 | 性能 |
| 所属章节 | [分布式搜索与工程](README.md) |
| 核心标签 | `distributed-search`, `infra`, `latency`, `cache` |

## 面试官到底在考什么

这道题表面在问“搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？”，实际主要看三件事：**是否掌握核心定义/机制、是否能说明边界与 trade-off、是否能把算法落到可观测的线上系统**。回答建议采用“结论 → 原理 → 极限/反例 → 工业实现 → 指标”的顺序。

## 30 秒回答

缓存可以位于 query normalization、filter bitset、posting/block、feature、embedding、model result 与最终结果等多层。完整 query-result cache 对长尾 query 命中率可能很低，因此更细粒度复 用常更稳。

## 5 分钟深度回答

- Head query 结果缓存收益巨大，但 freshness 与 personalization 会降低可复用性。
- Filter cache 适合高复用结构化条件，如 category/status。
- Embedding cache 对重复 query 或 session rewrite 很有价值。
- Feature cache 可缓存 document static features。
- OS page cache 其实是 Lucene 性能的重要组成，不应只盯应用层缓存。
- 缓存 key 必须包含 model/index/version、locale、permission 等影响结果的上下文。

## 进一步深挖：从“会答”到“能做”

#### 搜索基础设施的 SLO 思维

搜索是典型 fan-out 系统，平均延迟没有太大意义。必须关注 p95/p99、slow-shard rate、timeout/partial-result rate、merge pressure、cache hit、freshness lag。一个 shard 的长尾会被 fan-out 放大，因此“减少最慢节点概率”常比继续优化平均 CPU 时间更重要。

### 本章高级视角

Infra 面试要用 SLO 和 failure model 说话。说明正常路径之外，还要覆盖 node/shard timeout、index publish failure、CDC lag、model service unavailable、feature miss 与 partial results；并给出降级路径。

### 工业落地时必须补充的 6 个问题

1. **数据从哪里来？** 标签/统计量/embedding/点击信号如何生成，是否存在偏差或版本漂移？
2. **线上预算是多少？** candidate 数、CPU/GPU、内存、网络 fan-out 与 p99 latency 分别是多少？
3. **离线怎么验证？** 需要什么 golden set、oracle analysis、slice 与 counterfactual/ablation？
4. **线上看什么？** 除主指标外，至少准备 latency、zero-result/timeout、quality guardrail 与成本指标。
5. **失败如何降级？** 模型、向量服务、feature store 或 shard 异常时是否能回退到 lexical / cache / static rule？
6. **如何回滚和复现？** index、model、feature schema、query rewrite policy 是否版本化并可灰度？

### 追问链：参考回答
**追问 1：Personalized search 如何缓存？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 2：缓存击穿如何处理？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 3：Index refresh 后哪些 cache 失效？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

## 第二轮专业扩展（v2）

> 本节是在第一版题解之上新增的工程与研究视角，目标是让回答达到高级搜索算法 / Relevance / Retrieval 面试的深度。

### 核心机制再拆一层

cache 分 query/filter/result/feature/embedding；完整 result cache 对长尾 query 命中低；更适合缓存稳定 filter bitmap、head query、embedding 与昂贵 feature。

不要停留在名词解释。面试时建议主动回答三个问题：**它改变了哪一个概率/排序/数据结构？它用什么近似换来了什么成本？它最容易在哪类 query 或数据分布上失败？**

### 数据链路与可复现性

分布式搜索必须管理 shard routing、replica state、segment/index version、CDC offset、cache key/version 和 query deadline。没有一致的版本元数据就无法解释同一 query 在不同节点结果不一致。

建议把所有可能影响结果的资产版本化：`data/index snapshot → analyzer/feature schema → model/config → serving policy → evaluation set`。只有这样，线上 bad case 才能被可靠重放。

### 复杂度、成本与规模感

关注 fan-out 的尾延迟放大：一次请求打到 N 个 shard，整体延迟接近最慢 shard，而不是平均 shard。容量规划需要 QPS × fan-out × per-shard work，并预留 merge/GC/compaction。

回答复杂度时不要只写 Big-O；至少再补一个真实工程维度：**内存/字节、候选数、网络 fan-out、模型调用数、cache locality、p99 或更新成本**。算法岗高级面试非常看这种规模感。

### 白板公式 / 伪代码 / 实验抓手

本题不要求为了“显得技术”而硬写代码。白板上更重要的是把 **输入 → 状态/统计量 → 决策 → 输出 → 复杂度 → 失败边界** 连起来，并给出一个可验证的反例或极限情况。

### 失败模式与线上诊断

热点 shard、over-sharding、merge storm、GC、page-cache miss、network retransmit、replica lag、CDC backlog、cache stampede 都会把平均 50 ms 拉成 p99 秒级。

诊断时优先问：“**正确答案在哪一步第一次消失？**”如果到当前阶段输入里就没有正确候选，这一阶段再复杂也无法修复；如果候选存在但顺序错，才进入评分、特征、模型或融合分析。

### 可观测性：上线后必须能回答什么

按 coordinator/shard 分解 latency，记录 queue time、service time、fan-out、timeout shard、merge/GC、I/O wait、cache hit、replica lag 与 CDC watermark。

最少保留按 query slice 的指标，而不是只看全局均值。常见 slice 包括 head/tail、navigational/informational、rare entity、语言/地区、长短 query、长短文档、新老内容、filter selectivity 与设备。

### Senior / Staff 级追问

1. **如何把 2s p99 拆成 queueing、service、fan-out、straggler 的可行动指标？**
   - 回答应先定义目标与约束，再给实验设计；不要只给“换某算法”的结论。
2. **发生部分 shard 超时时，返回 partial result 还是 fail whole request？**
   - 回答应包含可观测信号、对照/消融、上线 guardrail 和失败回退。

高级系统回答要使用 deadline propagation、partial result、hedged request/replica routing、backpressure、load shedding 和版本化回滚，而不仅是“加机器”。

### 面试回答分层标准

- **及格（60 分）**：定义正确，能说明输入/输出与一个核心优缺点。
- **较强（75 分）**：能写关键公式/流程，说明至少两个 trade-off，并指出适用与失败场景。
- **高级（85 分）**：能给数量级或复杂度，说明数据如何构建、线上如何观测、如何用实验验证。
- **Senior/Staff（90+）**：能把该技术放进完整搜索链路，讨论 SLO、成本、bias、降级、版本化、回滚和优先级，并能用 oracle/ablation 证明为什么要做这项改动。

### 复习时建议做的最小实验

把本题做成一个可复现小实验：固定一组 20–100 个 query 和 golden relevance，改变**一个**关键变量，记录质量、延迟/成本和失败样本。最终产出一张 `quality–cost` 曲线和 5 个 bad cases。这样面试时就不再只是“背知识”，而是能讲出自己的工程判断。

## PDF 原始追问链

- Personalized search 如何缓存？
- 缓存击穿如何处理？
- Index refresh 后哪些 cache 失效？

## 高频失分点 / Gotcha

缓存设计的核心不是“加 Redis”，而是找到真正重复的计算与正确失效边界。

### 加强版 Gotchas

- 不要把“算法名字”当作系统答案：面试官通常会继续问数据、参数、SLO、更新与失败恢复。
- 不要只报全局平均指标：至少按 head/tail query、语言/类目、文档长度、新老用户或 filter selectivity 做 slice。
- 不要把 offline gain 直接等价为 online gain：线上还有曝光偏差、延迟、缓存、展示和反馈环。
- 数学题至少检查一个极限情况；系统题至少做一次数量级估算。

## 实战练习

> **练习：** 把本题用 5 分钟白板讲清楚，并补充一个真实线上 failure case、一个可观测指标和一个降级方案。

完成标准：能在不看答案的情况下，先用 30 秒给结论，再用 5 分钟白板说明原理、至少两个 trade-off、一个 failure case 和验证指标。

## 一句话记忆

先测复用，再决定缓存层级。

## 参考资料

- [全局参考资料](../../references/README.md)

[← 上一题](Q092-mysql-search-cdc-sync.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q094-search-tail-latency-debugging.md)
