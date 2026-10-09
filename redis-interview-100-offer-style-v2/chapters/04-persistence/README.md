# Chapter 04 · 持久化：RDB、AOF 与恢复

围绕 RPO/RTO 理解 fork、COW、AOF rewrite、Multi-Part AOF 和 Redis 8.10 BACKUP。

## 本章目标

完成 Q031–Q040 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q031](q031.md) | RDB 是什么？ | 基础必会 | PDF p.38 |
| [Q032](q032.md) | SAVE 和 BGSAVE 有什么区别？ | 基础必会 | PDF p.39 |
| [Q033](q033.md) | 什么是 Copy-On-Write？ | 中级 | PDF p.40 |
| [Q034](q034.md) | AOF 是什么？ | 基础必会 | PDF p.41 |
| [Q035](q035.md) | AOF 为什么需要 rewrite？ | 中级 | PDF p.42 |
| [Q036](q036.md) | Redis 7 以后的 Multi-Part AOF 是什么？ | 中级 | PDF p.43 |
| [Q037](q037.md) | RDB 和 AOF 应该选哪个？ | 基础必会 | PDF p.44 |
| [Q038](q038.md) | RDB 与 AOF 同时开启，Redis 重启优先使用什么？ | 中级 | PDF p.45 |
| [Q039](q039.md) | AOF everysec 是不是绝对只丢 1 秒数据？ | 高级 | PDF p.46 |
| [Q040](q040.md) | Redis 8.10 的 BACKUP 有什么意义？ | 新版加分 | PDF p.47 |

## 本章工程主线

- 所有持久化答案都应落到 RPO/RTO 和恢复演练。
- 容量需要预留 fork/COW、rewrite、备份期间的峰值。

## 官方参考

- [persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/)
- [redis810](https://redis.io/docs/latest/develop/whats-new/8-10/)

[← 返回总目录](../../README.md)
