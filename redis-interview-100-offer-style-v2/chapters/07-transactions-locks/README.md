# Chapter 07 · 事务、Lua、Functions 与分布式锁

理解 Redis 的原子性到底保证什么；把 WATCH、脚本和锁放进真实的并发/租约问题中。

## 本章目标

完成 Q061–Q070 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q061](q061.md) | Redis 单个命令为什么可以认为是原子的？ | 基础必会 | PDF p.71 |
| [Q062](q062.md) | MULTI/EXEC 是什么？ | 基础必会 | PDF p.72 |
| [Q063](q063.md) | Redis Transaction 支持 rollback 吗？ | 基础必会 | PDF p.73 |
| [Q064](q064.md) | WATCH 是怎么实现乐观锁的？ | 中级 | PDF p.74 |
| [Q065](q065.md) | Pipeline 和 Transaction 有什么区别？ | 基础必会 | PDF p.75 |
| [Q066](q066.md) | Lua Script 为什么经常用于 Redis？ | 中级 | PDF p.76 |
| [Q067](q067.md) | Lua Script 最大风险是什么？ | 中级 | PDF p.77 |
| [Q068](q068.md) | Redis Functions 和 Lua EVAL 有什么区别？ | 中级 | PDF p.78 |
| [Q069](q069.md) | 怎么正确实现单 Redis 实例分布式锁？ | 基础必会 | PDF p.79 |
| [Q070](q070.md) | Redlock 是否绝对安全？ | 高级 | PDF p.80 |

## 本章工程主线

- 原子性、隔离、持久性、租约与 exactly-once 是不同概念。
- 涉及外部系统副作用时，必须设计幂等或 fencing。

## 官方参考

- [transactions](https://redis.io/docs/latest/develop/using-commands/transactions/)
- [pipelining](https://redis.io/docs/latest/develop/using-commands/pipelining/)
- [locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)

[← 返回总目录](../../README.md)
