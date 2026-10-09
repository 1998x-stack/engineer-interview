# 六条高价值追问链

这是原 PDF “附录 B” 的扩展版。训练方式是从链上任一点开始，连续解释后续节点之间的因果关系。

## 进程线程链

`Process vs Thread → Context Switch → Address Space → TLB/Cache → Race → Mutex → Futex → Priority Inversion`

关联题：
- [Q14 Process 与 Thread 到底有什么区别？](../questions/02-process-thread-ipc/q14.md)
- [Q17 Copy-on-Write 为什么让 fork 变快？](../questions/02-process-thread-ipc/q17.md)
- [Q33 什么是 Race Condition？为什么 counter++ 不安全？](../questions/04-concurrency-sync/q33.md)
- [Q35 Mutex 与 Semaphore 的本质区别？](../questions/04-concurrency-sync/q35.md)
- [Q47 Futex 为什么能让 Mutex 的无竞争路径很快？](../questions/04-concurrency-sync/q47.md)
- [Q55 Priority Inversion 是什么？如何解决？](../questions/05-deadlock/q55.md)

## 虚拟内存链

`Virtual Memory → Page Table → TLB → Page Fault → COW → mmap → Page Cache → Reclaim → Swap → OOM`

关联题：
- [Q56 为什么需要 Virtual Memory？](../questions/06-memory-virtual-memory/q56.md)
- [Q57 Virtual Address 如何转换为 Physical Address？](../questions/06-memory-virtual-memory/q57.md)
- [Q60 TLB 是什么？为什么必须有？](../questions/06-memory-virtual-memory/q60.md)
- [Q62 Page Fault 发生后 OS 做什么？](../questions/06-memory-virtual-memory/q62.md)
- [Q68 COW 为什么一定通过 Page Fault 驱动？](../questions/06-memory-virtual-memory/q68.md)
- [Q69 mmap 是什么？为什么数据库/存储系统关心它？](../questions/06-memory-virtual-memory/q69.md)
- [Q77 Page Cache 是什么？为什么第二次读文件更快？](../questions/07-filesystem-storage/q77.md)
- [Q97 OOM Killer 为什么不能简单杀 RSS 最大的进程？](../questions/09-linux-container-performance/q97.md)

## 文件系统链

`FD → open file description → VFS → dentry/inode → Page Cache → writeback → fsync → journal → crash consistency`

关联题：
- [Q75 File Descriptor 到底是什么？](../questions/07-filesystem-storage/q75.md)
- [Q74 open("/a/b/c") 大致发生什么？](../questions/07-filesystem-storage/q74.md)
- [Q73 inode 是什么？文件名存在哪里？](../questions/07-filesystem-storage/q73.md)
- [Q77 Page Cache 是什么？为什么第二次读文件更快？](../questions/07-filesystem-storage/q77.md)
- [Q79 write 返回后，数据一定落盘了吗？](../questions/07-filesystem-storage/q79.md)
- [Q80 Journaling File System 为什么需要 Journal？](../questions/07-filesystem-storage/q80.md)
- [Q82 为什么 rename 常用于原子文件更新？](../questions/07-filesystem-storage/q82.md)

## 并发链

`Race → Atomic → Memory Ordering → Mutex/Semaphore → Condition Variable → Deadlock → Starvation/Livelock`

关联题：
- [Q33 什么是 Race Condition？为什么 counter++ 不安全？](../questions/04-concurrency-sync/q33.md)
- [Q40 Atomic Operation 是什么？CAS 为什么重要？](../questions/04-concurrency-sync/q40.md)
- [Q41 为什么只有 Atomic 还不够？Memory Ordering 是什么？](../questions/04-concurrency-sync/q41.md)
- [Q35 Mutex 与 Semaphore 的本质区别？](../questions/04-concurrency-sync/q35.md)
- [Q39 Condition Variable 为什么必须和 Mutex 配合？](../questions/04-concurrency-sync/q39.md)
- [Q48 什么是 Deadlock？四个必要条件是什么？](../questions/05-deadlock/q48.md)
- [Q53 Deadlock 与 Livelock 有什么区别？](../questions/05-deadlock/q53.md)
- [Q54 Starvation 与 Deadlock 有什么区别？](../questions/05-deadlock/q54.md)

## I/O 链

`Interrupt/DMA → blocking/non-blocking → select/poll/epoll → ET/LT → Reactor/Proactor → io_uring → zero-copy`

关联题：
- [Q85 Polling、Interrupt、DMA 分别解决什么？](../questions/08-io-high-performance/q85.md)
- [Q86 Blocking、Non-blocking、Sync、Async 是同一组概念吗？](../questions/08-io-high-performance/q86.md)
- [Q87 select、poll、epoll 有什么区别？](../questions/08-io-high-performance/q87.md)
- [Q88 epoll LT 与 ET 有什么区别？](../questions/08-io-high-performance/q88.md)
- [Q89 Reactor 与 Proactor 有什么区别？](../questions/08-io-high-performance/q89.md)
- [Q90 io_uring 为什么重要？](../questions/08-io-high-performance/q90.md)
- [Q91 Zero Copy 是什么？真的 0 次复制吗？](../questions/08-io-high-performance/q91.md)

## 线上排障链

`P99 ↑ → CPU/scheduler → lock/futex → page fault/reclaim → disk latency → network → syscall trace → perf/eBPF`

关联题：
- [Q100 线上服务 P99 延迟突然暴涨，如何做完整 OS 排查？](../questions/09-linux-container-performance/q100.md)
- [Q98 CPU 使用率不高但服务很慢，怎么排查？](../questions/09-linux-container-performance/q98.md)
- [Q47 Futex 为什么能让 Mutex 的无竞争路径很快？](../questions/04-concurrency-sync/q47.md)
- [Q62 Page Fault 发生后 OS 做什么？](../questions/06-memory-virtual-memory/q62.md)
- [Q67 什么是 Thrashing？如何识别和缓解？](../questions/06-memory-virtual-memory/q67.md)
- [Q99 File Descriptor 不断增长，如何判断 FD Leak？](../questions/09-linux-container-performance/q99.md)
