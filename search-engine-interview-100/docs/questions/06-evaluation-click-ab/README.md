# 第 6 章 · 搜索指标、点击偏差与实验

> 题目范围：Q053–Q062 · 共 10 题

## 本章目标

### 本章高级视角

指标必须和产品任务对齐。导航型搜索可能 MRR 更重要；多相关文档探索型搜索更适合 NDCG/MAP；召回服务首先看 Recall。任何 click-derived metric 都要说明 exposure mechanism，否则“相关性提升”可能只是展示策略变化。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Evaluation & Experimentation 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | Recall / MRR / MAP / NDCG / CTR / guardrails |
| 白板要求 | 手算一组 NDCG；解释 click bias、IPS 和 A/B 设计。 |
| 高频失分 | 把 click 当 relevance，或只看 p-value 不看实验设计。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q053 | [Precision@K 与 Recall@K 分别衡量什么？](Q053-precision-recall-at-k.md) | 2/5 | S |
| Q054 | [MRR 是什么？适合什么场景？](Q054-mrr.md) | 2/5 | S |
| Q055 | [MAP 是什么？与 MRR 有何不同？](Q055-map-average-precision.md) | 3/5 | A |
| Q056 | [NDCG 是什么？为什么是搜索面试必考？](Q056-ndcg.md) | 4/5 | S |
| Q057 | [为什么 NDCG 比 Accuracy 更适合 Search？](Q057-why-ndcg-not-accuracy.md) | 2/5 | A |
| Q058 | [Recall@1000 提升但 NDCG@10 下降，怎么解释？](Q058-recall-up-ndcg-down.md) | 4/5 | S |
| Q059 | [为什么 Click 不能直接当 Relevance Label？](Q059-clicks-vs-relevance-labels.md) | 4/5 | S |
| Q060 | [如何处理 Position Bias？什么是 IPS？](Q060-position-bias-ips.md) | 5/5 | S |
| Q061 | [Offline 指标涨了，Online CTR/满意度为什么可能下降？](Q061-offline-up-online-down.md) | 4/5 | S |
| Q062 | [搜索 A/B Test 应如何设计？](Q062-search-ab-testing.md) | 4/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
