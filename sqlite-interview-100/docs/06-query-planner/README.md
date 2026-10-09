# 第 06 章：Query Planner 与 SQL 优化

> **范围**：EQP / Statistics / Join / OR / Skip-Scan

Query Planner 题的核心是 **cost-based choice**。Planner 不是“看见索引就用”，而是在候选访问路径、join order、排序、临时 B-Tree、统计信息之间估算成本。面试中应习惯用 `EXPLAIN QUERY PLAN` 先观察 plan shape，再用 `ANALYZE`/`PRAGMA optimize` 与真实数据分布解释为什么计划发生变化。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 051 | [EXPLAIN 与 EXPLAIN QUERY PLAN 有什么区别？](051-explain-vs-eqp.md) | 中 | 高 | EQP / VDBE |
| 052 | [EQP 中 SCAN 与 SEARCH 有何区别？](052-scan-vs-search.md) | 中 | 高 | EQP |
| 053 | [USE TEMP B-TREE FOR ORDER BY 表示什么？](053-temp-btree-order-by.md) | 中 | 高 | 排序 / EQP |
| 054 | [ANALYZE 为什么会改变执行计划？](054-analyze-statistics.md) | 中 | 高 | ANALYZE / 统计 |
| 055 | [现代 SQLite 为什么推荐 PRAGMA optimize？](055-pragma-optimize.md) | 中 | 高 | 统计 / 运维 |
| 056 | [SQLite Join 主要用什么算法？](056-join-algorithm.md) | 中 | 高 | Join / Planner |
| 057 | [SQLite 会严格按 FROM 中的书写顺序 Join 吗？](057-join-order.md) | 中 | 高 | Join reorder |
| 058 | [OR 条件一定不能走索引吗？](058-multi-index-or.md) | 中 | 高 | OR Optimization |
| 059 | [什么是 Skip-Scan？](059-skip-scan.md) | 中 | 高 | Skip-scan |
| 060 | [Correlated Subquery 为什么容易慢？](060-correlated-subquery.md) | 中 | 高 | Subquery |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../05-indexes/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../07-storage-engine/README.md)
