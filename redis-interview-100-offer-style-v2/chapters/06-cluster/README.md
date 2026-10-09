# Chapter 06 · Redis Cluster 与水平扩展

从 16,384 slots、MOVED/ASK、Hash Tag 到 Resharding 和故障转移，能解释 Cluster 的一致性边界。

## 本章目标

完成 Q051–Q060 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q051](q051.md) | Redis Cluster 为什么是 16384 个 slot？ | 基础必会 | PDF p.60 |
| [Q052](q052.md) | Redis Cluster 为什么不用一致性哈希？ | 中级 | PDF p.61 |
| [Q053](q053.md) | Cluster Client 怎么知道 Key 在哪个节点？ | 基础必会 | PDF p.62 |
| [Q054](q054.md) | MOVED 和 ASK 有什么区别？ | 中级 | PDF p.63 |
| [Q055](q055.md) | 什么是 Hash Tag？ | 基础必会 | PDF p.64 |
| [Q056](q056.md) | 为什么 Cluster 多 Key 操作经常报 CROSSSLOT？ | 基础必会 | PDF p.65 |
| [Q057](q057.md) | Redis Cluster Resharding 怎么工作？ | 中级 | PDF p.66 |
| [Q058](q058.md) | Cluster 怎么检测节点故障？ | 中级 | PDF p.67 |
| [Q059](q059.md) | Cluster 是强一致系统吗？ | 高级 | PDF p.68 |
| [Q060](q060.md) | Redis Cluster 最少为什么经常部署 6 个实例？ | 基础必会 | PDF p.69 |

## 本章工程主线

- 先判断操作是否跨 slot，再谈事务/脚本。
- 扩容和故障转移都按最热 shard 而不是集群平均值规划。

## 官方参考

- [cluster_spec](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/)
- [cluster_scale](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/)

[← 返回总目录](../../README.md)
