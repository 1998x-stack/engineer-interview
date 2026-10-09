---
id: 67
title: "Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？"
chapter: "第七章 HTTP/1.1、HTTP/2 与应用层协议"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["HTTP Cache"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 067. Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：HTTP Cache  
> **本章**：[第七章 HTTP/1.1、HTTP/2 与应用层协议](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **HTTP Cache** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> `max-age` 定义 freshness lifetime；`no-cache` 通常允许存储但复用前必须 revalidate；`no-store` 要求不存储；`private` 限制共享缓存存储；`must-revalidate` 要求过期后在未成功验证时不能随意使用 stale response。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 缓存分为 browser/private cache 与 CDN/shared cache。
2. 缓存策略需同时考虑 Vary、Authorization、Cookie 与 Cache Key。
3. “强缓存/协商缓存”是常见教学术语，但最好映射到 freshness 与 validation 两个标准概念。

## 二次深化：工程上还必须知道什么

no-cache 不是“完全不缓存”，而是强调复用前重新验证；no-store 才是更接近“不要存储”。回答缓存题时最好同时说 freshness lifetime 与 validator（ETag/Last-Modified）。

### 本章共同的工程视角

- 先区分 HTTP semantics 与具体版本的 message framing；GET/POST、状态码、缓存语义跨 HTTP/1.1/2/3 共享。
- HTTP/2 的多路复用发生在一个 TCP 连接内，因此仍继承 TCP 有序字节流造成的 transport HOL。
- 缓存题要同时区分 freshness、validation、storage policy，不要把 no-cache 与 no-store 混淆。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Cache-Control 要分“能否存”“何时算新鲜”“过期后是否可复用”

### 第一性原理

- `max-age` 控制 freshness lifetime；`no-cache` 通常允许存储但 reuse 前必须 revalidate；`no-store` 要求不要存储；`private` 限制 shared cache 复用；`must-revalidate` 收紧 stale response 使用。
- Shared cache 还可使用 `s-maxage` 覆盖共享缓存的新鲜度策略，而 private browser cache 不按同样方式解释。
- `Vary` 参与 cache key 选择，告诉 cache 哪些 request fields 会改变 response representation。

### Stale 策略

`stale-while-revalidate` 允许在后台更新时暂时服务 stale，减少用户 tail latency；`stale-if-error` 类策略在 origin 故障时提升可用性。是否可用要看具体规范/实现和业务一致性要求。

### Cookie/授权边界

带 Authorization/Cookie 的 response 是否可共享缓存必须非常谨慎；错误 cache key 或错误 `public/private` 可能造成严重用户数据泄漏。

### 线上案例推演

部署后发现 CDN hit ratio 极低，检查 `Vary`、Set-Cookie、Cache-Control、query normalization；如果 `no-cache` 被团队误写成“绝对不能缓存”，就会错误理解实际 revalidation 流量。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 HTTP Cache 说明关键状态、字段或数据路径。
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

### 追问 1：s-maxage 与 max-age 有何区别？

**参考回答**：缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。

### 追问 2：stale-while-revalidate 为什么能降尾延迟？

**参考回答**：缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。

### 追问 3：Vary: Accept-Encoding 如何影响缓存键？

**参考回答**：缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。

## 高频易错点（PDF 原内容）

- ❌ 把 no-cache 解释成绝对不缓存。
- ❌ 忽略 private data 被共享 CDN 缓存的安全风险。

## 动手验证 / 抓包实验（PDF 原内容）

对静态资源设置不同 Cache-Control，用浏览器 DevTools 观察 memory/disk cache、304 与网络请求。

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

- [068. ETag/If-None-Match 与 Last-Modified/If-Modified-Since 如何工作？](068-etag-last-modified.md)
- [060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？](../06-dns-cdn/060-cdn-acceleration.md)
- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](../10-troubleshooting-system-design/091-url-to-page-full-path.md)

## 复习卡片

- **一句话**：`max-age` 定义 freshness lifetime；`no-cache` 通常允许存储但复用前必须 revalidate；`no-store` 要求不存储；`private` 限制共享缓存存储；`must-revalidate` 要求过期后在未成功验证时不能随意使用 stale response。
- **必须会解释**：HTTP Cache。
- **必须避免**：把 no-cache 解释成绝对不缓存。
- **必须会验证**：对静态资源设置不同 Cache-Control，用浏览器 DevTools 观察 memory/disk cache、304 与网络请求。
