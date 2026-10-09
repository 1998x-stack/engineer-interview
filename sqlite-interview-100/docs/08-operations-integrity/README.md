# 第 08 章：运维、备份与完整性

> **范围**：VACUUM / PRAGMA / FK / Corruption / Migration

运维题的重点是“**不要破坏 SQLite 对文件集合和事务边界的假设**”。VACUUM、backup、schema migration、foreign keys、integrity check、threading mode 都需要明确连接级或文件级前提。遇到疑似 corruption 时优先保全现场，避免随意删除 `-wal`/`-journal`，再进行只读检查和可验证恢复。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 071 | [VACUUM 到底做什么？](071-vacuum.md) | 中 | 高 | VACUUM |
| 072 | [VACUUM 与 auto_vacuum 有什么区别？](072-auto-vacuum.md) | 中 | 高 | 空间回收 |
| 073 | [为什么 VACUUM 后 ROWID 可能改变？](073-vacuum-rowid-change.md) | 中 | 高 | ROWID / VACUUM |
| 074 | [integrity_check 与 quick_check 有什么区别？](074-integrity-check.md) | 中 | 高 | 完整性 |
| 075 | [SQLite Foreign Key 为什么是经典陷阱题？](075-foreign-keys.md) | 中 | 高 | Foreign Key |
| 076 | [如何安全修改 SQLite Schema？](076-schema-migration.md) | 中 | 高 | Migration / 3.53 |
| 077 | [REINDEX 是什么？为什么 3.53 有 REINDEX EXPRESSIONS？](077-reindex-expressions.md) | 中 | 高 | REINDEX / 版本 |
| 078 | [什么是 Schema Cookie？](078-schema-cookie.md) | 中 | 高 | Schema / Prepared |
| 079 | [SQLite 线程安全模式有哪些？](079-threading-modes.md) | 中 | 高 | 线程安全 |
| 080 | [SQLite 数据库最常见的真正 corruption 原因有哪些？](080-corruption-causes.md) | 中 | 高 | Corruption |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../07-storage-engine/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../09-advanced-features/README.md)
