---
title: "题 027 Read transaction 升级为 Write transaction 为什么会失败？"
question_id: 27
chapter: 3
chapter_name: "事务、隔离与并发"
difficulty: "中"
frequency: "高"
tags: ["Snapshot", "Busy"]
source_hint: "Transaction"
sqlite_baseline: "3.53.4"
version_sensitive: false
---

# 题 027：Read transaction 升级为 Write transaction 为什么会失败？

> **章节**：事务、隔离与并发  
> **难度**：中 ｜ **频率**：高 ｜ **标签**：Snapshot / Busy  
> **版本基线**：SQLite 3.53.4（2026-07-24）

[← 返回章节目录](README.md) ｜ [总目录](../README.md)

## 1. 面试官到底在考什么

这道题不只考定义。高质量回答应该体现三层能力：

1. **语义层**：给出准确结论，明确成立前提。
2. **实现层**：把结论连接到 SQLite 的 Planner / VDBE / B-Tree / Pager / WAL / VFS 中相关层。
3. **工程层**：说明何时值得使用、何时会失效，以及如何用实验或诊断工具验证。

事务题应画出连接级状态机：**无事务 → read transaction →（可能升级）write transaction → COMMIT/ROLLBACK**。SQLite 可以有多个 reader，但同一数据库同时只有一个 writer。`BEGIN DEFERRED/IMMEDIATE/EXCLUSIVE` 的差别，本质是“什么时候争取写事务以及在特定 journal mode 下对 reader 的影响”。遇到 `SQLITE_BUSY` 时要分析持锁者和事务生命周期，而不是只调大 timeout。

## 2. 30 秒标准回答

结论因为 DEFERRED 事务先持有一个历史 snapshot；如果其他连接已修改/正在修改数据库，升级写事务可能无法成立并返回 SQLITE_BUSY。

## 3. 原理推导（Know-Why）

尤其在 WAL 中，读事务看到的 snapshot 不会随着其他连接 commit 自动前移。某些场景会出现 SQLITE_BUSY_SNAPSHOT：当前连接若写入，会基于已经过时的历史视图分叉。若业务语义要求“读到的状态就是随后修改的依据”，从 BEGIN IMMEDIATE 开始通常更可预测。

## 4. 深入分析

### 4.1 关键推导

升级失败往往不是“锁功能坏了”，而是当前 read snapshot 与数据库后来发生的写入使升级不再安全/可立即获取写事务。

### 4.2 关键推导

错误处理应区分 `SQLITE_BUSY`、扩展错误码以及是否可以从事务边界重新执行。

## 5. 代码 / 白板 / 可复现实验

### 建议动手实验

```sql
-- 打开两个 sqlite3 终端连接同一个 db
-- Connection A
BEGIN;
SELECT * FROM demo WHERE id=1;

-- Connection B
BEGIN IMMEDIATE;
UPDATE demo SET value=value+1 WHERE id=1;
COMMIT;

-- 回到 A，尝试写并观察返回码/行为
UPDATE demo SET value=value+1 WHERE id=1;
```
用两个连接而不是单连接脚本，才能真实观察事务竞争。

## 6. 边界条件与常见误区

- ⚠ 认为 busy_timeout 一定能把 snapshot 升级问题等到成功。

进一步检查：

- 是否把 MySQL/PostgreSQL 的语义直接迁移到了 SQLite？
- 是否区分了“SQL 看起来等价”和“Planner 能证明等价”？
- 是否把性能优化说成了绝对规则，而没有用 EQP/benchmark 验证？
- 是否忽略了连接级 PRAGMA、事务生命周期或构建选项？

## 7. 面试官继续追问

- → SQLITE_BUSY 与 SQLITE_BUSY_SNAPSHOT 区别？

建议继续准备两类追问：

- **实现追问**：这个行为最终由哪个 SQLite 子系统负责？
- **生产追问**：如果线上出现相反现象，你如何用最小实验定位原因？

## 8. 工程实践 Checklist

- [ ] 记录事务开始与结束
- [ ] 明确 read/write transaction 状态
- [ ] 把网络/磁盘外部 I/O 移出写事务
- [ ] 对 BUSY 设计有界重试

## 9. 相关题目

- [题 026 SQLite 同一数据库能同时有两个 Writer 吗？](../03-transactions-concurrency/026-single-writer.md)
- [题 028 busy_timeout 是什么？能解决所有锁问题吗？](../03-transactions-concurrency/028-busy-timeout.md)
- [题 022 BEGIN DEFERRED 是什么？](../03-transactions-concurrency/022-begin-deferred.md)
- [题 023 BEGIN IMMEDIATE 与 DEFERRED 有何区别？](../03-transactions-concurrency/023-begin-immediate.md)
- [题 091 线上持续出现 database is locked，如何系统排查？](../10-production-design/091-database-is-locked.md)

## 10. 面试评分 Rubric

> 这部分用于自测，也可以直接给面试官/出题人作为评分参考。

| 档位 | 表现 |
|---|---|
| **0 分：概念混淆** | 把 SQLite 与 client/server 数据库的机制混为一谈，或给出与题目相反的结论。 |
| **1 分：背到结论** | 能说出“结论因为 DEFERRED 事务先持有一个历史 snapshot；如果其他连接已修改/正在修改数据库，升级写事务可能无法成立并返回 SQLITE_BUSY。”，但无法解释为什么、适用前提或如何验证。 |
| **2 分：机制正确** | 能把结论连接到本题所属的 SQLite 子系统，并指出至少一个边界条件。 |
| **3 分：工程可用** | 能给出最小实验/SQL/EQP/PRAGMA 证据，并讨论性能、正确性或运维权衡。 |
| **4 分：专家级** | 能进一步解释源码/文件结构/状态机层面的原因，识别版本敏感点，并对真实生产场景给出可观测、可回归的方案。 |

**建议口述结构**：先给结论（10 秒）→ 给机制（20～40 秒）→ 给反例/边界（20 秒）→ 如果面试官继续追问，再画白板或给实验。

## 11. 专业深化：把这题讲到实现层

### 11.1 本题在 SQLite 整体架构中的位置

```text
No transaction
   ↓ BEGIN / implicit txn
Read transaction / snapshot
   ↓ (if write is needed)
Acquire writer capability
   ↓
Write transaction
   ↓
COMMIT / ROLLBACK
```

高质量回答要以“connection 级事务状态机”解释并发，而不是把锁理解成某一行或某一 SQL 的属性。SQLite 允许多个 reader，但同一 database 的写入最终被串行化；WAL 改善 reader/writer 并发，不会变成多 writer MVCC 数据库。

针对 **“Read transaction 升级为 Write transaction 为什么会失败？”**，还应补充这一条专业判断：

> WAL 下典型升级失败可表现为 `SQLITE_BUSY_SNAPSHOT`：旧 read snapshot 不能直接分叉成新的历史并写回，否则会破坏串行化。解决思路是重启事务或从一开始用 IMMEDIATE。

### 11.2 从“结论”推导到“为什么”

不要用数据库通识替代 SQLite 机制。建议按下面四层递进：

1. **SQL/语义层**：先明确本题结论，以及它是否依赖 journal mode、表类型、连接设置、索引结构或 SQLite 版本。
2. **Planner/执行层**：说明 SQLite 是否需要额外 seek、scan、sort、lock、type conversion、checkpoint 或 constraint check。
3. **B-Tree/Pager/WAL 层**：如果问题涉及性能或并发，继续说明最终会落到哪些 page、B-Tree、journal/WAL 或 VFS 操作。
4. **工程层**：给出可以监控的指标和可以复现的最小实验，而不是只说“通常更快/更安全”。

### 11.3 如何验证，而不是“凭经验回答”

至少用两个独立 connection 做实验，并记录每个连接的 `BEGIN` 类型、第一条读/写语句、错误码和提交时刻。锁问题不能用单连接脚本真实复现。

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

并发优化的第一原则是缩短写事务，把网络请求、文件 I/O、模型推理等外部等待移出事务；第二原则才是 busy handler、WAL、队列和批处理。

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

- `src/pager.c`：事务和 journal 协调
- `src/btree.c`：B-Tree transaction 接口
- `src/wal.c`：WAL writer/read-mark/checkpoint
- `src/main.c`：busy handler/connection API
- `src/vdbe.c`：statement 生命周期与 implicit transaction

> SQLite 官方发布常见的是 amalgamation `sqlite3.c`；上面的文件名指 SQLite 源码树中的逻辑模块，便于定位实现。源码行为仍应以目标版本为准。

- [统一源码阅读指南](../16-source-reading-guide.md)

### 13.2 对应章节实验

- [进入「事务与并发双连接 Lab」](../labs/03-transactions-lab.md)

建议把实验结果（SQLite 版本、schema、数据规模、EQP、耗时）记录到自己的笔记中。面试时能说出“我实际验证过”，通常比单纯背术语更有说服力。

### 13.3 一分钟复习卡

- **一句话结论**：结论因为 DEFERRED 事务先持有一个历史 snapshot；如果其他连接已修改/正在修改数据库，升级写事务可能无法成立并返回 SQLITE_BUSY。
- **必须解释的 Why**：它为什么由当前 SQLite 子系统的实现产生？
- **一个反例/边界**：什么条件变化后不能直接套用这条结论？
- **一个验证工具**：本题优先用哪一个——`EXPLAIN QUERY PLAN`、`typeof()`、`PRAGMA`、双连接并发实验、文件大小/page 统计？
- **一个生产指标**：延迟、返回行数、事务时长、BUSY、WAL size、page/index size 中哪个最能证明问题？

## 14. 官方资料与源码阅读

- [transaction](https://www.sqlite.org/lang_transaction.html)
- [isolation](https://www.sqlite.org/isolation.html)

> 仓库内容以随附 PDF 为主干，并在此基础上增加工程化推导、实验与官方文档入口。若目标应用使用旧版 SQLite，请优先按目标版本文档核对版本敏感行为。

