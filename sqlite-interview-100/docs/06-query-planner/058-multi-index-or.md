---
title: "题 058 OR 条件一定不能走索引吗？"
question_id: 58
chapter: 6
chapter_name: "Query Planner 与 SQL 优化"
difficulty: "中"
frequency: "高"
tags: ["OR Optimization"]
source_hint: "EQP/Optimizer"
sqlite_baseline: "3.53.4"
version_sensitive: false
---

# 题 058：OR 条件一定不能走索引吗？

> **章节**：Query Planner 与 SQL 优化  
> **难度**：中 ｜ **频率**：高 ｜ **标签**：OR Optimization  
> **版本基线**：SQLite 3.53.4（2026-07-24）

[← 返回章节目录](README.md) ｜ [总目录](../README.md)

## 1. 面试官到底在考什么

这道题不只考定义。高质量回答应该体现三层能力：

1. **语义层**：给出准确结论，明确成立前提。
2. **实现层**：把结论连接到 SQLite 的 Planner / VDBE / B-Tree / Pager / WAL / VFS 中相关层。
3. **工程层**：说明何时值得使用、何时会失效，以及如何用实验或诊断工具验证。

Query Planner 题的核心是 **cost-based choice**。Planner 不是“看见索引就用”，而是在候选访问路径、join order、排序、临时 B-Tree、统计信息之间估算成本。面试中应习惯用 `EXPLAIN QUERY PLAN` 先观察 plan shape，再用 `ANALYZE`/`PRAGMA optimize` 与真实数据分布解释为什么计划发生变化。

## 2. 30 秒标准回答

结论不是。若 OR 各分支都可索引，SQLite 可以使用 MULTI-INDEX OR 等策略分别检索后组合 rowids。

## 3. 原理推导（Know-Why）

这体现 planner 会把 OR 拆成多个可索引 term 的高级优化。若某个分支不可索引或选择性极差，可能退回其他方案。实际判断应看 EQP，而不是背“OR 导致全表扫描”这种过时规则。

## 4. 深入分析

### 4.1 关键推导

把题目中的 **OR 条件一定不能走索引吗** 放回本章的统一模型中分析，而不是孤立背结论。

### 4.2 关键推导

回答时至少覆盖：SQL/Schema 层可观察行为、SQLite 内部实现原因、以及生产环境中的性能或一致性代价。

### 4.3 关键推导

如果面试官改变前提（SQLite 版本、journal mode、rowid/WITHOUT ROWID、数据分布），应重新判断而不是坚持绝对答案。

## 5. 代码 / 白板 / 可复现实验

### PDF 中的白板/代码示例

```text
WHERE a=1 OR b=2
```

### 建议动手实验

```sql
EXPLAIN QUERY PLAN
SELECT ...;

PRAGMA optimize;
```
记录优化前后的 plan，而不是只比较一次 wall-clock；小样本缓存会让单次耗时很不稳定。

## 6. 边界条件与常见误区

- ⚠ 把 OR 一律改写 UNION 而不验证。

进一步检查：

- 是否把 MySQL/PostgreSQL 的语义直接迁移到了 SQLite？
- 是否区分了“SQL 看起来等价”和“Planner 能证明等价”？
- 是否把性能优化说成了绝对规则，而没有用 EQP/benchmark 验证？
- 是否忽略了连接级 PRAGMA、事务生命周期或构建选项？

## 7. 面试官继续追问

- → OR-to-IN rewrite 什么时候发生？

建议继续准备两类追问：

- **实现追问**：这个行为最终由哪个 SQLite 子系统负责？
- **生产追问**：如果线上出现相反现象，你如何用最小实验定位原因？

## 8. 工程实践 Checklist

- [ ] 先看 EQP 而不是猜
- [ ] 确保统计信息合理
- [ ] 区分 scan/search/temp b-tree
- [ ] 对参数和真实分布做 benchmark

## 9. 相关题目

- [题 057 SQLite 会严格按 FROM 中的书写顺序 Join 吗？](../06-query-planner/057-join-order.md)
- [题 059 什么是 Skip-Scan？](../06-query-planner/059-skip-scan.md)

## 10. 面试评分 Rubric

> 这部分用于自测，也可以直接给面试官/出题人作为评分参考。

| 档位 | 表现 |
|---|---|
| **0 分：概念混淆** | 把 SQLite 与 client/server 数据库的机制混为一谈，或给出与题目相反的结论。 |
| **1 分：背到结论** | 能说出“结论不是。若 OR 各分支都可索引，SQLite 可以使用 MULTI-INDEX OR 等策略分别检索后组合 rowids。”，但无法解释为什么、适用前提或如何验证。 |
| **2 分：机制正确** | 能把结论连接到本题所属的 SQLite 子系统，并指出至少一个边界条件。 |
| **3 分：工程可用** | 能给出最小实验/SQL/EQP/PRAGMA 证据，并讨论性能、正确性或运维权衡。 |
| **4 分：专家级** | 能进一步解释源码/文件结构/状态机层面的原因，识别版本敏感点，并对真实生产场景给出可观测、可回归的方案。 |

**建议口述结构**：先给结论（10 秒）→ 给机制（20～40 秒）→ 给反例/边界（20 秒）→ 如果面试官继续追问，再画白板或给实验。

## 11. 专业深化：把这题讲到实现层

### 11.1 本题在 SQLite 整体架构中的位置

```text
SQL predicates / joins / order
          ↓
Candidate loops + indexes
          ↓
Cardinality / cost estimates
          ↓
Join order + access paths
          ↓
VDBE program
```

SQLite 是 cost-based planner。真正专业的优化过程是“先拿计划和数据分布证据，再改 SQL/索引，再复测”，而不是根据经验强行指定某个索引。

针对 **“OR 条件一定不能走索引吗？”**，还应补充这一条专业判断：

> OR 优化可能对各分支分别使用索引后合并 rowid；如果某个 OR 分支完全不可索引，整体成本判断可能转向 full scan。

### 11.2 从“结论”推导到“为什么”

不要用数据库通识替代 SQLite 机制。建议按下面四层递进：

1. **SQL/语义层**：先明确本题结论，以及它是否依赖 journal mode、表类型、连接设置、索引结构或 SQLite 版本。
2. **Planner/执行层**：说明 SQLite 是否需要额外 seek、scan、sort、lock、type conversion、checkpoint 或 constraint check。
3. **B-Tree/Pager/WAL 层**：如果问题涉及性能或并发，继续说明最终会落到哪些 page、B-Tree、journal/WAL 或 VFS 操作。
4. **工程层**：给出可以监控的指标和可以复现的最小实验，而不是只说“通常更快/更安全”。

### 11.3 如何验证，而不是“凭经验回答”

同时使用 `.eqp on`、`EXPLAIN QUERY PLAN`、必要时 `EXPLAIN`；对统计相关问题检查 `sqlite_stat1`（及构建支持时的 stat4），并用 `PRAGMA optimize`/`ANALYZE` 后重新比较。

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

Planner 选择的是估算成本最小计划，不是“看起来最聪明”的计划。统计信息过时、低质量索引、数据分布偏斜或 correlated subquery 都可能使估算与现实偏离。

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

- `src/where.c / wherecode.c / whereexpr.c`：WHERE loop 与代码生成
- `src/select.c`：SELECT、子查询与 join 处理
- `src/analyze.c`：ANALYZE/statistics
- `src/vdbe.c`：最终 opcode 执行
- `src/expr.c`：表达式分析

> SQLite 官方发布常见的是 amalgamation `sqlite3.c`；上面的文件名指 SQLite 源码树中的逻辑模块，便于定位实现。源码行为仍应以目标版本为准。

- [统一源码阅读指南](../16-source-reading-guide.md)

### 13.2 对应章节实验

- [进入「Query Planner Lab」](../labs/06-planner-lab.md)

建议把实验结果（SQLite 版本、schema、数据规模、EQP、耗时）记录到自己的笔记中。面试时能说出“我实际验证过”，通常比单纯背术语更有说服力。

### 13.3 一分钟复习卡

- **一句话结论**：结论不是。若 OR 各分支都可索引，SQLite 可以使用 MULTI-INDEX OR 等策略分别检索后组合 rowids。
- **必须解释的 Why**：它为什么由当前 SQLite 子系统的实现产生？
- **一个反例/边界**：什么条件变化后不能直接套用这条结论？
- **一个验证工具**：本题优先用哪一个——`EXPLAIN QUERY PLAN`、`typeof()`、`PRAGMA`、双连接并发实验、文件大小/page 统计？
- **一个生产指标**：延迟、返回行数、事务时长、BUSY、WAL size、page/index size 中哪个最能证明问题？

## 14. 官方资料与源码阅读

- [eqp](https://www.sqlite.org/eqp.html)
- [optoverview](https://www.sqlite.org/optoverview.html)
- [queryplanner](https://www.sqlite.org/queryplanner.html)

> 仓库内容以随附 PDF 为主干，并在此基础上增加工程化推导、实验与官方文档入口。若目标应用使用旧版 SQLite，请优先按目标版本文档核对版本敏感行为。

