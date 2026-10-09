# 第 07 章：存储引擎与底层原理

> **范围**：VDBE / B-Tree / Page / Pager / VFS

底层题建议始终沿固定链路回答：**SQL → VDBE → B-Tree → Pager/Page Cache → VFS → OS**。表和索引最终都是 B-Tree；B-Tree 以 page 为存储与 I/O 单位；Pager 负责 page cache、事务与文件锁；VFS 隔离操作系统差异。这样能把 ROWID、overflow page、freelist、WAL 和 corruption 风险串成一套统一模型。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 061 | [一条 SQL 在 SQLite 内部大致经历什么？](061-sql-execution-pipeline.md) | 中 | 高 | 内部架构 |
| 062 | [VDBE 是什么？](062-vdbe.md) | 中 | 高 | VDBE |
| 063 | [Rowid Table 的数据如何存？](063-rowid-table-storage.md) | 中 | 高 | Table B-Tree |
| 064 | [Index B-Tree 与 Table B-Tree 有什么差异？](064-index-vs-table-btree.md) | 中 | 高 | Index B-Tree |
| 065 | [SQLite Page 是什么？](065-page.md) | 中 | 高 | Page / Pager |
| 066 | [为什么大 TEXT/BLOB 可能需要 Overflow Page？](066-overflow-page.md) | 中 | 高 | Overflow Page |
| 067 | [Varint 是什么？为什么 SQLite 大量使用？](067-varint.md) | 中 | 高 | File format |
| 068 | [DELETE 很多数据后文件为什么不立刻变小？](068-freelist.md) | 中 | 高 | Freelist |
| 069 | [什么是 WITHOUT ROWID？](069-without-rowid.md) | 中 | 高 | WITHOUT ROWID |
| 070 | [WITHOUT ROWID 有哪些限制和语义变化？](070-without-rowid-limitations.md) | 中 | 高 | WITHOUT ROWID |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../06-query-planner/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../08-operations-integrity/README.md)
