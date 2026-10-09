# Chapter 08 · Pub/Sub、Streams 与消息处理

从 fire-and-forget 到 Consumer Group、PEL、XAUTOCLAIM/XNACK，建立至少一次消费与幂等意识。

## 本章目标

完成 Q071–Q080 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q071](q071.md) | Redis Pub/Sub 的特点是什么？ | 基础必会 | PDF p.82 |
| [Q072](q072.md) | Pub/Sub 和 Stream 最大区别是什么？ | 基础必会 | PDF p.83 |
| [Q073](q073.md) | Redis Stream 的 ID 是什么？ | 基础必会 | PDF p.84 |
| [Q074](q074.md) | Consumer Group 是什么？ | 基础必会 | PDF p.85 |
| [Q075](q075.md) | 什么是 PEL？ | 中级 | PDF p.86 |
| [Q076](q076.md) | Consumer 崩溃后 Pending Message 怎么处理？ | 中级 | PDF p.87 |
| [Q077](q077.md) | Redis Streams 能保证 exactly-once 吗？ | 高级 | PDF p.88 |
| [Q078](q078.md) | Redis 8.8 XNACK 解决了什么？ | 新版加分 | PDF p.89 |
| [Q079](q079.md) | Redis Stream 怎么防止无限增长？ | 中级 | PDF p.90 |
| [Q080](q080.md) | Redis 和 Kafka 应该怎么选？ | 高级 | PDF p.91 |

## 本章工程主线

- 消息投递语义与业务效果语义要分开。
- 监控 lag、PEL、delivery count、毒消息与 retention。

## 官方参考

- [pubsub](https://redis.io/docs/latest/develop/pubsub/)
- [streams](https://redis.io/docs/latest/develop/data-types/streams/)

[← 返回总目录](../../README.md)
