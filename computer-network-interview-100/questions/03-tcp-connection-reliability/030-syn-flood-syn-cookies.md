---
id: 30
title: "SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？"
chapter: "第三章 TCP 连接、状态机与可靠性"
difficulty: "工程"
frequency: "★★★★★"
tags: ["SYN Flood", "SYN Cookie"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 030. SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？

> **定位**：工程 · **面试频率**：★★★★★ · **标签**：SYN Flood / SYN Cookie  
> **本章**：[第三章 TCP 连接、状态机与可靠性](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **SYN Flood / SYN Cookie** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> SYN Flood 通过大量不完成握手的 SYN 消耗半连接队列与状态资源。SYN Cookie 在压力下把部分连接状态编码进服务端生成的序列号，减少 SYN_RECV 状态存储，但它是过载防御机制，不应替代正确 backlog、容量规划和上游 DDoS 防护。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 攻击可使用伪造源地址，使服务端 SYN+ACK 发向不存在或无关主机。
2. 正常高峰也可能把 SYN queue 打满，因此要区分攻击与容量不足。
3. 边缘防护、SYN proxy、rate limit、Anycast 等可在更上游吸收攻击。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- TCP 是有状态的可靠字节流；状态机、序号空间、ACK 语义和定时器是理解所有 TCP 题的共同底座。
- 不要把“内核收到”“对端 TCP 确认”“对端应用读到”“业务处理成功”混成一个层次。
- 排障时必须把主动关闭方、连接状态、Seq/Ack 时间线和应用生命周期放在一起看。

<!-- V2-ENRICHMENT-START -->
## V2 深入：SYN Flood 攻击的是“握手前状态与资源”，SYN Cookies 是降级型防护

### 第一性原理

- 攻击者大量发送 SYN、伪造源或不完成最后 ACK，使服务端在 SYN-RECEIVED 保留大量半连接状态并重传 SYN+ACK。
- SYN queue 与 accept queue 不同：前者保存未完成握手，后者保存已完成握手、等待应用 `accept()` 的连接。
- SYN Cookies 在压力下把一部分本应保存在 server state 的信息编码进 SYN+ACK sequence，从最终 ACK 恢复/验证，从而降低半连接状态消耗。

### 为什么不是万能方案

Cookies 只针对一类 handshake state exhaustion；攻击仍可能消耗带宽、CPU、NIC、firewall/conntrack，且某些 TCP option/扩展能力在 cookie 路径下可能受限制或需要额外机制。因此正常容量不足时应扩 backlog/应用处理，而不是把 syncookies 当常态性能方案。

### 与 ACK/全连接攻击区分

ACK flood、建立完整连接后的 request flood、TLS handshake flood 都攻击不同资源层。只看 SYN_RECV 数量不够，应结合 SYN rate、SYN+ACK retrans、listen overflow、conntrack/NIC drops、CPU softirq。

### 线上案例推演

新连接失败但 SYN queue 不满、accept queue 满且 worker CPU 高，根因不是 SYN Flood；这是已完成握手后应用消费不及时，应查 accept/worker/backpressure。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 SYN Flood、SYN Cookie 说明关键状态、字段或数据路径。
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

### 追问 1：SYN queue 与 accept queue 有何不同？

**参考回答**：SYN queue 保存未完成握手的半连接；accept queue 保存已完成握手、等待应用 accept 的连接。一个受攻击不代表另一个也满。

### 追问 2：syncookies 打开后是否所有连接都使用 cookie？

**参考回答**：Linux syncookies 主要在 SYN queue pressure/overflow 等条件下作为 fallback，并非所有正常连接无条件使用；具体行为应结合内核版本和配置。

### 追问 3：SYN Flood 和 ACK Flood 有何差别？

**参考回答**：SYN Flood 打握手状态/带宽；ACK Flood 常是大量无状态/伪造 ACK 消耗 ACL/conntrack/CPU 或链路，两者 packet state 和防护点不同。

## 高频易错点（PDF 原内容）

- ❌ 把 SYN Cookie 当成“验证码”。
- ❌ 看到 SYN_RECV 多就直接认定 DDoS。

## 动手验证 / 抓包实验（PDF 原内容）

在隔离实验环境使用 hping3 低速模拟未完成握手，观察 `ss state syn-recv` 和内核 counters，避免对公网目标测试。

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

- [022. TCP 三次握手完整过程是什么？每一步同步了什么状态？](022-tcp-three-way-handshake.md)
- [045. TCP 半连接队列、全连接队列与 listen(backlog) 有什么关系？](../04-tcp-performance-congestion/045-syn-queue-accept-queue-backlog.md)
- [096. 大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？](../10-troubleshooting-system-design/096-syn-recv-troubleshooting.md)

## 复习卡片

- **一句话**：SYN Flood 通过大量不完成握手的 SYN 消耗半连接队列与状态资源。SYN Cookie 在压力下把部分连接状态编码进服务端生成的序列号，减少 SYN_RECV 状态存储，但它是过载防御机制，不应替代正确 backlog、容量规划和上游 DDoS 防护。
- **必须会解释**：SYN Flood / SYN Cookie。
- **必须避免**：把 SYN Cookie 当成“验证码”。
- **必须会验证**：在隔离实验环境使用 hping3 低速模拟未完成握手，观察 `ss state syn-recv` 和内核 counters，避免对公网目标测试。
