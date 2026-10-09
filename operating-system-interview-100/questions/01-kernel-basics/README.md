# 第 1 章：操作系统与内核基础

> 从抽象、保护边界、系统调用到启动与中断，建立 OS 的总框架。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q01](q01.md) | 什么是操作系统？它真正解决了什么问题？ | ★★★★★ | 基础 | `OS/抽象/资源管理` |
| [Q02](q02.md) | 用户态和内核态有什么区别？为什么要分层？ | ★★★★★ | 基础 | `privilege/ring/syscall` |
| [Q03](q03.md) | System Call 和普通函数调用有什么区别？ | ★★★★★ | 基础 | `syscall/libc/privilege` |
| [Q04](q04.md) | 宏内核、微内核与模块化内核如何比较？ | ★★★☆☆ | 中等 | `monolithic/microkernel/module` |
| [Q05](q05.md) | Interrupt、Exception、Trap、System Call 如何区分？ | ★★★★☆ | 中等 | `interrupt/exception/trap` |
| [Q06](q06.md) | 从开机到第一个用户进程，系统经历什么？ | ★★★☆☆ | 中等 | `boot/UEFI/kernel/PID1` |
| [Q07](q07.md) | 为什么进程不能直接共享所有物理内存？ | ★★★★☆ | 基础 | `isolation/page protection` |
| [Q08](q08.md) | Timer Interrupt 为什么是抢占式多任务的关键？ | ★★★★☆ | 中等 | `timer/preemption/scheduler` |
| [Q09](q09.md) | Kernel Stack 与 User Stack 有何区别？ | ★★★☆☆ | 中等 | `stack/syscall/thread` |
| [Q10](q10.md) | 为什么 OS 大量依赖抽象？抽象有什么代价？ | ★★★☆☆ | 基础 | `abstraction/API/cost` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
