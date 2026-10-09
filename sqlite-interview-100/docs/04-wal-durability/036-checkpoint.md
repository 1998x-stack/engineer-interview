---
title: "题 036 Checkpoint 是什么？"
question_id: 36
chapter: 4
chapter_name: "Journal、WAL 与持久性"
difficulty: "中"
frequency: "高"
tags: ["WAL", "Checkpoint"]
source_hint: "WAL"
sqlite_baseline: "3.53.4"
version_sensitive: false
---

# 题 036：Checkpoint 是什么？

> **章节**：Journal、WAL 与持久性  
> **难度**：中 ｜ **频率**：高 ｜ **标签**：WAL / Checkpoint  
> **版本基线**：SQLite 3.53.4（2026-07-24）

[← 返回章节目录](README.md) ｜ [总目录](../README.md)

## 1. 面试官到底在考什么

这道题不只考定义。高质量回答应该体现三层能力：

1. **语义层**：给出准确结论，明确成立前提。
2. **实现层**：把结论连接到 SQLite 的 Planner / VDBE / B-Tree / Pager / WAL / VFS 中相关层。
3. **工程层**：说明何时值得使用、何时会失效，以及如何用实验或诊断工具验证。

Journal/WAL 题的统一坐标是“**如何让页面修改同时满足原子性、崩溃恢复和并发读取**”。Rollback journal 保存 before-image；WAL 保存 after-image 并把 checkpoint 延后。WAL 提升的是 reader/writer 重叠能力，不会突破单 writer 约束。任何 WAL 性能问题最终都可以下钻到：WAL append、reader end mark、wal-index、checkpoint progress 与 fsync/synchronous 策略。

## 2. 30 秒标准回答

结论把 WAL 中已提交的有效 page frames 复制回主数据库。

## 3. 原理推导（Know-Why）

Checkpoint 可与 reader 部分并发，但不能越过仍被某个 reader snapshot 依赖的 WAL 点。完整 checkpoint 后，在没有连接仍引用旧 WAL 状态时，后续写事务可以 reset/reuse WAL。checkpoint 策略影响写延迟、WAL 大小与读性能。

## 4. 深入分析

### 4.1 关键推导

Checkpoint 不是 COMMIT。COMMIT 让事务逻辑上持久可见；checkpoint 是把 WAL 中已提交 page 搬回主数据库。

### 4.2 关键推导

分析 checkpoint 要问 mode、当前 reader end mark、WAL 大小、是否能 reset/truncate，以及谁承担 checkpoint 工作。

## 5. 代码 / 白板 / 可复现实验

### 建议动手实验

```sql
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;
PRAGMA wal_checkpoint(PASSIVE);
```
配合观察数据库目录中的 `-wal` / `-shm` 文件以及长 read transaction 对 checkpoint 的影响。

## 6. 边界条件与常见误区

- ⚠ 把 checkpoint 当 commit。

进一步检查：

- 是否把 MySQL/PostgreSQL 的语义直接迁移到了 SQLite？
- 是否区分了“SQL 看起来等价”和“Planner 能证明等价”？
- 是否把性能优化说成了绝对规则，而没有用 EQP/benchmark 验证？
- 是否忽略了连接级 PRAGMA、事务生命周期或构建选项？

## 7. 面试官继续追问

- → PASSIVE/FULL/RESTART/TRUNCATE checkpoint 模式差异？

建议继续准备两类追问：

- **实现追问**：这个行为最终由哪个 SQLite 子系统负责？
- **生产追问**：如果线上出现相反现象，你如何用最小实验定位原因？

## 8. 工程实践 Checklist

- [ ] 记录 journal_mode/synchronous
- [ ] 监控 WAL 大小和 checkpoint
- [ ] 及时结束 reader statement
- [ ] 不要手工删除活动 WAL/journal

## 9. 相关题目

- [题 035 为什么 WAL 不适合普通网络文件系统？](../04-wal-durability/035-wal-network-filesystem.md)
- [题 037 为什么长期 Reader 会导致 WAL 越来越大？](../04-wal-durability/037-checkpoint-starvation.md)
- [题 033 WAL 为什么允许 Reader 与 Writer 并发？](../04-wal-durability/033-wal-read-write-concurrency.md)
- [题 040 2026 年为什么 SQLite 3.53 系列值得关注？](../04-wal-durability/040-sqlite-3-53.md)

## 10. 面试评分 Rubric

> 这部分用于自测，也可以直接给面试官/出题人作为评分参考。

| 档位 | 表现 |
|---|---|
| **0 分：概念混淆** | 把 SQLite 与 client/server 数据库的机制混为一谈，或给出与题目相反的结论。 |
| **1 分：背到结论** | 能说出“结论把 WAL 中已提交的有效 page frames 复制回主数据库。”，但无法解释为什么、适用前提或如何验证。 |
| **2 分：机制正确** | 能把结论连接到本题所属的 SQLite 子系统，并指出至少一个边界条件。 |
| **3 分：工程可用** | 能给出最小实验/SQL/EQP/PRAGMA 证据，并讨论性能、正确性或运维权衡。 |
| **4 分：专家级** | 能进一步解释源码/文件结构/状态机层面的原因，识别版本敏感点，并对真实生产场景给出可观测、可回归的方案。 |

**建议口述结构**：先给结论（10 秒）→ 给机制（20～40 秒）→ 给反例/边界（20 秒）→ 如果面试官继续追问，再画白板或给实验。

## 11. 专业深化：把这题讲到实现层

### 11.1 本题在 SQLite 整体架构中的位置

```text
Rollback mode:  old page → journal → overwrite DB → commit
WAL mode:       new page → append WAL → commit → checkpoint → DB
```

这一章要同时回答三个问题：原子性如何恢复、reader 看到哪个版本、什么时候数据从 journal/WAL 回到主库。只会说“WAL 更快”远远不够，必须能解释 read mark、checkpoint、fsync/synchronous 与 crash recovery。

针对 **“Checkpoint 是什么？”**，还应补充这一条专业判断：

> Checkpoint 不是 COMMIT。COMMIT 只需要让事务在 WAL 中成为已提交；checkpoint 是后续把已提交 frame 回写主库。把二者混为一谈会错误解释延迟与 durability。

### 11.2 从“结论”推导到“为什么”

不要用数据库通识替代 SQLite 机制。建议按下面四层递进：

1. **SQL/语义层**：先明确本题结论，以及它是否依赖 journal mode、表类型、连接设置、索引结构或 SQLite 版本。
2. **Planner/执行层**：说明 SQLite 是否需要额外 seek、scan、sort、lock、type conversion、checkpoint 或 constraint check。
3. **B-Tree/Pager/WAL 层**：如果问题涉及性能或并发，继续说明最终会落到哪些 page、B-Tree、journal/WAL 或 VFS 操作。
4. **工程层**：给出可以监控的指标和可以复现的最小实验，而不是只说“通常更快/更安全”。

### 11.3 如何验证，而不是“凭经验回答”

观察 `db-wal`/`db-shm` 文件尺寸，执行 `PRAGMA wal_checkpoint(PASSIVE|FULL|TRUNCATE)`，并在长 reader 存在时重复写入，验证 checkpoint 为什么被 reader 边界限制。

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

WAL 通常更利于读写并发，但引入额外文件、checkpoint 运维、长 reader 风险与同机共享内存依赖。持久性设置则是在吞吐、延迟和断电数据保证之间取舍。

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

- `src/wal.c`：WAL frame、read-mark、checkpoint
- `src/pager.c`：rollback/WAL 模式统一事务接口
- `src/os_unix.c / os_win.c`：锁与同步调用
- `src/main.c`：PRAGMA/API 入口

> SQLite 官方发布常见的是 amalgamation `sqlite3.c`；上面的文件名指 SQLite 源码树中的逻辑模块，便于定位实现。源码行为仍应以目标版本为准。

- [统一源码阅读指南](../16-source-reading-guide.md)

### 13.2 对应章节实验

- [进入「WAL 与 Checkpoint Lab」](../labs/04-wal-checkpoint-lab.md)

建议把实验结果（SQLite 版本、schema、数据规模、EQP、耗时）记录到自己的笔记中。面试时能说出“我实际验证过”，通常比单纯背术语更有说服力。

### 13.3 一分钟复习卡

- **一句话结论**：结论把 WAL 中已提交的有效 page frames 复制回主数据库。
- **必须解释的 Why**：它为什么由当前 SQLite 子系统的实现产生？
- **一个反例/边界**：什么条件变化后不能直接套用这条结论？
- **一个验证工具**：本题优先用哪一个——`EXPLAIN QUERY PLAN`、`typeof()`、`PRAGMA`、双连接并发实验、文件大小/page 统计？
- **一个生产指标**：延迟、返回行数、事务时长、BUSY、WAL size、page/index size 中哪个最能证明问题？

## 14. 官方资料与源码阅读

- [wal](https://www.sqlite.org/wal.html)
- [atomic](https://www.sqlite.org/atomiccommit.html)
- [locking](https://www.sqlite.org/lockingv3.html)

> 仓库内容以随附 PDF 为主干，并在此基础上增加工程化推导、实验与官方文档入口。若目标应用使用旧版 SQLite，请优先按目标版本文档核对版本敏感行为。

