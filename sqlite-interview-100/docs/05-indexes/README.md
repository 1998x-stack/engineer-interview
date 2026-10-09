# 第 05 章：索引设计

> **范围**：B-Tree / Composite / Covering / Partial / Expression

索引题不要停在“建索引”。要从 **B-Tree 的字典序** 推导：哪些谓词能形成连续搜索区间、排序是否天然满足、是否需要回表、索引宽度对缓存与写放大的代价。联合索引、覆盖索引、partial index、expression index 都是在“缩小搜索空间”和“降低额外 I/O”这两个目标上做不同权衡。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 041 | [SQLite 普通索引底层是什么？](041-index-btree.md) | 中 | 高 | 索引 / B-Tree |
| 042 | [联合索引 (a,b,c) 能有效服务哪些条件？](042-composite-index.md) | 中 | 高 | 联合索引 |
| 043 | [什么是 Covering Index？](043-covering-index.md) | 中 | 高 | Covering Index |
| 044 | [有 (a,b,c) 后还需要单列索引 (a) 吗？](044-redundant-prefix-index.md) | 中 | 高 | 索引治理 |
| 045 | [什么是 Partial Index？](045-partial-index.md) | 中 | 高 | Partial Index |
| 046 | [如何用 Partial UNIQUE Index 保证“每个用户最多一条 active 记录”？](046-partial-unique-index.md) | 中 | 高 | Partial / Constraint |
| 047 | [什么是 Expression Index？](047-expression-index.md) | 中 | 高 | Expression Index |
| 048 | [为什么 INDEX ON (x+y)，查询 WHERE y+x=10 可能不用索引？](048-expression-syntax-match.md) | 中 | 高 | Expression Index |
| 049 | [为什么 Expression Index 只能使用 deterministic function？](049-deterministic-functions.md) | 中 | 高 | Deterministic / REINDEX |
| 050 | [为什么“有索引”反而可能比 Full Scan 慢？](050-index-vs-full-scan.md) | 中 | 高 | 选择性 / Cost |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../04-wal-durability/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../06-query-planner/README.md)
