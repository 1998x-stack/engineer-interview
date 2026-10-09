---
id: 22
title: "TCP 三次握手完整过程是什么？每一步同步了什么状态？"
chapter: "第三章 TCP 连接、状态机与可靠性"
difficulty: "基础"
frequency: "★★★★★"
tags: ["TCP Handshake", "ISN"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 022. TCP 三次握手完整过程是什么？每一步同步了什么状态？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：TCP Handshake / ISN  
> **本章**：[第三章 TCP 连接、状态机与可靠性](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **TCP Handshake / ISN** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 客户端发送 SYN(seq=x)，服务端返回 SYN+ACK(seq=y, ack=x+1)，客户端再 ACK(ack=y+1)。三次握手不仅确认双向路径，也同步双方初始序列号、TCP options，并让两端状态机安全进入 ESTABLISHED。

## 核心时序 / 心智模型（PDF 原内容）

```text
Client                         Server
  | ---- SYN seq=x -----------> |
  | <--- SYN,ACK seq=y -------- |
  | ---- ACK ack=y+1 ---------> |
  |       ESTABLISHED           |
```

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. SYN 本身占用一个序列号，因此 ACK 为 ISN+1。
2. SYN 中会协商 MSS、Window Scale、SACK Permitted、Timestamp 等能力。
3. 服务端收到首个 SYN 后进入 SYN-RECEIVED，客户端发完 SYN 后处于 SYN-SENT。

## 二次深化：工程上还必须知道什么

握手不是单纯“确认收发能力”，更准确地说是同步双方初始序号并建立两端 TCP 状态。面试官继续追问旧 SYN、SYN+ACK 重传、SYN Cookies 时，只有序号空间/状态机模型才能稳定回答。

### 本章共同的工程视角

- TCP 是有状态的可靠字节流；状态机、序号空间、ACK 语义和定时器是理解所有 TCP 题的共同底座。
- 不要把“内核收到”“对端 TCP 确认”“对端应用读到”“业务处理成功”混成一个层次。
- 排障时必须把主动关闭方、连接状态、Seq/Ack 时间线和应用生命周期放在一起看。

<!-- V2-ENRICHMENT-START -->
## V2 深入：三次握手真正建立的是双方的序号空间、能力与状态

### 第一性原理

- Client SYN 声明自己的 ISN 与 TCP options；Server SYN+ACK 同时确认 Client ISN 并声明自己的 ISN；第三次 ACK 证明 Client 已收到 Server 的序号空间。
- SYN 消耗一个 sequence number，因此对 SYN 的累计确认是 `ISN+1`。
- MSS、Window Scale、SACK Permitted、Timestamp 等 option 只能/主要在 SYN 阶段协商，连接建立后不能随意“重新协商”。

### 状态机级细节

Client 常经历 `CLOSED → SYN-SENT → ESTABLISHED`；Server 常经历 `LISTEN → SYN-RECEIVED → ESTABLISHED`。握手 packet 丢失不会立即失败，而由 retransmission timer 驱动重发。第三个 ACK 可以是纯 ACK，也可以与第一批 application data 同 segment 携带。

### 为什么旧 SYN 是问题

TCP 连接以四元组与序号空间区分新旧数据。如果网络中延迟的旧 SYN/segment 被误当成新连接的一部分，可能污染新状态。握手的双向确认与 ISN 机制让双方能验证“这次连接”的序号上下文。

### 线上案例推演

抓包看到 `SYN → SYN,ACK → ACK` 很快但应用 `accept()` 很慢，说明协议握手与应用 accept queue 消费是两个阶段；此时应查 accept queue/worker，而不是继续解释三次握手本身。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“TCP 三次握手完整过程是什么？每一步同步了什么状态？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 TCP Handshake、ISN 说明关键状态、字段或数据路径。
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

### 追问 1：第三次 ACK 丢失会怎样？

**参考回答**：若最后 ACK 丢失，Server 仍在 SYN-RECEIVED 并可能重传 SYN+ACK；Client 收到后会再次 ACK。若 Client 随后发送带正确 ACK 的 data，Server 也可据此完成握手。

### 追问 2：SYN 与普通数据为什么使用同一序列空间？

**参考回答**：SYN/FIN 都属于同一 TCP sequence space，使控制事件与数据顺序具有统一的可确认语义；因此 SYN 会消耗一个序号并被 ACK 为 ISN+1。

### 追问 3：TCP Fast Open 改变了什么？

**参考回答**：TCP Fast Open 在具备有效 cookie 等条件时允许 SYN 携带早期数据，减少部分建连等待；它没有取消 TCP 状态机，还要处理重放、回退和中间盒兼容。

## 高频易错点（PDF 原内容）

- ❌ 只会背 SYN/SYN-ACK/ACK，不知道 seq/ack。
- ❌ 说“三次只是为了确认双方收发能力”，没有状态同步视角。

## 动手验证 / 抓包实验（PDF 原内容）

抓取 `curl` 的 TCP 建连，逐帧标出 Flags、Seq、Ack、MSS、WS、SACK。

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

- [023. 为什么 TCP 需要三次握手，不能两次？](023-why-three-way-handshake.md)
- [024. 第三次握手 ACK 丢失后，客户端立刻带数据发送，服务端能建立连接吗？](024-third-ack-lost-with-data.md)
- [030. SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？](030-syn-flood-syn-cookies.md)

## 复习卡片

- **一句话**：客户端发送 SYN(seq=x)，服务端返回 SYN+ACK(seq=y, ack=x+1)，客户端再 ACK(ack=y+1)。三次握手不仅确认双向路径，也同步双方初始序列号、TCP options，并让两端状态机安全进入 ESTABLISHED。
- **必须会解释**：TCP Handshake / ISN。
- **必须避免**：只会背 SYN/SYN-ACK/ACK，不知道 seq/ack。
- **必须会验证**：抓取 `curl` 的 TCP 建连，逐帧标出 Flags、Seq、Ack、MSS、WS、SACK。
