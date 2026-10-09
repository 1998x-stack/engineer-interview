---
title: "题 048 为什么 INDEX ON (x+y)，查询 WHERE y+x=10 可能不用索引？"
question_id: 48
chapter: 5
chapter_name: "索引设计"
difficulty: "中"
frequency: "高"
tags: ["Expression Index"]
source_hint: "Expression index"
sqlite_baseline: "3.53.4"
version_sensitive: false
---

# 题 048：为什么 INDEX ON (x+y)，查询 WHERE y+x=10 可能不用索引？

> **章节**：索引设计  
> **难度**：中 ｜ **频率**：高 ｜ **标签**：Expression Index  
> **版本基线**：SQLite 3.53.4（2026-07-24）

[← 返回章节目录](README.md) ｜ [总目录](../README.md)

## 1. 面试官到底在考什么

这道题不只考定义。高质量回答应该体现三层能力：

1. **语义层**：给出准确结论，明确成立前提。
2. **实现层**：把结论连接到 SQLite 的 Planner / VDBE / B-Tree / Pager / WAL / VFS 中相关层。
3. **工程层**：说明何时值得使用、何时会失效，以及如何用实验或诊断工具验证。

索引题不要停在“建索引”。要从 **B-Tree 的字典序** 推导：哪些谓词能形成连续搜索区间、排序是否天然满足、是否需要回表、索引宽度对缓存与写放大的代价。联合索引、覆盖索引、partial index、expression index 都是在“缩小搜索空间”和“降低额外 I/O”这两个目标上做不同权衡。

## 2. 30 秒标准回答

结论因为 SQLite planner 不做一般代数等价推理，表达式通常要与 CREATE INDEX 中写法一致（允许少量语法差异）。

## 3. 原理推导（Know-Why）

这是非常典型的“数学等价 != planner 可匹配”。工程上应该把常用表达式标准化到同一写法，或者用 generated column 统一抽象，避免 ORM 随机改写表达式顺序。

## 4. 深入分析

### 4.1 关键推导

Expression index 的匹配偏语法结构而不是代数定理证明；`x+y` 与 `y+x` 虽数学等价，不代表 planner 会重写成同一表达式。

### 4.2 关键推导

工程上应统一表达式写法，或抽象为 generated column，避免 ORM/代码风格变化破坏索引命中。

## 5. 代码 / 白板 / 可复现实验

### PDF 中的白板/代码示例

```sql
CREATE INDEX idx_xy ON t(x+y);
-- 更稳：WHERE x+y=10
-- 而不是：WHERE y+x=10
```

### 建议动手实验

```sql
EXPLAIN QUERY PLAN
SELECT * FROM t WHERE a=? AND b=? ORDER BY c LIMIT 20;

PRAGMA index_list('t');
PRAGMA index_xinfo('your_index');
```
先用 EQP 证明索引是否命中，再讨论“理论上应该”。

## 6. 边界条件与常见误区

- ⚠ 认为优化器会做交换律证明。

进一步检查：

- 是否把 MySQL/PostgreSQL 的语义直接迁移到了 SQLite？
- 是否区分了“SQL 看起来等价”和“Planner 能证明等价”？
- 是否把性能优化说成了绝对规则，而没有用 EQP/benchmark 验证？
- 是否忽略了连接级 PRAGMA、事务生命周期或构建选项？

## 7. 面试官继续追问

- → 空白、括号等 minor syntactic difference 是否允许？

建议继续准备两类追问：

- **实现追问**：这个行为最终由哪个 SQLite 子系统负责？
- **生产追问**：如果线上出现相反现象，你如何用最小实验定位原因？

## 8. 工程实践 Checklist

- [ ] 先列查询谓词和 ORDER BY
- [ ] 检查选择性与结果比例
- [ ] 用 EQP 验证
- [ ] 计算索引写放大和覆盖收益

## 9. 相关题目

- [题 047 什么是 Expression Index？](../05-indexes/047-expression-index.md)
- [题 049 为什么 Expression Index 只能使用 deterministic function？](../05-indexes/049-deterministic-functions.md)
- [题 088 Generated Column 和 Expression Index 怎么选？](../09-advanced-features/088-generated-vs-expression-index.md)

## 10. 面试评分 Rubric

> 这部分用于自测，也可以直接给面试官/出题人作为评分参考。

| 档位 | 表现 |
|---|---|
| **0 分：概念混淆** | 把 SQLite 与 client/server 数据库的机制混为一谈，或给出与题目相反的结论。 |
| **1 分：背到结论** | 能说出“结论因为 SQLite planner 不做一般代数等价推理，表达式通常要与 CREATE INDEX 中写法一致（允许少量语法差异）。”，但无法解释为什么、适用前提或如何验证。 |
| **2 分：机制正确** | 能把结论连接到本题所属的 SQLite 子系统，并指出至少一个边界条件。 |
| **3 分：工程可用** | 能给出最小实验/SQL/EQP/PRAGMA 证据，并讨论性能、正确性或运维权衡。 |
| **4 分：专家级** | 能进一步解释源码/文件结构/状态机层面的原因，识别版本敏感点，并对真实生产场景给出可观测、可回归的方案。 |

**建议口述结构**：先给结论（10 秒）→ 给机制（20～40 秒）→ 给反例/边界（20 秒）→ 如果面试官继续追问，再画白板或给实验。

## 11. 专业深化：把这题讲到实现层

### 11.1 本题在 SQLite 整体架构中的位置

```text
Predicate + ORDER BY + projection
          ↓
Can one B-Tree provide a narrow contiguous range?
          ↓
Can it provide required order?
          ↓
Can it cover output columns and avoid table lookup?
```

索引题的核心不是背“最左前缀”，而是从 B-Tree 字典序推导连续搜索区间，并把过滤、排序、LIMIT、回表次数和写放大放在同一成本模型里。

针对 **“为什么 INDEX ON (x+y)，查询 WHERE y+x=10 可能不用索引？”**，还应补充这一条专业判断：

> SQLite 对 expression index 的匹配以语法结构为主，不做一般代数定理证明。`x+y` 与 `y+x` 数学等价，但 planner 不因此自动替换；这是“优化器可证明性”和“数学等价性”不同的典型案例。

### 11.2 从“结论”推导到“为什么”

不要用数据库通识替代 SQLite 机制。建议按下面四层递进：

1. **SQL/语义层**：先明确本题结论，以及它是否依赖 journal mode、表类型、连接设置、索引结构或 SQLite 版本。
2. **Planner/执行层**：说明 SQLite 是否需要额外 seek、scan、sort、lock、type conversion、checkpoint 或 constraint check。
3. **B-Tree/Pager/WAL 层**：如果问题涉及性能或并发，继续说明最终会落到哪些 page、B-Tree、journal/WAL 或 VFS 操作。
4. **工程层**：给出可以监控的指标和可以复现的最小实验，而不是只说“通常更快/更安全”。

### 11.3 如何验证，而不是“凭经验回答”

每个索引结论都用 `EXPLAIN QUERY PLAN` 验证，同时对比建索引前后页数/文件大小、写入速度和查询延迟；必要时用 `PRAGMA index_list`、`index_xinfo` 确认真实结构。

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

更宽的联合/覆盖索引能减少读取和排序，但会增加存储、cache footprint、INSERT/UPDATE/DELETE 成本。Partial/Expression Index 则用更强约束换更小索引或更直接的表达式访问路径。

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

- `src/btree.c`：索引 B-Tree 存取
- `src/where.c / where*.c`：索引候选与成本估算
- `src/build.c`：CREATE INDEX
- `src/expr.c`：表达式匹配与确定性规则
- `src/analyze.c`：统计信息

> SQLite 官方发布常见的是 amalgamation `sqlite3.c`；上面的文件名指 SQLite 源码树中的逻辑模块，便于定位实现。源码行为仍应以目标版本为准。

- [统一源码阅读指南](../16-source-reading-guide.md)

### 13.2 对应章节实验

- [进入「索引设计 Lab」](../labs/05-index-lab.md)

建议把实验结果（SQLite 版本、schema、数据规模、EQP、耗时）记录到自己的笔记中。面试时能说出“我实际验证过”，通常比单纯背术语更有说服力。

### 13.3 一分钟复习卡

- **一句话结论**：结论因为 SQLite planner 不做一般代数等价推理，表达式通常要与 CREATE INDEX 中写法一致（允许少量语法差异）。
- **必须解释的 Why**：它为什么由当前 SQLite 子系统的实现产生？
- **一个反例/边界**：什么条件变化后不能直接套用这条结论？
- **一个验证工具**：本题优先用哪一个——`EXPLAIN QUERY PLAN`、`typeof()`、`PRAGMA`、双连接并发实验、文件大小/page 统计？
- **一个生产指标**：延迟、返回行数、事务时长、BUSY、WAL size、page/index size 中哪个最能证明问题？

## 14. 官方资料与源码阅读

- [expridx](https://www.sqlite.org/expridx.html)
- [optoverview](https://www.sqlite.org/optoverview.html)

> 仓库内容以随附 PDF 为主干，并在此基础上增加工程化推导、实验与官方文档入口。若目标应用使用旧版 SQLite，请优先按目标版本文档核对版本敏感行为。

