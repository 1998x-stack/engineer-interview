---
id: 95
title: "大量 CLOSE_WAIT 的完整排障流程是什么？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "工程"
frequency: "★★★★★"
tags: ["CLOSE_WAIT", "Application Leak"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 095. 大量 CLOSE_WAIT 的完整排障流程是什么？

> **定位**：工程 · **面试频率**：★★★★★ · **标签**：CLOSE_WAIT / Application Leak  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **CLOSE_WAIT / Application Leak** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 先用 `ss -tanp state close-wait` 找 PID/远端与数量，确认对端已正常 FIN；再检查应用未 close 的代码路径、异常处理、HTTP body 未关闭、连接池、线程阻塞和 fd 泄漏。长期 CLOSE_WAIT 几乎总需要修业务资源生命周期。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 监控 FD 数与 CLOSE_WAIT 同步增长可强化泄漏判断。
2. 重启只能释放资源，不会修复根因。
3. Go 的 http.Response.Body、Java stream/connection、C++ RAII 都有典型坑。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
## V2 深入：CLOSE_WAIT 排障必须落到“哪个对象为什么没有 close fd”

### 第一性原理

CLOSE_WAIT 已经证明 peer FIN 到达且 kernel 完成 ACK；剩下的是 local application lifecycle。核心不是网络重传，而是资源所有权。

### 推荐流程

1. `ss -tanp state close-wait` 找 PID/remote。
2. `lsof -p`/fd count 看是否持续增长。
3. 按调用路径/endpoint 与异常率关联。
4. 抓 thread dump/goroutine/heap profile 找持有连接的对象。
5. 修复 finally/defer/RAII、body close、pool return，并加泄漏监控。

### FIN_WAIT_2 关联

对端已经主动 close并收到本端 ACK 后，可能处于 FIN_WAIT_2 等待本端 FIN；因此一端大量 CLOSE_WAIT 可能同时给 peer 制造大量 FIN_WAIT_2。

### 线上案例推演

只在 downstream 500 error 时 CLOSE_WAIT 增长，通常说明 error path 没释放 response body/socket。优先 code review异常分支，而不是网络设备。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“大量 CLOSE_WAIT 的完整排障流程是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 CLOSE_WAIT、Application Leak 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `curl -w`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `curl -w` |
| 辅助 | `ss -s` |
| 性能/路径 | `mtr` |
| 深挖 | `tcpdump -w out.pcap` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：如何用 eBPF 跟踪 socket close 生命周期？

**参考回答**：epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。 定位socket生命周期可先按PID/FD关联 `ss -p`、`/proc/<pid>/fd`，再用strace/eBPF跟踪 accept/close/shutdown 和调用栈；连接池“归还”通常只是回到用户态池，不等于内核close。

### 追问 2：连接池中“归还”与真正 close 的关系？

**参考回答**：TCP Keepalive是内核级空闲连接探测；HTTP persistent/Keep-Alive是应用层连接复用语义。连接池需要 idle/lifetime限制避免长期持有失效或已漂移的连接；HTTP/2通常减少并发连接需求但实现仍可能保留多连接做隔离/容错。

### 追问 3：对端 RST 时还会进入 CLOSE_WAIT 吗？

**参考回答**：FIN表示一个方向“不会再发送更多字节”，支持半关闭和有序收尾；RST表示异常终止/立即重置连接，通常不提供优雅 half-close 语义。shutdown(SHUT_WR)只关闭发送方向，close()则释放文件描述符并进入完整关闭流程。 CLOSE_WAIT说明本端 TCP 已收到对端 FIN，但本地应用尚未 close()；对端在相应阶段可能处于 FIN_WAIT_2。大量 CLOSE_WAIT通常先查应用资源生命周期而不是网络。

## 高频易错点（PDF 原内容）

- ❌ 调 `tcp_fin_timeout` 试图解决 CLOSE_WAIT。
- ❌ 只找网络团队，不检查应用。

## 动手验证 / 抓包实验（PDF 原内容）

结合 lsof、线程 dump、heap/resource trace 找到最早创建但未关闭的 socket 调用路径。

### 实验验收标准

能给出“现象 → 假设 → 指标/抓包 → 排除/确认 → 根因”的完整闭环。

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

- [Linux Kernel Documentation - IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [028. CLOSE_WAIT 大量堆积通常说明什么？](../03-tcp-connection-reliability/028-close-wait-leak.md)
- [081. 一个 TCP Server 从 socket() 到处理请求的系统调用流程是什么？](../09-linux-socket-io/081-tcp-server-socket-syscalls.md)
- [092. 用户说“网站突然很慢”，你如何系统化拆解而不是猜？](092-website-slow-troubleshooting.md)

## 复习卡片

- **一句话**：先用 `ss -tanp state close-wait` 找 PID/远端与数量，确认对端已正常 FIN；再检查应用未 close 的代码路径、异常处理、HTTP body 未关闭、连接池、线程阻塞和 fd 泄漏。长期 CLOSE_WAIT 几乎总需要修业务资源生命周期。
- **必须会解释**：CLOSE_WAIT / Application Leak。
- **必须避免**：调 `tcp_fin_timeout` 试图解决 CLOSE_WAIT。
- **必须会验证**：结合 lsof、线程 dump、heap/resource trace 找到最早创建但未关闭的 socket 调用路径。
