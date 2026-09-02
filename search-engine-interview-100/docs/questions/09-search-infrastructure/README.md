# 第 9 章 · 分布式搜索与工程

> 题目范围：Q085–Q094 · 共 10 题

## 本章目标

### 本章高级视角

Infra 面试要用 SLO 和 failure model 说话。说明正常路径之外，还要覆盖 node/shard timeout、index publish failure、CDC lag、model service unavailable、feature miss 与 partial results；并给出降级路径。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Search Infrastructure 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | p50/p95/p99 / shard fan-out / merge / replica lag / CDC watermark |
| 白板要求 | 画 scatter-gather + deadline；解释 CDC/outbox 和 NRT/refresh。 |
| 高频失分 | 看到延迟就“加机器”，不会按 stage/shard 分解尾延迟。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q085 | [为什么 Search Index 要做 Sharding？](Q085-search-index-sharding.md) | 2/5 | S |
| Q086 | [分布式 Search Query 的 Scatter-Gather 怎么工作？](Q086-scatter-gather-search.md) | 3/5 | S |
| Q087 | [为什么每个 Shard 只返回 Local TopK 可能有问题？](Q087-distributed-topk-pitfalls.md) | 4/5 | A |
| Q088 | [Primary Shard 与 Replica 的区别是什么？](Q088-primary-vs-replica-shard.md) | 2/5 | A |
| Q089 | [Shard 越多是不是查询越快？什么是 Over-sharding？](Q089-over-sharding.md) | 3/5 | S |
| Q090 | [什么是 Near Real-Time（NRT）Search？](Q090-near-real-time-search.md) | 3/5 | S |
| Q091 | [Refresh Interval 为什么存在 Freshness-Throughput Trade-off？](Q091-refresh-interval-tradeoff.md) | 3/5 | S |
| Q092 | [搜索索引如何与 MySQL/业务数据库保持同步？](Q092-mysql-search-cdc-sync.md) | 4/5 | S |
| Q093 | [搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？](Q093-search-caching.md) | 3/5 | A |
| Q094 | [搜索延迟从 50ms 突然变成 2s，怎么系统排查？](Q094-search-tail-latency-debugging.md) | 5/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
