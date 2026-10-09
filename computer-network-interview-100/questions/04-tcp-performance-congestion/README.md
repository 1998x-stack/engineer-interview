# 第四章 TCP 性能、窗口与拥塞控制

理解吞吐为什么受到 RTT、窗口、拥塞算法和系统队列共同约束。

## 本章能力目标

- 吞吐取决于窗口、RTT、丢包、排队和拥塞算法，不能只用“带宽大”解释性能。
- 先区分 rwnd（接收端能力）和 cwnd（网络承载估计），再讨论实际 in-flight 上限。
- 拥塞控制算法的目标是动态探测路径可用容量；不同算法对 loss、RTT 与 queue 的解释不同。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **吞吐由多重上限共同决定**：application data、`rwnd`、`cwnd`、BDP、pacing、socket/qdisc/device queue 都可能限制。
- **流控保护 receiver，拥塞控制保护 network**：zero-window 与 loss/ECN/RTT growth 的信号必须分开。
- **拥塞算法是 operating-point 策略**：Reno/CUBIC/BBR 的核心区别是如何探测容量、识别拥塞、恢复发送。

### 本章白板题

1. 计算 10Gbps × 80ms 的 BDP，并解释 window 不够时为何零丢包也跑不满。
2. 在同一图上画 rwnd/cwnd/ssthresh/flight size。
3. 对比 Reno、CUBIC、BBR 的增长/减速信号与 queue 行为。

### 最小实验组合

`ss -tin`、`tc qdisc/netem`、`iperf3`、`nstat`。至少做一次高 RTT + loss 实验，观察 cwnd/retrans/throughput，而不是只背公式。
<!-- CHAPTER-V2-END -->

## 题目目录

- [036. Flow Control 与 Congestion Control 的区别是什么？](036-flow-vs-congestion-control.md) · 基础 · ★★★★★
- [037. Slow Start 为什么叫“慢启动”，它的增长其实有多快？](037-tcp-slow-start.md) · 进阶 · ★★★★☆
- [038. Fast Retransmit 与 Fast Recovery 分别是什么？](038-fast-retransmit-fast-recovery.md) · 进阶 · ★★★★☆
- [039. rwnd、cwnd、ssthresh 三者是什么关系？](039-rwnd-cwnd-ssthresh.md) · 进阶 · ★★★★★
- [040. TCP Reno 与 CUBIC 的核心差异是什么？](040-reno-vs-cubic.md) · 进阶 · ★★★★☆
- [041. BBR 与 CUBIC 的核心思想差在哪里？](041-bbr-vs-cubic.md) · 进阶 · ★★★★☆
- [042. Nagle Algorithm 解决什么？为什么交互式 RPC 常设置 TCP_NODELAY？](042-nagle-tcp-nodelay.md) · 进阶 · ★★★★☆
- [043. TCP_NODELAY 到底改变什么，不改变什么？](043-tcp-nodelay-boundaries.md) · 进阶 · ★★★☆☆
- [044. BDP 是什么？为什么高带宽长 RTT 链路需要大窗口？](044-bandwidth-delay-product.md) · 进阶 · ★★★★★
- [045. TCP 半连接队列、全连接队列与 listen(backlog) 有什么关系？](045-syn-queue-accept-queue-backlog.md) · 工程 · ★★★★★

## 推荐实践工具

- `ss -ti`
- `tc qdisc`
- `iperf3`
- `nstat -az | grep -i retrans`

[← 返回全书目录](../../README.md)
