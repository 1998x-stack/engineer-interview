---
id: 82
title: "Blocking Socket 与 Non-blocking Socket 的核心区别是什么？"
chapter: "第九章 Socket、epoll 与 Linux 网络栈"
difficulty: "基础"
frequency: "★★★★★"
tags: ["Blocking", "EAGAIN"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 082. Blocking Socket 与 Non-blocking Socket 的核心区别是什么？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：Blocking / EAGAIN  
> **本章**：[第九章 Socket、epoll 与 Linux 网络栈](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Blocking / EAGAIN** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 阻塞 socket 在当前操作无法继续时会让调用线程睡眠等待；非阻塞 socket 会立即返回 `EAGAIN/EWOULDBLOCK`（connect 可能 EINPROGRESS），由应用稍后根据 readiness 再尝试。非阻塞本身不会自动提高性能，通常要与事件驱动架构结合。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. readiness 表示“现在尝试大概率不会阻塞”，不是数据永远够用。
2. 非阻塞 send 可能只写入部分数据，必须维护剩余 buffer。
3. 连接建立、读、写、accept 都有各自的非阻塞状态处理。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 高并发网络程序的关键是把“等待就绪”和“真正读写数据”分开，epoll 通知 readiness，而不是替应用完成 read/write。
- ET 模式的正确性依赖 nonblocking + drain-until-EAGAIN；任何阻塞系统调用都可能卡住整个 event loop。
- 性能优化必须追踪数据路径：NIC queue → softirq/NAPI → protocol stack → socket queue → userspace。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Nonblocking 改变的是 syscall“等待行为”，不改变 socket 协议语义

### 第一性原理

- Blocking `read()` 在当前无数据且连接未结束时可睡眠等待；nonblocking 则立即返回 `EAGAIN/EWOULDBLOCK`。
- EOF 是 `read()==0`，表示 peer 已 orderly close 发送方向；EAGAIN 表示“现在没有数据，但以后可能有”，两者必须严格区分。
- Nonblocking 并不让 IO 自动完成，它通常与 readiness mechanism（epoll/kqueue）配合，应用仍需显式 read/write。

### Nonblocking connect

`connect()` 可能返回 `EINPROGRESS`；之后 writable event 只表示连接尝试“完成了某种结果”，必须用 `getsockopt(SO_ERROR)` 判断成功或具体错误。

### Write readiness

大多数时间 socket send buffer 都有空间，如果永久订阅 writable event，event loop 可能被持续唤醒形成 busy loop。常见做法是只有发生 partial write/EAGAIN、确实有 pending output 时才开启 EPOLLOUT。

### 线上案例推演

事件循环 CPU 100% 而业务 QPS 很低，检查是否所有连接永久注册 EPOLLOUT；这类 bug 不是网络拥塞，而是 readiness subscription 设计错误。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“Blocking Socket 与 Non-blocking Socket 的核心区别是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Blocking、EAGAIN 说明关键状态、字段或数据路径。
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

### 追问 1：nonblocking connect 如何判断成功？

**参考回答**：证书验证要建立到本地信任锚的有效链；缺失中间证书会让不能自动补链的客户端失败。自签名证书默认不在信任库中所以报错。Certificate Transparency通过公开可审计日志提高错误/恶意签发的可发现性。

### 追问 2：为什么 write-ready 事件通常不应一直订阅？

**参考回答**：EAGAIN表示nonblocking操作当前不能继续但连接仍存在，EOF通常表现为read返回0。可写事件在大多数空闲socket上长期成立，因此应只在有待发送buffer时订阅。ET模式不能用一次FIONREAD完全替代“读到EAGAIN”，TLS层还需处理SSL内部缓冲与WANT_READ/WANT_WRITE。

### 追问 3：EAGAIN 与 EOF 如何区分？

**参考回答**：EAGAIN表示nonblocking操作当前不能继续但连接仍存在，EOF通常表现为read返回0。可写事件在大多数空闲socket上长期成立，因此应只在有待发送buffer时订阅。ET模式不能用一次FIONREAD完全替代“读到EAGAIN”，TLS层还需处理SSL内部缓冲与WANT_READ/WANT_WRITE。

## 高频易错点（PDF 原内容）

- ❌ 把 nonblocking 理解成“异步 IO”。
- ❌ 忽略 partial write。

## 动手验证 / 抓包实验（PDF 原内容）

将 socket 设置 O_NONBLOCK，故意填满 send buffer，观察 send 返回部分写/EAGAIN。

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
- [Linux man-pages - tcp(7)](https://man7.org/linux/man-pages/man7/tcp.7.html)
- [Linux Kernel Documentation - IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [081. 一个 TCP Server 从 socket() 到处理请求的系统调用流程是什么？](081-tcp-server-socket-syscalls.md)
- [085. epoll LT 与 ET 有什么区别？ET 为什么要求“读到 EAGAIN”？](085-epoll-lt-vs-et.md)
- [086. 为什么 epoll ET 几乎总与 nonblocking socket 搭配？](086-epoll-et-nonblocking.md)

## 复习卡片

- **一句话**：阻塞 socket 在当前操作无法继续时会让调用线程睡眠等待；非阻塞 socket 会立即返回 `EAGAIN/EWOULDBLOCK`（connect 可能 EINPROGRESS），由应用稍后根据 readiness 再尝试。非阻塞本身不会自动提高性能，通常要与事件驱动架构结合。
- **必须会解释**：Blocking / EAGAIN。
- **必须避免**：把 nonblocking 理解成“异步 IO”。
- **必须会验证**：将 socket 设置 O_NONBLOCK，故意填满 send buffer，观察 send 返回部分写/EAGAIN。
