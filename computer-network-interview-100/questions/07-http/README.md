# 第七章 HTTP/1.1、HTTP/2 与应用层协议

从 HTTP 语义深入到 framing、缓存、多路复用与 RPC。

## 本章能力目标

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **HTTP Semantics 与 wire format 分离**：GET/POST/status/cache 语义跨 HTTP/1.1、2、3 共享；framing/streaming 机制不同。
- **缓存题先问 cache key/freshness/validation/shared scope**，不要把 `no-cache` 解释成“不能缓存”。
- **多路复用不等于无队头阻塞**：HTTP/2 stream 与 TCP byte stream 是两个层次。

### 本章白板题

1. 画 HTTP/1.1 message framing，解释 Content-Length/chunked 以及 CL.TE 风险。
2. 给出 GET/PUT/DELETE/POST，分别判断 safe/idempotent/cacheable 与业务重试策略。
3. 画 HTTP/2 stream/frame 与 TCP、HTTP/3 stream 与 QUIC 的对应关系。

### 最小实验组合

`curl -v/--http2/--http3`、浏览器 DevTools、`nghttp`/Wireshark HTTP2（可用时）。至少验证一次 ETag/304 和 Cache-Control revalidation。
<!-- CHAPTER-V2-END -->

## 题目目录

- [061. HTTP/1.1 Request/Response 报文结构是什么？](061-http11-message-structure.md) · 基础 · ★★★★★
- [062. GET 与 POST 真正的区别是什么？safe、idempotent、cacheable 如何区分？](062-get-vs-post-semantics.md) · 基础 · ★★★★★
- [063. 常见 HTTP 状态码中，301/302/307/308、401/403、502/504 怎么区分？](063-http-status-codes.md) · 基础 · ★★★★★
- [064. HTTP “无状态”是什么意思？Cookie、Session、Token 为什么出现？](064-http-stateless-cookie-session-token.md) · 基础 · ★★★★☆
- [065. HTTP Persistent Connection 与 TCP 长连接是什么关系？](065-http-persistent-connection.md) · 基础 · ★★★★☆
- [066. Content-Length 与 chunked transfer encoding 解决什么？](066-content-length-chunked.md) · 进阶 · ★★★★☆
- [067. Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？](067-cache-control.md) · 进阶 · ★★★★★
- [068. ETag/If-None-Match 与 Last-Modified/If-Modified-Since 如何工作？](068-etag-last-modified.md) · 进阶 · ★★★★☆
- [069. HTTP/1.1 与 HTTP/2 的核心差异是什么？](069-http11-vs-http2.md) · 进阶 · ★★★★★
- [070. HTTP/2 为什么仍存在 Head-of-Line Blocking？](070-http2-head-of-line-blocking.md) · 进阶 · ★★★★★
- [071. HPACK 与 QPACK 为什么不能完全相同？](071-hpack-vs-qpack.md) · 进阶 · ★★★☆☆
- [072. WebSocket、SSE、Long Polling 应该怎么选？](072-websocket-sse-long-polling.md) · 进阶 · ★★★★☆
- [073. gRPC 为什么常运行在 HTTP/2 上？](073-grpc-http2.md) · 进阶 · ★★★★☆

## 推荐实践工具

- `curl -v`
- `curl --http2`
- `nghttp`
- `browser DevTools Network`

[← 返回全书目录](../../README.md)
