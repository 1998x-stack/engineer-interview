---
id: 63
title: "常见 HTTP 状态码中，301/302/307/308、401/403、502/504 怎么区分？"
chapter: "第七章 HTTP/1.1、HTTP/2 与应用层协议"
difficulty: "基础"
frequency: "★★★★★"
tags: ["Status Code", "Gateway"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 063. 常见 HTTP 状态码中，301/302/307/308、401/403、502/504 怎么区分？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：Status Code / Gateway  
> **本章**：[第七章 HTTP/1.1、HTTP/2 与应用层协议](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Status Code / Gateway** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 301/308 表示永久重定向，302/307 表示临时；307/308 明确保留原 method/body。401 通常表示缺少/无效认证并可带 WWW-Authenticate，403 表示服务器理解但拒绝授权。502 是 gateway 从 upstream 得到无效响应，504 是等待 upstream 超时。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 3xx 的客户端行为历史兼容性很复杂，307/308 更适合要求 method 不变。
2. 429 通常用于速率限制，503 用于暂时不可用。
3. 应用框架返回 500 与反向代理返回 502/504 的定位层不同。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Status Code 体现“这次 HTTP 交互处在哪个故障层”

### 第一性原理

- 301/308 是永久重定向语义；302/307 是临时语义。307/308 明确保留 method/content，而历史 user-agent 对 301/302 的 POST 可能改成 GET，因此实际行为需要理解兼容历史。
- 401 表示需要/缺失有效 authentication credentials，通常伴随 `WWW-Authenticate`；403 表示服务器理解身份/请求但拒绝授权或策略不允许。
- 502 是 gateway/proxy 从 upstream 获得无效/失败 response；504 是 gateway 等 upstream 超时；408 是**当前 server 等 client request 超时**，责任方向不同。

### 代理链思维

Client → CDN → L7 LB → service → downstream。某层返回 502/504 时，必须知道谁是“gateway”，它的 upstream 是谁。502 可以来自 connection reset、protocol parse failure、TLS to upstream failure 等，并不等于 upstream 返回了一个 HTTP 500。

### 线上案例推演

用户看到 504，而 service access log 没有对应 request，问题可能发生在 LB→service 建连/排队前；若 service 收到并处理 10s 而 LB timeout 5s，则 service 最后返回 200 也无法改变客户端已经收到 504 的事实。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“常见 HTTP 状态码中，301/302/307/308、401/403、502/504 怎么区分？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Status Code、Gateway 说明关键状态、字段或数据路径。
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

### 追问 1：为什么登录失效通常是 401 而非 403？

**参考回答**：401表示请求缺少/无效的认证凭据并可触发认证挑战，403表示服务器理解身份/请求但拒绝授权。502是网关从上游得到无效/失败响应，504是等待上游超时，408是服务器等待客户端请求超时。

### 追问 2：502 可能由 connection reset 触发吗？

**参考回答**：401表示请求缺少/无效的认证凭据并可触发认证挑战，403表示服务器理解身份/请求但拒绝授权。502是网关从上游得到无效/失败响应，504是等待上游超时，408是服务器等待客户端请求超时。 证书验证要建立到本地信任锚的有效链；缺失中间证书会让不能自动补链的客户端失败。自签名证书默认不在信任库中所以报错。Certificate Transparency通过公开可审计日志提高错误/恶意签发的可发现性。

### 追问 3：504 与客户端 408 有什么不同？

**参考回答**：401表示请求缺少/无效的认证凭据并可触发认证挑战，403表示服务器理解身份/请求但拒绝授权。502是网关从上游得到无效/失败响应，504是等待上游超时，408是服务器等待客户端请求超时。

## 高频易错点（PDF 原内容）

- ❌ 把 401 解释成“未授权”而 403 “未认证”，方向常说反。
- ❌ 认为所有 5xx 都是后端应用 Bug。

## 动手验证 / 抓包实验（PDF 原内容）

构造 upstream sleep、upstream reset、认证失败三种场景，观察 Nginx/Envoy 返回的状态码和日志。

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
- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](../10-troubleshooting-system-design/091-url-to-page-full-path.md)
- [092. 用户说“网站突然很慢”，你如何系统化拆解而不是猜？](../10-troubleshooting-system-design/092-website-slow-troubleshooting.md)

## 复习卡片

- **一句话**：301/308 表示永久重定向，302/307 表示临时；307/308 明确保留原 method/body。401 通常表示缺少/无效认证并可带 WWW-Authenticate，403 表示服务器理解但拒绝授权。502 是 gateway 从 upstream 得到无效响应，504 是等待 upstream 超时。
- **必须会解释**：Status Code / Gateway。
- **必须避免**：把 401 解释成“未授权”而 403 “未认证”，方向常说反。
- **必须会验证**：构造 upstream sleep、upstream reset、认证失败三种场景，观察 Nginx/Envoy 返回的状态码和日志。
