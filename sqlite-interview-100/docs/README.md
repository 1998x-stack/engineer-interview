# SQLite 面试 100 题 - 全部题目索引

1. [SQLite 架构与定位](01-architecture/README.md) - Embedded / Serverless / ACID / 选型边界
2. [类型、Schema 与 ROWID](02-types-schema-rowid/README.md) - Storage Class / Affinity / STRICT / ROWID
3. [事务、隔离与并发](03-transactions-concurrency/README.md) - Transaction / Lock / Busy / Snapshot
4. [Journal、WAL 与持久性](04-wal-durability/README.md) - Rollback Journal / WAL / Checkpoint / Crash
5. [索引设计](05-indexes/README.md) - B-Tree / Composite / Covering / Partial / Expression
6. [Query Planner 与 SQL 优化](06-query-planner/README.md) - EQP / Statistics / Join / OR / Skip-Scan
7. [存储引擎与底层原理](07-storage-engine/README.md) - VDBE / B-Tree / Page / Pager / VFS
8. [运维、备份与完整性](08-operations-integrity/README.md) - VACUUM / PRAGMA / FK / Corruption / Migration
9. [高级能力](09-advanced-features/README.md) - FTS5 / JSONB / Generated Columns / UPSERT
10. [生产故障与系统设计](10-production-design/README.md) - Lock / Bulk Write / Large Scale / Offline-First

## 100 题总表

| 题号 | 题目 | 章节 | 难度 | 频率 |
|---:|---|---|---|---|
| 001 | [SQLite 是什么？与 MySQL/PostgreSQL 最大区别是什么？](01-architecture/001-sqlite-vs-client-server.md) | SQLite 架构与定位 | 中 | 高 |
| 002 | [SQLite 为什么不需要启动数据库服务？](01-architecture/002-why-serverless.md) | SQLite 架构与定位 | 中 | 高 |
| 003 | [SQLite 最适合哪些场景？](01-architecture/003-best-fit-scenarios.md) | SQLite 架构与定位 | 中 | 高 |
| 004 | [哪些场景不适合 SQLite？](01-architecture/004-when-not-to-use-sqlite.md) | SQLite 架构与定位 | 中 | 高 |
| 005 | [SQLite 能保证 ACID 吗？](01-architecture/005-acid-guarantees.md) | SQLite 架构与定位 | 中 | 高 |
| 006 | [SQLite 是内存数据库还是磁盘数据库？](01-architecture/006-memory-vs-disk.md) | SQLite 架构与定位 | 中 | 高 |
| 007 | [SQLite 数据库理论最大能有多大？](01-architecture/007-database-size-limits.md) | SQLite 架构与定位 | 中 | 高 |
| 008 | [“单文件数据库”是否意味着永远只有一个文件？](01-architecture/008-single-file-myth.md) | SQLite 架构与定位 | 中 | 高 |
| 009 | [为什么 SQLite 在移动端特别流行？](01-architecture/009-why-mobile.md) | SQLite 架构与定位 | 中 | 高 |
| 010 | [如何用一句话概括 SQLite 的设计哲学？](01-architecture/010-design-philosophy.md) | SQLite 架构与定位 | 中 | 高 |
| 011 | [SQLite 真正有哪些数据类型？](02-types-schema-rowid/011-storage-classes.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 012 | [什么是 Type Affinity？](02-types-schema-rowid/012-type-affinity.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 013 | [VARCHAR(10) 是否最多存 10 个字符？](02-types-schema-rowid/013-varchar-length.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 014 | [SQLite 有 BOOLEAN 类型吗？](02-types-schema-rowid/014-boolean.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 015 | [SQLite 如何保存日期时间？](02-types-schema-rowid/015-date-time-storage.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 016 | [STRICT TABLE 解决了什么问题？](02-types-schema-rowid/016-strict-tables.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 017 | [STRICT TABLE 中 ANY 有什么特殊语义？](02-types-schema-rowid/017-strict-any.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 018 | [什么是 ROWID？](02-types-schema-rowid/018-rowid.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 019 | [INTEGER PRIMARY KEY 和 INT PRIMARY KEY 一样吗？](02-types-schema-rowid/019-integer-primary-key.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 020 | [INTEGER PRIMARY KEY AUTOINCREMENT 与普通 INTEGER PRIMARY KEY 的区别？](02-types-schema-rowid/020-autoincrement.md) | 类型、Schema 与 ROWID | 中 | 高 |
| 021 | [不写 BEGIN，一条 INSERT 有事务吗？](03-transactions-concurrency/021-implicit-transaction.md) | 事务、隔离与并发 | 中 | 高 |
| 022 | [BEGIN DEFERRED 是什么？](03-transactions-concurrency/022-begin-deferred.md) | 事务、隔离与并发 | 中 | 高 |
| 023 | [BEGIN IMMEDIATE 与 DEFERRED 有何区别？](03-transactions-concurrency/023-begin-immediate.md) | 事务、隔离与并发 | 中 | 高 |
| 024 | [BEGIN EXCLUSIVE 与 IMMEDIATE 有何区别？](03-transactions-concurrency/024-begin-exclusive.md) | 事务、隔离与并发 | 中 | 高 |
| 025 | [SQLite 支持并发读吗？](03-transactions-concurrency/025-concurrent-reads.md) | 事务、隔离与并发 | 中 | 高 |
| 026 | [SQLite 同一数据库能同时有两个 Writer 吗？](03-transactions-concurrency/026-single-writer.md) | 事务、隔离与并发 | 中 | 高 |
| 027 | [Read transaction 升级为 Write transaction 为什么会失败？](03-transactions-concurrency/027-read-to-write-upgrade.md) | 事务、隔离与并发 | 中 | 高 |
| 028 | [busy_timeout 是什么？能解决所有锁问题吗？](03-transactions-concurrency/028-busy-timeout.md) | 事务、隔离与并发 | 中 | 高 |
| 029 | [SQLite 支持嵌套事务吗？](03-transactions-concurrency/029-savepoint-nesting.md) | 事务、隔离与并发 | 中 | 高 |
| 030 | [PRAGMA read_uncommitted=ON 就一定能脏读吗？](03-transactions-concurrency/030-read-uncommitted.md) | 事务、隔离与并发 | 中 | 高 |
| 031 | [Rollback Journal 的基本原理是什么？](04-wal-durability/031-rollback-journal.md) | Journal、WAL 与持久性 | 中 | 高 |
| 032 | [WAL 的基本原理是什么？](04-wal-durability/032-wal-basics.md) | Journal、WAL 与持久性 | 中 | 高 |
| 033 | [WAL 为什么允许 Reader 与 Writer 并发？](04-wal-durability/033-wal-read-write-concurrency.md) | Journal、WAL 与持久性 | 中 | 高 |
| 034 | [WAL 是否意味着完全没有锁？](04-wal-durability/034-wal-still-locks.md) | Journal、WAL 与持久性 | 中 | 高 |
| 035 | [为什么 WAL 不适合普通网络文件系统？](04-wal-durability/035-wal-network-filesystem.md) | Journal、WAL 与持久性 | 中 | 高 |
| 036 | [Checkpoint 是什么？](04-wal-durability/036-checkpoint.md) | Journal、WAL 与持久性 | 中 | 高 |
| 037 | [为什么长期 Reader 会导致 WAL 越来越大？](04-wal-durability/037-checkpoint-starvation.md) | Journal、WAL 与持久性 | 中 | 高 |
| 038 | [PRAGMA synchronous 控制什么？](04-wal-durability/038-synchronous.md) | Journal、WAL 与持久性 | 中 | 高 |
| 039 | [什么是 Hot Journal？](04-wal-durability/039-hot-journal.md) | Journal、WAL 与持久性 | 中 | 高 |
| 040 | [2026 年为什么 SQLite 3.53 系列值得关注？](04-wal-durability/040-sqlite-3-53.md) | Journal、WAL 与持久性 | 中 | 高 |
| 041 | [SQLite 普通索引底层是什么？](05-indexes/041-index-btree.md) | 索引设计 | 中 | 高 |
| 042 | [联合索引 (a,b,c) 能有效服务哪些条件？](05-indexes/042-composite-index.md) | 索引设计 | 中 | 高 |
| 043 | [什么是 Covering Index？](05-indexes/043-covering-index.md) | 索引设计 | 中 | 高 |
| 044 | [有 (a,b,c) 后还需要单列索引 (a) 吗？](05-indexes/044-redundant-prefix-index.md) | 索引设计 | 中 | 高 |
| 045 | [什么是 Partial Index？](05-indexes/045-partial-index.md) | 索引设计 | 中 | 高 |
| 046 | [如何用 Partial UNIQUE Index 保证“每个用户最多一条 active 记 录”？](05-indexes/046-partial-unique-index.md) | 索引设计 | 中 | 高 |
| 047 | [什么是 Expression Index？](05-indexes/047-expression-index.md) | 索引设计 | 中 | 高 |
| 048 | [为什么 INDEX ON (x+y)，查询 WHERE y+x=10 可能不用索引？](05-indexes/048-expression-syntax-match.md) | 索引设计 | 中 | 高 |
| 049 | [为什么 Expression Index 只能使用 deterministic function？](05-indexes/049-deterministic-functions.md) | 索引设计 | 中 | 高 |
| 050 | [为什么“有索引”反而可能比 Full Scan 慢？](05-indexes/050-index-vs-full-scan.md) | 索引设计 | 中 | 高 |
| 051 | [EXPLAIN 与 EXPLAIN QUERY PLAN 有什么区别？](06-query-planner/051-explain-vs-eqp.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 052 | [EQP 中 SCAN 与 SEARCH 有何区别？](06-query-planner/052-scan-vs-search.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 053 | [USE TEMP B-TREE FOR ORDER BY 表示什么？](06-query-planner/053-temp-btree-order-by.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 054 | [ANALYZE 为什么会改变执行计划？](06-query-planner/054-analyze-statistics.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 055 | [现代 SQLite 为什么推荐 PRAGMA optimize？](06-query-planner/055-pragma-optimize.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 056 | [SQLite Join 主要用什么算法？](06-query-planner/056-join-algorithm.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 057 | [SQLite 会严格按 FROM 中的书写顺序 Join 吗？](06-query-planner/057-join-order.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 058 | [OR 条件一定不能走索引吗？](06-query-planner/058-multi-index-or.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 059 | [什么是 Skip-Scan？](06-query-planner/059-skip-scan.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 060 | [Correlated Subquery 为什么容易慢？](06-query-planner/060-correlated-subquery.md) | Query Planner 与 SQL 优化 | 中 | 高 |
| 061 | [一条 SQL 在 SQLite 内部大致经历什么？](07-storage-engine/061-sql-execution-pipeline.md) | 存储引擎与底层原理 | 中 | 高 |
| 062 | [VDBE 是什么？](07-storage-engine/062-vdbe.md) | 存储引擎与底层原理 | 中 | 高 |
| 063 | [Rowid Table 的数据如何存？](07-storage-engine/063-rowid-table-storage.md) | 存储引擎与底层原理 | 中 | 高 |
| 064 | [Index B-Tree 与 Table B-Tree 有什么差异？](07-storage-engine/064-index-vs-table-btree.md) | 存储引擎与底层原理 | 中 | 高 |
| 065 | [SQLite Page 是什么？](07-storage-engine/065-page.md) | 存储引擎与底层原理 | 中 | 高 |
| 066 | [为什么大 TEXT/BLOB 可能需要 Overflow Page？](07-storage-engine/066-overflow-page.md) | 存储引擎与底层原理 | 中 | 高 |
| 067 | [Varint 是什么？为什么 SQLite 大量使用？](07-storage-engine/067-varint.md) | 存储引擎与底层原理 | 中 | 高 |
| 068 | [DELETE 很多数据后文件为什么不立刻变小？](07-storage-engine/068-freelist.md) | 存储引擎与底层原理 | 中 | 高 |
| 069 | [什么是 WITHOUT ROWID？](07-storage-engine/069-without-rowid.md) | 存储引擎与底层原理 | 中 | 高 |
| 070 | [WITHOUT ROWID 有哪些限制和语义变化？](07-storage-engine/070-without-rowid-limitations.md) | 存储引擎与底层原理 | 中 | 高 |
| 071 | [VACUUM 到底做什么？](08-operations-integrity/071-vacuum.md) | 运维、备份与完整性 | 中 | 高 |
| 072 | [VACUUM 与 auto_vacuum 有什么区别？](08-operations-integrity/072-auto-vacuum.md) | 运维、备份与完整性 | 中 | 高 |
| 073 | [为什么 VACUUM 后 ROWID 可能改变？](08-operations-integrity/073-vacuum-rowid-change.md) | 运维、备份与完整性 | 中 | 高 |
| 074 | [integrity_check 与 quick_check 有什么区别？](08-operations-integrity/074-integrity-check.md) | 运维、备份与完整性 | 中 | 高 |
| 075 | [SQLite Foreign Key 为什么是经典陷阱题？](08-operations-integrity/075-foreign-keys.md) | 运维、备份与完整性 | 中 | 高 |
| 076 | [如何安全修改 SQLite Schema？](08-operations-integrity/076-schema-migration.md) | 运维、备份与完整性 | 中 | 高 |
| 077 | [REINDEX 是什么？为什么 3.53 有 REINDEX EXPRESSIONS？](08-operations-integrity/077-reindex-expressions.md) | 运维、备份与完整性 | 中 | 高 |
| 078 | [什么是 Schema Cookie？](08-operations-integrity/078-schema-cookie.md) | 运维、备份与完整性 | 中 | 高 |
| 079 | [SQLite 线程安全模式有哪些？](08-operations-integrity/079-threading-modes.md) | 运维、备份与完整性 | 中 | 高 |
| 080 | [SQLite 数据库最常见的真正 corruption 原因有哪些？](08-operations-integrity/080-corruption-causes.md) | 运维、备份与完整性 | 中 | 高 |
| 081 | [为什么不能直接用 LIKE '%keyword%' 做大规模全文搜索？](09-advanced-features/081-fts5-vs-like.md) | 高级能力 | 中 | 高 |
| 082 | [FTS5 tokenizer 为什么非常重要？](09-advanced-features/082-fts5-tokenizer.md) | 高级能力 | 中 | 高 |
| 083 | [什么是 FTS5 External Content Table？](09-advanced-features/083-fts5-external-content.md) | 高级能力 | 中 | 高 |
| 084 | [什么是 Contentless FTS5？](09-advanced-features/084-fts5-contentless.md) | 高级能力 | 中 | 高 |
| 085 | [SQLite JSON 是不是独立 column type？](09-advanced-features/085-json-storage.md) | 高级能力 | 中 | 高 |
| 086 | [什么是 SQLite JSONB？](09-advanced-features/086-jsonb.md) | 高级能力 | 中 | 高 |
| 087 | [Generated Column 的 VIRTUAL 与 STORED 有什么区别？](09-advanced-features/087-generated-columns.md) | 高级能力 | 中 | 高 |
| 088 | [Generated Column 和 Expression Index 怎么选？](09-advanced-features/088-generated-vs-expression-index.md) | 高级能力 | 中 | 高 |
| 089 | [UPSERT 与 INSERT OR REPLACE 有什么区别？](09-advanced-features/089-upsert-vs-replace.md) | 高级能力 | 中 | 高 |
| 090 | [SQLite 五种 ON CONFLICT 策略是什么？](09-advanced-features/090-on-conflict.md) | 高级能力 | 中 | 高 |
| 091 | [线上持续出现 database is locked，如何系统排查？](10-production-design/091-database-is-locked.md) | 生产故障与系统设计 | 中 | 高 |
| 092 | [100 个线程都要写 SQLite，如何设计？](10-production-design/092-many-writers.md) | 生产故障与系统设计 | 中 | 高 |
| 093 | [插入 100 万条数据为什么“一条一 COMMIT”极慢？](10-production-design/093-bulk-insert.md) | 生产故障与系统设计 | 中 | 高 |
| 094 | [移动 App：大量读取、少量后台写，你会选择什么 journal mode？](10-production-design/094-mobile-journal-mode.md) | 生产故障与系统设计 | 中 | 高 |
| 095 | [1 亿行 SQLite 查询慢，第一步做什么？](10-production-design/095-hundred-million-row-query.md) | 生产故障与系统设计 | 中 | 高 |
| 096 | [如何为 WHERE user_id=? AND status=? ORDER BY created_at DESC LIMIT 20 设计索引？](10-production-design/096-feed-index-design.md) | 生产故障与系统设计 | 中 | 高 |
| 097 | [一个用户可以有很多历史邮箱，但只能有一个“当前邮箱”，Schema 怎么设计？](10-production-design/097-one-current-row.md) | 生产故障与系统设计 | 中 | 高 |
| 098 | [如何设计 1000 万篇文档的本地全文搜索？](10-production-design/098-local-full-text-search.md) | 生产故障与系统设计 | 中 | 高 |
| 099 | [App 跨多个历史版本升级 Schema，migration 怎么设计？](10-production-design/099-multi-version-migration.md) | 生产故障与系统设计 | 中 | 高 |
| 100 | [如何为 Offline-First Notes App 设计 SQLite 架构？](10-production-design/100-offline-first-notes.md) | 生产故障与系统设计 | 中 | 高 |

## 实战实验室

- [10 个章节级可复现实验](labs/README.md)
