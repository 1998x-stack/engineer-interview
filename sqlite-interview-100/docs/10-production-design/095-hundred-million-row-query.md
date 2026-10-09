---
title: "题 095 1 亿行 SQLite 查询慢，第一步做什么？"
question_id: 95
chapter: 10
chapter_name: "生产故障与系统设计"
difficulty: "中"
frequency: "高"
tags: ["性能诊断"]
source_hint: "EQP/Planner"
sqlite_baseline: "3.53.4"
version_sensitive: false
---

# 题 095：1 亿行 SQLite 查询慢，第一步做什么？

> **章节**：生产故障与系统设计  
> **难度**：中 ｜ **频率**：高 ｜ **标签**：性能诊断  
> **版本基线**：SQLite 3.53.4（2026-07-24）

[← 返回章节目录](README.md) ｜ [总目录](../README.md)

## 1. 面试官到底在考什么

这道题不只考定义。高质量回答应该体现三层能力：

1. **语义层**：给出准确结论，明确成立前提。
2. **实现层**：把结论连接到 SQLite 的 Planner / VDBE / B-Tree / Pager / WAL / VFS 中相关层。
3. **工程层**：说明何时值得使用、何时会失效，以及如何用实验或诊断工具验证。

系统设计题要把前九章组合成可运行架构：**短事务、受控 writer、明确索引、可观测 query plan、正确 WAL/checkpoint、可回放 migration、稳定业务 ID、可靠备份与完整性检查**。如果设计中出现“拿着写事务等待网络”“100 个线程直接抢同一个 writer”“用 rowid 当跨设备 ID”，通常已经暴露了架构问题。

## 2. 30 秒标准回答

结论先 EXPLAIN QUERY PLAN，并测真实返回行数/选择性；再检查索引、排序、统计和 SQL shape，而不是凭行数决定换数据库。

## 3. 原理推导（Know-Why）

诊断顺序：SCAN/SEARCH？是否使用期望联合/覆盖索引？是否 USE TEMP B-TREE？WHERE 过滤后还剩多少行？LIMIT 能否早停？PRAGMA optimize/统计是否新鲜？表与索引是否过宽？很多“SQLite 太慢”最终是 O(N) query 被错误地执行了。

## 4. 深入分析

### 4.1 关键推导

亿级行数不是诊断结论。先用 EQP 确认访问路径，再量化返回比例、索引宽度、排序、临时 B-Tree 和数据分布。

### 4.2 关键推导

如果查询需要返回几十个百分点的整表数据，再漂亮的索引也无法消除必须读取的大量数据。

## 5. 代码 / 白板 / 可复现实验

### 建议动手实验

```sql
SELECT sqlite_version();
PRAGMA compile_options;
```
面试前在目标环境确认 SQLite 版本与构建选项，避免把“当前官方能力”误当成“目标应用一定启用”。

## 6. 边界条件与常见误区

- ⚠ 先加所有单列索引，导致写慢但查询仍不理想。

进一步检查：

- 是否把 MySQL/PostgreSQL 的语义直接迁移到了 SQLite？
- 是否区分了“SQL 看起来等价”和“Planner 能证明等价”？
- 是否把性能优化说成了绝对规则，而没有用 EQP/benchmark 验证？
- 是否忽略了连接级 PRAGMA、事务生命周期或构建选项？

## 7. 面试官继续追问

- → 什么指标说明应该架构升级到 server DB？

建议继续准备两类追问：

- **实现追问**：这个行为最终由哪个 SQLite 子系统负责？
- **生产追问**：如果线上出现相反现象，你如何用最小实验定位原因？

## 8. 工程实践 Checklist

- [ ] 短事务
- [ ] writer serialization/backpressure
- [ ] 稳定业务 ID
- [ ] 可观测 EQP/WAL/busy
- [ ] 迁移与备份可验证
- [ ] 网络 I/O 不占写事务

## 9. 相关题目

- [题 094 移动 App：大量读取、少量后台写，你会选择什么 journal mode？](../10-production-design/094-mobile-journal-mode.md)
- [题 096 如何为 WHERE user_id=? AND status=? ORDER BY created_at DESC LIMIT 20 设计索引？](../10-production-design/096-feed-index-design.md)
- [题 042 联合索引 (a,b,c) 能有效服务哪些条件？](../05-indexes/042-composite-index.md)
- [题 050 为什么“有索引”反而可能比 Full Scan 慢？](../05-indexes/050-index-vs-full-scan.md)
- [题 051 EXPLAIN 与 EXPLAIN QUERY PLAN 有什么区别？](../06-query-planner/051-explain-vs-eqp.md)
- [题 054 ANALYZE 为什么会改变执行计划？](../06-query-planner/054-analyze-statistics.md)

## 10. 面试评分 Rubric

> 这部分用于自测，也可以直接给面试官/出题人作为评分参考。

| 档位 | 表现 |
|---|---|
| **0 分：概念混淆** | 把 SQLite 与 client/server 数据库的机制混为一谈，或给出与题目相反的结论。 |
| **1 分：背到结论** | 能说出“结论先 EXPLAIN QUERY PLAN，并测真实返回行数/选择性；再检查索引、排序、统计和 SQL shape，而不是凭行数决定换数据库。”，但无法解释为什么、适用前提或如何验证。 |
| **2 分：机制正确** | 能把结论连接到本题所属的 SQLite 子系统，并指出至少一个边界条件。 |
| **3 分：工程可用** | 能给出最小实验/SQL/EQP/PRAGMA 证据，并讨论性能、正确性或运维权衡。 |
| **4 分：专家级** | 能进一步解释源码/文件结构/状态机层面的原因，识别版本敏感点，并对真实生产场景给出可观测、可回归的方案。 |

**建议口述结构**：先给结论（10 秒）→ 给机制（20～40 秒）→ 给反例/边界（20 秒）→ 如果面试官继续追问，再画白板或给实验。

## 11. 专业深化：把这题讲到实现层

### 11.1 本题在 SQLite 整体架构中的位置

```text
Workload
 ├─ read/write ratio
 ├─ transaction duration
 ├─ query shapes
 ├─ data growth
 └─ sync/backup/migration
       ↓
SQLite architecture decisions
       ↓
Observability + load test + failure test
```

系统设计题要求把前九章组合起来：事务边界、writer 调度、索引与计划、WAL/checkpoint、迁移、备份、稳定业务 ID 和可观测性必须形成闭环。单独说某个 PRAGMA 很难得到高分。

针对 **“1 亿行 SQLite 查询慢，第一步做什么？”**，还应补充这一条专业判断：

> 亿级行数不是诊断信息。先拿 top SQL、参数、EQP、结果行数和数据分布，再判断是缺索引、回表太多、临时排序、统计失真还是查询本身返回过多数据。

### 11.2 从“结论”推导到“为什么”

不要用数据库通识替代 SQLite 机制。建议按下面四层递进：

1. **SQL/语义层**：先明确本题结论，以及它是否依赖 journal mode、表类型、连接设置、索引结构或 SQLite 版本。
2. **Planner/执行层**：说明 SQLite 是否需要额外 seek、scan、sort、lock、type conversion、checkpoint 或 constraint check。
3. **B-Tree/Pager/WAL 层**：如果问题涉及性能或并发，继续说明最终会落到哪些 page、B-Tree、journal/WAL 或 VFS 操作。
4. **工程层**：给出可以监控的指标和可以复现的最小实验，而不是只说“通常更快/更安全”。

### 11.3 如何验证，而不是“凭经验回答”

用真实并发模型和真实数据分布压测；记录 p50/p95/p99、BUSY 次数、事务时长、WAL size/checkpoint、top SQL 的 EQP 和数据库增长曲线。

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

生产优化的目标不是最大 QPS，而是可预测延迟、数据正确性、可恢复性和可维护性。SQLite 能承载很大数据量，但架构是否适合主要由写竞争与部署拓扑决定。

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

- `src/wal.c / pager.c`：并发与持久化
- `src/where*.c`：查询计划
- `src/btree.c`：存储访问
- `src/backup.c`：在线备份
- `sqlite3.c amalgamation + release notes`：部署版本核验

> SQLite 官方发布常见的是 amalgamation `sqlite3.c`；上面的文件名指 SQLite 源码树中的逻辑模块，便于定位实现。源码行为仍应以目标版本为准。

- [统一源码阅读指南](../16-source-reading-guide.md)

### 13.2 对应章节实验

- [进入「生产压测与故障注入 Lab」](../labs/10-production-lab.md)

建议把实验结果（SQLite 版本、schema、数据规模、EQP、耗时）记录到自己的笔记中。面试时能说出“我实际验证过”，通常比单纯背术语更有说服力。

### 13.3 一分钟复习卡

- **一句话结论**：结论先 EXPLAIN QUERY PLAN，并测真实返回行数/选择性；再检查索引、排序、统计和 SQL shape，而不是凭行数决定换数据库。
- **必须解释的 Why**：它为什么由当前 SQLite 子系统的实现产生？
- **一个反例/边界**：什么条件变化后不能直接套用这条结论？
- **一个验证工具**：本题优先用哪一个——`EXPLAIN QUERY PLAN`、`typeof()`、`PRAGMA`、双连接并发实验、文件大小/page 统计？
- **一个生产指标**：延迟、返回行数、事务时长、BUSY、WAL size、page/index size 中哪个最能证明问题？

## 14. 官方资料与源码阅读

- [transaction](https://www.sqlite.org/lang_transaction.html)
- [wal](https://www.sqlite.org/wal.html)
- [queryplanner](https://www.sqlite.org/queryplanner.html)

> 仓库内容以随附 PDF 为主干，并在此基础上增加工程化推导、实验与官方文档入口。若目标应用使用旧版 SQLite，请优先按目标版本文档核对版本敏感行为。

