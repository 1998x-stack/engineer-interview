# Chapter 10 · Redis 8.x 与系统设计压轴题

覆盖 Redis 8 新数据类型与命令，并以秒杀、排行榜、限流和生产架构完成综合设计。

## 本章目标

完成 Q091–Q100 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q091](q091.md) | Redis 8 最大的架构变化是什么？ | 新版加分 | PDF p.104 |
| [Q092](q092.md) | Vector Set 和 Redis Query Engine Vector Search 怎么选？ | 新版加分 | PDF p.105 |
| [Q093](q093.md) | Bloom Filter 为什么适合解决缓存穿透？ | 中级 | PDF p.106 |
| [Q094](q094.md) | Count-Min Sketch、Top-K、t-digest 有什么作用？ | 新版加分 | PDF p.107 |
| [Q095](q095.md) | Redis 8.8 的 Array 与传统 List 有什么不同？ | 新版加分 | PDF p.108 |
| [Q096](q096.md) | Redis 8.8 INCREX 为什么值得关注？ | 新版加分 | PDF p.109 |
| [Q097](q097.md) | 设计一个秒杀库存系统，你会怎么用 Redis？ | 系统设计 | PDF p.110 |
| [Q098](q098.md) | 设计一个高并发排行榜系统。 | 系统设计 | PDF p.111 |
| [Q099](q099.md) | 设计一个 Redis Rate Limiter，有哪些算法？ | 系统设计 | PDF p.112 |
| [Q100](q100.md) | 终极题：如果让你设计一个生产级 Redis 架构，你会怎么做？ | 系统设计 | PDF p.113 |

## 本章工程主线

- 新版能力要说明版本基线与回退方案。
- 系统设计必须把容量、可用性、一致性和成本写成可验证指标。

## 官方参考

- [redis810](https://redis.io/docs/latest/develop/whats-new/8-10/)
- [redis88](https://redis.io/docs/latest/develop/whats-new/8-8/)
- [data_types](https://redis.io/docs/latest/develop/data-types/)
- [cluster_spec](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)

[← 返回总目录](../../README.md)
