---
id: Q056
title: "NDCG 是什么？为什么是搜索面试必考？"
chapter: 6
chapter_title: "搜索指标、点击偏差与实验"
difficulty: 4
frequency: "S"
roles: "评估 / LTR"
tags:
  - evaluation
  - click-bias
  - ab-testing
  - ndcg
source: "搜索引擎算法岗面试宝典 PDF, 2026 Edition"
status: "expanded-v2"
last_updated: "2026-09-02"
---

# Q056 · NDCG 是什么？为什么是搜索面试必考？

[← 上一题](Q055-map-average-precision.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q057-why-ndcg-not-accuracy.md)

> 本题“30 秒回答 / 深度拆解 / 原始追问 / Gotcha / 一句话记忆”来自配套 PDF；“工程化补充 / 推导 / 练习 / 追问参考回答”等为仓库扩展内容。

## 题目画像

| 维度 | 内容 |
|---|---|
| 难度 | 4/5 |
| 频率 | S |
| 适用岗位 | 评估 / LTR |
| 所属章节 | [搜索指标、点击偏差与实验](README.md) |
| 核心标签 | `evaluation`, `click-bias`, `ab-testing`, `ndcg` |

## 面试官到底在考什么

这道题表面在问“NDCG 是什么？为什么是搜索面试必考？”，实际主要看三件事：**是否掌握核心定义/机制、是否能说明边界与 trade-off、是否能把算法落到可观测的线上系统**。回答建议采用“结论 → 原理 → 极限/反例 → 工业实现 → 指标”的顺序。

## 30 秒回答

NDCG 同时表达“高相关等级更值钱”和“越靠前越值钱”，再用理想排序归一化到可跨 query 比较的尺 度，因此非常适合 graded relevance 的 Web/电商搜索。

## 5 分钟深度回答

- Gain 常用 2reli − 1，让 3→4 的提升比 0→1 更重要。
- Discount 常用 1/ log2 (i + 1)，体现顶部位置价值更高。
- IDCG@K 是把同一 query 的 labels 理想排序后的 DCG。
- N DCG = DCG/IDCG，理想排序为 1。
- LambdaRank/LambdaMART 常用 ∆N DCG 衡量 pair swap 的重要度。

## 数学 / 白板推导

### NDCG 白板公式

$$DCG@K=\sum_{i=1}^{K}\frac{2^{rel_i}-1}{\log_2(i+1)}$$

$$NDCG@K=\frac{DCG@K}{IDCG@K}$$

面试时最好现场算一个 3 个结果的小例子，并解释两个设计：**graded relevance gain** 与 **position discount**。

## 进一步深挖：从“会答”到“能做”

#### 评价指标的三个层级

建议把指标分成：**retrieval ceiling**（Recall@K）、**ranking quality**（NDCG/MRR/MAP）、**online utility**（成功搜索率、CTR/CVR、abandonment）。离线涨而线上跌时，优先检查 label mismatch、slice shift、latency、presentation 与 feedback loop，而不是直接怀疑“实验噪声”。

### 本章高级视角

指标必须和产品任务对齐。导航型搜索可能 MRR 更重要；多相关文档探索型搜索更适合 NDCG/MAP；召回服务首先看 Recall。任何 click-derived metric 都要说明 exposure mechanism，否则“相关性提升”可能只是展示策略变化。

### 工业落地时必须补充的 6 个问题

1. **数据从哪里来？** 标签/统计量/embedding/点击信号如何生成，是否存在偏差或版本漂移？
2. **线上预算是多少？** candidate 数、CPU/GPU、内存、网络 fan-out 与 p99 latency 分别是多少？
3. **离线怎么验证？** 需要什么 golden set、oracle analysis、slice 与 counterfactual/ablation？
4. **线上看什么？** 除主指标外，至少准备 latency、zero-result/timeout、quality guardrail 与成本指标。
5. **失败如何降级？** 模型、向量服务、feature store 或 shard 异常时是否能回退到 lexical / cache / static rule？
6. **如何回滚和复现？** index、model、feature schema、query rewrite policy 是否版本化并可灰度？

### 追问链：参考回答
**追问 1：为什么要归一化？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 2：Gain 为什么常用指数而不是直接 rel？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

**追问 3：IDCG=0 怎么处理？**

回答时先给定义，再给边界条件与可观测指标；如果是算法选择题，用“效果、延迟、内存、更新、可解释性”五维 trade-off 组织。

## 第二轮专业扩展（v2）

> 本节是在第一版题解之上新增的工程与研究视角，目标是让回答达到高级搜索算法 / Relevance / Retrieval 面试的深度。

### 核心机制再拆一层

NDCG = DCG/IDCG；gain 表示 graded relevance，log discount 强调顶部；必须说明无 relevant 文档时的约定与 cutoff K。

不要停留在名词解释。面试时建议主动回答三个问题：**它改变了哪一个概率/排序/数据结构？它用什么近似换来了什么成本？它最容易在哪类 query 或数据分布上失败？**

### 数据链路与可复现性

评估数据必须区分人工 relevance、点击弱标签、业务 outcome 和在线 exposure。每个 label 都有生成机制，不能把“观测到的行为”直接当成“真实相关性”。

建议把所有可能影响结果的资产版本化：`data/index snapshot → analyzer/feature schema → model/config → serving policy → evaluation set`。只有这样，线上 bad case 才能被可靠重放。

### 复杂度、成本与规模感

指标计算本身不是瓶颈，真正成本是标注、实验流量与误判机会成本。建立小而稳定的 gold set，再配大规模弱监督，是常见的成本平衡。

回答复杂度时不要只写 Big-O；至少再补一个真实工程维度：**内存/字节、候选数、网络 fan-out、模型调用数、cache locality、p99 或更新成本**。算法岗高级面试非常看这种规模感。

### 白板公式 / 伪代码 / 实验抓手

```python
import math
def dcg(rels, k):
    return sum((2**r - 1) / math.log2(i + 2)
               for i, r in enumerate(rels[:k]))

def ndcg(rels, k):
    ideal = sorted(rels, reverse=True)
    denom = dcg(ideal, k)
    return 0.0 if denom == 0 else dcg(rels, k) / denom
```

### 失败模式与线上诊断

最危险的是 metric gaming：CTR 上升但满意度下降、NDCG 上升但 tail query 变差、Recall 上升但 ranker 被噪声候选拖垮。

诊断时优先问：“**正确答案在哪一步第一次消失？**”如果到当前阶段输入里就没有正确候选，这一阶段再复杂也无法修复；如果候选存在但顺序错，才进入评分、特征、模型或融合分析。

### 可观测性：上线后必须能回答什么

离线必须分 slice；在线同时看 primary metric、guardrail、SRM、p95/p99、zero-result/abandonment、长期 retention 或 conversion。

最少保留按 query slice 的指标，而不是只看全局均值。常见 slice 包括 head/tail、navigational/informational、rare entity、语言/地区、长短 query、长短文档、新老内容、filter selectivity 与设备。

### Senior / Staff 级追问

1. **如果 primary metric 显著上涨但 guardrail 下降，如何做上线决策？**
   - 回答应先定义目标与约束，再给实验设计；不要只给“换某算法”的结论。
2. **怎样构建长期稳定、不会被模型迭代污染的 gold set？**
   - 回答应包含可观测信号、对照/消融、上线 guardrail 和失败回退。

Staff 级评估回答应明确因果边界：什么能由离线相关性证明，什么必须 A/B；如何处理 exposure bias、novelty effect、multiple testing 和实验污染。

### 面试回答分层标准

- **及格（60 分）**：定义正确，能说明输入/输出与一个核心优缺点。
- **较强（75 分）**：能写关键公式/流程，说明至少两个 trade-off，并指出适用与失败场景。
- **高级（85 分）**：能给数量级或复杂度，说明数据如何构建、线上如何观测、如何用实验验证。
- **Senior/Staff（90+）**：能把该技术放进完整搜索链路，讨论 SLO、成本、bias、降级、版本化、回滚和优先级，并能用 oracle/ablation 证明为什么要做这项改动。

### 复习时建议做的最小实验

把本题做成一个可复现小实验：固定一组 20–100 个 query 和 golden relevance，改变**一个**关键变量，记录质量、延迟/成本和失败样本。最终产出一张 `quality–cost` 曲线和 5 个 bad cases。这样面试时就不再只是“背知识”，而是能讲出自己的工程判断。

## PDF 原始追问链

- 为什么要归一化？
- Gain 为什么常用指数而不是直接 rel？
- IDCG=0 怎么处理？

## 高频失分点 / Gotcha

面试时不要只写公式；必须讲清 gain、discount、normalization 三个设计选择。

### 加强版 Gotchas

- 不要把“算法名字”当作系统答案：面试官通常会继续问数据、参数、SLO、更新与失败恢复。
- 不要只报全局平均指标：至少按 head/tail query、语言/类目、文档长度、新老用户或 filter selectivity 做 slice。
- 不要把 offline gain 直接等价为 online gain：线上还有曝光偏差、延迟、缓存、展示和反馈环。
- 数学题至少检查一个极限情况；系统题至少做一次数量级估算。

## 实战练习

> **练习：** 手算一个 relevance=[3,0,2,1] 的 NDCG@4。

完成标准：能在不看答案的情况下，先用 30 秒给结论，再用 5 分钟白板说明原理、至少两个 trade-off、一个 failure case 和验证指标。

## 一句话记忆

NDCG = “价值”× “位置折扣”÷ “该 query 的理想上限”。

## 参考资料

- **R1** [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/)

[← 上一题](Q055-map-average-precision.md) · [章节索引](README.md) · [全局索引](../../INDEX.md) · [下一题 →](Q057-why-ndcg-not-accuracy.md)
