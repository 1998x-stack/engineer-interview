# 第三章 TCP 连接、状态机与可靠性

面试最高频核心：握手、挥手、TIME_WAIT、序号、重传与 framing。

## 本章能力目标

- TCP 是有状态的可靠字节流；状态机、序号空间、ACK 语义和定时器是理解所有 TCP 题的共同底座。
- 不要把“内核收到”“对端 TCP 确认”“对端应用读到”“业务处理成功”混成一个层次。
- 排障时必须把主动关闭方、连接状态、Seq/Ack 时间线和应用生命周期放在一起看。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **TCP 是两个方向的有序字节序号空间**：SYN/FIN、SEQ/ACK、half-close、四次挥手都从这里推导。
- **传输确认 ≠ 业务确认**：`send()`、TCP ACK、peer `read()`、业务 commit 是四个不同里程碑。
- **状态机 + 时间线是唯一稳定的答题方式**：握手/重传/TIME_WAIT/CLOSE_WAIT 都应落到状态与 packet evidence。

### 本章白板题

1. 画三次握手，标 ISN、ACK、MSS/WS/SACK options 与状态迁移。
2. 画“第三 ACK 丢失 + Client 带数据”的时间线。
3. 给出一个订单请求连接 reset 场景，解释为什么 TCP 无法提供 Exactly Once。

### 最小实验组合

`ss -tanpi`、`tcpdump -nn -S`、Wireshark Seq/Ack/SACK、`nstat -az`。实验必须能把抓包中的 Seq/Ack 与 socket 状态一一对应。
<!-- CHAPTER-V2-END -->

## 题目目录

- [021. TCP 与 UDP 的本质区别是什么？不要只说“可靠/不可靠”。](021-tcp-vs-udp.md) · 基础 · ★★★★★
- [022. TCP 三次握手完整过程是什么？每一步同步了什么状态？](022-tcp-three-way-handshake.md) · 基础 · ★★★★★
- [023. 为什么 TCP 需要三次握手，不能两次？](023-why-three-way-handshake.md) · 进阶 · ★★★★★
- [024. 第三次握手 ACK 丢失后，客户端立刻带数据发送，服务端能建立连接吗？](024-third-ack-lost-with-data.md) · 进阶 · ★★★★☆
- [025. TCP 为什么通常需要四次挥手？FIN 与 ACK 的语义是什么？](025-tcp-four-way-close.md) · 基础 · ★★★★★
- [026. TIME_WAIT 为什么存在？为什么经常讨论 2MSL？](026-time-wait-2msl.md) · 进阶 · ★★★★★
- [027. 服务器几十万个 TIME_WAIT，应该怎么分析而不是直接改内核参数？](027-time-wait-at-scale.md) · 工程 · ★★★★★
- [028. CLOSE_WAIT 大量堆积通常说明什么？](028-close-wait-leak.md) · 工程 · ★★★★★
- [029. 什么是 TCP Half-close？什么时候有用？](029-tcp-half-close.md) · 进阶 · ★★★☆☆
- [030. SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？](030-syn-flood-syn-cookies.md) · 工程 · ★★★★★
- [031. TCP Sequence Number 与 ACK Number 到底在确认什么？](031-tcp-seq-ack.md) · 基础 · ★★★★★
- [032. TCP 可靠性由哪些机制共同保证？](032-tcp-reliability.md) · 基础 · ★★★★★
- [033. 超时重传、快速重传和 SACK 分别解决什么？](033-rto-fast-retransmit-sack.md) · 进阶 · ★★★★★
- [034. TCP 滑动窗口解决什么问题？发送窗口为什么不是固定大小？](034-tcp-sliding-window.md) · 基础 · ★★★★★
- [035. 所谓 TCP “粘包/拆包”到底是什么？应用层怎样正确 framing？](035-tcp-stream-framing.md) · 基础 · ★★★★★

## 推荐实践工具

- `ss -tanpi`
- `tcpdump -nn -S`
- `nstat -az`
- `Wireshark TCP Stream Graph`

[← 返回全书目录](../../README.md)
