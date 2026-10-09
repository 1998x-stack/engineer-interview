# Linux Kernel 源码阅读地图

> 目标：把 100 道面试题从“概念记忆”连接到可验证的 Linux 实现。不要从头顺序阅读内核源码，而是从用户可见 API 沿调用链向下。

## 1. 进程与系统调用

- 关键对象：`task_struct`、`mm_struct`、`files_struct`、`signal_struct`。
- 入口：`fork/clone/execve/wait4`、系统调用入口代码。
- 阅读法：先理解对象共享关系，再追 `clone` flags 如何决定线程/进程语义。

## 2. 调度

- 关键对象：per-CPU runqueue、调度实体、调度类。
- 当前重点：公平调度从传统 CFS 直觉逐步演进到 EEVDF 的 eligibility / virtual deadline。
- 阅读法：先看 scheduler 文档，再进入 `kernel/sched/`，不要先背红黑树细节。

## 3. 并发与同步

- 关键对象：mutex、rwsem、spinlock、futex wait queues。
- 关键原则：正确性不变量 → memory ordering → fast path/slow path → contention。
- 工具：`perf lock`、`strace -e futex`、ThreadSanitizer、`perf c2c`。

## 4. 内存管理

- 关键对象：`mm_struct`、VMA、页表、folio/page、zone、buddy、SLUB。
- 调用链：VA → TLB → page table → fault → allocation/page cache/reclaim。
- 工具：`/proc/<pid>/smaps*`、`vmstat`、`pidstat -r`、`perf` TLB counters、PSI。

## 5. VFS 与文件系统

- 关键对象：`files_struct → struct file → dentry → inode → address_space`。
- 调用链：`open/read/write/fsync/rename` → VFS → filesystem → page cache → block。
- 工具：`strace`、`lsof`、`iostat`、filesystem-specific tracing。

## 6. I/O

- readiness：`select/poll/epoll`。
- completion：`io_uring`。
- block：BIO/request/blk-mq；network：socket queue/NAPI/DMA。
- 阅读法：先明确“谁提交、谁搬数据、谁通知完成”。

## 7. Container / cgroup / performance

- namespaces：视图与身份边界。
- cgroup v2：CPU/memory/io/pids 的资源层级。
- 排障：PSI + cgroup counters + perf/eBPF。

## 推荐顺序

```text
man page / kernel doc
   ↓
最小可复现实验
   ↓
trace / perf 得到真实调用证据
   ↓
只阅读命中的源码路径
   ↓
回到面试题总结机制、不变量与 trade-off
```
