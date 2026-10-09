# Chapter 03 · TTL、缓存模式与淘汰

把缓存穿透、击穿、雪崩、一致性与 LRU/LFU 串成完整缓存工程知识链。

## 本章目标

完成 Q021–Q030 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q021](q021.md) | Redis Key 是怎么过期的？ | 基础必会 | PDF p.27 |
| [Q022](q022.md) | TTL 到了，Key 一定瞬间从内存消失吗？ | 基础必会 | PDF p.28 |
| [Q023](q023.md) | Redis 的过期在主从之间怎么保持一致？ | 中级 | PDF p.29 |
| [Q024](q024.md) | Redis 有哪些 maxmemory 淘汰策略？ | 基础必会 | PDF p.30 |
| [Q025](q025.md) | LRU 和 LFU 有什么区别？ | 基础必会 | PDF p.31 |
| [Q026](q026.md) | 什么是缓存穿透？ | 基础必会 | PDF p.32 |
| [Q027](q027.md) | 什么是缓存击穿？ | 基础必会 | PDF p.33 |
| [Q028](q028.md) | 什么是缓存雪崩？ | 基础必会 | PDF p.34 |
| [Q029](q029.md) | Cache Aside 如何保证数据库和 Redis 一致性？ | 高级 | PDF p.35 |
| [Q030](q030.md) | Redis Client-Side Caching 是什么？ | 中级 | PDF p.36 |

## 本章工程主线

- 缓存方案必须同时写出 miss、回源、失效、重试和降级路径。
- 关注 hit ratio 之外的数据库 QPS、stale window 与 p99。

## 官方参考

- [eviction](https://redis.io/docs/latest/develop/reference/eviction/)
- [client_cache](https://redis.io/docs/latest/develop/clients/client-side-caching/)
- [data_types](https://redis.io/docs/latest/develop/data-types/)

[← 返回总目录](../../README.md)
