---
id: 34
title: "TCP 滑动窗口解决什么问题？发送窗口为什么不是固定大小？"
chapter: "第三章 TCP 连接、状态机与可靠性"
difficulty: "基础"
frequency: "★★★★★"
tags: ["Sliding Window", "Pipeline"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 034. TCP 滑动窗口解决什么问题？发送窗口为什么不是固定大小？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：Sliding Window / Pipeline  
> **本章**：[第三章 TCP 连接、状态机与可靠性](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Sliding Window / Pipeline** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 滑动窗口允许多个未确认字节同时在途，避免 stop-and-wait 在大 RTT 链路上浪费带宽。发送窗口随 ACK 前移，并同时受接收方 `rwnd` 与拥塞控制 `cwnd` 约束，所以是动态的。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 窗口本质上限制“允许 outstanding 的序列空间”。
2. Window Scale option 让 TCP 窗口突破 16-bit 头字段的直接上限，适合大 BDP。
3. ACK 到来使左边界前移，应用新数据可进入窗口右侧。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- TCP 是有状态的可靠字节流；状态机、序号空间、ACK 语义和定时器是理解所有 TCP 题的共同底座。
- 不要把“内核收到”“对端 TCP 确认”“对端应用读到”“业务处理成功”混成一个层次。
- 排障时必须把主动关闭方、连接状态、Seq/Ack 时间线和应用生命周期放在一起看。

<!-- V2-ENRICHMENT-START -->
## V2 深入：滑动窗口把“可靠性”与“流水线并行”结合起来

### 第一性原理

- Stop-and-wait 每个 RTT 只能推进极少数据；滑动窗口允许多个未确认字节同时 in-flight，吞吐上限才可能接近 BDP。
- Sender usable window 同时受 peer advertised `rwnd` 与本地 congestion-control `cwnd` 约束，并随 ACK/应用消费/网络状态动态变化。
- Window Scale 只能在 SYN 中协商，因为双方必须从连接开始就一致解释 16-bit Window 字段的缩放因子。

### Zero Window 与 Persist

如果 receiver application 读得太慢，receive buffer 满，peer 可通告 zero window。Sender 不能继续正常推进数据，但会使用 persist/window probe 机制避免“窗口更新丢失后双方永久等待”。

### Socket buffer 与窗口

`SO_RCVBUF`/autotuning 决定接收 buffer 能力，但 advertised rwnd 还受协议实现和当前 buffer occupation 影响；“把 buffer 调大”也不等价于吞吐一定提高，cwnd/RTT/应用处理仍可能是瓶颈。

### 线上案例推演

`ss -tin` 若显示 `rcv_space`/window 小、peer zero-window，且应用线程消费慢，增加带宽无效；瓶颈在 receiver backpressure。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“TCP 滑动窗口解决什么问题？发送窗口为什么不是固定大小？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Sliding Window、Pipeline 说明关键状态、字段或数据路径。
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

### 追问 1：Window Scale 为什么必须在握手协商？

**参考回答**：Window Scale在握手时协商是因为它改变窗口字段的解释。rwnd最终受接收 socket buffer 和应用读取速度影响；零窗口时发送端停止正常数据推进，并通过窗口探测等待接收端重新开放窗口。 BDP=带宽×RTT，表示要填满路径大致需要多少在途数据。高带宽、高 RTT（例如卫星/跨洲链路）需要足够大的发送/接收窗口，否则单连接无法跑满。

### 追问 2：零窗口时连接怎么恢复？

**参考回答**：Window Scale在握手时协商是因为它改变窗口字段的解释。rwnd最终受接收 socket buffer 和应用读取速度影响；零窗口时发送端停止正常数据推进，并通过窗口探测等待接收端重新开放窗口。

### 追问 3：窗口与 socket buffer 有什么关系？

**参考回答**：Window Scale在握手时协商是因为它改变窗口字段的解释。rwnd最终受接收 socket buffer 和应用读取速度影响；零窗口时发送端停止正常数据推进，并通过窗口探测等待接收端重新开放窗口。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

## 高频易错点（PDF 原内容）

- ❌ 把滑动窗口只解释成“批量发包”。
- ❌ 认为发送窗口只由接收端决定。

## 动手验证 / 抓包实验（PDF 原内容）

在 `ss -ti` 中查看 send/receive window、cwnd，并在高 RTT netem 环境观察吞吐与窗口变化。

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

- [036. Flow Control 与 Congestion Control 的区别是什么？](../04-tcp-performance-congestion/036-flow-vs-congestion-control.md)
- [039. rwnd、cwnd、ssthresh 三者是什么关系？](../04-tcp-performance-congestion/039-rwnd-cwnd-ssthresh.md)
- [044. BDP 是什么？为什么高带宽长 RTT 链路需要大窗口？](../04-tcp-performance-congestion/044-bandwidth-delay-product.md)

## 复习卡片

- **一句话**：滑动窗口允许多个未确认字节同时在途，避免 stop-and-wait 在大 RTT 链路上浪费带宽。发送窗口随 ACK 前移，并同时受接收方 `rwnd` 与拥塞控制 `cwnd` 约束，所以是动态的。
- **必须会解释**：Sliding Window / Pipeline。
- **必须避免**：把滑动窗口只解释成“批量发包”。
- **必须会验证**：在 `ss -ti` 中查看 send/receive window、cwnd，并在高 RTT netem 环境观察吞吐与窗口变化。
