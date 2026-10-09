# 附录 A · 30 个高频追问速查

1. Redis 快到底快在哪里？单线程解释够吗？
2. Big Key 与 Hot Key 如何分别发现和治理？
3. listpack 为什么只适合小对象？
4. ZSet 为什么同时需要 member lookup 与有序范围能力？
5. TTL 到点为什么不等于内存瞬间下降？
6. allkeys-lru 与 volatile-lru 如何选？
7. 缓存击穿为什么本质是请求合并问题？
8. 为什么 Cache Aside 不能声称强一致？
9. BGSAVE 的 fork 和 COW 分别带来什么风险？
10. AOF everysec 的“1 秒”为什么不能承诺为绝对上限？
11. 为什么 Multi-Part AOF 能减少 rewrite 压力？
12. PSYNC 什么时候退化成 full resync？
13. replication backlog 应该怎么定容量？
14. WAIT 为什么不是共识协议？
15. SDOWN、ODOWN、quorum、majority 如何串起来？
16. 为什么 Cluster 是 slots 而不是一致性哈希？
17. MOVED/ASK 在 resharding 中分别表示什么？
18. Hash Tag 如何同时解决 CROSSSLOT 又可能制造 Hot Slot？
19. Redis Cluster 为什么仍可能丢已确认写？
20. MULTI/EXEC 和 SQL transaction 最大的语义差异？
21. WATCH 的乐观锁在 key 过期时会怎样？
22. Pipeline 与 Lua 都能少 RTT，二者的边界是什么？
23. 为什么 Redis 锁需要 unique token？
24. 为什么 lease-based lock 最后还要考虑 fencing？
25. Pub/Sub 与 Streams 如何按可靠性选？
26. PEL 为什么意味着 Streams 更自然地提供 at-least-once？
27. XAUTOCLAIM 与 XNACK 分别解决什么故障？
28. SLOWLOG 没异常但 p99 高，下一步怎么查？
29. used_memory 没到 maxmemory，机器为什么仍可能 OOM？
30. 设计 Redis 架构时如何把 SLO、RPO、RTO 映射到具体配置？

## 使用方法

随机抽 10 个问题，每个限制 90 秒。第一句必须给结论，最后一句必须给“失效边界或验证方法”。
