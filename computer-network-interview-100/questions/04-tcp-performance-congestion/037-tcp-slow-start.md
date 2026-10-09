---
id: 37
title: "Slow Start 为什么叫“慢启动”，它的增长其实有多快？"
chapter: "第四章 TCP 性能、窗口与拥塞控制"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["Slow Start", "ssthresh"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 037. Slow Start 为什么叫“慢启动”，它的增长其实有多快？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：Slow Start / ssthresh  
> **本章**：[第四章 TCP 性能、窗口与拥塞控制](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Slow Start / ssthresh** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> Slow Start 是相对“直接以大窗口灌满未知网络”而言谨慎。经典上 cwnd 随 ACK 在每个 RTT 近似指数增长，直到达到 ssthresh 或检测到拥塞，再进入更温和的拥塞避免阶段。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 初始 cwnd 现代实现通常不是 1 MSS，具体遵循实现与标准演进。
2. 指数增长意味着短连接性能高度受初始窗口和 RTT 影响。
3. loss/ECN 会改变 ssthresh、cwnd，并进入相应恢复状态。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 吞吐取决于窗口、RTT、丢包、排队和拥塞算法，不能只用“带宽大”解释性能。
- 先区分 rwnd（接收端能力）和 cwnd（网络承载估计），再讨论实际 in-flight 上限。
- 拥塞控制算法的目标是动态探测路径可用容量；不同算法对 loss、RTT 与 queue 的解释不同。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Slow Start 的“慢”是相对于一开始就按未知容量全速发送

### 第一性原理

- Slow Start 从相对较小的 initial congestion window 出发，通过 ACK clock 快速增加 cwnd；理想化看每 RTT 近似指数增长。
- 其目标是在不知道 path capacity 的前提下快速探测，同时避免直接向网络注入一个巨大 burst。
- 达到 ssthresh、检测 congestion 或由现代算法的 startup detector 判断后进入更保守增长阶段。

### 为什么短请求敏感

如果 response 只有几 RTT 就结束，连接可能大部分生命周期都处于 startup，初始窗口与 RTT 对 TTFB/下载完成时间影响很大。Connection reuse/HTTP2/QUIC resumption 可以避免每个小请求重新从冷启动状态开始。

### 现代边界

CUBIC 可结合 HyStart++ 更早发现 delay increase，BBR 的 startup 又是另一种容量探测逻辑；因此面试时区分“经典 RFC 5681 slow start”与“某算法的具体 startup 实现”。

### 线上案例推演

高 RTT 用户下载很多几十 KB 对象明显慢，而大文件最终吞吐正常，可能是每个新连接 startup/handshake 成本占比过高；优先验证连接复用和 RTT，而不是只看峰值带宽。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“Slow Start 为什么叫“慢启动”，它的增长其实有多快？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Slow Start、ssthresh 说明关键状态、字段或数据路径。
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

### 追问 1：为什么短 Web 请求受 Slow Start 影响明显？

**参考回答**：短 Web 请求可能在连接还没增长到稳定 cwnd 前就结束，因此 initial cwnd、RTT 和 connection reuse 对完成时间占比很高。

### 追问 2：ssthresh 如何更新？

**参考回答**：经典算法在拥塞事件后设置/更新 ssthresh，具体计算与 congestion controller/recovery 相关；不能把一个固定数值当永恒规则。

### 追问 3：拥塞窗口为何以字节/MSS 为单位变化？

**参考回答**：cwnd 实质约束在途数据量，实现常以字节维护并结合 MSS/SMSS 调整；教材用‘几个 MSS’只是方便表达增长规模。

## 高频易错点（PDF 原内容）

- ❌ 机械背 1,2,4,8，不说明它是“每 RTT 近似翻倍”。
- ❌ 认为慢启动只在连接第一次建立时发生。

## 动手验证 / 抓包实验（PDF 原内容）

在带宽足够、RTT 可控的 netem 环境抓取新连接，观察 `ss -ti` 中 cwnd 随时间增长。

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

- [038. Fast Retransmit 与 Fast Recovery 分别是什么？](038-fast-retransmit-fast-recovery.md)
- [039. rwnd、cwnd、ssthresh 三者是什么关系？](039-rwnd-cwnd-ssthresh.md)
- [040. TCP Reno 与 CUBIC 的核心差异是什么？](040-reno-vs-cubic.md)

## 复习卡片

- **一句话**：Slow Start 是相对“直接以大窗口灌满未知网络”而言谨慎。经典上 cwnd 随 ACK 在每个 RTT 近似指数增长，直到达到 ssthresh 或检测到拥塞，再进入更温和的拥塞避免阶段。
- **必须会解释**：Slow Start / ssthresh。
- **必须避免**：机械背 1,2,4,8，不说明它是“每 RTT 近似翻倍”。
- **必须会验证**：在带宽足够、RTT 可控的 netem 环境抓取新连接，观察 `ss -ti` 中 cwnd 随时间增长。
