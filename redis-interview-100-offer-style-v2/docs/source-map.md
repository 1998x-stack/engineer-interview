# PDF → Markdown 内容映射

母版：`docs/pdf/Redis_Interview_100_Offer_Style_2026.pdf`（118 页）

| PDF 页 | Markdown | 题目 |
|---:|---|---|
| 5 | [`chapters/01-data-modeling/q001.md`](../chapters/01-data-modeling/q001.md) | Q001 · Redis 为什么这么快？ |
| 6 | [`chapters/01-data-modeling/q002.md`](../chapters/01-data-modeling/q002.md) | Q002 · Redis 和 Memcached 有什么区别？ |
| 7 | [`chapters/01-data-modeling/q003.md`](../chapters/01-data-modeling/q003.md) | Q003 · Redis 有哪些核心数据类型？分别怎么选？ |
| 8 | [`chapters/01-data-modeling/q004.md`](../chapters/01-data-modeling/q004.md) | Q004 · String 最大能做什么？为什么 String 不只是字符串？ |
| 9 | [`chapters/01-data-modeling/q005.md`](../chapters/01-data-modeling/q005.md) | Q005 · Hash 和 String JSON 应该怎么选？ |
| 10 | [`chapters/01-data-modeling/q006.md`](../chapters/01-data-modeling/q006.md) | Q006 · List 可以实现消息队列吗？ |
| 11 | [`chapters/01-data-modeling/q007.md`](../chapters/01-data-modeling/q007.md) | Q007 · Set 最适合哪些场景？ |
| 12 | [`chapters/01-data-modeling/q008.md`](../chapters/01-data-modeling/q008.md) | Q008 · Sorted Set 为什么能做排行榜？ |
| 13 | [`chapters/01-data-modeling/q009.md`](../chapters/01-data-modeling/q009.md) | Q009 · Sorted Set 为什么通常使用 skiplist，而不是平衡树？ |
| 14 | [`chapters/01-data-modeling/q010.md`](../chapters/01-data-modeling/q010.md) | Q010 · Bitmap 和 HyperLogLog 分别解决什么问题？ |
| 16 | [`chapters/02-internals-memory/q011.md`](../chapters/02-internals-memory/q011.md) | Q011 · Redis String 底层为什么不用普通 C 字符串？ |
| 17 | [`chapters/02-internals-memory/q012.md`](../chapters/02-internals-memory/q012.md) | Q012 · embstr、raw、int 有什么区别？ |
| 18 | [`chapters/02-internals-memory/q013.md`](../chapters/02-internals-memory/q013.md) | Q013 · List 的底层结构是什么？ |
| 19 | [`chapters/02-internals-memory/q014.md`](../chapters/02-internals-memory/q014.md) | Q014 · Hash 的底层结构是什么？ |
| 20 | [`chapters/02-internals-memory/q015.md`](../chapters/02-internals-memory/q015.md) | Q015 · Redis 为什么会自动改变 encoding？ |
| 21 | [`chapters/02-internals-memory/q016.md`](../chapters/02-internals-memory/q016.md) | Q016 · 什么是 Big Key？ |
| 22 | [`chapters/02-internals-memory/q017.md`](../chapters/02-internals-memory/q017.md) | Q017 · Big Key 如何治理？ |
| 23 | [`chapters/02-internals-memory/q018.md`](../chapters/02-internals-memory/q018.md) | Q018 · 什么是 Hot Key？ |
| 24 | [`chapters/02-internals-memory/q019.md`](../chapters/02-internals-memory/q019.md) | Q019 · Hot Key 怎么解决？ |
| 25 | [`chapters/02-internals-memory/q020.md`](../chapters/02-internals-memory/q020.md) | Q020 · Redis 为什么可能出现内存碎片？ |
| 27 | [`chapters/03-cache-ttl-eviction/q021.md`](../chapters/03-cache-ttl-eviction/q021.md) | Q021 · Redis Key 是怎么过期的？ |
| 28 | [`chapters/03-cache-ttl-eviction/q022.md`](../chapters/03-cache-ttl-eviction/q022.md) | Q022 · TTL 到了，Key 一定瞬间从内存消失吗？ |
| 29 | [`chapters/03-cache-ttl-eviction/q023.md`](../chapters/03-cache-ttl-eviction/q023.md) | Q023 · Redis 的过期在主从之间怎么保持一致？ |
| 30 | [`chapters/03-cache-ttl-eviction/q024.md`](../chapters/03-cache-ttl-eviction/q024.md) | Q024 · Redis 有哪些 maxmemory 淘汰策略？ |
| 31 | [`chapters/03-cache-ttl-eviction/q025.md`](../chapters/03-cache-ttl-eviction/q025.md) | Q025 · LRU 和 LFU 有什么区别？ |
| 32 | [`chapters/03-cache-ttl-eviction/q026.md`](../chapters/03-cache-ttl-eviction/q026.md) | Q026 · 什么是缓存穿透？ |
| 33 | [`chapters/03-cache-ttl-eviction/q027.md`](../chapters/03-cache-ttl-eviction/q027.md) | Q027 · 什么是缓存击穿？ |
| 34 | [`chapters/03-cache-ttl-eviction/q028.md`](../chapters/03-cache-ttl-eviction/q028.md) | Q028 · 什么是缓存雪崩？ |
| 35 | [`chapters/03-cache-ttl-eviction/q029.md`](../chapters/03-cache-ttl-eviction/q029.md) | Q029 · Cache Aside 如何保证数据库和 Redis 一致性？ |
| 36 | [`chapters/03-cache-ttl-eviction/q030.md`](../chapters/03-cache-ttl-eviction/q030.md) | Q030 · Redis Client-Side Caching 是什么？ |
| 38 | [`chapters/04-persistence/q031.md`](../chapters/04-persistence/q031.md) | Q031 · RDB 是什么？ |
| 39 | [`chapters/04-persistence/q032.md`](../chapters/04-persistence/q032.md) | Q032 · SAVE 和 BGSAVE 有什么区别？ |
| 40 | [`chapters/04-persistence/q033.md`](../chapters/04-persistence/q033.md) | Q033 · 什么是 Copy-On-Write？ |
| 41 | [`chapters/04-persistence/q034.md`](../chapters/04-persistence/q034.md) | Q034 · AOF 是什么？ |
| 42 | [`chapters/04-persistence/q035.md`](../chapters/04-persistence/q035.md) | Q035 · AOF 为什么需要 rewrite？ |
| 43 | [`chapters/04-persistence/q036.md`](../chapters/04-persistence/q036.md) | Q036 · Redis 7 以后的 Multi-Part AOF 是什么？ |
| 44 | [`chapters/04-persistence/q037.md`](../chapters/04-persistence/q037.md) | Q037 · RDB 和 AOF 应该选哪个？ |
| 45 | [`chapters/04-persistence/q038.md`](../chapters/04-persistence/q038.md) | Q038 · RDB 与 AOF 同时开启，Redis 重启优先使用什么？ |
| 46 | [`chapters/04-persistence/q039.md`](../chapters/04-persistence/q039.md) | Q039 · AOF everysec 是不是绝对只丢 1 秒数据？ |
| 47 | [`chapters/04-persistence/q040.md`](../chapters/04-persistence/q040.md) | Q040 · Redis 8.10 的 BACKUP 有什么意义？ |
| 49 | [`chapters/05-replication-sentinel/q041.md`](../chapters/05-replication-sentinel/q041.md) | Q041 · Redis 主从复制是同步还是异步？ |
| 50 | [`chapters/05-replication-sentinel/q042.md`](../chapters/05-replication-sentinel/q042.md) | Q042 · Redis 全量复制是怎样发生的？ |
| 51 | [`chapters/05-replication-sentinel/q043.md`](../chapters/05-replication-sentinel/q043.md) | Q043 · 什么是 PSYNC？ |
| 52 | [`chapters/05-replication-sentinel/q044.md`](../chapters/05-replication-sentinel/q044.md) | Q044 · replication backlog 是干什么的？ |
| 53 | [`chapters/05-replication-sentinel/q045.md`](../chapters/05-replication-sentinel/q045.md) | Q045 · WAIT 能不能保证 Redis 强一致？ |
| 54 | [`chapters/05-replication-sentinel/q046.md`](../chapters/05-replication-sentinel/q046.md) | Q046 · Redis Sentinel 是干什么的？ |
| 55 | [`chapters/05-replication-sentinel/q047.md`](../chapters/05-replication-sentinel/q047.md) | Q047 · Sentinel 的 SDOWN 和 ODOWN 是什么？ |
| 56 | [`chapters/05-replication-sentinel/q048.md`](../chapters/05-replication-sentinel/q048.md) | Q048 · Sentinel quorum 和 majority 有什么区别？ |
| 57 | [`chapters/05-replication-sentinel/q049.md`](../chapters/05-replication-sentinel/q049.md) | Q049 · Sentinel 为什么推荐奇数个？ |
| 58 | [`chapters/05-replication-sentinel/q050.md`](../chapters/05-replication-sentinel/q050.md) | Q050 · Sentinel 会不会脑裂？ |
| 60 | [`chapters/06-cluster/q051.md`](../chapters/06-cluster/q051.md) | Q051 · Redis Cluster 为什么是 16384 个 slot？ |
| 61 | [`chapters/06-cluster/q052.md`](../chapters/06-cluster/q052.md) | Q052 · Redis Cluster 为什么不用一致性哈希？ |
| 62 | [`chapters/06-cluster/q053.md`](../chapters/06-cluster/q053.md) | Q053 · Cluster Client 怎么知道 Key 在哪个节点？ |
| 63 | [`chapters/06-cluster/q054.md`](../chapters/06-cluster/q054.md) | Q054 · MOVED 和 ASK 有什么区别？ |
| 64 | [`chapters/06-cluster/q055.md`](../chapters/06-cluster/q055.md) | Q055 · 什么是 Hash Tag？ |
| 65 | [`chapters/06-cluster/q056.md`](../chapters/06-cluster/q056.md) | Q056 · 为什么 Cluster 多 Key 操作经常报 CROSSSLOT？ |
| 66 | [`chapters/06-cluster/q057.md`](../chapters/06-cluster/q057.md) | Q057 · Redis Cluster Resharding 怎么工作？ |
| 67 | [`chapters/06-cluster/q058.md`](../chapters/06-cluster/q058.md) | Q058 · Cluster 怎么检测节点故障？ |
| 68 | [`chapters/06-cluster/q059.md`](../chapters/06-cluster/q059.md) | Q059 · Cluster 是强一致系统吗？ |
| 69 | [`chapters/06-cluster/q060.md`](../chapters/06-cluster/q060.md) | Q060 · Redis Cluster 最少为什么经常部署 6 个实例？ |
| 71 | [`chapters/07-transactions-locks/q061.md`](../chapters/07-transactions-locks/q061.md) | Q061 · Redis 单个命令为什么可以认为是原子的？ |
| 72 | [`chapters/07-transactions-locks/q062.md`](../chapters/07-transactions-locks/q062.md) | Q062 · MULTI/EXEC 是什么？ |
| 73 | [`chapters/07-transactions-locks/q063.md`](../chapters/07-transactions-locks/q063.md) | Q063 · Redis Transaction 支持 rollback 吗？ |
| 74 | [`chapters/07-transactions-locks/q064.md`](../chapters/07-transactions-locks/q064.md) | Q064 · WATCH 是怎么实现乐观锁的？ |
| 75 | [`chapters/07-transactions-locks/q065.md`](../chapters/07-transactions-locks/q065.md) | Q065 · Pipeline 和 Transaction 有什么区别？ |
| 76 | [`chapters/07-transactions-locks/q066.md`](../chapters/07-transactions-locks/q066.md) | Q066 · Lua Script 为什么经常用于 Redis？ |
| 77 | [`chapters/07-transactions-locks/q067.md`](../chapters/07-transactions-locks/q067.md) | Q067 · Lua Script 最大风险是什么？ |
| 78 | [`chapters/07-transactions-locks/q068.md`](../chapters/07-transactions-locks/q068.md) | Q068 · Redis Functions 和 Lua EVAL 有什么区别？ |
| 79 | [`chapters/07-transactions-locks/q069.md`](../chapters/07-transactions-locks/q069.md) | Q069 · 怎么正确实现单 Redis 实例分布式锁？ |
| 80 | [`chapters/07-transactions-locks/q070.md`](../chapters/07-transactions-locks/q070.md) | Q070 · Redlock 是否绝对安全？ |
| 82 | [`chapters/08-messaging-streams/q071.md`](../chapters/08-messaging-streams/q071.md) | Q071 · Redis Pub/Sub 的特点是什么？ |
| 83 | [`chapters/08-messaging-streams/q072.md`](../chapters/08-messaging-streams/q072.md) | Q072 · Pub/Sub 和 Stream 最大区别是什么？ |
| 84 | [`chapters/08-messaging-streams/q073.md`](../chapters/08-messaging-streams/q073.md) | Q073 · Redis Stream 的 ID 是什么？ |
| 85 | [`chapters/08-messaging-streams/q074.md`](../chapters/08-messaging-streams/q074.md) | Q074 · Consumer Group 是什么？ |
| 86 | [`chapters/08-messaging-streams/q075.md`](../chapters/08-messaging-streams/q075.md) | Q075 · 什么是 PEL？ |
| 87 | [`chapters/08-messaging-streams/q076.md`](../chapters/08-messaging-streams/q076.md) | Q076 · Consumer 崩溃后 Pending Message 怎么处理？ |
| 88 | [`chapters/08-messaging-streams/q077.md`](../chapters/08-messaging-streams/q077.md) | Q077 · Redis Streams 能保证 exactly-once 吗？ |
| 89 | [`chapters/08-messaging-streams/q078.md`](../chapters/08-messaging-streams/q078.md) | Q078 · Redis 8.8 XNACK 解决了什么？ |
| 90 | [`chapters/08-messaging-streams/q079.md`](../chapters/08-messaging-streams/q079.md) | Q079 · Redis Stream 怎么防止无限增长？ |
| 91 | [`chapters/08-messaging-streams/q080.md`](../chapters/08-messaging-streams/q080.md) | Q080 · Redis 和 Kafka 应该怎么选？ |
| 93 | [`chapters/09-operations-performance/q081.md`](../chapters/09-operations-performance/q081.md) | Q081 · 为什么生产环境不要使用 KEYS *？ |
| 94 | [`chapters/09-operations-performance/q082.md`](../chapters/09-operations-performance/q082.md) | Q082 · SCAN 会不会漏 Key 或重复 Key？ |
| 95 | [`chapters/09-operations-performance/q083.md`](../chapters/09-operations-performance/q083.md) | Q083 · Redis 延迟突然从 1 ms 变成 500 ms，怎么排查？ |
| 96 | [`chapters/09-operations-performance/q084.md`](../chapters/09-operations-performance/q084.md) | Q084 · SLOWLOG 记录的是网络耗时吗？ |
| 97 | [`chapters/09-operations-performance/q085.md`](../chapters/09-operations-performance/q085.md) | Q085 · Pipeline 为什么能提高吞吐？ |
| 98 | [`chapters/09-operations-performance/q086.md`](../chapters/09-operations-performance/q086.md) | Q086 · Redis CPU 100%，最先看什么？ |
| 99 | [`chapters/09-operations-performance/q087.md`](../chapters/09-operations-performance/q087.md) | Q087 · Redis OOM 了怎么办？ |
| 100 | [`chapters/09-operations-performance/q088.md`](../chapters/09-operations-performance/q088.md) | Q088 · 为什么 Redis 不应该使用 Swap？ |
| 101 | [`chapters/09-operations-performance/q089.md`](../chapters/09-operations-performance/q089.md) | Q089 · Redis 应该怎么做安全控制？ |
| 102 | [`chapters/09-operations-performance/q090.md`](../chapters/09-operations-performance/q090.md) | Q090 · Redis 监控最重要的指标有哪些？ |
| 104 | [`chapters/10-redis8-system-design/q091.md`](../chapters/10-redis8-system-design/q091.md) | Q091 · Redis 8 最大的架构变化是什么？ |
| 105 | [`chapters/10-redis8-system-design/q092.md`](../chapters/10-redis8-system-design/q092.md) | Q092 · Vector Set 和 Redis Query Engine Vector Search 怎么选？ |
| 106 | [`chapters/10-redis8-system-design/q093.md`](../chapters/10-redis8-system-design/q093.md) | Q093 · Bloom Filter 为什么适合解决缓存穿透？ |
| 107 | [`chapters/10-redis8-system-design/q094.md`](../chapters/10-redis8-system-design/q094.md) | Q094 · Count-Min Sketch、Top-K、t-digest 有什么作用？ |
| 108 | [`chapters/10-redis8-system-design/q095.md`](../chapters/10-redis8-system-design/q095.md) | Q095 · Redis 8.8 的 Array 与传统 List 有什么不同？ |
| 109 | [`chapters/10-redis8-system-design/q096.md`](../chapters/10-redis8-system-design/q096.md) | Q096 · Redis 8.8 INCREX 为什么值得关注？ |
| 110 | [`chapters/10-redis8-system-design/q097.md`](../chapters/10-redis8-system-design/q097.md) | Q097 · 设计一个秒杀库存系统，你会怎么用 Redis？ |
| 111 | [`chapters/10-redis8-system-design/q098.md`](../chapters/10-redis8-system-design/q098.md) | Q098 · 设计一个高并发排行榜系统。 |
| 112 | [`chapters/10-redis8-system-design/q099.md`](../chapters/10-redis8-system-design/q099.md) | Q099 · 设计一个 Redis Rate Limiter，有哪些算法？ |
| 113 | [`chapters/10-redis8-system-design/q100.md`](../chapters/10-redis8-system-design/q100.md) | Q100 · 终极题：如果让你设计一个生产级 Redis 架构，你会怎么做？ |

附录映射：

- p.114 → `docs/appendix/a-followups.md`
- p.115 → `docs/appendix/b-production-runbook.md`
- p.116 → `docs/appendix/c-study-plan.md`
- p.117 → `docs/appendix/d-version-matrix.md`
- p.118 → `docs/references.md`