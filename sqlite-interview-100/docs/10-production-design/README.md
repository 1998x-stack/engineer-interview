# 第 10 章：生产故障与系统设计

> **范围**：Lock / Bulk Write / Large Scale / Offline-First

系统设计题要把前九章组合成可运行架构：**短事务、受控 writer、明确索引、可观测 query plan、正确 WAL/checkpoint、可回放 migration、稳定业务 ID、可靠备份与完整性检查**。如果设计中出现“拿着写事务等待网络”“100 个线程直接抢同一个 writer”“用 rowid 当跨设备 ID”，通常已经暴露了架构问题。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 091 | [线上持续出现 database is locked，如何系统排查？](091-database-is-locked.md) | 中 | 高 | 故障排查 / S 级 |
| 092 | [100 个线程都要写 SQLite，如何设计？](092-many-writers.md) | 中 | 高 | 系统设计 / Writer Queue |
| 093 | [插入 100 万条数据为什么“一条一 COMMIT”极慢？](093-bulk-insert.md) | 中 | 高 | Bulk insert |
| 094 | [移动 App：大量读取、少量后台写，你会选择什么 journal mode？](094-mobile-journal-mode.md) | 中 | 高 | 移动端 / WAL |
| 095 | [1 亿行 SQLite 查询慢，第一步做什么？](095-hundred-million-row-query.md) | 中 | 高 | 性能诊断 |
| 096 | [如何为 WHERE user_id=? AND status=? ORDER BY created_at DESC LIMIT 20 设计索引？](096-feed-index-design.md) | 中 | 高 | 索引设计 / S 级 |
| 097 | [一个用户可以有很多历史邮箱，但只能有一个“当前邮箱”，Schema 怎么设计？](097-one-current-row.md) | 中 | 高 | 约束设计 |
| 098 | [如何设计 1000 万篇文档的本地全文搜索？](098-local-full-text-search.md) | 中 | 高 | FTS5 / 系统设计 |
| 099 | [App 跨多个历史版本升级 Schema，migration 怎么设计？](099-multi-version-migration.md) | 中 | 高 | Migration |
| 100 | [如何为 Offline-First Notes App 设计 SQLite 架构？](100-offline-first-notes.md) | 中 | 高 | 系统设计 / 终极题 |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../09-advanced-features/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../README.md)
