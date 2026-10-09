---
id: 36
title: "Flow Control 与 Congestion Control 的区别是什么？"
chapter: "第四章 TCP 性能、窗口与拥塞控制"
difficulty: "基础"
frequency: "★★★★★"
tags: ["rwnd", "cwnd"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 036. Flow Control 与 Congestion Control 的区别是什么？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：rwnd / cwnd  
> **本章**：[第四章 TCP 性能、窗口与拥塞控制](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **rwnd / cwnd** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 流量控制保护接收端，避免发送速度超过其缓冲和处理能力，主要信号是 `rwnd`；拥塞控制保护网络路径，避免在瓶颈链路制造持续排队和丢包，主要由发送端维护 `cwnd`。可发送在途量通常受 `min(rwnd, cwnd)` 约束。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 接收端通过 TCP Window 字段通告可接收空间。
2. 拥塞控制根据 ACK、loss、ECN、RTT 等信号估计网络容量。
3. 接收端再强也无法绕过网络瓶颈；网络再空也不能把接收端缓冲打爆。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 吞吐取决于窗口、RTT、丢包、排队和拥塞算法，不能只用“带宽大”解释性能。
- 先区分 rwnd（接收端能力）和 cwnd（网络承载估计），再讨论实际 in-flight 上限。
- 拥塞控制算法的目标是动态探测路径可用容量；不同算法对 loss、RTT 与 queue 的解释不同。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Flow Control 保护接收端，Congestion Control 保护共享网络

### 第一性原理

- `rwnd` 反映 receiver buffer/消费能力，防止 sender 把接收端内存淹没；这是端到端 flow control。
- `cwnd`/pacing 根据网络 congestion signal 控制 in-flight/发送速率，防止路径 queue/loss 崩溃；这是 congestion control。
- 实际发送通常受到两者更严格者约束，近似理解为 `in_flight ≤ min(rwnd, cwnd)`。

### 信号归类

Zero Window 是 flow-control 信号；loss/ECN/RTT growth 等主要用于 congestion signal。应用读取慢会减少可用 receive buffer，导致 rwnd 下降，但并不意味着网络拥塞。

### 为什么必须分开

如果混淆两者，就会对 zero-window 去调 CUBIC/BBR，或对拥塞丢包只增大 receiver buffer。排障必须同时看 `cwnd`、`rtt`、retrans 与 advertised window/send-q/recv-q。

### 线上案例推演

吞吐低时若 `cwnd` 很大、无 retrans，但 peer advertised window 极小，网络容量并不是瓶颈；应查对端应用或 receive buffer。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“Flow Control 与 Congestion Control 的区别是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 rwnd、cwnd 说明关键状态、字段或数据路径。
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

### 追问 1：Zero Window 是流控还是拥塞？

**参考回答**：Zero Window 是接收端通告没有可用 receive-buffer 空间，属于 flow control；拥塞窗口可能仍很大。

### 追问 2：ECN 属于哪一类信号？

**参考回答**：ECN 是网络拥塞显式信号，属于 congestion-control 反馈；它不表示接收端应用 buffer 满。

### 追问 3：应用读得慢会如何影响 rwnd？

**参考回答**：应用读慢会让 receive buffer 占用增加，可通告 rwnd 逐渐缩小甚至 0，从而反压 sender。

## 高频易错点（PDF 原内容）

- ❌ 把 flow control 和 congestion control 当同义词。
- ❌ 说最终窗口是 rwnd+cwnd。

## 动手验证 / 抓包实验（PDF 原内容）

用接收端故意不 read 的程序观察 Window 逐步缩小甚至 Zero Window；与注入丢包导致 cwnd 下降对比。

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
- [039. rwnd、cwnd、ssthresh 三者是什么关系？](039-rwnd-cwnd-ssthresh.md)
- [041. BBR 与 CUBIC 的核心思想差在哪里？](041-bbr-vs-cubic.md)

## 复习卡片

- **一句话**：流量控制保护接收端，避免发送速度超过其缓冲和处理能力，主要信号是 `rwnd`；拥塞控制保护网络路径，避免在瓶颈链路制造持续排队和丢包，主要由发送端维护 `cwnd`。可发送在途量通常受 `min(rwnd, cwnd)` 约束。
- **必须会解释**：rwnd / cwnd。
- **必须避免**：把 flow control 和 congestion control 当同义词。
- **必须会验证**：用接收端故意不 read 的程序观察 Window 逐步缩小甚至 Zero Window；与注入丢包导致 cwnd 下降对比。
