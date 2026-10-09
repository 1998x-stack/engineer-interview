# Redis 面试主题交叉索引

章节适合系统学习，主题索引适合二刷与面试前冲刺。同一道题可以属于多个能力域。

## 数据结构与内存

- [Q003 · Redis 有哪些核心数据类型？分别怎么选？](../chapters/01-data-modeling/q003.md)
- [Q009 · Sorted Set 为什么通常使用 skiplist，而不是平衡树？](../chapters/01-data-modeling/q009.md)
- [Q011 · Redis String 底层为什么不用普通 C 字符串？](../chapters/02-internals-memory/q011.md)
- [Q013 · List 的底层结构是什么？](../chapters/02-internals-memory/q013.md)
- [Q014 · Hash 的底层结构是什么？](../chapters/02-internals-memory/q014.md)
- [Q015 · Redis 为什么会自动改变 encoding？](../chapters/02-internals-memory/q015.md)
- [Q020 · Redis 为什么可能出现内存碎片？](../chapters/02-internals-memory/q020.md)

## Big Key / Hot Key / 容量

- [Q016 · 什么是 Big Key？](../chapters/02-internals-memory/q016.md)
- [Q017 · Big Key 如何治理？](../chapters/02-internals-memory/q017.md)
- [Q018 · 什么是 Hot Key？](../chapters/02-internals-memory/q018.md)
- [Q019 · Hot Key 怎么解决？](../chapters/02-internals-memory/q019.md)
- [Q087 · Redis OOM 了怎么办？](../chapters/09-operations-performance/q087.md)
- [Q100 · 生产级 Redis 架构](../chapters/10-redis8-system-design/q100.md)

## 缓存与一致性

- [Q026 · 缓存穿透](../chapters/03-cache-ttl-eviction/q026.md)
- [Q027 · 缓存击穿](../chapters/03-cache-ttl-eviction/q027.md)
- [Q028 · 缓存雪崩](../chapters/03-cache-ttl-eviction/q028.md)
- [Q029 · Cache Aside 一致性](../chapters/03-cache-ttl-eviction/q029.md)
- [Q030 · Client-Side Caching](../chapters/03-cache-ttl-eviction/q030.md)
- [Q093 · Bloom Filter 与缓存穿透](../chapters/10-redis8-system-design/q093.md)

## 持久化 / RPO / RTO

- [Q031 · RDB](../chapters/04-persistence/q031.md)
- [Q033 · Copy-On-Write](../chapters/04-persistence/q033.md)
- [Q034 · AOF](../chapters/04-persistence/q034.md)
- [Q036 · Multi-Part AOF](../chapters/04-persistence/q036.md)
- [Q037 · RDB vs AOF](../chapters/04-persistence/q037.md)
- [Q039 · AOF everysec 的数据丢失边界](../chapters/04-persistence/q039.md)
- [Q040 · Redis 8.10 BACKUP](../chapters/04-persistence/q040.md)

## 高可用与一致性边界

- [Q041 · 异步复制](../chapters/05-replication-sentinel/q041.md)
- [Q043 · PSYNC](../chapters/05-replication-sentinel/q043.md)
- [Q044 · replication backlog](../chapters/05-replication-sentinel/q044.md)
- [Q045 · WAIT 与强一致](../chapters/05-replication-sentinel/q045.md)
- [Q048 · Sentinel quorum vs majority](../chapters/05-replication-sentinel/q048.md)
- [Q050 · Sentinel 脑裂边界](../chapters/05-replication-sentinel/q050.md)
- [Q059 · Cluster 是否强一致](../chapters/06-cluster/q059.md)

## Cluster 与水平扩展

- [Q051 · 16384 slots](../chapters/06-cluster/q051.md)
- [Q052 · 为什么不是一致性哈希](../chapters/06-cluster/q052.md)
- [Q054 · MOVED vs ASK](../chapters/06-cluster/q054.md)
- [Q055 · Hash Tag](../chapters/06-cluster/q055.md)
- [Q056 · CROSSSLOT](../chapters/06-cluster/q056.md)
- [Q057 · Resharding](../chapters/06-cluster/q057.md)
- [Q060 · 为什么常见 3 主 3 从](../chapters/06-cluster/q060.md)

## 原子性、事务与锁

- [Q061 · 单命令原子性](../chapters/07-transactions-locks/q061.md)
- [Q062 · MULTI/EXEC](../chapters/07-transactions-locks/q062.md)
- [Q063 · Redis Transaction rollback](../chapters/07-transactions-locks/q063.md)
- [Q064 · WATCH](../chapters/07-transactions-locks/q064.md)
- [Q066 · Lua](../chapters/07-transactions-locks/q066.md)
- [Q069 · 单实例分布式锁](../chapters/07-transactions-locks/q069.md)
- [Q070 · Redlock 与 fencing](../chapters/07-transactions-locks/q070.md)

## 消息语义与幂等

- [Q071 · Pub/Sub](../chapters/08-messaging-streams/q071.md)
- [Q072 · Pub/Sub vs Stream](../chapters/08-messaging-streams/q072.md)
- [Q074 · Consumer Group](../chapters/08-messaging-streams/q074.md)
- [Q075 · PEL](../chapters/08-messaging-streams/q075.md)
- [Q076 · XAUTOCLAIM](../chapters/08-messaging-streams/q076.md)
- [Q077 · exactly-once 边界](../chapters/08-messaging-streams/q077.md)
- [Q078 · XNACK](../chapters/08-messaging-streams/q078.md)
- [Q080 · Redis Streams vs Kafka](../chapters/08-messaging-streams/q080.md)

## 性能与事故排查

- [Q081 · 为什么不用 KEYS *](../chapters/09-operations-performance/q081.md)
- [Q082 · SCAN 语义](../chapters/09-operations-performance/q082.md)
- [Q083 · 1ms → 500ms 延迟排查](../chapters/09-operations-performance/q083.md)
- [Q084 · SLOWLOG 边界](../chapters/09-operations-performance/q084.md)
- [Q085 · Pipeline 吞吐](../chapters/09-operations-performance/q085.md)
- [Q086 · CPU 100%](../chapters/09-operations-performance/q086.md)
- [Q087 · OOM](../chapters/09-operations-performance/q087.md)
- [Q088 · Swap](../chapters/09-operations-performance/q088.md)
- [Q090 · 核心监控指标](../chapters/09-operations-performance/q090.md)

## Redis 8.x 新版加分

- [Q040 · BACKUP](../chapters/04-persistence/q040.md)
- [Q078 · XNACK](../chapters/08-messaging-streams/q078.md)
- [Q091 · Redis 8 架构变化](../chapters/10-redis8-system-design/q091.md)
- [Q092 · Vector Set vs Query Engine](../chapters/10-redis8-system-design/q092.md)
- [Q094 · CMS / Top-K / t-digest](../chapters/10-redis8-system-design/q094.md)
- [Q095 · Array vs List](../chapters/10-redis8-system-design/q095.md)
- [Q096 · INCREX](../chapters/10-redis8-system-design/q096.md)

## 系统设计压轴

- [Q097 · 秒杀库存系统](../chapters/10-redis8-system-design/q097.md)
- [Q098 · 高并发排行榜](../chapters/10-redis8-system-design/q098.md)
- [Q099 · Rate Limiter](../chapters/10-redis8-system-design/q099.md)
- [Q100 · 生产级 Redis 架构](../chapters/10-redis8-system-design/q100.md)
