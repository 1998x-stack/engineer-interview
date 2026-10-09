# Chapter 09 · 性能诊断、运维与安全

把 SLOWLOG、LATENCY、CPU、内存、fork、Swap、ACL/TLS 和可观测性组成排障路径。

## 本章目标

完成 Q081–Q090 后，应能在不依赖命令记忆的情况下解释核心机制，并能够说明至少一个“什么时候不该这么做”的边界。

## 学习建议

1. 第一遍：每题先口述 60 秒标准回答。
2. 第二遍：只看“深度扩展 / 追问树 / Gotchas”。
3. 第三遍：把命令和指标放进真实故障场景验证。
4. 本章复习结束后，随机抽 3 题画白板时序或状态机。

## 题目索引

| 题号 | 题目 | 难度 | 母版页 |
|---|---|---|---|
| [Q081](q081.md) | 为什么生产环境不要使用 KEYS *？ | 基础必会 | PDF p.93 |
| [Q082](q082.md) | SCAN 会不会漏 Key 或重复 Key？ | 中级 | PDF p.94 |
| [Q083](q083.md) | Redis 延迟突然从 1 ms 变成 500 ms，怎么排查？ | 高级 | PDF p.95 |
| [Q084](q084.md) | SLOWLOG 记录的是网络耗时吗？ | 基础必会 | PDF p.96 |
| [Q085](q085.md) | Pipeline 为什么能提高吞吐？ | 基础必会 | PDF p.97 |
| [Q086](q086.md) | Redis CPU 100%，最先看什么？ | 高级 | PDF p.98 |
| [Q087](q087.md) | Redis OOM 了怎么办？ | 高级 | PDF p.99 |
| [Q088](q088.md) | 为什么 Redis 不应该使用 Swap？ | 基础必会 | PDF p.100 |
| [Q089](q089.md) | Redis 应该怎么做安全控制？ | 基础必会 | PDF p.101 |
| [Q090](q090.md) | Redis 监控最重要的指标有哪些？ | 基础必会 | PDF p.102 |

## 本章工程主线

- 排障要按时间轴和层次验证假设，而不是堆命令。
- 保留证据优先于“先重启看看”。

## 官方参考

- [latency](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency/)
- [latency_monitor](https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor/)
- [cli](https://redis.io/docs/latest/develop/tools/cli/)

[← 返回总目录](../../README.md)
