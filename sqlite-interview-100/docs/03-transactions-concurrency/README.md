# 第 03 章：事务、隔离与并发

> **范围**：Transaction / Lock / Busy / Snapshot

事务题应画出连接级状态机：**无事务 → read transaction →（可能升级）write transaction → COMMIT/ROLLBACK**。SQLite 可以有多个 reader，但同一数据库同时只有一个 writer。`BEGIN DEFERRED/IMMEDIATE/EXCLUSIVE` 的差别，本质是“什么时候争取写事务以及在特定 journal mode 下对 reader 的影响”。遇到 `SQLITE_BUSY` 时要分析持锁者和事务生命周期，而不是只调大 timeout。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 021 | [不写 BEGIN，一条 INSERT 有事务吗？](021-implicit-transaction.md) | 中 | 高 | 事务 |
| 022 | [BEGIN DEFERRED 是什么？](022-begin-deferred.md) | 中 | 高 | 事务 / 锁 |
| 023 | [BEGIN IMMEDIATE 与 DEFERRED 有何区别？](023-begin-immediate.md) | 中 | 高 | 事务 / Busy |
| 024 | [BEGIN EXCLUSIVE 与 IMMEDIATE 有何区别？](024-begin-exclusive.md) | 中 | 高 | 事务 / 版本语义 |
| 025 | [SQLite 支持并发读吗？](025-concurrent-reads.md) | 中 | 高 | 并发 |
| 026 | [SQLite 同一数据库能同时有两个 Writer 吗？](026-single-writer.md) | 中 | 高 | 并发 / WAL |
| 027 | [Read transaction 升级为 Write transaction 为什么会失败？](027-read-to-write-upgrade.md) | 中 | 高 | Snapshot / Busy |
| 028 | [busy_timeout 是什么？能解决所有锁问题吗？](028-busy-timeout.md) | 中 | 高 | Busy / 工程 |
| 029 | [SQLite 支持嵌套事务吗？](029-savepoint-nesting.md) | 中 | 高 | SAVEPOINT |
| 030 | [PRAGMA read_uncommitted=ON 就一定能脏读吗？](030-read-uncommitted.md) | 中 | 高 | 隔离级别 |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../02-types-schema-rowid/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../04-wal-durability/README.md)
