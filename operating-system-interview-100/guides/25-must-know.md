# 25 道必会题

这是原 PDF “附录 A” 的仓库化版本。

| 题号 | 题目 | 核心主题 | 训练目标 |
|---|---|---|---|
| [Q02](../questions/01-kernel-basics/q02.md) | 用户态和内核态有什么区别？为什么要分层？ | `privilege/ring/syscall` | 60 秒核心回答 + 5 分钟深挖 |
| [Q03](../questions/01-kernel-basics/q03.md) | System Call 和普通函数调用有什么区别？ | `syscall/libc/privilege` | 60 秒核心回答 + 5 分钟深挖 |
| [Q14](../questions/02-process-thread-ipc/q14.md) | Process 与 Thread 到底有什么区别？ | `process/thread/resource-sharing` | 60 秒核心回答 + 5 分钟深挖 |
| [Q16](../questions/02-process-thread-ipc/q16.md) | fork、exec、wait 分别做什么？ | `fork/exec/wait` | 60 秒核心回答 + 5 分钟深挖 |
| [Q17](../questions/02-process-thread-ipc/q17.md) | Copy-on-Write 为什么让 fork 变快？ | `COW/page-fault/fork` | 60 秒核心回答 + 5 分钟深挖 |
| [Q19](../questions/02-process-thread-ipc/q19.md) | IPC 有哪些方式？如何选择？ | `pipe/shared-memory/socket/queue` | 60 秒核心回答 + 5 分钟深挖 |
| [Q23](../questions/03-cpu-scheduling/q23.md) | Preemptive 与 Non-preemptive Scheduling 的差异？ | `preemption/scheduling` | 60 秒核心回答 + 5 分钟深挖 |
| [Q24](../questions/03-cpu-scheduling/q24.md) | 如何评价一个调度算法？ | `throughput/latency/fairness` | 60 秒核心回答 + 5 分钟深挖 |
| [Q33](../questions/04-concurrency-sync/q33.md) | 什么是 Race Condition？为什么 counter++ 不安全？ | `race/atomicity` | 60 秒核心回答 + 5 分钟深挖 |
| [Q35](../questions/04-concurrency-sync/q35.md) | Mutex 与 Semaphore 的本质区别？ | `mutex/semaphore/ownership` | 60 秒核心回答 + 5 分钟深挖 |
| [Q37](../questions/04-concurrency-sync/q37.md) | Spinlock 与 Mutex 如何选择？ | `spinlock/mutex/contention` | 60 秒核心回答 + 5 分钟深挖 |
| [Q39](../questions/04-concurrency-sync/q39.md) | Condition Variable 为什么必须和 Mutex 配合？ | `condition-variable/predicate` | 60 秒核心回答 + 5 分钟深挖 |
| [Q41](../questions/04-concurrency-sync/q41.md) | 为什么只有 Atomic 还不够？Memory Ordering 是什么？ | `memory-order/acquire/release` | 60 秒核心回答 + 5 分钟深挖 |
| [Q42](../questions/04-concurrency-sync/q42.md) | Producer-Consumer 如何用 Mutex + Semaphore 正确实现？ | `producer-consumer/bounded-buffer` | 60 秒核心回答 + 5 分钟深挖 |
| [Q48](../questions/05-deadlock/q48.md) | 什么是 Deadlock？四个必要条件是什么？ | `deadlock/Coffman` | 60 秒核心回答 + 5 分钟深挖 |
| [Q49](../questions/05-deadlock/q49.md) | Deadlock Prevention 怎么做？ | `prevention/lock-order` | 60 秒核心回答 + 5 分钟深挖 |
| [Q56](../questions/06-memory-virtual-memory/q56.md) | 为什么需要 Virtual Memory？ | `virtual-memory/isolation/demand-paging` | 60 秒核心回答 + 5 分钟深挖 |
| [Q57](../questions/06-memory-virtual-memory/q57.md) | Virtual Address 如何转换为 Physical Address？ | `MMU/page-table/TLB` | 60 秒核心回答 + 5 分钟深挖 |
| [Q60](../questions/06-memory-virtual-memory/q60.md) | TLB 是什么？为什么必须有？ | `TLB/translation-cache` | 60 秒核心回答 + 5 分钟深挖 |
| [Q62](../questions/06-memory-virtual-memory/q62.md) | Page Fault 发生后 OS 做什么？ | `page-fault/fault-handler` | 60 秒核心回答 + 5 分钟深挖 |
| [Q69](../questions/06-memory-virtual-memory/q69.md) | mmap 是什么？为什么数据库/存储系统关心它？ | `mmap/file-backed/page-cache` | 60 秒核心回答 + 5 分钟深挖 |
| [Q74](../questions/07-filesystem-storage/q74.md) | open("/a/b/c") 大致发生什么？ | `VFS/path-lookup/dentry/inode` | 60 秒核心回答 + 5 分钟深挖 |
| [Q77](../questions/07-filesystem-storage/q77.md) | Page Cache 是什么？为什么第二次读文件更快？ | `page-cache/read/writeback` | 60 秒核心回答 + 5 分钟深挖 |
| [Q87](../questions/08-io-high-performance/q87.md) | select、poll、epoll 有什么区别？ | `select/poll/epoll` | 60 秒核心回答 + 5 分钟深挖 |
| [Q100](../questions/09-linux-container-performance/q100.md) | 线上服务 P99 延迟突然暴涨，如何做完整 OS 排查？ | `P99/perf/strace/IO/memory/network` | 60 秒核心回答 + 5 分钟深挖 |

## 建议

不要按“背完 25 个定义”学习。每题至少训练三个层次：**一句话本质 → 机制链 → Linux/工程落点**。
