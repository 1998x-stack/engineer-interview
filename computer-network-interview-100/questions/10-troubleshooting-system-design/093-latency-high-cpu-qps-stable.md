---
id: 93
title: "服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "工程"
frequency: "★★★★★"
tags: ["Tail Latency", "Queueing"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 093. 服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？

> **定位**：工程 · **面试频率**：★★★★★ · **标签**：Tail Latency / Queueing  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Tail Latency / Queueing** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 应考虑 CPU 之外的等待：网络 RTT/packet loss/retransmission、DNS、连接池耗尽、锁/线程池、磁盘/DB、GC、跨 AZ 路由、NIC/softirq、下游 timeout、队列排队等。系统性能问题通常是“等待在哪里”，而非只看计算量。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 丢包很少也可能显著放大 p99，因为重传至少增加一个 RTT 或 RTO。
2. 连接池耗尽会让请求在应用入口排队，CPU 反而可能下降。
3. 路由变化可能让 RTT 突然增加但应用指标看起来正常。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
## V2 深入：CPU/QPS 不变而 latency 上升，优先想“等待时间”而不是“计算量”

### 第一性原理

Latency 可以花在 network RTT/loss/retrans、queue、lock、connection pool、DNS、downstream、storage IO 上，这些都会让 wall-clock 变长而 CPU 不一定升高。Little's Law 还能导致同 QPS 下 concurrent in-flight 增加。

### 网络假设

RTT 上升、packet loss 触发 RTO、PMTU black hole、route change、NAT/conntrack pressure、receiver zero-window 都可能表现为等待。`ss -tin` 的 rtt/retrans/cwnd/send-q 与 trace timing 能帮助区分。

### 应用等待假设

DB connection pool 等待、thread semaphore、RPC upstream timeout、GC pause、DNS resolver 卡顿也会让 CPU 空闲但请求排队。必须有 queue time/trace span，而不是只看 host CPU。

### 线上案例推演

QPS 1000 始终不变，平均 service CPU 30%，p99 从 100ms 到 5s，同时 active request 数暴涨：这是典型等待/queue 膨胀信号，下一步应找哪个 span time 增加。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Tail Latency、Queueing 说明关键状态、字段或数据路径。
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

### 追问 1：如何用 Little’s Law 理解队列堆积？

**参考回答**：TTL/Hop Limit 属于 IP 层防环机制，耗尽时通常由路由器丢包并回 ICMP Time Exceeded，而不是生成 TCP RST；RST是 TCP 端点的连接语义。 p99上升而p50稳定通常说明只影响尾部请求的排队、GC、重试、冷缓存、跨区或少量坏路径。Little's Law可用 L=λW 理解在到达率不变时等待时间上升如何对应系统中在途/排队数量增长。CDN miss storm会同时推高回源QPS、TTFB和源站队列。

### 追问 2：怎样从 retrans counter 判断网络丢包？

**参考回答**：epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 3：跨 AZ 流量为什么会引入 tail latency？

**参考回答**：p99上升而p50稳定通常说明只影响尾部请求的排队、GC、重试、冷缓存、跨区或少量坏路径。Little's Law可用 L=λW 理解在到达率不变时等待时间上升如何对应系统中在途/排队数量增长。CDN miss storm会同时推高回源QPS、TTFB和源站队列。

## 高频易错点（PDF 原内容）

- ❌ CPU 不高就排除服务器问题。
- ❌ 看到 RTT 高就直接归因公网。

## 动手验证 / 抓包实验（PDF 原内容）

对比事故前后 `ss -s` retrans、TCP RTT、连接池等待、线程池 queue、DB latency 与路由路径。

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

- 本题以 PDF 原始题解与同章权威协议索引为主；详见 [`references/README.md`](../../references/README.md)。

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [092. 用户说“网站突然很慢”，你如何系统化拆解而不是猜？](092-website-slow-troubleshooting.md)
- [097. 网络服务 CPU 很高但业务线程不忙，可能是什么？](097-network-cpu-softirq.md)
- [100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？](100-tcpdump-wireshark-analysis.md)

## 复习卡片

- **一句话**：应考虑 CPU 之外的等待：网络 RTT/packet loss/retransmission、DNS、连接池耗尽、锁/线程池、磁盘/DB、GC、跨 AZ 路由、NIC/softirq、下游 timeout、队列排队等。系统性能问题通常是“等待在哪里”，而非只看计算量。
- **必须会解释**：Tail Latency / Queueing。
- **必须避免**：CPU 不高就排除服务器问题。
- **必须会验证**：对比事故前后 `ss -s` retrans、TCP RTT、连接池等待、线程池 queue、DB latency 与路由路径。
