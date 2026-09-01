# Memcached 面试 100 题 · 源码穿透版

> 100 个问题，一题一 Markdown。内容从 PDF 基线进一步扩展到源码、并发、性能、生产实践和实验。

## 10 章导航

- [01. 基础架构与设计哲学](01-architecture-design/README.md) · 第 001-010 题
- [02. Item 与 SET/GET 源码链路](02-item-set-get-source/README.md) · 第 011-020 题
- [03. Slab Allocator 与内存管理](03-slab-memory/README.md) · 第 021-030 题
- [04. Assoc / Hash Table](04-assoc-hashtable/README.md) · 第 031-040 题
- [05. LRU、TTL 与 Eviction](05-lru-ttl-eviction/README.md) · 第 041-050 题
- [06. 线程、锁、Libevent 与协议](06-thread-lock-libevent-protocol/README.md) · 第 051-060 题
- [07. 一致性哈希与分布式 Memcached](07-consistent-hashing-distributed/README.md) · 第 061-070 题
- [08. 缓存一致性、雪崩、击穿与热点](08-cache-consistency-resilience/README.md) · 第 071-080 题
- [09. 监控、容量规划与故障诊断](09-observability-capacity-troubleshooting/README.md) · 第 081-090 题
- [10. 高级特性、源码与系统设计](10-advanced-source-system-design/README.md) · 第 091-100 题

## 全量题目索引

| # | 题目 | 章 | 难度 | 重要度 | 必刷 |
|---:|---|---:|:---:|:---:|:---:|
| 001 | [Memcached 是什么？为什么它能够作为 KV 存储？](01-architecture-design/001.md) | 1 | P0 | ★★★★★ | ⭐ |
| 002 | [为什么说 Memcached 是 Cache，而不是 Database？](01-architecture-design/002.md) | 1 | P0 | ★★★★★ | ⭐ |
| 003 | [Memcached 为什么快？](01-architecture-design/003.md) | 1 | P0 | ★★★★★ | ⭐ |
| 004 | [Memcached 与 Redis 最根本的区别是什么？](01-architecture-design/004.md) | 1 | P0 | ★★★★☆ |  |
| 005 | [Memcached 是不是一个分布式系统？](01-architecture-design/005.md) | 1 | P0 | ★★★★★ | ⭐ |
| 006 | [Memcached 的分布式逻辑到底在哪里？](01-architecture-design/006.md) | 1 | P0 | ★★★★☆ |  |
| 007 | [Memcached 存进去的对象到底是什么？](01-architecture-design/007.md) | 1 | P0 | ★★★★☆ |  |
| 008 | [为什么 Memcached 不支持 SQL、范围查询和 JOIN？](01-architecture-design/008.md) | 1 | P0 | ★★★★☆ |  |
| 009 | [set、add、replace 的语义差异是什么？](01-architecture-design/009.md) | 1 | P0 | ★★★★☆ |  |
| 010 | [Cache miss 后 Memcached 会自动查数据库吗？](01-architecture-design/010.md) | 1 | P0 | ★★★★☆ |  |
| 011 | [为什么 struct item 是 Memcached 最核心的数据结构？](02-item-set-get-source/011.md) | 2 | P0 | ★★★★★ | ⭐ |
| 012 | [从 set foo bar 开始，说出核心源码调用链。](02-item-set-get-source/012.md) | 2 | P0 | ★★★★★ | ⭐ |
| 013 | [为什么 Memcached 先分配 Item，再读取 value？](02-item-set-get-source/013.md) | 2 | P1 | ★★★☆☆ |  |
| 014 | [新 Item 在什么时候真正对 GET 可见？](02-item-set-get-source/014.md) | 2 | P0 | ★★★★★ | ⭐ |
| 015 | [Item 为什么需要 refcount？](02-item-set-get-source/015.md) | 2 | P0 | ★★★★★ | ⭐ |
| 016 | [第二次 set foo newValue 是直接覆盖旧内存吗？](02-item-set-get-source/016.md) | 2 | P1 | ★★★☆☆ |  |
| 017 | [delete foo 在内部发生什么？](02-item-set-get-source/017.md) | 2 | P1 | ★★★☆☆ |  |
| 018 | [get foo 的源码逻辑如何走？](02-item-set-get-source/018.md) | 2 | P1 | ★★★☆☆ |  |
| 019 | [append/prepend 为什么比普通 set 更复杂？](02-item-set-get-source/019.md) | 2 | P1 | ★★★☆☆ |  |
| 020 | [Memcached 的 CAS 是怎么工作的？](02-item-set-get-source/020.md) | 2 | P0 | ★★★★☆ |  |
| 021 | [Memcached 为什么不用普通 malloc/free 管理所有 Item？](03-slab-memory/021.md) | 3 | P0 | ★★★★★ | ⭐ |
| 022 | [Page、Slab Class、Chunk、Item 的关系是什么？](03-slab-memory/022.md) | 3 | P0 | ★★★★★ | ⭐ |
| 023 | [Slab Class 为什么需要 Growth Factor？](03-slab-memory/023.md) | 3 | P1 | ★★★☆☆ |  |
| 024 | [Slab 解决了什么碎片，又引入了什么碎片？](03-slab-memory/024.md) | 3 | P0 | ★★★★★ | ⭐ |
| 025 | [如何根据 Item 大小选择 Slab Class？](03-slab-memory/025.md) | 3 | P1 | ★★★☆☆ |  |
| 026 | [为什么明明还有内存，一个 SET 仍可能发生 eviction？](03-slab-memory/026.md) | 3 | P1 | ★★★★★ | ⭐ |
| 027 | [Slab Reassign / Automove 是什么？](03-slab-memory/027.md) | 3 | P1 | ★★★☆☆ |  |
| 028 | [Memcached 如何处理很大的 Item？](03-slab-memory/028.md) | 3 | P2 | ★★★☆☆ |  |
| 029 | [-m 4G 是否表示进程 RSS 绝对不会超过 4GB？](03-slab-memory/029.md) | 3 | P1 | ★★★☆☆ |  |
| 030 | [Memcached 最大 Item 是不是固定 1MB？](03-slab-memory/030.md) | 3 | P0 | ★★★★☆ |  |
| 031 | [assoc 模块干什么？](04-assoc-hashtable/031.md) | 4 | P0 | ★★★★★ | ⭐ |
| 032 | [h_next 和 next/prev 有什么区别？](04-assoc-hashtable/032.md) | 4 | P0 | ★★★★★ | ⭐ |
| 033 | [Memcached 怎么处理 Hash Collision？](04-assoc-hashtable/033.md) | 4 | P0 | ★★★★☆ |  |
| 034 | [HashTable 为什么不能无限小？](04-assoc-hashtable/034.md) | 4 | P1 | ★★★☆☆ |  |
| 035 | [Rehash 为什么可能成为性能问题？](04-assoc-hashtable/035.md) | 4 | P2 | ★★★☆☆ |  |
| 036 | [Internal Hash 与 Consistent Hash 是同一个东西吗？](04-assoc-hashtable/036.md) | 4 | P0 | ★★★★☆ |  |
| 037 | [如果 Hash 函数分布不好会怎样？](04-assoc-hashtable/037.md) | 4 | P1 | ★★★☆☆ |  |
| 038 | [为什么 HashTable 存 item* 而不是复制 Value？](04-assoc-hashtable/038.md) | 4 | P1 | ★★★☆☆ |  |
| 039 | [为什么删除 Item 时必须同时处理 Assoc 与 LRU？](04-assoc-hashtable/039.md) | 4 | P1 | ★★★☆☆ |  |
| 040 | [现场实现一个 Mini-Memcached HashTable 怎么做？](04-assoc-hashtable/040.md) | 4 | P1 | ★★★☆☆ |  |
| 041 | [Memcached 当前还是最简单的一根 LRU 链吗？](05-lru-ttl-eviction/041.md) | 5 | P0 | ★★★★★ | ⭐ |
| 042 | [HOT/WARM/COLD 分别解决什么问题？](05-lru-ttl-eviction/042.md) | 5 | P1 | ★★★☆☆ |  |
| 043 | [为什么不在每一次 GET 时同步移动 LRU 节点？](05-lru-ttl-eviction/043.md) | 5 | P2 | ★★★★★ | ⭐ |
| 044 | [TTL 到了以后 Item 会在那一秒立刻被物理删除吗？](05-lru-ttl-eviction/044.md) | 5 | P0 | ★★★★★ | ⭐ |
| 045 | [LRU Crawler 是干什么的？](05-lru-ttl-eviction/045.md) | 5 | P1 | ★★★☆☆ |  |
| 046 | [经典“30 天 TTL 陷阱”是什么？](05-lru-ttl-eviction/046.md) | 5 | P0 | ★★★★★ | ⭐ |
| 047 | [Expiration 和 Eviction 有什么区别？](05-lru-ttl-eviction/047.md) | 5 | P0 | ★★★★★ | ⭐ |
| 048 | [刚被 GET 的 Item 会不会同时被另一个线程 Evict？](05-lru-ttl-eviction/048.md) | 5 | P2 | ★★★☆☆ |  |
| 049 | [什么叫 noeviction？有什么风险？](05-lru-ttl-eviction/049.md) | 5 | P1 | ★★★☆☆ |  |
| 050 | [为什么要看每个 slab class 的 eviction，而不只看全局？](05-lru-ttl-eviction/050.md) | 5 | P1 | ★★★☆☆ |  |
| 051 | [Memcached 是“一连接一线程”吗？](06-thread-lock-libevent-protocol/051.md) | 6 | P0 | ★★★★★ | ⭐ |
| 052 | [Libevent 在 Memcached 中解决什么问题？](06-thread-lock-libevent-protocol/052.md) | 6 | P0 | ★★★★☆ |  |
| 053 | [新连接是怎么交给 Worker 的？](06-thread-lock-libevent-protocol/053.md) | 6 | P1 | ★★★☆☆ |  |
| 054 | [为什么 Memcached 不是线程越多越快？](06-thread-lock-libevent-protocol/054.md) | 6 | P0 | ★★★★☆ |  |
| 055 | [Memcached 内部有哪些典型 Lock？](06-thread-lock-libevent-protocol/055.md) | 6 | P1 | ★★★★★ | ⭐ |
| 056 | [为什么不能只用一个 Global Mutex？](06-thread-lock-libevent-protocol/056.md) | 6 | P0 | ★★★★☆ |  |
| 057 | [Memcached 现在有哪些协议？](06-thread-lock-libevent-protocol/057.md) | 6 | P1 | ★★★★★ | ⭐ |
| 058 | [为什么 Binary Protocol 被 Deprecated？](06-thread-lock-libevent-protocol/058.md) | 6 | P1 | ★★★☆☆ |  |
| 059 | [Meta Protocol 解决了什么传统 GET/SET 难表达的问题？](06-thread-lock-libevent-protocol/059.md) | 6 | P2 | ★★★☆☆ |  |
| 060 | [为什么 Multi-get 通常比循环 get() 好？](06-thread-lock-libevent-protocol/060.md) | 6 | P0 | ★★★★☆ |  |
| 061 | [为什么不能简单使用 hash(key) % N？](07-consistent-hashing-distributed/061.md) | 7 | P0 | ★★★★★ | ⭐ |
| 062 | [一致性哈希解决什么？](07-consistent-hashing-distributed/062.md) | 7 | P0 | ★★★★★ | ⭐ |
| 063 | [Virtual Node 是干什么的？](07-consistent-hashing-distributed/063.md) | 7 | P0 | ★★★★☆ |  |
| 064 | [一致性哈希是在 Memcached Server 内部完成的吗？](07-consistent-hashing-distributed/064.md) | 7 | P0 | ★★★★★ | ⭐ |
| 065 | [加一台 Memcached 后，旧数据会自动迁过去吗？](07-consistent-hashing-distributed/065.md) | 7 | P0 | ★★★★☆ |  |
| 066 | [一台 Memcached Node 突然挂了会发生什么？](07-consistent-hashing-distributed/066.md) | 7 | P0 | ★★★★★ | ⭐ |
| 067 | [Memcached 原生是不是自动复制两份？](07-consistent-hashing-distributed/067.md) | 7 | P0 | ★★★★☆ |  |
| 068 | [为什么缓存系统不一定需要强复制？](07-consistent-hashing-distributed/068.md) | 7 | P1 | ★★★☆☆ |  |
| 069 | [两个客户端的 Hash Ring 配置不一致会怎样？](07-consistent-hashing-distributed/069.md) | 7 | P1 | ★★★☆☆ |  |
| 070 | [Built-in Proxy 是否改变了传统模型？](07-consistent-hashing-distributed/070.md) | 7 | P2 | ★★★☆☆ |  |
| 071 | [什么是 Cache Aside？](08-cache-consistency-resilience/071.md) | 8 | P0 | ★★★★★ | ⭐ |
| 072 | [更新数据库与删除缓存，先做哪个？](08-cache-consistency-resilience/072.md) | 8 | P0 | ★★★★★ | ⭐ |
| 073 | [为什么通常推荐 DELETE Cache，而不是 UPDATE Cache？](08-cache-consistency-resilience/073.md) | 8 | P1 | ★★★☆☆ |  |
| 074 | [什么叫缓存穿透？](08-cache-consistency-resilience/074.md) | 8 | P0 | ★★★★☆ |  |
| 075 | [什么叫缓存击穿 / Stampede？](08-cache-consistency-resilience/075.md) | 8 | P0 | ★★★★★ | ⭐ |
| 076 | [什么叫缓存雪崩？](08-cache-consistency-resilience/076.md) | 8 | P0 | ★★★★★ | ⭐ |
| 077 | [Hot Key 有什么危险？](08-cache-consistency-resilience/077.md) | 8 | P0 | ★★★★★ | ⭐ |
| 078 | [CAS 能不能解决缓存与数据库的强一致性？](08-cache-consistency-resilience/078.md) | 8 | P1 | ★★★☆☆ |  |
| 079 | [incr/decr 为什么适合做轻量计数器？](08-cache-consistency-resilience/079.md) | 8 | P1 | ★★★☆☆ |  |
| 080 | [Session 能不能存在 Memcached？](08-cache-consistency-resilience/080.md) | 8 | P0 | ★★★★☆ |  |
| 081 | [生产 Memcached 第一眼看哪些指标？](09-observability-capacity-troubleshooting/081.md) | 9 | P0 | ★★★★★ | ⭐ |
| 082 | [Hit Rate 怎么计算？](09-observability-capacity-troubleshooting/082.md) | 9 | P0 | ★★★★☆ |  |
| 083 | [evictions 持续增长说明什么？](09-observability-capacity-troubleshooting/083.md) | 9 | P0 | ★★★★★ | ⭐ |
| 084 | [为什么 Item 过期后 curr_items 可能没有立即下降？](09-observability-capacity-troubleshooting/084.md) | 9 | P1 | ★★★☆☆ |  |
| 085 | [get_misses 突然暴涨，你怎么排查？](09-observability-capacity-troubleshooting/085.md) | 9 | P1 | ★★★☆☆ |  |
| 086 | [listen_disabled_num 很高说明什么？](09-observability-capacity-troubleshooting/086.md) | 9 | P1 | ★★★☆☆ |  |
| 087 | [为什么应该使用 Persistent Connections？](09-observability-capacity-troubleshooting/087.md) | 9 | P0 | ★★★★☆ |  |
| 088 | [stats slabs 能帮助判断什么？](09-observability-capacity-troubleshooting/088.md) | 9 | P1 | ★★★☆☆ |  |
| 089 | [Memcached 在 NUMA 机器上有什么问题？](09-observability-capacity-troubleshooting/089.md) | 9 | P2 | ★★★☆☆ |  |
| 090 | [为什么 Swap 对 Memcached 特别危险？](09-observability-capacity-troubleshooting/090.md) | 9 | P0 | ★★★★★ | ⭐ |
| 091 | [Extstore 是什么？Memcached 不是纯 RAM 吗？](10-advanced-source-system-design/091.md) | 10 | P2 | ★★★☆☆ |  |
| 092 | [Extstore 为什么仍需要大量 RAM？](10-advanced-source-system-design/092.md) | 10 | P2 | ★★★☆☆ |  |
| 093 | [什么是 Warm Restart？](10-advanced-source-system-design/093.md) | 10 | P2 | ★★★☆☆ |  |
| 094 | [Meta Protocol 怎么实现 stale-while-revalidate？](10-advanced-source-system-design/094.md) | 10 | P2 | ★★★☆☆ |  |
| 095 | [Meta CAS Override 有什么用途？](10-advanced-source-system-design/095.md) | 10 | P2 | ★★★☆☆ |  |
| 096 | [Built-in Proxy 为什么值得关注？](10-advanced-source-system-design/096.md) | 10 | P2 | ★★★☆☆ |  |
| 097 | [让你设计 100 万 QPS 的 Memcached 集群，怎么回答？](10-advanced-source-system-design/097.md) | 10 | P0 | ★★★★★ | ⭐ |
| 098 | [一个 Node 故障后，怎样避免数据库被 MISS 打死？](10-advanced-source-system-design/098.md) | 10 | P0 | ★★★★★ | ⭐ |
| 099 | [什么场景下会明确选择 Memcached，而不是 Redis？](10-advanced-source-system-design/099.md) | 10 | P1 | ★★★☆☆ |  |
| 100 | [如果让你现场实现一个 Mini-Memcached，你怎么拆？](10-advanced-source-system-design/100.md) | 10 | P0 | ★★★★★ | ⭐ |

## 源码辅助索引

- [Memcached 1.6.45 源码符号地图](../references/source-symbol-map.md)
- [官方资料与源码索引](../references/official-sources.md)
