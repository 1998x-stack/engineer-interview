# S 级必刷 25 题

1. [题 012 什么是 Type Affinity？](02-types-schema-rowid/012-type-affinity.md)
2. [题 016 STRICT TABLE 解决了什么问题？](02-types-schema-rowid/016-strict-tables.md)
3. [题 018 什么是 ROWID？](02-types-schema-rowid/018-rowid.md)
4. [题 019 INTEGER PRIMARY KEY 和 INT PRIMARY KEY 一样吗？](02-types-schema-rowid/019-integer-primary-key.md)
5. [题 020 INTEGER PRIMARY KEY AUTOINCREMENT 与普通 INTEGER PRIMARY KEY 的区别？](02-types-schema-rowid/020-autoincrement.md)
6. [题 022 BEGIN DEFERRED 是什么？](03-transactions-concurrency/022-begin-deferred.md)
7. [题 023 BEGIN IMMEDIATE 与 DEFERRED 有何区别？](03-transactions-concurrency/023-begin-immediate.md)
8. [题 024 BEGIN EXCLUSIVE 与 IMMEDIATE 有何区别？](03-transactions-concurrency/024-begin-exclusive.md)
9. [题 026 SQLite 同一数据库能同时有两个 Writer 吗？](03-transactions-concurrency/026-single-writer.md)
10. [题 027 Read transaction 升级为 Write transaction 为什么会失败？](03-transactions-concurrency/027-read-to-write-upgrade.md)
11. [题 032 WAL 的基本原理是什么？](04-wal-durability/032-wal-basics.md)
12. [题 033 WAL 为什么允许 Reader 与 Writer 并发？](04-wal-durability/033-wal-read-write-concurrency.md)
13. [题 036 Checkpoint 是什么？](04-wal-durability/036-checkpoint.md)
14. [题 037 为什么长期 Reader 会导致 WAL 越来越大？](04-wal-durability/037-checkpoint-starvation.md)
15. [题 042 联合索引 (a,b,c) 能有效服务哪些条件？](05-indexes/042-composite-index.md)
16. [题 043 什么是 Covering Index？](05-indexes/043-covering-index.md)
17. [题 045 什么是 Partial Index？](05-indexes/045-partial-index.md)
18. [题 048 为什么 INDEX ON (x+y)，查询 WHERE y+x=10 可能不用索引？](05-indexes/048-expression-syntax-match.md)
19. [题 050 为什么“有索引”反而可能比 Full Scan 慢？](05-indexes/050-index-vs-full-scan.md)
20. [题 051 EXPLAIN 与 EXPLAIN QUERY PLAN 有什么区别？](06-query-planner/051-explain-vs-eqp.md)
21. [题 054 ANALYZE 为什么会改变执行计划？](06-query-planner/054-analyze-statistics.md)
22. [题 056 SQLite Join 主要用什么算法？](06-query-planner/056-join-algorithm.md)
23. [题 089 UPSERT 与 INSERT OR REPLACE 有什么区别？](09-advanced-features/089-upsert-vs-replace.md)
24. [题 091 线上持续出现 database is locked，如何系统排查？](10-production-design/091-database-is-locked.md)
25. [题 100 如何为 Offline-First Notes App 设计 SQLite 架构？](10-production-design/100-offline-first-notes.md)

## 冲刺方法

如果只剩 2 小时：先把这 25 题逐题口述到能解释“为什么”；再重点白板推演题 091、096、100。
