# 题目总索引

> 100 道题的可搜索索引。GitHub 页面中可直接用浏览器查找关键词。

| 题号 | 题目 | 章节 | 高频度 |
|---|---|---|---:|
| [Q01](../questions/01-kernel-basics/q01.md) | 什么是操作系统？它真正解决了什么问题？ | 操作系统与内核基础 | ★★★★★ |
| [Q02](../questions/01-kernel-basics/q02.md) | 用户态和内核态有什么区别？为什么要分层？ | 操作系统与内核基础 | ★★★★★ |
| [Q03](../questions/01-kernel-basics/q03.md) | System Call 和普通函数调用有什么区别？ | 操作系统与内核基础 | ★★★★★ |
| [Q04](../questions/01-kernel-basics/q04.md) | 宏内核、微内核与模块化内核如何比较？ | 操作系统与内核基础 | ★★★☆☆ |
| [Q05](../questions/01-kernel-basics/q05.md) | Interrupt、Exception、Trap、System Call 如何区分？ | 操作系统与内核基础 | ★★★★☆ |
| [Q06](../questions/01-kernel-basics/q06.md) | 从开机到第一个用户进程，系统经历什么？ | 操作系统与内核基础 | ★★★☆☆ |
| [Q07](../questions/01-kernel-basics/q07.md) | 为什么进程不能直接共享所有物理内存？ | 操作系统与内核基础 | ★★★★☆ |
| [Q08](../questions/01-kernel-basics/q08.md) | Timer Interrupt 为什么是抢占式多任务的关键？ | 操作系统与内核基础 | ★★★★☆ |
| [Q09](../questions/01-kernel-basics/q09.md) | Kernel Stack 与 User Stack 有何区别？ | 操作系统与内核基础 | ★★★☆☆ |
| [Q10](../questions/01-kernel-basics/q10.md) | 为什么 OS 大量依赖抽象？抽象有什么代价？ | 操作系统与内核基础 | ★★★☆☆ |
| [Q11](../questions/02-process-thread-ipc/q11.md) | Program 与 Process 有什么区别？ | 进程、线程与 IPC | ★★★★★ |
| [Q12](../questions/02-process-thread-ipc/q12.md) | PCB 里有什么？Linux 的 task_struct 表示什么？ | 进程、线程与 IPC | ★★★★☆ |
| [Q13](../questions/02-process-thread-ipc/q13.md) | 进程有哪些状态？Ready 和 Waiting 的本质区别是什么？ | 进程、线程与 IPC | ★★★★★ |
| [Q14](../questions/02-process-thread-ipc/q14.md) | Process 与 Thread 到底有什么区别？ | 进程、线程与 IPC | ★★★★★ |
| [Q15](../questions/02-process-thread-ipc/q15.md) | User-level Thread 与 Kernel Thread 有什么区别？ | 进程、线程与 IPC | ★★★★☆ |
| [Q16](../questions/02-process-thread-ipc/q16.md) | fork、exec、wait 分别做什么？ | 进程、线程与 IPC | ★★★★★ |
| [Q17](../questions/02-process-thread-ipc/q17.md) | Copy-on-Write 为什么让 fork 变快？ | 进程、线程与 IPC | ★★★★★ |
| [Q18](../questions/02-process-thread-ipc/q18.md) | Zombie Process 与 Orphan Process 有什么区别？ | 进程、线程与 IPC | ★★★★★ |
| [Q19](../questions/02-process-thread-ipc/q19.md) | IPC 有哪些方式？如何选择？ | 进程、线程与 IPC | ★★★★★ |
| [Q20](../questions/02-process-thread-ipc/q20.md) | Pipe 与 Socket 的差异是什么？ | 进程、线程与 IPC | ★★★★☆ |
| [Q21](../questions/02-process-thread-ipc/q21.md) | 为什么 Shared Memory 通常吞吐很高？ | 进程、线程与 IPC | ★★★★★ |
| [Q22](../questions/02-process-thread-ipc/q22.md) | Signal 是什么？为什么 Signal Handler 很难写？ | 进程、线程与 IPC | ★★★★☆ |
| [Q23](../questions/03-cpu-scheduling/q23.md) | Preemptive 与 Non-preemptive Scheduling 的差异？ | CPU 调度 | ★★★★★ |
| [Q24](../questions/03-cpu-scheduling/q24.md) | 如何评价一个调度算法？ | CPU 调度 | ★★★★★ |
| [Q25](../questions/03-cpu-scheduling/q25.md) | FCFS 为什么会产生 Convoy Effect？ | CPU 调度 | ★★★★☆ |
| [Q26](../questions/03-cpu-scheduling/q26.md) | SJF 为什么理论优秀但现实难实现？ | CPU 调度 | ★★★★☆ |
| [Q27](../questions/03-cpu-scheduling/q27.md) | Round Robin 时间片应该多大？ | CPU 调度 | ★★★★☆ |
| [Q28](../questions/03-cpu-scheduling/q28.md) | Priority Scheduling 为什么会 starvation？Aging 如何解决？ | CPU 调度 | ★★★★★ |
| [Q29](../questions/03-cpu-scheduling/q29.md) | MLFQ 为什么适合交互式任务？ | CPU 调度 | ★★★★☆ |
| [Q30](../questions/03-cpu-scheduling/q30.md) | Real-time Scheduling 与普通调度最大的区别？ | CPU 调度 | ★★★☆☆ |
| [Q31](../questions/03-cpu-scheduling/q31.md) | CPU Affinity 为什么可能提升性能？ | CPU 调度 | ★★★★☆ |
| [Q32](../questions/03-cpu-scheduling/q32.md) | 现代 Linux 还是 CFS 吗？EEVDF 是什么？ | CPU 调度 | ★★★★★ |
| [Q33](../questions/04-concurrency-sync/q33.md) | 什么是 Race Condition？为什么 counter++ 不安全？ | 并发与同步 | ★★★★★ |
| [Q34](../questions/04-concurrency-sync/q34.md) | Critical Section 的正确性要求是什么？ | 并发与同步 | ★★★★☆ |
| [Q35](../questions/04-concurrency-sync/q35.md) | Mutex 与 Semaphore 的本质区别？ | 并发与同步 | ★★★★★ |
| [Q36](../questions/04-concurrency-sync/q36.md) | Binary Semaphore 和 Mutex 一样吗？ | 并发与同步 | ★★★★★ |
| [Q37](../questions/04-concurrency-sync/q37.md) | Spinlock 与 Mutex 如何选择？ | 并发与同步 | ★★★★★ |
| [Q38](../questions/04-concurrency-sync/q38.md) | Reader-Writer Lock 什么时候有价值？ | 并发与同步 | ★★★★☆ |
| [Q39](../questions/04-concurrency-sync/q39.md) | Condition Variable 为什么必须和 Mutex 配合？ | 并发与同步 | ★★★★★ |
| [Q40](../questions/04-concurrency-sync/q40.md) | Atomic Operation 是什么？CAS 为什么重要？ | 并发与同步 | ★★★★★ |
| [Q41](../questions/04-concurrency-sync/q41.md) | 为什么只有 Atomic 还不够？Memory Ordering 是什么？ | 并发与同步 | ★★★★★ |
| [Q42](../questions/04-concurrency-sync/q42.md) | Producer-Consumer 如何用 Mutex + Semaphore 正确实现？ | 并发与同步 | ★★★★★ |
| [Q43](../questions/04-concurrency-sync/q43.md) | Reader-Writer Problem 的几种策略有什么 trade-off？ | 并发与同步 | ★★★★☆ |
| [Q44](../questions/04-concurrency-sync/q44.md) | Dining Philosophers 为什么经典？怎么避免死锁？ | 并发与同步 | ★★★★☆ |
| [Q45](../questions/04-concurrency-sync/q45.md) | Thread-safe 与 Reentrant 是一回事吗？ | 并发与同步 | ★★★★☆ |
| [Q46](../questions/04-concurrency-sync/q46.md) | False Sharing 是什么？为什么没有数据竞争也会很慢？ | 并发与同步 | ★★★★★ |
| [Q47](../questions/04-concurrency-sync/q47.md) | Futex 为什么能让 Mutex 的无竞争路径很快？ | 并发与同步 | ★★★★★ |
| [Q48](../questions/05-deadlock/q48.md) | 什么是 Deadlock？四个必要条件是什么？ | 死锁 | ★★★★★ |
| [Q49](../questions/05-deadlock/q49.md) | Deadlock Prevention 怎么做？ | 死锁 | ★★★★★ |
| [Q50](../questions/05-deadlock/q50.md) | Deadlock Avoidance 与 Prevention 有什么区别？ | 死锁 | ★★★★☆ |
| [Q51](../questions/05-deadlock/q51.md) | Safe、Unsafe、Deadlock State 如何区分？ | 死锁 | ★★★★★ |
| [Q52](../questions/05-deadlock/q52.md) | 如何检测 Deadlock？Wait-for Graph 怎么用？ | 死锁 | ★★★★☆ |
| [Q53](../questions/05-deadlock/q53.md) | Deadlock 与 Livelock 有什么区别？ | 死锁 | ★★★★★ |
| [Q54](../questions/05-deadlock/q54.md) | Starvation 与 Deadlock 有什么区别？ | 死锁 | ★★★★★ |
| [Q55](../questions/05-deadlock/q55.md) | Priority Inversion 是什么？如何解决？ | 死锁 | ★★★★★ |
| [Q56](../questions/06-memory-virtual-memory/q56.md) | 为什么需要 Virtual Memory？ | 内存与虚拟内存 | ★★★★★ |
| [Q57](../questions/06-memory-virtual-memory/q57.md) | Virtual Address 如何转换为 Physical Address？ | 内存与虚拟内存 | ★★★★★ |
| [Q58](../questions/06-memory-virtual-memory/q58.md) | Paging 与 Segmentation 有什么区别？ | 内存与虚拟内存 | ★★★★★ |
| [Q59](../questions/06-memory-virtual-memory/q59.md) | VA→PA 的页表项通常包含什么？ | 内存与虚拟内存 | ★★★★★ |
| [Q60](../questions/06-memory-virtual-memory/q60.md) | TLB 是什么？为什么必须有？ | 内存与虚拟内存 | ★★★★★ |
| [Q61](../questions/06-memory-virtual-memory/q61.md) | 为什么 Page Table 要多级？ | 内存与虚拟内存 | ★★★★★ |
| [Q62](../questions/06-memory-virtual-memory/q62.md) | Page Fault 发生后 OS 做什么？ | 内存与虚拟内存 | ★★★★★ |
| [Q63](../questions/06-memory-virtual-memory/q63.md) | Minor Page Fault 与 Major Page Fault 有何区别？ | 内存与虚拟内存 | ★★★★☆ |
| [Q64](../questions/06-memory-virtual-memory/q64.md) | 什么是 Demand Paging？ | 内存与虚拟内存 | ★★★★★ |
| [Q65](../questions/06-memory-virtual-memory/q65.md) | Page Replacement 常见算法及真实系统差异？ | 内存与虚拟内存 | ★★★★★ |
| [Q66](../questions/06-memory-virtual-memory/q66.md) | 什么是 Belady’s Anomaly？ | 内存与虚拟内存 | ★★★★☆ |
| [Q67](../questions/06-memory-virtual-memory/q67.md) | 什么是 Thrashing？如何识别和缓解？ | 内存与虚拟内存 | ★★★★★ |
| [Q68](../questions/06-memory-virtual-memory/q68.md) | COW 为什么一定通过 Page Fault 驱动？ | 内存与虚拟内存 | ★★★★★ |
| [Q69](../questions/06-memory-virtual-memory/q69.md) | mmap 是什么？为什么数据库/存储系统关心它？ | 内存与虚拟内存 | ★★★★★ |
| [Q70](../questions/06-memory-virtual-memory/q70.md) | malloc 是 System Call 吗？底层如何向 OS 要内存？ | 内存与虚拟内存 | ★★★★★ |
| [Q71](../questions/06-memory-virtual-memory/q71.md) | Internal 与 External Fragmentation 的区别？ | 内存与虚拟内存 | ★★★★★ |
| [Q72](../questions/06-memory-virtual-memory/q72.md) | Buddy Allocator 与 Slab/SLUB 分别解决什么？ | 内存与虚拟内存 | ★★★★☆ |
| [Q73](../questions/07-filesystem-storage/q73.md) | inode 是什么？文件名存在哪里？ | 文件系统与存储 | ★★★★★ |
| [Q74](../questions/07-filesystem-storage/q74.md) | open( | 文件系统与存储 | ★★★★★ |
| [Q75](../questions/07-filesystem-storage/q75.md) | File Descriptor 到底是什么？ | 文件系统与存储 | ★★★★★ |
| [Q76](../questions/07-filesystem-storage/q76.md) | Hard Link 与 Symbolic Link 的区别？ | 文件系统与存储 | ★★★★★ |
| [Q77](../questions/07-filesystem-storage/q77.md) | Page Cache 是什么？为什么第二次读文件更快？ | 文件系统与存储 | ★★★★★ |
| [Q78](../questions/07-filesystem-storage/q78.md) | Buffered I/O 与 Direct I/O 如何取舍？ | 文件系统与存储 | ★★★★☆ |
| [Q79](../questions/07-filesystem-storage/q79.md) | write 返回后，数据一定落盘了吗？ | 文件系统与存储 | ★★★★★ |
| [Q80](../questions/07-filesystem-storage/q80.md) | Journaling File System 为什么需要 Journal？ | 文件系统与存储 | ★★★★★ |
| [Q81](../questions/07-filesystem-storage/q81.md) | ext4 data=ordered / writeback / journal 有何差异？ | 文件系统与存储 | ★★★★☆ |
| [Q82](../questions/07-filesystem-storage/q82.md) | 为什么 rename 常用于原子文件更新？ | 文件系统与存储 | ★★★★★ |
| [Q83](../questions/07-filesystem-storage/q83.md) | 打开的文件被 rm 后为什么还能继续读？ | 文件系统与存储 | ★★★★★ |
| [Q84](../questions/07-filesystem-storage/q84.md) | RAID 0/1/5/6/10 的 trade-off？ | 文件系统与存储 | ★★★☆☆ |
| [Q85](../questions/08-io-high-performance/q85.md) | Polling、Interrupt、DMA 分别解决什么？ | I/O 与高性能系统 | ★★★★★ |
| [Q86](../questions/08-io-high-performance/q86.md) | Blocking、Non-blocking、Sync、Async 是同一组概念吗？ | I/O 与高性能系统 | ★★★★★ |
| [Q87](../questions/08-io-high-performance/q87.md) | select、poll、epoll 有什么区别？ | I/O 与高性能系统 | ★★★★★ |
| [Q88](../questions/08-io-high-performance/q88.md) | epoll LT 与 ET 有什么区别？ | I/O 与高性能系统 | ★★★★★ |
| [Q89](../questions/08-io-high-performance/q89.md) | Reactor 与 Proactor 有什么区别？ | I/O 与高性能系统 | ★★★★☆ |
| [Q90](../questions/08-io-high-performance/q90.md) | io_uring 为什么重要？ | I/O 与高性能系统 | ★★★★★ |
| [Q91](../questions/08-io-high-performance/q91.md) | Zero Copy 是什么？真的 0 次复制吗？ | I/O 与高性能系统 | ★★★★☆ |
| [Q92](../questions/08-io-high-performance/q92.md) | 为什么 HDD 时代的 Disk Scheduling 在 SSD 上重要性下降？ | I/O 与高性能系统 | ★★★☆☆ |
| [Q93](../questions/09-linux-container-performance/q93.md) | Container 为什么不是“小型 VM”？ | Linux、容器与性能排障 | ★★★★★ |
| [Q94](../questions/09-linux-container-performance/q94.md) | Namespace 与 Cgroup 有什么区别？ | Linux、容器与性能排障 | ★★★★★ |
| [Q95](../questions/09-linux-container-performance/q95.md) | 为什么容器里的 root 不一定是 Host root？ | Linux、容器与性能排障 | ★★★★☆ |
| [Q96](../questions/09-linux-container-performance/q96.md) | malloc(100GB) 为什么在 32GB RAM 机器上可能成功？ | Linux、容器与性能排障 | ★★★★★ |
| [Q97](../questions/09-linux-container-performance/q97.md) | OOM Killer 为什么不能简单杀 RSS 最大的进程？ | Linux、容器与性能排障 | ★★★★★ |
| [Q98](../questions/09-linux-container-performance/q98.md) | CPU 使用率不高但服务很慢，怎么排查？ | Linux、容器与性能排障 | ★★★★★ |
| [Q99](../questions/09-linux-container-performance/q99.md) | File Descriptor 不断增长，如何判断 FD Leak？ | Linux、容器与性能排障 | ★★★★★ |
| [Q100](../questions/09-linux-container-performance/q100.md) | 线上服务 P99 延迟突然暴涨，如何做完整 OS 排查？ | Linux、容器与性能排障 | ★★★★★ |
