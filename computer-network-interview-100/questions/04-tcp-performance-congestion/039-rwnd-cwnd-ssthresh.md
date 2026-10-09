---
id: 39
title: "rwnd、cwnd、ssthresh 三者是什么关系？"
chapter: "第四章 TCP 性能、窗口与拥塞控制"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["窗口", "拥塞状态"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 039. rwnd、cwnd、ssthresh 三者是什么关系？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：窗口 / 拥塞状态  
> **本章**：[第四章 TCP 性能、窗口与拥塞控制](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **窗口 / 拥塞状态** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> `rwnd` 是接收端通告的接收能力；`cwnd` 是发送端根据网络拥塞状态维护的在途上限；`ssthresh` 是经典拥塞控制中 Slow Start 与 Congestion Avoidance 的切换参考。真正能飞行的数据受前两者最小值限制。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. rwnd 可受应用读取速度和 receive buffer 影响。
2. cwnd 与 RTT、ACK、loss/ECN 等网络反馈相关。
3. ssthresh 不是“网络带宽”，只是控制算法中的状态变量。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 吞吐取决于窗口、RTT、丢包、排队和拥塞算法，不能只用“带宽大”解释性能。
- 先区分 rwnd（接收端能力）和 cwnd（网络承载估计），再讨论实际 in-flight 上限。
- 拥塞控制算法的目标是动态探测路径可用容量；不同算法对 loss、RTT 与 queue 的解释不同。

<!-- V2-ENRICHMENT-START -->
## V2 深入：`rwnd/cwnd/ssthresh` 分别描述接收容量、网络容量估计和增长阶段边界

### 第一性原理

- `rwnd` 来自 peer，代表 flow-control ceiling；`cwnd` 在 sender 本地，是 congestion-control state；`ssthresh` 是经典 TCP 决定 startup/avoidance 行为的状态变量。
- 发送受 `min(rwnd,cwnd)` 近似约束，但还受 application data、pacing、TSO、qdisc、socket buffer 等限制。
- `ssthresh` 不是接收窗口，也不是“网络带宽大小”。

### 高 BDP 与 Window Scale

TCP header 原始 Window 字段只有 16 bit，若不协商 scaling，在高 BDP 路径上 rwnd ceiling 可能严重限制吞吐。Window Scale 在 SYN 中双向协商，并且每个方向的 scale factor 可以不同。

### 诊断思路

`cwnd` 大但吞吐低：检查 application-limited、rwnd、loss、pacing、CPU、send buffer；`rwnd` 大也不代表应用消费快，因为 kernel receive buffer/autotuning 可能暂时吸收数据。

### 线上案例推演

1Gbps/100ms path 的 BDP 约 12.5MB；若 effective receive window 只有几百 KB，即使零丢包和巨大 cwnd，也无法跑满链路。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“rwnd、cwnd、ssthresh 三者是什么关系？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 窗口、拥塞状态 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `ss -ti`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ss -ti` |
| 辅助 | `tc qdisc` |
| 性能/路径 | `iperf3` |
| 深挖 | `nstat -az | grep -i retrans` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：为什么高 BDP 链路需要 Window Scale？

**参考回答**：高 BDP 路径需要大 receive window；Window Scale 在 SYN 中协商把 16-bit窗口字段扩展解释到更大范围，否则 rwnd 会成为吞吐 ceiling。

### 追问 2：cwnd 很大但吞吐仍低可能是什么原因？

**参考回答**：可能 application-limited、peer rwnd 小、pacing/CPU/qdisc 限制、实际 RTT高或 loss recovery；`cwnd` 只是多个约束之一。

### 追问 3：rwnd 很大是否代表接收端应用处理很快？

**参考回答**：不代表。内核 receive buffer 可以暂时吸收大量数据，即使应用处理慢；必须结合 recv-q、应用消费率和 window 演化判断。

## 高频易错点（PDF 原内容）

- ❌ 把 ssthresh 当成第三个独立硬限制并与前两者取最小。
- ❌ 认为 cwnd 由接收端发给发送端。

## 动手验证 / 抓包实验（PDF 原内容）

`ss -ti` 查看 cwnd/rtt；结合 `/proc/sys/net/ipv4/tcp_rmem` 和 socket buffer 配置理解 rwnd 来源。

### 实验验收标准

能把吞吐/延迟变化与 RTT、cwnd/rwnd、loss、queue 之一建立可验证联系。

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

- [RFC 9293 - Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html)
- [RFC 5681 - TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [034. TCP 滑动窗口解决什么问题？发送窗口为什么不是固定大小？](../03-tcp-connection-reliability/034-tcp-sliding-window.md)
- [036. Flow Control 与 Congestion Control 的区别是什么？](036-flow-vs-congestion-control.md)
- [044. BDP 是什么？为什么高带宽长 RTT 链路需要大窗口？](044-bandwidth-delay-product.md)

## 复习卡片

- **一句话**：`rwnd` 是接收端通告的接收能力；`cwnd` 是发送端根据网络拥塞状态维护的在途上限；`ssthresh` 是经典拥塞控制中 Slow Start 与 Congestion Avoidance 的切换参考。真正能飞行的数据受前两者最小值限制。
- **必须会解释**：窗口 / 拥塞状态。
- **必须避免**：把 ssthresh 当成第三个独立硬限制并与前两者取最小。
- **必须会验证**：`ss -ti` 查看 cwnd/rtt；结合 `/proc/sys/net/ipv4/tcp_rmem` 和 socket buffer 配置理解 rwnd 来源。
