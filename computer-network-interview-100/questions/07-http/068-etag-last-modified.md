---
id: 68
title: "ETag/If-None-Match 与 Last-Modified/If-Modified-Since 如何工作？"
chapter: "第七章 HTTP/1.1、HTTP/2 与应用层协议"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["Conditional Request", "304"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 068. ETag/If-None-Match 与 Last-Modified/If-Modified-Since 如何工作？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：Conditional Request / 304  
> **本章**：[第七章 HTTP/1.1、HTTP/2 与应用层协议](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Conditional Request / 304** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 它们用于缓存验证：客户端持有旧 representation，发送 validator；服务器若判断资源未变化，可返回 304 不传 body。ETag 可表达更精确的版本标识，Last-Modified 基于时间且粒度/时钟可能有限。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 强 ETag 要求字节级等价；弱 ETag 表示语义等价，使用 `W/` 前缀。
2. If-None-Match 在常见 GET 缓存验证中优先于日期 validator。
3. 304 响应仍包含必要的缓存元数据更新。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Conditional Request 把“是否变化”与“重新传 body”分离

### 第一性原理

- ETag 是 server 给 representation 的 opaque validator；Client 用 `If-None-Match` 验证缓存副本，未变化可返回 304，不再传 body。
- Last-Modified/If-Modified-Since 基于时间，是较弱/粒度有限 validator；ETag 可以表达更精确版本。
- `If-Match` 是前置条件：只有当前 entity tag 匹配才执行，可用于 optimistic concurrency、防 lost update。

### Strong vs Weak Validator

ETag 可以是 strong/weak；strong validator 要求 representation byte-equivalent 等更严格语义，weak 更适合“语义等价但字节可能不同”的缓存验证。不能把 ETag 简单等于 MD5。

### 分布式坑

如果多个实例用 inode/mtime/随机值生成 ETag，同一内容在不同 server 可能 ETag 不一致，导致缓存抖动。更可靠方式是稳定 content hash、version ID 或统一生成策略。

### 线上案例推演

静态文件每次都 200 而非 304，检查 CDN 是否剥离 ETag、压缩版本是否导致不同 validator、多个 origin 是否一致；不要只看浏览器缓存开关。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“ETag/If-None-Match 与 Last-Modified/If-Modified-Since 如何工作？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Conditional Request、304 说明关键状态、字段或数据路径。
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

### 追问 1：为什么静态文件可用 hash 做 ETag？

**参考回答**：ETag是表示版本的 opaque validator；If-None-Match用于缓存验证，If-Match可用于乐观并发控制。分布式服务若各节点生成不一致 ETag，会导致无谓 miss/并发控制错误。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 2：分布式服务器生成 ETag 有什么坑？

**参考回答**：ETag是表示版本的 opaque validator；If-None-Match用于缓存验证，If-Match可用于乐观并发控制。分布式服务若各节点生成不一致 ETag，会导致无谓 miss/并发控制错误。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 3：If-Match 如何用于乐观并发控制？

**参考回答**：ETag是表示版本的 opaque validator；If-None-Match用于缓存验证，If-Match可用于乐观并发控制。分布式服务若各节点生成不一致 ETag，会导致无谓 miss/并发控制错误。

## 高频易错点（PDF 原内容）

- ❌ 认为 304 是“服务器没有响应”。
- ❌ 把 Last-Modified 当成可靠唯一版本号。

## 动手验证 / 抓包实验（PDF 原内容）

用 `curl -I` 记录 ETag，再带 `If-None-Match` 请求验证 304；修改文件后再次观察。

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
- [RFC 9111 - HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [067. Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？](067-cache-control.md)
- [060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？](../06-dns-cdn/060-cdn-acceleration.md)
- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](../10-troubleshooting-system-design/091-url-to-page-full-path.md)

## 复习卡片

- **一句话**：它们用于缓存验证：客户端持有旧 representation，发送 validator；服务器若判断资源未变化，可返回 304 不传 body。ETag 可表达更精确的版本标识，Last-Modified 基于时间且粒度/时钟可能有限。
- **必须会解释**：Conditional Request / 304。
- **必须避免**：认为 304 是“服务器没有响应”。
- **必须会验证**：用 `curl -I` 记录 ETag，再带 `If-None-Match` 请求验证 304；修改文件后再次观察。
