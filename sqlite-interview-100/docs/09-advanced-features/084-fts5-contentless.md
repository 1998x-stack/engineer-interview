---
title: "题 084 什么是 Contentless FTS5？"
question_id: 84
chapter: 9
chapter_name: "高级能力"
difficulty: "中"
frequency: "高"
tags: ["FTS5", "版本"]
source_hint: "FTS5"
sqlite_baseline: "3.53.4"
version_sensitive: false
---

# 题 084：什么是 Contentless FTS5？

> **章节**：高级能力  
> **难度**：中 ｜ **频率**：高 ｜ **标签**：FTS5 / 版本  
> **版本基线**：SQLite 3.53.4（2026-07-24）

[← 返回章节目录](README.md) ｜ [总目录](../README.md)

## 1. 面试官到底在考什么

这道题不只考定义。高质量回答应该体现三层能力：

1. **语义层**：给出准确结论，明确成立前提。
2. **实现层**：把结论连接到 SQLite 的 Planner / VDBE / B-Tree / Pager / WAL / VFS 中相关层。
3. **工程层**：说明何时值得使用、何时会失效，以及如何用实验或诊断工具验证。

高级能力题应把功能放回数据结构：FTS5 是专门的倒排索引/虚拟表能力；JSON/JSONB 是值表示与函数体系；Generated Column 与 Expression Index 是“计算值是否进入 schema/索引”的不同抽象；UPSERT 与 conflict algorithm 则属于约束冲突后的写语义。答题时要强调功能边界，而不是只背语法。

## 2. 30 秒标准回答

结论 FTS5 只保存索引、不保留原始列值，能显著节省空间；读取原列通常得到 NULL。

## 3. 原理推导（Know-Why）

经典 contentless 模式的 UPDATE/DELETE 限制较多。自 3.43 起 contentless-delete 模式改善了常规 UPDATE/DELETE 支持，新代码如果不要求旧版本兼容通常更值得考虑。

## 4. 深入分析

### 4.1 关键推导

把题目中的 **什么是 Contentless FTS5** 放回本章的统一模型中分析，而不是孤立背结论。

### 4.2 关键推导

回答时至少覆盖：SQL/Schema 层可观察行为、SQLite 内部实现原因、以及生产环境中的性能或一致性代价。

### 4.3 关键推导

如果面试官改变前提（SQLite 版本、journal mode、rowid/WITHOUT ROWID、数据分布），应重新判断而不是坚持绝对答案。

## 5. 代码 / 白板 / 可复现实验

### 建议动手实验

```sql
CREATE VIRTUAL TABLE docs_fts USING fts5(title, body);
INSERT INTO docs_fts(title, body) VALUES ('SQLite WAL', 'checkpoint and snapshot isolation');
SELECT rowid, title FROM docs_fts WHERE docs_fts MATCH 'sqlite AND wal';
```

## 6. 边界条件与常见误区

- ⚠ 把 contentless 当普通表使用 SELECT * 取正文。

进一步检查：

- 是否把 MySQL/PostgreSQL 的语义直接迁移到了 SQLite？
- 是否区分了“SQL 看起来等价”和“Planner 能证明等价”？
- 是否把性能优化说成了绝对规则，而没有用 EQP/benchmark 验证？
- 是否忽略了连接级 PRAGMA、事务生命周期或构建选项？

## 7. 面试官继续追问

- → contentless-delete 的 tombstone/merge 有何含义？

建议继续准备两类追问：

- **实现追问**：这个行为最终由哪个 SQLite 子系统负责？
- **生产追问**：如果线上出现相反现象，你如何用最小实验定位原因？

## 8. 工程实践 Checklist

- [ ] 先确认扩展是否在目标构建启用
- [ ] 功能边界与一致性责任写进设计
- [ ] 对 tokenizer/schema/冲突副作用做测试

## 9. 相关题目

- [题 083 什么是 FTS5 External Content Table？](../09-advanced-features/083-fts5-external-content.md)
- [题 085 SQLite JSON 是不是独立 column type？](../09-advanced-features/085-json-storage.md)

## 10. 面试评分 Rubric

> 这部分用于自测，也可以直接给面试官/出题人作为评分参考。

| 档位 | 表现 |
|---|---|
| **0 分：概念混淆** | 把 SQLite 与 client/server 数据库的机制混为一谈，或给出与题目相反的结论。 |
| **1 分：背到结论** | 能说出“结论 FTS5 只保存索引、不保留原始列值，能显著节省空间；读取原列通常得到 NULL。”，但无法解释为什么、适用前提或如何验证。 |
| **2 分：机制正确** | 能把结论连接到本题所属的 SQLite 子系统，并指出至少一个边界条件。 |
| **3 分：工程可用** | 能给出最小实验/SQL/EQP/PRAGMA 证据，并讨论性能、正确性或运维权衡。 |
| **4 分：专家级** | 能进一步解释源码/文件结构/状态机层面的原因，识别版本敏感点，并对真实生产场景给出可观测、可回归的方案。 |

**建议口述结构**：先给结论（10 秒）→ 给机制（20～40 秒）→ 给反例/边界（20 秒）→ 如果面试官继续追问，再画白板或给实验。

## 11. 专业深化：把这题讲到实现层

### 11.1 本题在 SQLite 整体架构中的位置

```text
Relational core
 ├─ FTS5 virtual table → inverted index
 ├─ JSON/JSONB functions → document fragments
 ├─ Generated columns / expression indexes
 └─ UPSERT / conflict policies → write semantics
```

高级特性题的关键是知道“它属于关系核心、虚表扩展还是函数层”，并清楚它解决的问题、维护成本和一致性责任。尤其 FTS5 external/contentless 模式、JSONB 格式、REPLACE 删除再插入语义都容易被误解。

针对 **“什么是 Contentless FTS5？”**，还应补充这一条专业判断：

> contentless FTS 进一步不保存可返回的原文，适合只需要 rowid/匹配能力的索引场景；删除/更新语义要按具体 contentless 选项设计。

### 11.2 从“结论”推导到“为什么”

不要用数据库通识替代 SQLite 机制。建议按下面四层递进：

1. **SQL/语义层**：先明确本题结论，以及它是否依赖 journal mode、表类型、连接设置、索引结构或 SQLite 版本。
2. **Planner/执行层**：说明 SQLite 是否需要额外 seek、scan、sort、lock、type conversion、checkpoint 或 constraint check。
3. **B-Tree/Pager/WAL 层**：如果问题涉及性能或并发，继续说明最终会落到哪些 page、B-Tree、journal/WAL 或 VFS 操作。
4. **工程层**：给出可以监控的指标和可以复现的最小实验，而不是只说“通常更快/更安全”。

### 11.3 如何验证，而不是“凭经验回答”

使用最小表构造行为实验：FTS5 比较 MATCH 与 LIKE；JSON 用 `json_valid/json_extract`；generated column 查看 `table_xinfo`；UPSERT/REPLACE 配 trigger 和 FK 观察副作用。

推荐形成固定证据链：

```text
假设
 ↓
最小可复现数据/两个独立连接/代表性分布
 ↓
EXPLAIN QUERY PLAN / typeof() / PRAGMA / 错误码
 ↓
耗时、I/O、WAL/page/index 大小等指标
 ↓
修改一个变量后复测
```

### 11.4 性能、正确性与可维护性的三角权衡

高级能力能减少应用代码与外部依赖，但会引入专用索引、同步责任、版本兼容和 schema 复杂度。选型必须关注“是否可验证、是否可迁移、是否能重建”。

面试中如果只谈性能，容易漏掉 SQLite 最重要的工程特性：**很多优化本质是在“更少 I/O / 更短锁时间 / 更少重复计算”与“更多存储 / 更复杂 schema / 更强运维责任”之间交换成本。**

## 12. 反例、边界与故障注入

### 12.1 必须主动说明的边界

- 不把某个优化策略描述成“永远”。SQLite planner、数据分布、journal mode、编译选项与版本都可能改变结果。
- 不把“SQL 语义正确”与“执行计划高效”混为一谈；同样，也不把“计划看起来用了索引”与“真实运行一定更快”混为一谈。
- 不把连接级行为当成全局永久设置；`foreign_keys`、`busy_timeout`、部分 PRAGMA 和 transaction state 都要结合具体 connection。
- 涉及并发时必须区分 **reader/writer、writer/writer、read→write upgrade、checkpoint** 四类冲突。
- 涉及 schema/索引时要同时考虑读收益和写放大；涉及维护命令时要考虑锁窗口、磁盘空间与失败恢复。

### 12.2 建议的故障注入问题

把本题结论反过来问自己：

1. 什么数据分布或并发时序会让“通常正确”的经验失效？
2. 如果换成 WAL / rollback mode，结论是否变化？
3. 如果数据量扩大 100 倍，主要成本会从 CPU、B-Tree seek、page I/O、锁等待还是临时排序中哪一项暴露？
4. 如果应用崩溃在关键步骤中间，SQLite 能恢复什么，应用层还需要恢复什么？
5. 如何设计一个 20 行以内的 SQL/脚本，让同事复现这一行为？

## 13. 源码阅读路线与实战 Lab

### 13.1 源码入口

如果准备高级/源码岗位，不需要一上来通读 `sqlite3.c`。先围绕本题沿调用链阅读：

- `ext/fts5/*`：FTS5 tokenizer/index/query
- `src/json.c`：JSON/JSONB
- `src/insert.c`：UPSERT/REPLACE/conflict handling
- `src/build.c / expr.c`：generated columns 与 expression
- `src/vtab.c`：virtual table 框架

> SQLite 官方发布常见的是 amalgamation `sqlite3.c`；上面的文件名指 SQLite 源码树中的逻辑模块，便于定位实现。源码行为仍应以目标版本为准。

- [统一源码阅读指南](../16-source-reading-guide.md)

### 13.2 对应章节实验

- [进入「FTS5 / JSON / UPSERT Lab」](../labs/09-advanced-lab.md)

建议把实验结果（SQLite 版本、schema、数据规模、EQP、耗时）记录到自己的笔记中。面试时能说出“我实际验证过”，通常比单纯背术语更有说服力。

### 13.3 一分钟复习卡

- **一句话结论**：结论 FTS5 只保存索引、不保留原始列值，能显著节省空间；读取原列通常得到 NULL。
- **必须解释的 Why**：它为什么由当前 SQLite 子系统的实现产生？
- **一个反例/边界**：什么条件变化后不能直接套用这条结论？
- **一个验证工具**：本题优先用哪一个——`EXPLAIN QUERY PLAN`、`typeof()`、`PRAGMA`、双连接并发实验、文件大小/page 统计？
- **一个生产指标**：延迟、返回行数、事务时长、BUSY、WAL size、page/index size 中哪个最能证明问题？

## 14. 官方资料与源码阅读

- [fts5](https://www.sqlite.org/fts5.html)

> 仓库内容以随附 PDF 为主干，并在此基础上增加工程化推导、实验与官方文档入口。若目标应用使用旧版 SQLite，请优先按目标版本文档核对版本敏感行为。

