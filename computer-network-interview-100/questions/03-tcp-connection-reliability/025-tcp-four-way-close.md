---
id: 25
title: "TCP 为什么通常需要四次挥手？FIN 与 ACK 的语义是什么？"
chapter: "第三章 TCP 连接、状态机与可靠性"
difficulty: "基础"
frequency: "★★★★★"
tags: ["TCP Close", "Half-close"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 025. TCP 为什么通常需要四次挥手？FIN 与 ACK 的语义是什么？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：TCP Close / Half-close  
> **本章**：[第三章 TCP 连接、状态机与可靠性](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **TCP Close / Half-close** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> TCP 是全双工连接，两个方向可独立关闭。A 的 FIN 只表示“A 不再发送更多字节”，B 仍可能继续发送数据；因此对 A 的 FIN 先 ACK，等 B 自己发送完再发 FIN，最终由 A ACK，典型上表现为四个报文。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. ACK 可以和 FIN 合并，因此抓包不一定总是严格四个物理报文。
2. 收到 FIN 后应用 read() 最终会看到 EOF，但本端仍可写，形成 half-close。
3. 主动关闭方在最后 ACK 后通常进入 TIME_WAIT。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- TCP 是有状态的可靠字节流；状态机、序号空间、ACK 语义和定时器是理解所有 TCP 题的共同底座。
- 不要把“内核收到”“对端 TCP 确认”“对端应用读到”“业务处理成功”混成一个层次。
- 排障时必须把主动关闭方、连接状态、Seq/Ack 时间线和应用生命周期放在一起看。

<!-- V2-ENRICHMENT-START -->
## V2 深入：FIN 只关闭一个发送方向，TCP 才会出现“通常四次”

### 第一性原理

- TCP 是 full-duplex，两端发送方向独立；FIN 的语义是“我之后不再发送新的字节”，不是“整个连接立刻消失”。
- 收到 FIN 的一方先 ACK 是传输层确认，它的应用仍可能有未发送完的数据，因此自己的 FIN 可以稍后再发。
- 当 ACK 与本端 FIN 恰好能合并时，抓包可能表现为三段而非严格四个 packet。

### FIN 与 RST

FIN 是有序 sequence-space 事件，允许接收方读完已排队数据后得到 EOF；RST 更接近异常终止，可能使未读/未确认数据被丢弃并让应用得到 connection reset。`shutdown(SHUT_WR)` 是显式 half-close；`close()` 还涉及 fd 生命周期与 linger 行为。

### 状态机视角

主动关闭方可能经历 `FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT`；被动关闭方常经历 `CLOSE_WAIT → LAST_ACK`。TIME_WAIT 与 CLOSE_WAIT 的根因完全不同：一个是协议正确性状态，一个常反映应用未 close。

### 线上案例推演

若抓包显示 peer FIN 后本机立即 ACK，但 socket 长时间 CLOSE_WAIT，网络已经完成对端关闭通知，问题应转向本地应用为什么没有 close，而不是怀疑 FIN 丢包。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“TCP 为什么通常需要四次挥手？FIN 与 ACK 的语义是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 TCP Close、Half-close 说明关键状态、字段或数据路径。
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

### 追问 1：为什么有时只看到三次挥手？

**参考回答**：ACK 与本端 FIN 可以合并，例如收到 peer FIN 后应用也已经没有数据要发，于是回一个 FIN+ACK，抓包就可能只看到三段。

### 追问 2：shutdown(SHUT_WR) 与 close() 有何不同？

**参考回答**：`shutdown(SHUT_WR)` 只关闭发送方向，仍可读；`close()` 释放 fd/引用并触发完整 socket 生命周期，行为还受引用计数、linger 等影响。

### 追问 3：RST 与 FIN 的关闭语义有什么不同？

**参考回答**：FIN 是有序、优雅的单方向 EOF；RST 是异常/立即重置，接收端通常得到 connection reset，不提供优雅 half-close。

## 高频易错点（PDF 原内容）

- ❌ 认为 FIN 意味着“双方连接立即消失”。
- ❌ 把 TCP 双向字节流当作一条单向通道。

## 动手验证 / 抓包实验（PDF 原内容）

写一个 socket 程序调用 `shutdown(SHUT_WR)` 后继续 recv，观察 half-close。

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

- [026. TIME_WAIT 为什么存在？为什么经常讨论 2MSL？](026-time-wait-2msl.md)
- [028. CLOSE_WAIT 大量堆积通常说明什么？](028-close-wait-leak.md)
- [029. 什么是 TCP Half-close？什么时候有用？](029-tcp-half-close.md)

## 复习卡片

- **一句话**：TCP 是全双工连接，两个方向可独立关闭。A 的 FIN 只表示“A 不再发送更多字节”，B 仍可能继续发送数据；因此对 A 的 FIN 先 ACK，等 B 自己发送完再发 FIN，最终由 A ACK，典型上表现为四个报文。
- **必须会解释**：TCP Close / Half-close。
- **必须避免**：认为 FIN 意味着“双方连接立即消失”。
- **必须会验证**：写一个 socket 程序调用 `shutdown(SHUT_WR)` 后继续 recv，观察 half-close。
