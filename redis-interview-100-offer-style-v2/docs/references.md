# 官方参考资料

> 遇到版本、命令语义、复制/Cluster 写安全等问题时，优先回到 Redis 官方文档和 Cluster specification。博客和面经适合发现题型，不应替代协议与官方语义。

01. **data_types** — https://redis.io/docs/latest/develop/data-types/
02. **object_encoding** — https://redis.io/docs/latest/commands/object-encoding/
03. **eviction** — https://redis.io/docs/latest/develop/reference/eviction/
04. **client_cache** — https://redis.io/docs/latest/develop/clients/client-side-caching/
05. **persistence** — https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/
06. **replication** — https://redis.io/docs/latest/operate/oss_and_stack/management/replication/
07. **sentinel** — https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel/
08. **cluster_spec** — https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/
09. **cluster_scale** — https://redis.io/docs/latest/operate/oss_and_stack/management/scaling/
10. **transactions** — https://redis.io/docs/latest/develop/using-commands/transactions/
11. **pipelining** — https://redis.io/docs/latest/develop/using-commands/pipelining/
12. **locks** — https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/
13. **pubsub** — https://redis.io/docs/latest/develop/pubsub/
14. **streams** — https://redis.io/docs/latest/develop/data-types/streams/
15. **latency** — https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency/
16. **latency_monitor** — https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/latency-monitor/
17. **cli** — https://redis.io/docs/latest/develop/tools/cli/
18. **redis810** — https://redis.io/docs/latest/develop/whats-new/8-10/
19. **redis88** — https://redis.io/docs/latest/develop/whats-new/8-8/
20. **hashes** — https://redis.io/docs/latest/develop/data-types/hashes/

## 2026 基线核验

- Redis 8.10.1：2026 年 8 月安全更新。
- Redis 8.10：Compact Hash、HIMPORT、BACKUP、LMOVEM/BLMOVEM 等。
- Cluster：16384 slots，客户端重定向，异步复制写安全边界。
- Redis 7+：Multi-Part AOF。
