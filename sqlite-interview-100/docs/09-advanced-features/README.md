# 第 09 章：高级能力

> **范围**：FTS5 / JSONB / Generated Columns / UPSERT

高级能力题应把功能放回数据结构：FTS5 是专门的倒排索引/虚拟表能力；JSON/JSONB 是值表示与函数体系；Generated Column 与 Expression Index 是“计算值是否进入 schema/索引”的不同抽象；UPSERT 与 conflict algorithm 则属于约束冲突后的写语义。答题时要强调功能边界，而不是只背语法。

## 学习目标

- 能在 30 秒内给出每题结论。
- 能继续下钻到 SQLite 内部实现，而不是只背 SQL 语法。
- 能说明版本、journal mode、table 类型、数据分布等边界条件。
- 能用 sqlite3 CLI / `EXPLAIN QUERY PLAN` / PRAGMA 做最小复现实验。

## 本章题目

| 题号 | 题目 | 难度 | 频率 | 标签 |
|---:|---|---|---|---|
| 081 | [为什么不能直接用 LIKE '%keyword%' 做大规模全文搜索？](081-fts5-vs-like.md) | 中 | 高 | FTS5 |
| 082 | [FTS5 tokenizer 为什么非常重要？](082-fts5-tokenizer.md) | 中 | 高 | FTS5 / Tokenizer |
| 083 | [什么是 FTS5 External Content Table？](083-fts5-external-content.md) | 中 | 高 | FTS5 / External content |
| 084 | [什么是 Contentless FTS5？](084-fts5-contentless.md) | 中 | 高 | FTS5 / 版本 |
| 085 | [SQLite JSON 是不是独立 column type？](085-json-storage.md) | 中 | 高 | JSON1 |
| 086 | [什么是 SQLite JSONB？](086-jsonb.md) | 中 | 高 | JSONB / 版本 |
| 087 | [Generated Column 的 VIRTUAL 与 STORED 有什么区别？](087-generated-columns.md) | 中 | 高 | Generated Column |
| 088 | [Generated Column 和 Expression Index 怎么选？](088-generated-vs-expression-index.md) | 中 | 高 | Schema design |
| 089 | [UPSERT 与 INSERT OR REPLACE 有什么区别？](089-upsert-vs-replace.md) | 中 | 高 | UPSERT |
| 090 | [SQLite 五种 ON CONFLICT 策略是什么？](090-on-conflict.md) | 中 | 高 | Conflict resolution |

## 建议学习法

1. 第一遍只口述每题的“30 秒标准回答”。
2. 第二遍自己画底层因果链，再对照“原理推导”。
3. 第三遍运行题目里的实验，观察真实输出。
4. 第四遍做跨题串联：把本章概念与 WAL、B-Tree、Planner、Pager 互相解释。

[← 上一章](../08-operations-integrity/README.md) ｜ [总目录](../README.md) ｜ [下一章 →](../10-production-design/README.md)
