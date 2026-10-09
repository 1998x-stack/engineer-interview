# Chapter 01 · 数据结构与数据建模

从“会用命令”升级到“按访问模式建模”。选择数据结构时同时考虑操作复杂度、内存、Big Key 与 Cluster 约束。

## 本章目标

完成 Q001–Q010 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q001](q001.md) | Redis 为什么这么快？ | 基础必会 | PDF p.5 |
| [Q002](q002.md) | Redis 和 Memcached 有什么区别？ | 基础必会 | PDF p.6 |
| [Q003](q003.md) | Redis 有哪些核心数据类型？分别怎么选？ | 基础必会 | PDF p.7 |
| [Q004](q004.md) | String 最大能做什么？为什么 String 不只是字符串？ | 基础必会 | PDF p.8 |
| [Q005](q005.md) | Hash 和 String JSON 应该怎么选？ | 基础必会 | PDF p.9 |
| [Q006](q006.md) | List 可以实现消息队列吗？ | 基础必会 | PDF p.10 |
| [Q007](q007.md) | Set 最适合哪些场景？ | 基础必会 | PDF p.11 |
| [Q008](q008.md) | Sorted Set 为什么能做排行榜？ | 基础必会 | PDF p.12 |
| [Q009](q009.md) | Sorted Set 为什么通常使用 skiplist，而不是平衡树？ | 中级 | PDF p.13 |
| [Q010](q010.md) | Bitmap 和 HyperLogLog 分别解决什么问题？ | 基础必会 | PDF p.14 |

## 本章工程主线

- 先确定主读写路径，再选数据结构，不要从命令出发反推业务。
- 任何集合型结构都要给出最大基数、增长上限与清理策略。

## 官方参考

- [data_types](https://redis.io/docs/latest/develop/data-types/)
- [object_encoding](https://redis.io/docs/latest/commands/object-encoding/)

[← 返回总目录](../../README.md)
