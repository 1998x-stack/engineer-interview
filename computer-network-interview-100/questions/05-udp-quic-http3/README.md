# 第五章 UDP、QUIC 与 HTTP/3 传输基础

从“无连接数据报”到现代用户态可靠传输协议。

## 本章能力目标

- UDP 只提供数据报承载；可靠性、流控、拥塞控制、连接迁移等能力是 QUIC 自己实现的。
- HTTP/3 的关键收益不是“UDP 比 TCP 快”，而是 QUIC streams 避免 TCP 单字节流的跨流 HOL。
- QUIC 的用户态部署使协议迭代更快，但仍必须遵守互联网拥塞控制与安全约束。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **UDP 只是 datagram substrate**：QUIC 的可靠性、stream、TLS、流控、拥塞控制都在 QUIC 层实现。
- **HTTP/3 的关键不是“UDP 更快”**：真正价值是 QUIC stream 独立重组、用户态演进、Connection ID/迁移与集成 TLS。
- **没有协议能消除所有等待**：HTTP/3 仍有单 stream ordering、QPACK dependency 和 connection-wide congestion control。

### 本章白板题

1. 从零列出“可靠 UDP”必须补齐的机制，并解释为什么这会演化成完整 transport protocol。
2. 画 HTTP/2/TCP 与 HTTP/3/QUIC 的 stream→packet mapping，说明 HOL 差异。
3. 画 Wi-Fi→5G migration，标 Connection ID 与 path validation。

### 最小实验组合

`curl --http2/--http3`、Wireshark QUIC、qlog、`tc netem loss/delay`。关注 tail latency 与 stream completion，而不是只测无损 LAN 峰值。
<!-- CHAPTER-V2-END -->

## 题目目录

- [046. 如果基于 UDP 实现可靠传输，需要补哪些机制？](046-reliable-udp-design.md) · 进阶 · ★★★★☆
- [047. UDP 为什么不存在 TCP 那种“粘包”语义？](047-udp-datagram-boundaries.md) · 基础 · ★★★★☆
- [048. QUIC 为什么建立在 UDP 上，而不是直接改 TCP？](048-why-quic-over-udp.md) · 进阶 · ★★★★★
- [049. HTTP/2 已有多路复用，为什么 HTTP/3 仍需要 QUIC？](049-http2-vs-http3-hol.md) · 进阶 · ★★★★★
- [050. QUIC Connection Migration 为什么适合移动网络？](050-quic-connection-migration.md) · 进阶 · ★★★★☆
- [051. QUIC 为什么能减少首次/恢复连接延迟？0-RTT 的收益与风险是什么？](051-quic-handshake-0rtt.md) · 进阶 · ★★★★☆
- [052. QUIC 使用 UDP，是否就不需要拥塞控制和流量控制？](052-quic-flow-congestion-control.md) · 基础 · ★★★★☆

## 推荐实践工具

- `tcpdump -nn udp`
- `curl --http3`
- `qlog / QUIC trace`
- `Wireshark QUIC`

[← 返回全书目录](../../README.md)
