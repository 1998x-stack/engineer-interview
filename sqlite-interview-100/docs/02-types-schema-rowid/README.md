# 第 02 章：类型、Schema 与 ROWID

> **范围**：Storage Class / Affinity / STRICT / ROWID

类型题要区分三个层次：**值的 storage class、列的 type affinity、schema 约束**。普通 SQLite 是动态类型系统；affinity 是转换偏好，不是强类型声明。STRICT table 则把一部分约束提升为 schema 层的强保证。ROWID 题还要进一步连接到底层 table b-tree：`INTEGER PRIMARY KEY` 的特殊语义来自它与 ROWID 的别名关系，而不是 SQL 标准中的一般主键规则。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 011 | [SQLite 真正有哪些数据类型？](011-storage-classes.md) | 中 | 高 | 类型系统 |
| 012 | [什么是 Type Affinity？](012-type-affinity.md) | 中 | 高 | Affinity |
| 013 | [VARCHAR(10) 是否最多存 10 个字符？](013-varchar-length.md) | 中 | 高 | 类型陷阱 |
| 014 | [SQLite 有 BOOLEAN 类型吗？](014-boolean.md) | 中 | 高 | 类型 |
| 015 | [SQLite 如何保存日期时间？](015-date-time-storage.md) | 中 | 高 | 时间 |
| 016 | [STRICT TABLE 解决了什么问题？](016-strict-tables.md) | 中 | 高 | STRICT / 版本敏感 |
| 017 | [STRICT TABLE 中 ANY 有什么特殊语义？](017-strict-any.md) | 中 | 高 | STRICT |
| 018 | [什么是 ROWID？](018-rowid.md) | 中 | 高 | ROWID / B-Tree |
| 019 | [INTEGER PRIMARY KEY 和 INT PRIMARY KEY 一样吗？](019-integer-primary-key.md) | 中 | 高 | ROWID / PK |
| 020 | [INTEGER PRIMARY KEY AUTOINCREMENT 与普通 INTEGER PRIMARY KEY 的区别？](020-autoincrement.md) | 中 | 高 | ROWID / AUTOINCREMENT |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../01-architecture/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../03-transactions-concurrency/README.md)
