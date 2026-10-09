# SQLite Interview 100 - 深入原理、工程实战与系统设计

> 100 道 SQLite 面试题，一个问题一个 Markdown。内容覆盖 SQL 使用、事务与锁、WAL、B-Tree/Pager、Query Planner、索引、FTS5、JSONB、运维与 Offline-First 系统设计。

[![SQLite](https://img.shields.io/badge/SQLite-3.53.4-blue)](https://www.sqlite.org/releaselog/3_53_4.html)
![Questions](https://img.shields.io/badge/questions-100-success)
![Docs](https://img.shields.io/badge/docs-MkDocs%20ready-informational)

## v2 深度增强内容

本仓库的 100 道题已经从“面试提纲”升级为“可独立阅读的技术章节”。每题新增：

- 面试评分 Rubric（0～4 分）与专家级回答标准；
- SQLite 子系统定位与白板执行路径；
- 从 SQL 语义到 Planner/VDBE/B-Tree/Pager/WAL 的分层推导；
- 反例、边界条件与故障注入问题；
- 源码阅读入口（按章节指向 `where.c`、`btree.c`、`pager.c`、`wal.c`、`vdbe.c`、FTS5/JSON 等模块）；
- 一分钟复习卡与可观测指标；
- 10 个章节级可复现实战 Lab。

> 目标不是把答案写得更长，而是让每个结论都有 **机制、证据、边界和工程决策**。

## 为什么做这个仓库

SQLite 面试看似“数据库基础”，真正区分度却来自能否把 SQL 层现象下钻到 **Planner -> VDBE -> B-Tree -> Pager -> WAL/File Lock -> VFS**。本仓库以随附 PDF 为主干，把每题进一步扩展成可复习、可实验、可追问、可部署的独立知识单元。

## 仓库特点

- **100 题 = 100 个 Markdown**：适合逐题刷、PR 评论和深链接分享。
- **PDF 全量保留**：`book/SQLite面试100题_专业详解_2026.pdf`。
- **每题统一专业结构**：考点 -> 30 秒回答 -> Know-Why -> 深挖 -> 实验 -> 误区 -> 追问 -> Checklist -> 官方资料。
- **版本敏感标记**：基线 SQLite 3.53.4；提醒核对目标 runtime。
- **官方文档优先**：所有题均提供 sqlite.org 入口。
- **MkDocs / GitHub Pages Ready**：带 `mkdocs.yml` 和 CI 校验。

## 十章路线

| 章 | 专题 | 范围 | 题号 |
|---:|---|---|---:|
| 01 | [SQLite 架构与定位](docs/01-architecture/README.md) | Embedded / Serverless / ACID / 选型边界 | 001-010 |
| 02 | [类型、Schema 与 ROWID](docs/02-types-schema-rowid/README.md) | Storage Class / Affinity / STRICT / ROWID | 011-020 |
| 03 | [事务、隔离与并发](docs/03-transactions-concurrency/README.md) | Transaction / Lock / Busy / Snapshot | 021-030 |
| 04 | [Journal、WAL 与持久性](docs/04-wal-durability/README.md) | Rollback Journal / WAL / Checkpoint / Crash | 031-040 |
| 05 | [索引设计](docs/05-indexes/README.md) | B-Tree / Composite / Covering / Partial / Expression | 041-050 |
| 06 | [Query Planner 与 SQL 优化](docs/06-query-planner/README.md) | EQP / Statistics / Join / OR / Skip-Scan | 051-060 |
| 07 | [存储引擎与底层原理](docs/07-storage-engine/README.md) | VDBE / B-Tree / Page / Pager / VFS | 061-070 |
| 08 | [运维、备份与完整性](docs/08-operations-integrity/README.md) | VACUUM / PRAGMA / FK / Corruption / Migration | 071-080 |
| 09 | [高级能力](docs/09-advanced-features/README.md) | FTS5 / JSONB / Generated Columns / UPSERT | 081-090 |
| 10 | [生产故障与系统设计](docs/10-production-design/README.md) | Lock / Bulk Write / Large Scale / Offline-First | 091-100 |

## 快速入口

- [全部 100 题索引](docs/README.md)
- [实战实验室](docs/labs/README.md)
- [前言与学习方法](docs/00-preface.md)
- [S 级必刷 25 题](docs/11-s-tier.md)
- [SQLite 心智模型](docs/12-mental-model.md)
- [生产排障 Checklist](docs/13-production-checklist.md)
- [SQLite 官方资料](docs/14-official-references.md)
- [PDF ↔ Markdown 内容映射](docs/15-content-map.md)
- [PDF 原书](book/SQLite面试100题_专业详解_2026.pdf)

## 推荐刷题方式

```text
Level 1  能给出 30 秒结论
   ↓
Level 2  能解释 Know-Why
   ↓
Level 3  能画 B-Tree/WAL/事务状态白板
   ↓
Level 4  能用 EQP/PRAGMA/双连接实验验证
   ↓
Level 5  能处理 database is locked / 亿级查询 / Offline-first 系统设计
```

## 本地预览文档

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt
mkdocs serve
```

## 仓库自检

```bash
python scripts/validate_repo.py
```

校验内容包括：100 个题目文件是否齐全、题号是否唯一、核心章节是否齐全、10 个 Lab 是否存在、内部 Markdown 链接与 PDF 是否存在。当前 v2 题目正文平均约 5.7K 字符。

## 内容来源说明

- `book/` 中的 PDF 是本仓库内容主干。
- Markdown 在 PDF 基础上增加工程化分析、实验、交叉引用与 SQLite 官方文档入口。
- 学习组织方式参考“逐题拆解”的面试书思路，但不复制第三方书籍内容或版式。

## License

文档内容建议在公开发布前由仓库所有者选择合适许可证。本交付版本不替你自动决定版权许可；代码辅助脚本可按你的团队规范另行授权。
