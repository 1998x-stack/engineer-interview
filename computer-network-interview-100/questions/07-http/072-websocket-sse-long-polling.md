---
id: 72
title: "WebSocket、SSE、Long Polling 应该怎么选？"
chapter: "第七章 HTTP/1.1、HTTP/2 与应用层协议"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["Realtime", "Streaming"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 072. WebSocket、SSE、Long Polling 应该怎么选？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：Realtime / Streaming  
> **本章**：[第七章 HTTP/1.1、HTTP/2 与应用层协议](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Realtime / Streaming** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> Long Polling 仍是一问一答，只是服务端延迟响应；SSE 在 HTTP 上提供 server→client 的文本事件流，浏览器原生支持自动重连；WebSocket 建立双向全双工消息通道。选择依据是通信方向、消息频率、代理兼容、重连和运维复杂度。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. AI token streaming 常可用 SSE，简单、可穿透普通 HTTP 基础设施。
2. 在线协作/聊天的频繁双向消息更适合 WebSocket。
3. WebSocket 建连后仍需自己设计应用消息协议、心跳、认证刷新与 backpressure。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- V2-ENRICHMENT-START -->
## V2 深入：WebSocket、SSE、Long Polling 的核心区别是通信方向、消息模型与基础设施成本

### 第一性原理

- Long Polling 仍是 request/response：Server 延迟响应，Client 收到后重新发请求，兼容性高但有重复 header/connection scheduling 开销。
- SSE 是 server→client 的事件流，基于 HTTP streaming、文本 event format，天然有 Event ID/reconnect 语义，适合通知/LLM token stream 等单向推送。
- WebSocket 建立持久双向消息通道，适合 chat/collaboration/game control，但 proxy idle timeout、backpressure、connection lifecycle 更复杂。

### HTTP/2/3 时代

SSE 可以在 HTTP/2/3 stream 上承载；“HTTP/2 有 streaming 所以 SSE 消失”错误。WebSocket 在 HTTP/2 可通过 Extended CONNECT 等机制启动，基础设施是否支持要看 proxy/gateway 实现。

### 选型问题

考虑双向性、消息频率、二进制需求、浏览器 API、断线重连、proxy/CDN 支持、连接规模、鉴权与 backpressure，而不是只按“实时程度”选。

### 线上案例推演

若仅 Server 持续推送 AI token，SSE 往往比 WebSocket 简化得多；若 Client 也高频发送协作操作，则 full-duplex WebSocket/双向 streaming RPC 更合适。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“WebSocket、SSE、Long Polling 应该怎么选？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Realtime、Streaming 说明关键状态、字段或数据路径。
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

### 追问 1：SSE 为什么通常基于 UTF-8 文本？

**参考回答**：SSE是基于HTTP的单向文本事件流，天然适合服务端推送和自动重连；WebSocket提供双向消息通道，L7代理必须显式支持升级/隧道。HTTP/2/3 streaming是传输能力，SSE是其上具体事件格式与语义。

### 追问 2：WebSocket 如何穿过 L7 proxy？

**参考回答**：SSE是基于HTTP的单向文本事件流，天然适合服务端推送和自动重连；WebSocket提供双向消息通道，L7代理必须显式支持升级/隧道。HTTP/2/3 streaming是传输能力，SSE是其上具体事件格式与语义。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 3：HTTP/2/3 streaming 与 SSE 有何关系？

**参考回答**：SSE是基于HTTP的单向文本事件流，天然适合服务端推送和自动重连；WebSocket提供双向消息通道，L7代理必须显式支持升级/隧道。HTTP/2/3 streaming是传输能力，SSE是其上具体事件格式与语义。

## 高频易错点（PDF 原内容）

- ❌ 把 SSE 说成“单向 WebSocket”。
- ❌ 认为 WebSocket 天然保证业务消息不丢。

## 动手验证 / 抓包实验（PDF 原内容）

分别实现 SSE token stream 与 WebSocket echo，对比浏览器 API、重连与代理配置。

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
- [RFC 6455 - The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [073. gRPC 为什么常运行在 HTTP/2 上？](073-grpc-http2.md)
- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](../10-troubleshooting-system-design/091-url-to-page-full-path.md)
- [099. 设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？](../10-troubleshooting-system-design/099-million-tcp-connections.md)

## 复习卡片

- **一句话**：Long Polling 仍是一问一答，只是服务端延迟响应；SSE 在 HTTP 上提供 server→client 的文本事件流，浏览器原生支持自动重连；WebSocket 建立双向全双工消息通道。选择依据是通信方向、消息频率、代理兼容、重连和运维复杂度。
- **必须会解释**：Realtime / Streaming。
- **必须避免**：把 SSE 说成“单向 WebSocket”。
- **必须会验证**：分别实现 SSE token stream 与 WebSocket echo，对比浏览器 API、重连与代理配置。
