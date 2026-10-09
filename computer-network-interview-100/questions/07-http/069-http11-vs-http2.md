---
id: 69
title: "HTTP/1.1 与 HTTP/2 的核心差异是什么？"
chapter: "第七章 HTTP/1.1、HTTP/2 与应用层协议"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["HTTP/2", "Binary Framing"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 069. HTTP/1.1 与 HTTP/2 的核心差异是什么？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：HTTP/2 / Binary Framing  
> **本章**：[第七章 HTTP/1.1、HTTP/2 与应用层协议](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **HTTP/2 / Binary Framing** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> HTTP/2 保留 HTTP 方法、状态码和语义，但把传输表示改成二进制 frame，引入 stream、多路复用、HPACK 头压缩和流量控制，从而避免 HTTP/1.1 多连接/队列带来的大量效率问题。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 一个 HTTP/2 connection 中有多个独立 stream，frame 可交错传输。
2. Header block 通过 HPACK 压缩，减少重复 Cookie/User-Agent 等开销。
3. HTTP/2 仍通常运行在单个 TCP connection 上，因此保留 transport HOL。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- V2-ENRICHMENT-START -->
## V2 深入：HTTP/2 改的是 wire format 和并发模型，不改 HTTP 核心语义

### 第一性原理

- HTTP/2 使用 binary framing，把一个 connection 划分为多个 stream，并允许 frame interleaving；method/status/cache 等 HTTP 语义仍来自共同 HTTP Semantics。
- HPACK 压缩重复 header fields，显著降低多 request header overhead；stream-level flow control 允许 receiver 对并发 stream/connection 做 backpressure。
- HTTP/2 仍运行在 TCP 上，因此 transport reliability/order 和 congestion control 是 connection-wide TCP 提供的。

### Stream ID 与生命周期

Client/server 发起 stream 的 ID 规则、HEADERS/DATA/RST_STREAM/GOAWAY 等 frame 构成独立 stream 状态机。高级面试不必背所有 frame bit，但应知道 GOAWAY 用于 graceful shutdown/迁移未处理 stream。

### Server Push

Server Push 规范上存在，但浏览器生态实际大幅减少/禁用，原因包括缓存重复、调度复杂度与收益有限；不能把“HTTP/2 有 Server Push”当今天最重要卖点。

### 线上案例推演

HTTP/2 上一个 backend connection 承载几百 stream，单 connection reset 会同时影响很多 request；多路复用降低连接成本，也扩大单连接故障 blast radius。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“HTTP/1.1 与 HTTP/2 的核心差异是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 HTTP/2、Binary Framing 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `curl -v`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `curl -v` |
| 辅助 | `curl --http2` |
| 性能/路径 | `nghttp` |
| 深挖 | `browser DevTools Network` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：HTTP/2 Server Push 为什么实际使用减少？

**参考回答**：HTTP/2以 stream多路复用，一般客户端发起 stream使用奇数 ID、服务端 push使用偶数 ID。其 flow control是HTTP/2层的逐连接/逐流额度，与底层 TCP rwnd/cwnd 是不同层的约束。Server Push因缓存重复、复杂度和浏览器支持/收益不佳而实际使用下降。

### 追问 2：stream ID 奇偶规则是什么？

**参考回答**：HTTP/2以 stream多路复用，一般客户端发起 stream使用奇数 ID、服务端 push使用偶数 ID。其 flow control是HTTP/2层的逐连接/逐流额度，与底层 TCP rwnd/cwnd 是不同层的约束。Server Push因缓存重复、复杂度和浏览器支持/收益不佳而实际使用下降。

### 追问 3：HTTP/2 flow control 与 TCP flow control 是什么关系？

**参考回答**：HTTP/2以 stream多路复用，一般客户端发起 stream使用奇数 ID、服务端 push使用偶数 ID。其 flow control是HTTP/2层的逐连接/逐流额度，与底层 TCP rwnd/cwnd 是不同层的约束。Server Push因缓存重复、复杂度和浏览器支持/收益不佳而实际使用下降。

## 高频易错点（PDF 原内容）

- ❌ 认为 HTTP/2 改变了 GET/POST 语义。
- ❌ 说 HTTP/2 完全没有队头阻塞。

## 动手验证 / 抓包实验（PDF 原内容）

使用 `curl --http2 -v` 和浏览器 DevTools，观察同一 connection 的多 stream 请求。

### 实验验收标准

能从 HTTP method/status/header/frame 或 DevTools timing 中找到与题目语义一致的证据。

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

- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [RFC 9113 - HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [049. HTTP/2 已有多路复用，为什么 HTTP/3 仍需要 QUIC？](../05-udp-quic-http3/049-http2-vs-http3-hol.md)
- [070. HTTP/2 为什么仍存在 Head-of-Line Blocking？](070-http2-head-of-line-blocking.md)
- [073. gRPC 为什么常运行在 HTTP/2 上？](073-grpc-http2.md)

## 复习卡片

- **一句话**：HTTP/2 保留 HTTP 方法、状态码和语义，但把传输表示改成二进制 frame，引入 stream、多路复用、HPACK 头压缩和流量控制，从而避免 HTTP/1.1 多连接/队列带来的大量效率问题。
- **必须会解释**：HTTP/2 / Binary Framing。
- **必须避免**：认为 HTTP/2 改变了 GET/POST 语义。
- **必须会验证**：使用 `curl --http2 -v` 和浏览器 DevTools，观察同一 connection 的多 stream 请求。
