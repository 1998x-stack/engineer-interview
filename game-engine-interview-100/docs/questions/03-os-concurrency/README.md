# 第 3 章 · 操作系统、多线程与并发

从线程基础走到 Job System、原子内存序、线程所有权和 CPU/GPU 异步流水。

## 本章能力目标

- thread scheduling
- locks
- lock-free
- memory ordering
- render threading

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q021](Q021.md) | Process 与 Thread 的区别是什么？ | Intermediate | `concurrency, os` |
| [Q022](Q022.md) | Context Switch 为什么贵？ | Intermediate | `concurrency, os` |
| [Q023](Q023.md) | 什么是 Job System？为什么比“一个子系统一个线程”更可扩展？ | Advanced | `concurrency, os, job-system` |
| [Q024](Q024.md) | Mutex、Spinlock、Semaphore 怎么选？ | Intermediate | `concurrency, os` |
| [Q025](Q025.md) | 什么是 Deadlock？四个必要条件是什么？ | Intermediate | `concurrency, os` |
| [Q026](Q026.md) | 如何实现一个 SPSC 无锁环形队列？ | Advanced | `concurrency, os` |
| [Q027](Q027.md) | memory_order_relaxed / acquire / release 是什么？ | Advanced | `concurrency, os, memory-model` |
| [Q028](Q028.md) | 虚拟地址如何转换成物理地址？Page Fault 发生了什么？ | Advanced | `concurrency, os` |
| [Q029](Q029.md) | Game Thread 和 Render Thread 为什么要分开？ | Advanced | `concurrency, os` |
| [Q030](Q030.md) | Triple Buffering 与 Frames in Flight 有什么作用？ | Advanced | `concurrency, os` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
