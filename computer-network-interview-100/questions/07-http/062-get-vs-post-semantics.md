---
id: 62
title: "GET 与 POST 真正的区别是什么？safe、idempotent、cacheable 如何区分？"
chapter: "第七章 HTTP/1.1、HTTP/2 与应用层协议"
difficulty: "基础"
frequency: "★★★★★"
tags: ["HTTP Semantics"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 062. GET 与 POST 真正的区别是什么？safe、idempotent、cacheable 如何区分？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：HTTP Semantics  
> **本章**：[第七章 HTTP/1.1、HTTP/2 与应用层协议](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **HTTP Semantics** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> GET 的语义是获取资源表示，通常是 safe 且 idempotent；POST 表示让目标资源处理请求内容，通常不保证幂等。URL 参数与 body 只是常见约定，不是安全性边界。safe 指不期望改变服务器状态；idempotent 指重复执行效果与一次相同。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. PUT、DELETE 通常定义为 idempotent，但不一定 safe。
2. POST 可以被缓存，只是需要明确缓存语义，不能说“永远不能缓存”。
3. 敏感参数放 POST body 仍会被浏览器、代理、日志、服务端看到，HTTPS 才提供传输机密性。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- V2-ENRICHMENT-START -->
## V2 深入：GET/POST 的关键是 method semantics，URL/body 只是常见用法

### 第一性原理

- `safe` 表示客户端请求的语义是只读/不期望改变服务器状态；`idempotent` 表示相同请求重复执行一次或多次，对预期服务器状态的效果相同；`cacheable` 是缓存规范/响应指示决定的另一维度。
- GET 是 safe、idempotent；PUT/DELETE 语义上 idempotent 但不 safe；POST 一般不保证 idempotent。
- Method 语义影响 retry、cache、crawler、proxy 行为，因此不能只根据“GET 参数在 URL，POST 参数在 body”回答。

### 幂等不是“响应完全一样”

DELETE 第一次返回 204、第二次可能 404，但资源最终状态仍是“被删除”，所以语义可以是 idempotent。支付 POST 可通过 Idempotency-Key 把业务操作设计成可安全重试，但这是应用层额外协议，不会把 POST 标准语义改成天生幂等。

### GET Body

规范并未把“GET 绝对不能有 content”简单定义成语法错误，但其语义缺乏通用定义，许多 server/proxy/cache 不支持或忽略，因此工程上不应依赖。

### 线上案例推演

客户端 timeout 自动 retry 一个创建订单 POST，若没有幂等 key，transport uncertainty 可能变成重复订单；面试应把 HTTP method semantics 与业务 exactly-once 设计连起来。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“GET 与 POST 真正的区别是什么？safe、idempotent、cacheable 如何区分？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 HTTP Semantics 说明关键状态、字段或数据路径。
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

### 追问 1：支付接口为什么要设计幂等键？

**参考回答**：幂等描述“同一意图重复执行后的服务器效果”，不是“响应必须完全相同”。DELETE可幂等；支付类POST常通过幂等键补足应用语义。GET body在语法上并非绝对禁止，但没有广泛一致的语义与中间件兼容性，通常应避免。

### 追问 2：DELETE 重复调用为什么仍算 idempotent？

**参考回答**：幂等描述“同一意图重复执行后的服务器效果”，不是“响应必须完全相同”。DELETE可幂等；支付类POST常通过幂等键补足应用语义。GET body在语法上并非绝对禁止，但没有广泛一致的语义与中间件兼容性，通常应避免。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 3：GET 能不能有 body？

**参考回答**：幂等描述“同一意图重复执行后的服务器效果”，不是“响应必须完全相同”。DELETE可幂等；支付类POST常通过幂等键补足应用语义。GET body在语法上并非绝对禁止，但没有广泛一致的语义与中间件兼容性，通常应避免。 epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

## 高频易错点（PDF 原内容）

- ❌ “GET 长度有限、POST 无限”是错误概括。
- ❌ 把 method 名字当成权限控制。

## 动手验证 / 抓包实验（PDF 原内容）

为“创建订单”“查询订单”“更新全部字段”“部分更新”设计 HTTP method，并说明幂等策略。

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

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [061. HTTP/1.1 Request/Response 报文结构是什么？](061-http11-message-structure.md)
- [063. 常见 HTTP 状态码中，301/302/307/308、401/403、502/504 怎么区分？](063-http-status-codes.md)
- [067. Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？](067-cache-control.md)

## 复习卡片

- **一句话**：GET 的语义是获取资源表示，通常是 safe 且 idempotent；POST 表示让目标资源处理请求内容，通常不保证幂等。URL 参数与 body 只是常见约定，不是安全性边界。safe 指不期望改变服务器状态；idempotent 指重复执行效果与一次相同。
- **必须会解释**：HTTP Semantics。
- **必须避免**：“GET 长度有限、POST 无限”是错误概括。
- **必须会验证**：为“创建订单”“查询订单”“更新全部字段”“部分更新”设计 HTTP method，并说明幂等策略。
