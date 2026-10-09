# 第 8 章：I/O 与高性能系统

> 理解 interrupt/DMA、blocking/non-blocking、epoll、io_uring 与 zero-copy。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q85](q85.md) | Polling、Interrupt、DMA 分别解决什么？ | ★★★★★ | 基础 | `polling/interrupt/DMA` |
| [Q86](q86.md) | Blocking、Non-blocking、Sync、Async 是同一组概念吗？ | ★★★★★ | 中等 | `blocking/nonblocking/sync/async` |
| [Q87](q87.md) | select、poll、epoll 有什么区别？ | ★★★★★ | 中等 | `select/poll/epoll` |
| [Q88](q88.md) | epoll LT 与 ET 有什么区别？ | ★★★★★ | 中等 | `level-triggered/edge-triggered` |
| [Q89](q89.md) | Reactor 与 Proactor 有什么区别？ | ★★★★☆ | 高级 | `reactor/proactor/readiness/completion` |
| [Q90](q90.md) | io_uring 为什么重要？ | ★★★★★ | 高级 | `io_uring/SQ/CQ/async` |
| [Q91](q91.md) | Zero Copy 是什么？真的 0 次复制吗？ | ★★★★☆ | 中等 | `zero-copy/sendfile/splice` |
| [Q92](q92.md) | 为什么 HDD 时代的 Disk Scheduling 在 SSD 上重要性下降？ | ★★★☆☆ | 中等 | `SSTF/SCAN/SSD/NVMe` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
