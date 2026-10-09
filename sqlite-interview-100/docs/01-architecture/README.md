# 第 01 章：SQLite 架构与定位

> **范围**：Embedded / Serverless / ACID / 选型边界

SQLite 的架构题建议始终从“**进程边界**”入手。传统 client/server 数据库把连接管理、缓存、锁和持久化集中在 server；SQLite 把 parser、planner、VDBE、B-Tree、Pager 与 VFS 放进调用者进程。由此可以顺着推出部署方式、故障域、网络延迟、并发上限与运维模型。

判断 SQLite 是否合适时，不要只问“数据量大不大”，而要问：**数据是否天然归属于单机、写冲突能否被串行化、是否需要跨机器共享同一数据库文件、业务是否接受嵌入式运维模型。**

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 001 | [SQLite 是什么？与 MySQL/PostgreSQL 最大区别是什么？](001-sqlite-vs-client-server.md) | 中 | 高 | 架构 / Serverless |
| 002 | [SQLite 为什么不需要启动数据库服务？](002-why-serverless.md) | 中 | 高 | 架构 / VDBE |
| 003 | [SQLite 最适合哪些场景？](003-best-fit-scenarios.md) | 中 | 高 | 选型 |
| 004 | [哪些场景不适合 SQLite？](004-when-not-to-use-sqlite.md) | 中 | 高 | 选型 / 并发 |
| 005 | [SQLite 能保证 ACID 吗？](005-acid-guarantees.md) | 中 | 高 | ACID / Pager |
| 006 | [SQLite 是内存数据库还是磁盘数据库？](006-memory-vs-disk.md) | 中 | 高 | 基础 |
| 007 | [SQLite 数据库理论最大能有多大？](007-database-size-limits.md) | 中 | 高 | 容量 / Page |
| 008 | [“单文件数据库”是否意味着永远只有一个文件？](008-single-file-myth.md) | 中 | 高 | 文件 / WAL |
| 009 | [为什么 SQLite 在移动端特别流行？](009-why-mobile.md) | 中 | 高 | 移动端 |
| 010 | [如何用一句话概括 SQLite 的设计哲学？](010-design-philosophy.md) | 中 | 高 | 架构总览 |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../02-types-schema-rowid/README.md)
