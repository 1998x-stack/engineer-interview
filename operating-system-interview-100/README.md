# Operating System Interview 100

> 操作系统面试 100 道高频真题 · 深度解析 · Linux 工程化扩展

本仓库由《操作系统面试宝典：100 道高频真题·深度解析》重构而来。**每一道题一个 Markdown**，并在原 PDF 的核心内容上增加机制连接、答题层级、追问树、Linux 实验、工程排障视角和官方参考资料。

## V2 Deep-Dive：每题已升级为内核级技术文章

当前 100 道题全部增加了统一但**题目特定**的深度层：

- 机制级状态推演，而不是只给定义；
- CPU / Cache / TLB / 调度 / I/O 成本模型；
- Linux 内核对象、系统调用和源码阅读入口；
- 边界条件、反例、错误路径；
- 高级追问树与生产验证思路；
- 可复现实验与观察指标；
- 5 级面试评分 Rubric；
- 官方文档优先的进一步阅读。

同时新增 [`guides/kernel-source-reading-map.md`](guides/kernel-source-reading-map.md)，用于把 100 题映射到 Linux Kernel 源码子系统。

## 为什么不是“100 道八股”

目标不是把 100 个定义背下来，而是构建一张可以连续追问的因果图：

```text
Process / Thread → Scheduler → Synchronization → Deadlock
          │                         │
          └──────────────→ IPC / Futex / Atomics

Virtual Address → TLB → Page Table → Page Fault → Reclaim / Swap / OOM

open() → VFS → dentry/inode → Page Cache → Filesystem → Block I/O

read/write → non-blocking → epoll → io_uring → DMA / device
```

## 仓库内容

| 章 | 模块 | 题号 | 数量 | 学习目标 |
|---:|---|---|---:|---|
| 1 | [操作系统与内核基础](questions/01-kernel-basics/README.md) | Q01-Q10 | 10 | 从抽象、保护边界、系统调用到启动与中断，建立 OS 的总框架。 |
| 2 | [进程、线程与 IPC](questions/02-process-thread-ipc/README.md) | Q11-Q22 | 12 | 理解执行实体、资源共享、fork/COW、生命周期与进程间通信。 |
| 3 | [CPU 调度](questions/03-cpu-scheduling/README.md) | Q23-Q32 | 10 | 从经典调度算法走向 locality、实时调度与现代 Linux EEVDF。 |
| 4 | [并发与同步](questions/04-concurrency-sync/README.md) | Q33-Q47 | 15 | 从 race condition 到 mutex/semaphore、memory ordering、lock-free 与 futex。 |
| 5 | [死锁](questions/05-deadlock/README.md) | Q48-Q55 | 8 | 建立 progress/fairness 模型，掌握死锁预防、避免、检测与工程诊断。 |
| 6 | [内存与虚拟内存](questions/06-memory-virtual-memory/README.md) | Q56-Q72 | 17 | 打通 VA→TLB→Page Table→Page Fault→COW/Reclaim/Swap/OOM。 |
| 7 | [文件系统与存储](questions/07-filesystem-storage/README.md) | Q73-Q84 | 12 | 打通 FD→VFS→dentry/inode→page cache→writeback→journal→durability。 |
| 8 | [I/O 与高性能系统](questions/08-io-high-performance/README.md) | Q85-Q92 | 8 | 理解 interrupt/DMA、blocking/non-blocking、epoll、io_uring 与 zero-copy。 |
| 9 | [Linux、容器与性能排障](questions/09-linux-container-performance/README.md) | Q93-Q100 | 8 | 把 OS 原理落到 namespace/cgroup、OOM 与线上 P99 系统化排障。 |

## 快速开始

- **第一次系统学习**：[学习路线](guides/learning-roadmap.md)
- **学习答题结构**：[答题方法](guides/answering-method.md)
- **面试前 1-2 天冲刺**：[25 道必会题](guides/25-must-know.md)
- **训练连续追问**：[六条追问链](guides/follow-up-chains.md)
- **系统/Infra 岗**：[Linux 线上排障速查](guides/linux-troubleshooting.md)
- **完整目录**：[SUMMARY.md](SUMMARY.md)
- **题目总索引**：[guides/topic-index.md](guides/topic-index.md)
- **术语速查**：[guides/glossary.md](guides/glossary.md)
- **源码阅读**：[Linux Kernel 源码阅读地图](guides/kernel-source-reading-map.md)
- **V2 升级报告**：[ENRICHMENT_REPORT.md](ENRICHMENT_REPORT.md)
- **原始 83 页 PDF**：[book/操作系统面试宝典_100道高频真题_深度解析.pdf](book/操作系统面试宝典_100道高频真题_深度解析.pdf)

## 单题结构

每个 `qXX.md` 包含：

1. YAML 元数据（题号、章节、频率、难度、标签）
2. 一句话核心结论
3. PDF 原始深度解析
4. 仓库增强：机制/边界/性能视角
5. 30 秒 / 2 分钟 / 5 分钟答题模板
6. 面试官追问树
7. Gotcha / 反例
8. 面试评分 rubric
9. Linux / 工程实验
10. 机制级推演、性能模型与内核对象
11. 边界条件与高级追问树
12. 可复现实验与 5 级评分 Rubric
13. 90 秒高级口述答案与实验设计
14. 关联题目与延伸阅读

## 内容来源与增强边界

- **PDF-derived**：核心结论、深度解析、回答模板、追问、易错点，以及原 PDF 的章节/附录结构。
- **Repo enhancement**：知识连接图、回答分层、评分标准、Linux 命令/实验、跨题链接与扩展阅读。
- 公开面经只用于证明题型出现过；技术语义优先以 Linux Kernel 官方文档与 man-pages 核对。

## 推荐训练方法

```text
Round 1  看答案理解
Round 2  只看标题，60 秒口述
Round 3  追问链连续回答 5-10 分钟
Round 4  Linux 小实验验证机制
Round 5  用线上故障场景反向检验知识
```

## 仓库校验

```bash
python scripts/validate_repo.py
```

校验项包括：100 个题目 Markdown 是否齐全、题号是否连续、frontmatter 是否存在、README/SUMMARY 内部链接是否失效。

## 适用岗位

Backend / C++ / System Software / AI Infra / Database / Storage / SRE / Performance Engineering。

## 关于《剑指 Offer》式编排

本仓库借鉴的是“题目驱动、逐题深挖、重视追问与方法论”的**编排理念**，内容为独立原创整理；不复刻《剑指 Offer》的正文、题解或原文表达。

## License

本生成版本不预设公开许可。若准备公开发布，请由仓库所有者根据使用目标选择合适的代码/文档许可证。
