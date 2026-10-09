# 第 4 章：并发与同步

> 从 race condition 到 mutex/semaphore、memory ordering、lock-free 与 futex。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q33](q33.md) | 什么是 Race Condition？为什么 counter++ 不安全？ | ★★★★★ | 基础 | `race/atomicity` |
| [Q34](q34.md) | Critical Section 的正确性要求是什么？ | ★★★★☆ | 基础 | `mutual-exclusion/progress/bounded-waiting` |
| [Q35](q35.md) | Mutex 与 Semaphore 的本质区别？ | ★★★★★ | 基础 | `mutex/semaphore/ownership` |
| [Q36](q36.md) | Binary Semaphore 和 Mutex 一样吗？ | ★★★★★ | 中等 | `binary-semaphore/mutex` |
| [Q37](q37.md) | Spinlock 与 Mutex 如何选择？ | ★★★★★ | 中等 | `spinlock/mutex/contention` |
| [Q38](q38.md) | Reader-Writer Lock 什么时候有价值？ | ★★★★☆ | 中等 | `rwlock/read-heavy` |
| [Q39](q39.md) | Condition Variable 为什么必须和 Mutex 配合？ | ★★★★★ | 中等 | `condition-variable/predicate` |
| [Q40](q40.md) | Atomic Operation 是什么？CAS 为什么重要？ | ★★★★★ | 中等 | `atomic/CAS/lock-free` |
| [Q41](q41.md) | 为什么只有 Atomic 还不够？Memory Ordering 是什么？ | ★★★★★ | 高级 | `memory-order/acquire/release` |
| [Q42](q42.md) | Producer-Consumer 如何用 Mutex + Semaphore 正确实现？ | ★★★★★ | 中等 | `producer-consumer/bounded-buffer` |
| [Q43](q43.md) | Reader-Writer Problem 的几种策略有什么 trade-off？ | ★★★★☆ | 中等 | `reader-preference/writer-preference/fairness` |
| [Q44](q44.md) | Dining Philosophers 为什么经典？怎么避免死锁？ | ★★★★☆ | 中等 | `dining-philosophers/lock-order` |
| [Q45](q45.md) | Thread-safe 与 Reentrant 是一回事吗？ | ★★★★☆ | 高级 | `thread-safe/reentrant` |
| [Q46](q46.md) | False Sharing 是什么？为什么没有数据竞争也会很慢？ | ★★★★★ | 高级 | `cache-line/false-sharing` |
| [Q47](q47.md) | Futex 为什么能让 Mutex 的无竞争路径很快？ | ★★★★★ | 高级 | `futex/fast-path/slow-path` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
