# Chapter 05 · 复制与 Sentinel 高可用

掌握异步复制的写安全边界、PSYNC/backlog，以及 Sentinel 的主观/客观下线和选举语义。

## 本章目标

完成 Q041–Q050 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q041](q041.md) | Redis 主从复制是同步还是异步？ | 基础必会 | PDF p.49 |
| [Q042](q042.md) | Redis 全量复制是怎样发生的？ | 中级 | PDF p.50 |
| [Q043](q043.md) | 什么是 PSYNC？ | 中级 | PDF p.51 |
| [Q044](q044.md) | replication backlog 是干什么的？ | 中级 | PDF p.52 |
| [Q045](q045.md) | WAIT 能不能保证 Redis 强一致？ | 高级 | PDF p.53 |
| [Q046](q046.md) | Redis Sentinel 是干什么的？ | 基础必会 | PDF p.54 |
| [Q047](q047.md) | Sentinel 的 SDOWN 和 ODOWN 是什么？ | 中级 | PDF p.55 |
| [Q048](q048.md) | Sentinel quorum 和 majority 有什么区别？ | 高级 | PDF p.56 |
| [Q049](q049.md) | Sentinel 为什么推荐奇数个？ | 中级 | PDF p.57 |
| [Q050](q050.md) | Sentinel 会不会脑裂？ | 高级 | PDF p.58 |

## 本章工程主线

- HA 不是零丢写；先明确复制异步性，再讨论 failover。
- 把故障域（主机、机架、AZ）写入拓扑设计。

## 官方参考

- [replication](https://redis.io/docs/latest/operate/oss_and_stack/management/replication/)
- [sentinel](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/)

[← 返回总目录](../../README.md)
