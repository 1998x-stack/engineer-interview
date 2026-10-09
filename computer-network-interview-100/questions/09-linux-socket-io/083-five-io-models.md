---
id: 83
title: "经典五种 I/O Model 是什么？readiness 与 completion 的区别是什么？"
chapter: "第九章 Socket、epoll 与 Linux 网络栈"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["IO Model", "AIO"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 083. 经典五种 I/O Model 是什么？readiness 与 completion 的区别是什么？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：IO Model / AIO  
> **本章**：[第九章 Socket、epoll 与 Linux 网络栈](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **IO Model / AIO** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 经典教材常分为阻塞 IO、非阻塞 IO、IO 多路复用、信号驱动 IO、异步 IO。关键是区分“等待数据就绪”和“把数据拷贝到用户缓冲”两个阶段；epoll 主要通知 readiness，而真正 completion-based 异步 IO 会在操作完成后通知。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. select/poll/epoll 都属于 readiness-based multiplexing。
2. Linux io_uring 可覆盖更多 completion 风格操作，但具体语义取决于操作与模式。
3. 事件循环中仍需执行 recv/send，因此“epoll 异步读取了数据”是不准确表达。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 高并发网络程序的关键是把“等待就绪”和“真正读写数据”分开，epoll 通知 readiness，而不是替应用完成 read/write。
- ET 模式的正确性依赖 nonblocking + drain-until-EAGAIN；任何阻塞系统调用都可能卡住整个 event loop。
- 性能优化必须追踪数据路径：NIC queue → softirq/NAPI → protocol stack → socket queue → userspace。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Readiness 与 Completion 是理解 IO 模型的真正主线

### 第一性原理

- Readiness 模型告诉应用“现在做 read/write 大概率不会因等待数据而阻塞”，应用随后自己执行 syscall；select/poll/epoll/kqueue 属于这一思路。
- Completion 模型更接近“提交 IO 操作，完成后通知结果/bytes”，应用不必在 readiness 后再发起同一个同步 copy syscall；io_uring/IOCP 更接近 completion-oriented 设计。
- “异步”这个词常被混用，面试中应具体说清谁等待、谁执行、何时 copy、谁收到 completion。

### Reactor vs Proactor

Reactor：event loop 收到 readiness，再调用 handler 执行 IO；Proactor：先提交异步 IO，completion event 再交给 handler。真实框架可能混合使用，不必把所有 API 强行归为教科书五类。

### 文件 IO 为什么特殊

Regular file 常不存在 socket 那种“等网络数据到达”的 readiness；page fault/storage latency 仍可能阻塞。io_uring 能异步提交 read/write/fsync 等，对 file IO 更自然。

### 线上案例推演

网络服务 epoll event loop 偶发 100ms stall，如果 handler 同步读磁盘，epoll 本身没有问题；readiness 只管理 socket，blocking file IO 把整个 reactor 卡住。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“经典五种 I/O Model 是什么？readiness 与 completion 的区别是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 IO Model、AIO 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `ss -tanp`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ss -tanp` |
| 辅助 | `strace` |
| 性能/路径 | `perf top` |
| 深挖 | `cat /proc/softirqs` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：Reactor 与 Proactor 有什么区别？

**参考回答**：Reactor 等 readiness：事件到来后应用自己执行 read/write；Proactor 先提交异步操作，收到 completion 后处理结果。真实框架可能是混合模型。

### 追问 2：io_uring 为什么对文件 IO 更有意义？

**参考回答**：Regular file 的‘readable’不表示磁盘 IO 已完成，page-cache miss 仍可能阻塞；io_uring 可以真正提交 file read/write 并以 completion 通知，更贴近存储 IO。

### 追问 3：为什么信号驱动 IO 实际网络服务中不常见？

**参考回答**：Signal-driven IO 的信号处理/状态管理、可移植性和复杂度不如 epoll/kqueue/event loop 生态，生产网络服务较少把它作为主模型。

## 高频易错点（PDF 原内容）

- ❌ 把 epoll 直接称为 AIO。
- ❌ 只背五个名字，不讲两个阶段。

## 动手验证 / 抓包实验（PDF 原内容）

画出 blocking、epoll、io_uring 三种路径，标明谁等待、谁执行 copy、谁收到通知。

### 实验验收标准

能看到 readiness、EAGAIN、socket queue、softirq/CPU 等至少一层系统证据。

建议把实验结果记录成：**命令/抓包过滤器 → 观察到的字段/状态 → 与理论的对应关系 → 仍不能证明的部分**。这比只保存一张截图更接近线上排障习惯。

## 面试评分 Rubric

| 等级 | 表现 |
|---|---|
| 1/5 | 只会名词或结论，无法解释字段/状态/时序。 |
| 2/5 | 能复述主流程，但遇到异常路径或 Why 追问容易断。 |
| 3/5 | 能解释核心机制，并回答至少两个追问。 |
| 4/5 | 能说明设计取舍、边界条件，并结合 Linux/抓包证据。 |
| 5/5 | 能从业务现象反推协议/内核机制，主动指出不确定性并设计验证实验。 |

## 权威资料 / 延伸阅读

- [Linux man-pages - socket(7)](https://man7.org/linux/man-pages/man7/socket.7.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [082. Blocking Socket 与 Non-blocking Socket 的核心区别是什么？](082-blocking-vs-nonblocking-socket.md)
- [084. select、poll、epoll 的核心差异是什么？](084-select-poll-epoll.md)
- [089. Zero Copy 的目标是什么？sendfile、splice、mmap 各自大致减少了什么？](089-zero-copy-sendfile-splice-mmap.md)

## 复习卡片

- **一句话**：经典教材常分为阻塞 IO、非阻塞 IO、IO 多路复用、信号驱动 IO、异步 IO。关键是区分“等待数据就绪”和“把数据拷贝到用户缓冲”两个阶段；epoll 主要通知 readiness，而真正 completion-based 异步 IO 会在操作完成后通知。
- **必须会解释**：IO Model / AIO。
- **必须避免**：把 epoll 直接称为 AIO。
- **必须会验证**：画出 blocking、epoll、io_uring 三种路径，标明谁等待、谁执行 copy、谁收到通知。
