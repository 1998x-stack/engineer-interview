---
id: 55
title: "为什么“DNS 使用 UDP”是错误或不完整答案？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "基础"
frequency: "★★★★★"
tags: ["DNS", "UDP", "TCP"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 055. 为什么“DNS 使用 UDP”是错误或不完整答案？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：DNS / UDP / TCP  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **DNS / UDP / TCP** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> DNS 同时使用 UDP 与 TCP。普通查询常优先 UDP；当响应被截断、使用较大 DNSSEC 数据、进行 zone transfer 等场景会使用 TCP。现代 DNS 还可运行在 TLS/HTTPS/QUIC 等安全传输上。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 传统 UDP/TCP DNS 都通常使用 53 端口。
2. EDNS 扩大 UDP 可承载的 DNS 消息，但仍需考虑路径 MTU 与放大攻击。
3. DoT/DoH 改变的是传输与隐私模型，不改变 DNS 名称层次本身。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：DNS 的 transport 选择取决于场景，不是“53 端口=UDP”

### 第一性原理

- 经典 DNS query 常优先 UDP 以减少 connection overhead，但 DNS 同样定义 TCP transport。
- UDP response 若设置 TC（Truncated）bit，传统 resolver 可用 TCP 重试；AXFR/IXFR 等 zone transfer 也依赖有序可靠 transport。
- EDNS0 扩展可用 UDP payload size，但 path MTU、fragmentation 和 middlebox 使“越大越好”并不成立。

### 现代加密 DNS

DoT 在 TLS 上承载 DNS，DoH 在 HTTPS 上承载 DNS；它们保护 Client→Resolver 传输的机密性/完整性，不等于 DNSSEC。DNSSEC 验证 DNS data 的来源/完整性链，不能隐藏 query 内容。

### 工程边界

防火墙若只允许 UDP/53 而禁 TCP/53，会产生“小 DNS 正常、大/特殊查询失败”的隐蔽问题。递归 resolver 应监控 TCP fallback/TC rate/DNSSEC validation failure。

### 线上案例推演

新增大量 DNSSEC record 后部分用户解析失败，抓包发现 UDP response truncated 但 TCP/53 被防火墙丢弃；这不是权威 record 本身错误，而是 transport fallback 被阻断。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“为什么“DNS 使用 UDP”是错误或不完整答案？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 DNS、UDP、TCP 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `dig`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `dig` |
| 辅助 | `dig +trace` |
| 性能/路径 | `resolvectl statistics` |
| 深挖 | `curl -w` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：TC bit 表示什么？

**参考回答**：DNS既支持 UDP 也支持 TCP。普通查询通常先用 UDP；响应被截断（TC=1）、区域传送或某些大响应场景会使用 TCP。

### 追问 2：AXFR 为什么使用 TCP？

**参考回答**：DNS既支持 UDP 也支持 TCP。普通查询通常先用 UDP；响应被截断（TC=1）、区域传送或某些大响应场景会使用 TCP。

### 追问 3：DoH 与 DNSSEC 解决的是同一问题吗？

**参考回答**：DNSSEC验证 DNS数据的真实性/完整性，不加密查询内容；DoH/DoT保护客户端到 Resolver的传输通道，但不自动证明 Resolver本身可信。DNS amplification利用 UDP源地址伪造和“大响应/小请求”放大 DDoS。 SSE是基于HTTP的单向文本事件流，天然适合服务端推送和自动重连；WebSocket提供双向消息通道，L7代理必须显式支持升级/隧道。HTTP/2/3 streaming是传输能力，SSE是其上具体事件格式与语义。

## 高频易错点（PDF 原内容）

- ❌ 回答“DNS 永远 UDP 53”。
- ❌ 认为用了 DoH 就自动防 DNS 缓存污染。

## 动手验证 / 抓包实验（PDF 原内容）

用 `dig +tcp` 与普通 `dig` 比较；选择 DNSSEC 大响应查看 UDP size 与可能的 fallback。

### 实验验收标准

能观察 resolver/cache/authoritative 的不同角色，验证 TTL 或 DNS 响应链路。

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
- [RFC 1034 - Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 1035 - Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [053. 输入域名后，DNS 完整解析链路是什么？](053-dns-resolution-path.md)
- [057. DNS TTL 与 Negative Caching 是什么？](057-dns-ttl-negative-cache.md)
- [059. DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？](059-dns-cache-poisoning-dnssec-doh-dot.md)

## 复习卡片

- **一句话**：DNS 同时使用 UDP 与 TCP。普通查询常优先 UDP；当响应被截断、使用较大 DNSSEC 数据、进行 zone transfer 等场景会使用 TCP。现代 DNS 还可运行在 TLS/HTTPS/QUIC 等安全传输上。
- **必须会解释**：DNS / UDP / TCP。
- **必须避免**：回答“DNS 永远 UDP 53”。
- **必须会验证**：用 `dig +tcp` 与普通 `dig` 比较；选择 DNSSEC 大响应查看 UDP size 与可能的 fallback。
