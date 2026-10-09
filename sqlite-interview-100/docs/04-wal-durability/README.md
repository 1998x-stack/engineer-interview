# 第 04 章：Journal、WAL 与持久性

> **范围**：Rollback Journal / WAL / Checkpoint / Crash

Journal/WAL 题的统一坐标是“**如何让页面修改同时满足原子性、崩溃恢复和并发读取**”。Rollback journal 保存 before-image；WAL 保存 after-image 并把 checkpoint 延后。WAL 提升的是 reader/writer 重叠能力，不会突破单 writer 约束。任何 WAL 性能问题最终都可以下钻到：WAL append、reader end mark、wal-index、checkpoint progress 与 fsync/synchronous 策略。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 031 | [Rollback Journal 的基本原理是什么？](031-rollback-journal.md) | 中 | 高 | Journal / ACID |
| 032 | [WAL 的基本原理是什么？](032-wal-basics.md) | 中 | 高 | WAL |
| 033 | [WAL 为什么允许 Reader 与 Writer 并发？](033-wal-read-write-concurrency.md) | 中 | 高 | WAL / Snapshot |
| 034 | [WAL 是否意味着完全没有锁？](034-wal-still-locks.md) | 中 | 高 | WAL / 锁 |
| 035 | [为什么 WAL 不适合普通网络文件系统？](035-wal-network-filesystem.md) | 中 | 高 | WAL / 文件系统 |
| 036 | [Checkpoint 是什么？](036-checkpoint.md) | 中 | 高 | WAL / Checkpoint |
| 037 | [为什么长期 Reader 会导致 WAL 越来越大？](037-checkpoint-starvation.md) | 中 | 高 | Checkpoint starvation |
| 038 | [PRAGMA synchronous 控制什么？](038-synchronous.md) | 中 | 高 | Durability |
| 039 | [什么是 Hot Journal？](039-hot-journal.md) | 中 | 高 | Crash recovery |
| 040 | [2026 年为什么 SQLite 3.53 系列值得关注？](040-sqlite-3-53.md) | 中 | 高 | 版本 / 3.53 |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../03-transactions-concurrency/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../05-indexes/README.md)
