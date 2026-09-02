---
id: Q038
title: "LLM 如何用于 Query Rewrite？"
chapter: 4
chapter_title: "Query Understanding 与 Query Rewrite"
difficulty: 4
frequency: "A"
roles: "LLM Search"
tags:
  - query-understanding
  - query-rewrite
  - nlp
source: "搜索引擎算法岗面试宝典 PDF, 2026 Edition"
status: "expanded-v2"
last_updated: "2026-09-02"
---

# Q038 · LLM 如何用于 Query Rewrite？

[← 上一题](Q037-synonym-rewrite-expansion.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q039-llm-query-rewrite-risks.md)

> 本题“30 秒回答 / 深度拆解 / 原始追问 / Gotcha / 一句话记忆”来自配套 PDF；“工程化补充 / 推导 / 练习 / 追问参考回答”等为仓库扩展内容。

## 题目画像

| 维度 | 内容 |
|---|---|
| 难度 | 4/5 |
| 频率 | A |
| 适用岗位 | LLM Search |
| 所属章节 | [Query Understanding 与 Query Rewrite](README.md) |
| 核心标签 | `query-understanding`, `query-rewrite`, `nlp` |

## 面试官到底在考什么

这道题表面在问“LLM 如何用于 Query Rewrite？”，实际主要看三件事：**是否掌握核心定义/机制、是否能说明边界与 trade-off、是否能把算法落到可观测的线上系统**。回答建议采用“结论 → 原理 → 极限/反例 → 工业实现 → 指标”的顺序。

## 30 秒回答

LLM 适合把自然语言 query 解析成结构化意图、实体过滤条件和多条检索改写，但必须受 schema、词 表和保守策略约束，不能让模型自由“脑补”用户需求。

## 5 分钟深度回答

- 输入可包含原 query、session context、catalog schema、可用 filter/field 说明。
- 输出最好是结构化 JSON：intent、entities、filters、lexical_queries、semantic_queries。
- 对高价值字段做 deterministic validation，例如价格范围、品牌必须来自 catalog。
- 保留 original query 作为一个召回通道，rewrite 只做增量，降低 query drift。
- 低延迟可通过小模型蒸馏、缓存 head queries、异步或只对难 query 启用 LLM。

## 进一步深挖：从“会答”到“能做”

#### Query 侧的产品原则

Query Understanding 的首要风险通常是**过度修改用户意图**。任何 correction/rewrite/expansion 都应有 confidence、fallback 与可观测性；高风险 query（人名、型号、代码、医学/法律术语等）通常更适合保留 original query 并做多路召回，而不是强替换。

### 本章高级视角

Query 模型的收益通常取决于 error taxonomy，而不是模型参数量。先分清 typo、segmentation、entity、intent、attribute extraction、rewrite drift，再给每类设计独立 metric 和 fallback。LLM 引入后，最重要的新问题是可控性、稳定性、成本与 hallucinated constraints。

### 工业落地时必须补充的 6 个问题

1. **数据从哪里来？** 标签/统计量/embedding/点击信号如何生成，是否存在偏差或版本漂移？
2. **线上预算是多少？** candidate 数、CPU/GPU、内存、网络 fan-out 与 p99 latency 分别是多少？
3. **离线怎么验证？** 需要什么 golden set、oracle analysis、slice 与 counterfactual/ablation？
4. **线上看什么？** 除主指标外，至少准备 latency、zero-result/timeout、quality guardrail 与成本指标。
5. **失败如何降级？** 模型、向量服务、feature store 或 shard 异常时是否能回退到 lexical / cache / static rule？
6. **如何回滚和复现？** index、model、feature schema、query rewrite policy 是否版本化并可灰度？

### 追问链：参考回答
**追问 1：如何检测 LLM rewrite 是否漂移？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 2：为什么 dense rewrite 与 BM25 rewrite 可能不同？**

Dense 提供语义泛化，但会带来 ANN recall、索引刷新、过滤、内存与可解释性成本；通常作为多路召回或相关性特征，而不是无条件替换 lexical。

**追问 3：LLM 的成本如何控制？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

## 第二轮专业扩展（v2）

> 本节是在第一版题解之上新增的工程与研究视角，目标是让回答达到高级搜索算法 / Relevance / Retrieval 面试的深度。

### 核心机制再拆一层

LLM 可产 intent/entity/filter/多条 rewrite；生产上应做结构化输出、白名单 schema、置信路由、cache 和 original-query union。

不要停留在名词解释。面试时建议主动回答三个问题：**它改变了哪一个概率/排序/数据结构？它用什么近似换来了什么成本？它最容易在哪类 query 或数据分布上失败？**

### 数据链路与可复现性

Query Understanding 需要保存原 query、规范化 query、实体/属性、意图分布、rewrite candidates、最终执行 query 以及每一步置信度。否则线上 query drift 很难做根因分析。

建议把所有可能影响结果的资产版本化：`data/index snapshot → analyzer/feature schema → model/config → serving policy → evaluation set`。只有这样，线上 bad case 才能被可靠重放。

### 复杂度、成本与规模感

大多数 query 都是短文本，单条模型看似便宜，但高 QPS 下每增加一次远程 LLM 调用都会放大尾延迟和成本。常见策略是规则/小模型覆盖 head query，复杂模型只路由到高价值或低置信 query。

回答复杂度时不要只写 Big-O；至少再补一个真实工程维度：**内存/字节、候选数、网络 fan-out、模型调用数、cache locality、p99 或更新成本**。算法岗高级面试非常看这种规模感。

### 白板公式 / 伪代码 / 实验抓手

本题不要求为了“显得技术”而硬写代码。白板上更重要的是把 **输入 → 状态/统计量 → 决策 → 输出 → 复杂度 → 失败边界** 连起来，并给出一个可验证的反例或极限情况。

### 失败模式与线上诊断

重点区分 under-rewrite（召回不够）与 over-rewrite（意图漂移）；再看实体消歧、属性抽取、拼写纠错和多语言分词是否造成不可逆信息损失。

诊断时优先问：“**正确答案在哪一步第一次消失？**”如果到当前阶段输入里就没有正确候选，这一阶段再复杂也无法修复；如果候选存在但顺序错，才进入评分、特征、模型或融合分析。

### 可观测性：上线后必须能回答什么

监控 rewrite acceptance、original-vs-rewrite recall delta、query drift rate、zero-result rate、entity/intent confidence、人工 bad-case 与 head/tail slice。

最少保留按 query slice 的指标，而不是只看全局均值。常见 slice 包括 head/tail、navigational/informational、rare entity、语言/地区、长短 query、长短文档、新老内容、filter selectivity 与设备。

### Senior / Staff 级追问

1. **如何定义“rewrite 正确”，没有人工标签时怎么评估？**
   - 回答应先定义目标与约束，再给实验设计；不要只给“换某算法”的结论。
2. **如何让 LLM 只处理高价值 query，而不是全量增加成本？**
   - 回答应包含可观测信号、对照/消融、上线 guardrail 和失败回退。

高阶答案要说明“什么时候不改写”。保留 original query、并行执行 rewrite、可解释置信度和回退策略，往往比一个更强的生成模型更重要。

### 面试回答分层标准

- **及格（60 分）**：定义正确，能说明输入/输出与一个核心优缺点。
- **较强（75 分）**：能写关键公式/流程，说明至少两个 trade-off，并指出适用与失败场景。
- **高级（85 分）**：能给数量级或复杂度，说明数据如何构建、线上如何观测、如何用实验验证。
- **Senior/Staff（90+）**：能把该技术放进完整搜索链路，讨论 SLO、成本、bias、降级、版本化、回滚和优先级，并能用 oracle/ablation 证明为什么要做这项改动。

### 复习时建议做的最小实验

把本题做成一个可复现小实验：固定一组 20–100 个 query 和 golden relevance，改变**一个**关键变量，记录质量、延迟/成本和失败样本。最终产出一张 `quality–cost` 曲线和 5 个 bad cases。这样面试时就不再只是“背知识”，而是能讲出自己的工程判断。

## PDF 原始追问链

- 如何检测 LLM rewrite 是否漂移？
- 为什么 dense rewrite 与 BM25 rewrite 可能不同？
- LLM 的成本如何控制？

## 高频失分点 / Gotcha

把 LLM 放到关键路径前，应首先回答延迟、稳定性、可解释性和 fallback。

### 加强版 Gotchas

- 不要把“算法名字”当作系统答案：面试官通常会继续问数据、参数、SLO、更新与失败恢复。
- 不要只报全局平均指标：至少按 head/tail query、语言/类目、文档长度、新老用户或 filter selectivity 做 slice。
- 不要把 offline gain 直接等价为 online gain：线上还有曝光偏差、延迟、缓存、展示和反馈环。
- 数学题至少检查一个极限情况；系统题至少做一次数量级估算。

## 实战练习

> **练习：** 为 LLM query rewrite 设计 JSON schema、置信度、original-query fallback 和 rewrite drift 指标。

完成标准：能在不看答案的情况下，先用 30 秒给结论，再用 5 分钟白板说明原理、至少两个 trade-off、一个 failure case 和验证指标。

## 一句话记忆

LLM Rewrite 必须“受约束、可回退、可验证”。

## 参考资料

- [全局参考资料](../../references/README.md)

[← 上一题](Q037-synonym-rewrite-expansion.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q039-llm-query-rewrite-risks.md)
