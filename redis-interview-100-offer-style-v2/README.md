# Redis Interview 100 · Offer Style · 2026

> **100 道 Redis 高频面试真题的工程化 GitHub 版本**  
> 版本基线：**Redis Open Source 8.10.1（2026-08）**  
> 适用：后端研发 / Java / Go / C++ / 基础架构 / 分布式系统 / SRE

本仓库以《Redis 面试宝典 · 100 道高频真题》PDF 为母版，将 **100 道题全部拆成独立 Markdown**，并在不改变 PDF 主线的前提下进一步扩展：复杂度、内部实现、故障边界、追问树、可观测验证、版本差异、系统设计和生产 Gotchas。

> 本项目借鉴“面试题驱动、层层追问、总结方法”的学习方式，但不复制《剑指 Offer》的受版权保护原文、题目或版式。

## 为什么这个仓库不是“Redis 八股文”

每题统一使用下面的回答路径：

```text
30–60 秒结论
    ↓
关键机制 / 数据结构 / 状态机
    ↓
复杂度与资源成本
    ↓
故障 / 竞态 / 一致性边界
    ↓
可观测指标和验证命令
    ↓
生产方案与取舍
```

目标不是记住 100 个孤立答案，而是形成四条可以迁移的能力主线：

- 数据结构与内存；
- 缓存与一致性；
- 持久化、高可用与水平扩展；
- 性能排障与系统设计。

## v2 深度增强版

100 道题现已逐题增加 **专业深挖补充（v2）**：核心机制再推导、复杂度/容量模型、生产案例、失败模式、源码阅读路线、追问标准应答和复习检查表。目标是让每个 Markdown 都能单独作为一次 5–15 分钟的高级面试复习单元。

编辑规范见 [`docs/editorial-standard.md`](docs/editorial-standard.md)。


## 目录

| 章 | 主题 | 题号 | 重点 |
|---|---|---|---|
| 01 | [数据结构与数据建模](chapters/01-data-modeling/README.md) | Q001–Q010 | 从“会用命令”升级到“按访问模式建模”。选择数据结构时同时考虑操作复杂度、内存、Big Key 与 Cluster 约束。 |
| 02 | [底层编码与内存机制](chapters/02-internals-memory/README.md) | Q011–Q020 | 理解 SDS、listpack、quicklist、哈希表、跳表以及编码切换，建立 Big Key / Hot Key / 碎片治理能力。 |
| 03 | [TTL、缓存模式与淘汰](chapters/03-cache-ttl-eviction/README.md) | Q021–Q030 | 把缓存穿透、击穿、雪崩、一致性与 LRU/LFU 串成完整缓存工程知识链。 |
| 04 | [持久化：RDB、AOF 与恢复](chapters/04-persistence/README.md) | Q031–Q040 | 围绕 RPO/RTO 理解 fork、COW、AOF rewrite、Multi-Part AOF 和 Redis 8.10 BACKUP。 |
| 05 | [复制与 Sentinel 高可用](chapters/05-replication-sentinel/README.md) | Q041–Q050 | 掌握异步复制的写安全边界、PSYNC/backlog，以及 Sentinel 的主观/客观下线和选举语义。 |
| 06 | [Redis Cluster 与水平扩展](chapters/06-cluster/README.md) | Q051–Q060 | 从 16,384 slots、MOVED/ASK、Hash Tag 到 Resharding 和故障转移，能解释 Cluster 的一致性边界。 |
| 07 | [事务、Lua、Functions 与分布式锁](chapters/07-transactions-locks/README.md) | Q061–Q070 | 理解 Redis 的原子性到底保证什么；把 WATCH、脚本和锁放进真实的并发/租约问题中。 |
| 08 | [Pub/Sub、Streams 与消息处理](chapters/08-messaging-streams/README.md) | Q071–Q080 | 从 fire-and-forget 到 Consumer Group、PEL、XAUTOCLAIM/XNACK，建立至少一次消费与幂等意识。 |
| 09 | [性能诊断、运维与安全](chapters/09-operations-performance/README.md) | Q081–Q090 | 把 SLOWLOG、LATENCY、CPU、内存、fork、Swap、ACL/TLS 和可观测性组成排障路径。 |
| 10 | [Redis 8.x 与系统设计压轴题](chapters/10-redis8-system-design/README.md) | Q091–Q100 | 覆盖 Redis 8 新数据类型与命令，并以秒杀、排行榜、限流和生产架构完成综合设计。 |

## 快速入口

- [完整 100 题总索引](SUMMARY.md)
- [主题交叉索引](docs/topic-index.md)
- [PDF 母版](docs/pdf/Redis_Interview_100_Offer_Style_2026.pdf)
- [如何使用本书 / 面试答题法](docs/book-preface.md)
- [附录 A：30 个高频追问速查](docs/appendix/a-followups.md)
- [附录 B：生产故障排查 Runbook](docs/appendix/b-production-runbook.md)
- [附录 C：7 / 14 / 30 天复习计划](docs/appendix/c-study-plan.md)
- [附录 D：Redis 版本差异速览](docs/appendix/d-version-matrix.md)
- [官方参考资料](docs/references.md)
- [PDF → Markdown 内容映射](docs/source-map.md)

## 一题一个 Markdown 的结构

```text
chapters/
├── 01-data-modeling/
│   ├── README.md
│   ├── q001.md
│   ├── ...
│   └── q010.md
├── 02-internals-memory/
│   └── ...
└── 10-redis8-system-design/
    ├── q091.md
    └── q100.md
```

每个题目文件都包含：

- YAML front matter：题号、难度、章节、PDF 页码、版本基线；
- PDF 原始标准回答；
- PDF 原始原理拆解、追问、Gotchas、工程落地；
- 更深入的成本/复杂度模型；
- 可观测指标、故障注入实验与 Mermaid 白板图；
- 生产判断框架；
- 额外追问树；
- 可操作验证命令；
- Redis 8.x 版本注意；
- 60/80/90/100 分回答评分尺；
- 关联题目和官方文档。

## 推荐学习方式

### 第一轮：能答

每天 10 题，只要求 60 秒内说清“是什么 + 为什么”。

### 第二轮：能追问

关闭标准答案，只看题目，连续回答 2–4 层追问，并主动说出一个失效边界。

### 第三轮：能设计

从以下条件任意改一个重新推导：

- 数据量 ×100；
- p99 从 10 ms 收紧到 2 ms；
- 从单机改为 Cluster；
- 从纯缓存变成重要业务状态；
- 允许数据陈旧 5 秒 / 不允许丢已确认写；
- AZ 故障或网络分区 30 秒。

如果条件改变后仍只背原答案，说明知识还没有形成系统。

## 版本意识

仓库以 Redis Open Source **8.10.1（2026-08）** 为基线。经典语义与当前版本增量会明确区分，例如：

- Redis 7：Multi-Part AOF；
- Redis 8：Search / JSON / Time Series / probabilistic structures 等整合进主发行版；
- Redis 8.8：Array、INCREX、XNACK；
- Redis 8.10：Compact Hash、HIMPORT、BACKUP、LMOVEM/BLMOVEM 等。

## 随机模拟面试

```bash
# 随机 10 题
python scripts/random_quiz.py

# 只抽 Cluster 章节
python scripts/random_quiz.py --chapter 6 --count 5

# 只抽高级题
python scripts/random_quiz.py --difficulty 高级 --count 8
```

## 仓库质量保证

运行：

```bash
python scripts/validate_repo.py
```

校验内容包括：100 个题目文件是否齐全、front matter 题号是否匹配、章节链接与 PDF 是否存在、README/SUMMARY 是否覆盖全部题目。

## 内容来源与边界

- **母版内容**：仓库中的 PDF；每题的“PDF 原始”章节按母版语义保留。
- **扩展内容**：基于 Redis 官方当前文档与工程分析补充，重点增强复杂度、失效边界和生产验证。
- 遇到版本/命令语义/复制与 Cluster 写安全问题，以 Redis 官方文档和 Cluster specification 为优先依据。

## License

本仓库暂不替作者指定再分发许可证。公开发布前请在 `LICENSE.md` 中选择适合文档项目的许可证（例如 CC BY 4.0）并确认你的分发意图。
