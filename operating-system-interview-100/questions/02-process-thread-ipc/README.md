# 第 2 章：进程、线程与 IPC

> 理解执行实体、资源共享、fork/COW、生命周期与进程间通信。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q11](q11.md) | Program 与 Process 有什么区别？ | ★★★★★ | 基础 | `process/address-space/state` |
| [Q12](q12.md) | PCB 里有什么？Linux 的 task_struct 表示什么？ | ★★★★☆ | 中等 | `PCB/task_struct/scheduler` |
| [Q13](q13.md) | 进程有哪些状态？Ready 和 Waiting 的本质区别是什么？ | ★★★★★ | 基础 | `process-state/ready/waiting` |
| [Q14](q14.md) | Process 与 Thread 到底有什么区别？ | ★★★★★ | 基础 | `process/thread/resource-sharing` |
| [Q15](q15.md) | User-level Thread 与 Kernel Thread 有什么区别？ | ★★★★☆ | 中等 | `ULT/KLT/M:N` |
| [Q16](q16.md) | fork、exec、wait 分别做什么？ | ★★★★★ | 基础 | `fork/exec/wait` |
| [Q17](q17.md) | Copy-on-Write 为什么让 fork 变快？ | ★★★★★ | 中等 | `COW/page-fault/fork` |
| [Q18](q18.md) | Zombie Process 与 Orphan Process 有什么区别？ | ★★★★★ | 基础 | `zombie/orphan/wait` |
| [Q19](q19.md) | IPC 有哪些方式？如何选择？ | ★★★★★ | 中等 | `pipe/shared-memory/socket/queue` |
| [Q20](q20.md) | Pipe 与 Socket 的差异是什么？ | ★★★★☆ | 中等 | `pipe/socket/UDS` |
| [Q21](q21.md) | 为什么 Shared Memory 通常吞吐很高？ | ★★★★★ | 中等 | `shared-memory/mmap/synchronization` |
| [Q22](q22.md) | Signal 是什么？为什么 Signal Handler 很难写？ | ★★★★☆ | 高级 | `signal/async-signal-safe` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
