---
id: 85
title: "epoll LT 与 ET 有什么区别？ET 为什么要求“读到 EAGAIN”？"
chapter: "第九章 Socket、epoll 与 Linux 网络栈"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["epoll", "LT", "ET"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 085. epoll LT 与 ET 有什么区别？ET 为什么要求“读到 EAGAIN”？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：epoll / LT / ET  
> **本章**：[第九章 Socket、epoll 与 Linux 网络栈](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **epoll / LT / ET** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> LT 只要 fd 仍处于可读/可写状态就会持续报告；ET 更强调状态从未就绪到就绪的边沿变化，因此处理一次 EPOLLIN 时通常要循环 read，直到返回 EAGAIN，确保把当前可读数据 drain 完，否则剩余数据可能长时间没有新的边沿提醒。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. ET 可减少重复事件但增加状态机复杂度。
2. 对写事件同理：应尽量 flush 到 EAGAIN，再根据剩余 buffer 决定是否继续订阅 EPOLLOUT。
3. 无论 LT/ET 都必须正确处理 EOF、ERR、HUP。

## 二次深化：工程上还必须知道什么

ET 的核心不是“通知次数少”，而是状态边沿语义要求应用在一次 wakeup 中尽量排空当前可读/可写状态。若没有读到 EAGAIN 就返回，后续可能没有新的 edge 帮你再次唤醒。

### 本章共同的工程视角

- 高并发网络程序的关键是把“等待就绪”和“真正读写数据”分开，epoll 通知 readiness，而不是替应用完成 read/write。
- ET 模式的正确性依赖 nonblocking + drain-until-EAGAIN；任何阻塞系统调用都可能卡住整个 event loop。
- 性能优化必须追踪数据路径：NIC queue → softirq/NAPI → protocol stack → socket queue → userspace。

<!-- V2-ENRICHMENT-START -->
## V2 深入：LT 报“状态仍为真”，ET 报“状态发生边沿变化”

### 第一性原理

- LT 下，只要 receive buffer 仍可读，后续 `epoll_wait` 仍可能继续报告 readable；遗漏一次 read 通常还有机会再次收到事件。
- ET 下，应用应在收到 edge 后循环处理到 `EAGAIN`，把当前可消费状态 drain 掉；只读一次可能留下数据却没有新的 edge，造成连接“假死”。
- ET 的正确性依赖 nonblocking + 循环 drain + 完整 partial-read/write 状态机。

### EPOLLONESHOT

多线程 worker 处理同一个 fd 时，可用 ONESHOT 防止同一 fd 同时被多个线程重复处理；handler 完成后需要 rearm。它解决的是并发事件所有权，不等于 ET 本身。

### ET 不一定更快

LT 的额外重复 wakeup 在正确 drain 的服务里也可能很少；ET 则增加状态机复杂度。选型应根据 workload、框架成熟度，而不是把 ET 当高级版必选。

### 线上案例推演

ET server 在大 response/请求 burst 下偶发永不继续读，最常见 bug 就是每次 event 只 `recv()` 一次；抓包显示数据已到本机、recv-q 非空但应用不再醒来。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“epoll LT 与 ET 有什么区别？ET 为什么要求“读到 EAGAIN”？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 epoll、LT、ET 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `ss -tanp`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `strace -e epoll_wait,read,recvfrom` |
| 辅助 | `perf trace / bpftrace` |
| 性能/路径 | `ss -tin` |
| 深挖 | `最小ET server + EAGAIN日志` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：ET 下只读一次会发生什么？

**参考回答**：epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 2：EPOLLONESHOT 解决什么？

**参考回答**：epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 3：为什么 ET 不必然更快？

**参考回答**：epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

## 高频易错点（PDF 原内容）

- ❌ 把 ET 解释成“只通知一次，永远不再通知”。
- ❌ 没有处理 partial read/write。

## 动手验证 / 抓包实验（PDF 原内容）

构造一次写入 1MB 的客户端，ET server 每次只读 1KB，观察未 drain 时事件行为，再修复为循环到 EAGAIN。

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
- [Linux man-pages - epoll(7)](https://man7.org/linux/man-pages/man7/epoll.7.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [082. Blocking Socket 与 Non-blocking Socket 的核心区别是什么？](082-blocking-vs-nonblocking-socket.md)
- [084. select、poll、epoll 的核心差异是什么？](084-select-poll-epoll.md)
- [086. 为什么 epoll ET 几乎总与 nonblocking socket 搭配？](086-epoll-et-nonblocking.md)

## 复习卡片

- **一句话**：LT 只要 fd 仍处于可读/可写状态就会持续报告；ET 更强调状态从未就绪到就绪的边沿变化，因此处理一次 EPOLLIN 时通常要循环 read，直到返回 EAGAIN，确保把当前可读数据 drain 完，否则剩余数据可能长时间没有新的边沿提醒。
- **必须会解释**：epoll / LT / ET。
- **必须避免**：把 ET 解释成“只通知一次，永远不再通知”。
- **必须会验证**：构造一次写入 1MB 的客户端，ET server 每次只读 1KB，观察未 drain 时事件行为，再修复为循环到 EAGAIN。
