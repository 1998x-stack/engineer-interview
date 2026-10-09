---
id: 38
title: "Fast Retransmit 与 Fast Recovery 分别是什么？"
chapter: "第四章 TCP 性能、窗口与拥塞控制"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["Reno", "Loss Recovery"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 038. Fast Retransmit 与 Fast Recovery 分别是什么？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：Reno / Loss Recovery  
> **本章**：[第四章 TCP 性能、窗口与拥塞控制](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Reno / Loss Recovery** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> Fast Retransmit 通过重复 ACK 等信号在 RTO 到期前重传疑似丢失段；Fast Recovery 则是在确认网络仍有数据流动后，避免像超时那样把发送速率降到极低，尽快恢复拥塞窗口。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. Reno 时代的经典规则是 3 duplicate ACK 触发快速重传。
2. 超时通常代表更严重的拥塞/ACK 时钟中断，因此窗口缩减更激进。
3. 现代 Linux 的 recovery 还会结合 SACK、PRR、RACK 等机制。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 吞吐取决于窗口、RTT、丢包、排队和拥塞算法，不能只用“带宽大”解释性能。
- 先区分 rwnd（接收端能力）和 cwnd（网络承载估计），再讨论实际 in-flight 上限。
- 拥塞控制算法的目标是动态探测路径可用容量；不同算法对 loss、RTT 与 queue 的解释不同。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Fast Retransmit 负责“发现并重传”，Fast Recovery 负责“如何继续发”

### 第一性原理

- Duplicate ACK 表明 receiver 仍在收到后续数据，却缺前面的 gap，因此 sender 可以在 RTO 前推断 loss 并重传。
- Fast Recovery 的目标是在单个/少量 loss 后不要完全把管道清空，而是根据 ACK 继续估计网络中仍有多少数据在飞。
- Reno/NewReno/PRR 等对 loss recovery 中 cwnd/发送额度的计算不同，不能把所有现代 TCP 都说成同一个“3 dupACK 后 cwnd/2”公式。

### NewReno 与多丢包

Reno 在一个 window 多 packet loss 时恢复效率差；NewReno 借 partial ACK 改进，而 SACK/现代 recovery 能更明确知道多个 hole。PRR 进一步控制 recovery 期间发多少新数据，使发送更贴近目标 ssthresh。

### 线上案例推演

抓包中大量 duplicate ACK 后快速重传，但 connection 没有明显停顿，说明 fast recovery 在工作；若频繁触发 RTO 则影响通常更重，应继续查严重 loss、ACK path 或 RTT variance。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“Fast Retransmit 与 Fast Recovery 分别是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Reno、Loss Recovery 说明关键状态、字段或数据路径。
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

### 追问 1：为什么 dupACK 表明网络可能仍能传包？

**参考回答**：TCP ACK通常是累计确认：ACK=N表示 N 之前连续字节已收到。乱序时 ACK 可能停在缺口处并产生重复 ACK；SACK可额外报告已收到的非连续区间。

### 追问 2：PRR 解决了什么？

**参考回答**：Fast Retransmit在较强丢包迹象出现时不等 RTO就重传；Fast Recovery/PRR控制恢复阶段允许发送的数据量。NewReno改进了一个窗口内多丢包时的恢复行为。

### 追问 3：NewReno 与 Reno 在多丢包恢复上有什么差别？

**参考回答**：Fast Retransmit在较强丢包迹象出现时不等 RTO就重传；Fast Recovery/PRR控制恢复阶段允许发送的数据量。NewReno改进了一个窗口内多丢包时的恢复行为。 Reno拥塞避免近似按 RTT线性增长，CUBIC以立方函数随距上次拥塞点的时间调节窗口，更适合高 BDP 链路，同时保留 Reno-friendly 兼容区域。

## 高频易错点（PDF 原内容）

- ❌ 把 Fast Retransmit 和 Fast Recovery 合并成一个概念。
- ❌ 认为快速恢复“不降低 cwnd”。

## 动手验证 / 抓包实验（PDF 原内容）

注入单包丢失与持续丢失，比较是否进入 fast retransmit 以及何时落到 RTO。

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

- [033. 超时重传、快速重传和 SACK 分别解决什么？](../03-tcp-connection-reliability/033-rto-fast-retransmit-sack.md)
- [037. Slow Start 为什么叫“慢启动”，它的增长其实有多快？](037-tcp-slow-start.md)
- [040. TCP Reno 与 CUBIC 的核心差异是什么？](040-reno-vs-cubic.md)

## 复习卡片

- **一句话**：Fast Retransmit 通过重复 ACK 等信号在 RTO 到期前重传疑似丢失段；Fast Recovery 则是在确认网络仍有数据流动后，避免像超时那样把发送速率降到极低，尽快恢复拥塞窗口。
- **必须会解释**：Reno / Loss Recovery。
- **必须避免**：把 Fast Retransmit 和 Fast Recovery 合并成一个概念。
- **必须会验证**：注入单包丢失与持续丢失，比较是否进入 fast retransmit 以及何时落到 RTO。
