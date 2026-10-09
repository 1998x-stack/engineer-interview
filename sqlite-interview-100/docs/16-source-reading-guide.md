# SQLite 源码阅读指南

本仓库逐题给出源码模块入口。建议不要直接从 amalgamation `sqlite3.c` 顺序阅读，而是围绕问题沿调用链定位。

| 主题 | 源码树模块 | 建议关注 |
|---|---|---|
| API / Connection | `src/main.c` | connection、busy handler、公开 API |
| SQL prepare | `src/prepare.c` | parse/prepare/schema 检查 |
| VDBE | `src/vdbe.c` | opcode 执行、statement 生命周期 |
| Query Planner | `src/where.c`, `whereexpr.c`, `wherecode.c` | loop、索引候选、cost、代码生成 |
| SELECT / Join | `src/select.c` | join/subquery/flatten/materialization |
| B-Tree | `src/btree.c`, `btreeInt.h` | table/index page、cursor、cell |
| Pager | `src/pager.c` | page cache、transaction、journal |
| WAL | `src/wal.c` | frame、read-mark、checkpoint、WAL-index |
| Schema / DDL | `src/build.c` | CREATE TABLE/INDEX、schema objects |
| INSERT / Conflict | `src/insert.c` | ROWID、constraints、UPSERT/REPLACE |
| Statistics | `src/analyze.c` | ANALYZE、sqlite_stat* |
| VACUUM | `src/vacuum.c` | database rebuild |
| Backup | `src/backup.c` | Online Backup API |
| JSON | `src/json.c` | JSON/JSONB functions |
| FTS5 | `ext/fts5/` | tokenizer、segment、query、ranking |

## 阅读顺序建议

1. 先读官方 Architecture / Query Planner / File Format / WAL 文档，建立术语。
2. 用 `EXPLAIN QUERY PLAN` 或最小复现实验确定“现象”。
3. 在源码树中搜索对应 API、opcode、PRAGMA 或错误码。
4. 从公开入口向下跟 2～4 层调用，不要试图一次读完整模块。
5. 最后再回到 amalgamation `sqlite3.c` 对照目标 release。

## 版本纪律

源码行为必须与目标 SQLite release 对齐。仓库当前稳定基线为 **3.53.4（2026-07-24）**；如果运行时使用系统自带 SQLite、Android/iOS 内置版本或 Python/Node bundling，请先打印实际 runtime version 与 compile options。

- [SQLite Source Repository](https://sqlite.org/src/)
- [SQLite Architecture](https://sqlite.org/arch.html)
- [SQLite Query Planner](https://sqlite.org/queryplanner.html)
- [SQLite Database File Format](https://sqlite.org/fileformat2.html)
- [SQLite WAL](https://sqlite.org/wal.html)
