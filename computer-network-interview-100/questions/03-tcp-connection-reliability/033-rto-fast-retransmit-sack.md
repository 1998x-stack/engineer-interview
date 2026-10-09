---
id: 33
title: "超时重传、快速重传和 SACK 分别解决什么？"
chapter: "第三章 TCP 连接、状态机与可靠性"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["RTO", "Fast Retransmit", "SACK"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 033. 超时重传、快速重传和 SACK 分别解决什么？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：RTO / Fast Retransmit / SACK  
> **本章**：[第三章 TCP 连接、状态机与可靠性](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **RTO / Fast Retransmit / SACK** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> RTO 在 ACK 长时间缺失时兜底重传；经典快速重传利用多个重复 ACK 更早推断缺口，无需等计时器；SACK 告知发送端接收方已收到哪些离散区间，使发送端更精准补齐丢失数据。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. RTO 过小会产生虚假重传，过大则恢复慢，因此需基于 RTT 估计。
2. 重复 ACK 可能来自丢包，也可能来自乱序，所以现代实现还结合 SACK、RACK 等更复杂算法。
3. SACK 是 TCP option，需要双方能力支持。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- TCP 是有状态的可靠字节流；状态机、序号空间、ACK 语义和定时器是理解所有 TCP 题的共同底座。
- 不要把“内核收到”“对端 TCP 确认”“对端应用读到”“业务处理成功”混成一个层次。
- 排障时必须把主动关闭方、连接状态、Seq/Ack 时间线和应用生命周期放在一起看。

<!-- V2-ENRICHMENT-START -->
## V2 深入：RTO、Fast Retransmit、SACK 是不同层次的丢失恢复信号

### 第一性原理

- RTO 是“长时间没有足够进展”的 timer-based fallback，依据 SRTT/RTTVAR 估计并指数退避。
- Fast Retransmit 利用重复 ACK/SACK 等更早推断 gap，不必等 RTO。
- SACK 告诉 sender receiver 已拥有哪些非连续 byte ranges，减少一次窗口内多丢包时的盲目重传。

### 为什么“3 dupACK”不是物理定律

它是经典算法中的启发式阈值，用于在 loss 与 reordering 之间折中。现代 TCP 还可能使用 RACK 基于 packet transmission time/ACK evidence 推断 loss，不再只依赖 duplicate ACK 计数。

### Spurious Retransmission

大幅 reordering、突然 RTT spike、RTO 估计不准都可能导致 segment 实际未丢却被重传。性能分析要结合 original/retrans timestamp、DSACK/RACK 指标，而不是见 retrans 就说链路真的丢包。

### 线上案例推演

高延迟跨洲链路有少量乱序，Wireshark 标大量 Fast Retransmission，但接口 drop 很低。应进一步检查 SACK/DSACK、reordering depth 和 RACK，而不是直接要求运营商“修丢包”。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“超时重传、快速重传和 SACK 分别解决什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 RTO、Fast Retransmit、SACK 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `ss -tanpi`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ss -tanpi` |
| 辅助 | `tcpdump -nn -S` |
| 性能/路径 | `nstat -az` |
| 深挖 | `Wireshark TCP Stream Graph` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：为什么 3 duplicate ACK 不是数学真理？

**参考回答**：SACK允许接收端报告非连续已收区间，减少大窗口多丢包时的无谓重传；RACK更依赖时间/发送顺序判断丢包，避免把固定 dupACK 数当作唯一信号。Spurious retransmission则是误判丢包导致的多余重传。

### 追问 2：什么是 spurious retransmission？

**参考回答**：SACK允许接收端报告非连续已收区间，减少大窗口多丢包时的无谓重传；RACK更依赖时间/发送顺序判断丢包，避免把固定 dupACK 数当作唯一信号。Spurious retransmission则是误判丢包导致的多余重传。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 3：RACK 与经典 dupACK 有何思路差异？

**参考回答**：TCP ACK通常是累计确认：ACK=N表示 N 之前连续字节已收到。乱序时 ACK 可能停在缺口处并产生重复 ACK；SACK可额外报告已收到的非连续区间。 SACK允许接收端报告非连续已收区间，减少大窗口多丢包时的无谓重传；RACK更依赖时间/发送顺序判断丢包，避免把固定 dupACK 数当作唯一信号。Spurious retransmission则是误判丢包导致的多余重传。

## 高频易错点（PDF 原内容）

- ❌ 认为只要收到 3 个 ACK 就重传。
- ❌ 把 SACK 说成“替代累计 ACK”。

## 动手验证 / 抓包实验（PDF 原内容）

用 `tc netem loss` 在本地命名空间注入少量丢包，抓取 Dup ACK、SACK block 与 Retransmission。

### 实验验收标准

能从 TCP 状态、Seq/Ack、重传/窗口和应用 close/read/write 行为形成一致时间线。

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

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [032. TCP 可靠性由哪些机制共同保证？](032-tcp-reliability.md)
- [038. Fast Retransmit 与 Fast Recovery 分别是什么？](../04-tcp-performance-congestion/038-fast-retransmit-fast-recovery.md)
- [100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？](../10-troubleshooting-system-design/100-tcpdump-wireshark-analysis.md)

## 复习卡片

- **一句话**：RTO 在 ACK 长时间缺失时兜底重传；经典快速重传利用多个重复 ACK 更早推断缺口，无需等计时器；SACK 告知发送端接收方已收到哪些离散区间，使发送端更精准补齐丢失数据。
- **必须会解释**：RTO / Fast Retransmit / SACK。
- **必须避免**：认为只要收到 3 个 ACK 就重传。
- **必须会验证**：用 `tc netem loss` 在本地命名空间注入少量丢包，抓取 Dup ACK、SACK block 与 Retransmission。
