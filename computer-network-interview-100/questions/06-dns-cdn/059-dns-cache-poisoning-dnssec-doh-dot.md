---
id: 59
title: "DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["DNS Security"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 059. DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：DNS Security  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **DNS Security** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 缓存投毒试图把伪造 DNS 数据写入 Resolver，使域名解析到攻击者地址。DNSSEC 通过签名链验证 DNS 数据来源与完整性；DoH/DoT 主要加密客户端到 Resolver 的传输，防止链路窃听/篡改，但本身不证明上游 DNS 数据真实。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 随机 transaction ID 与源端口提升伪造响应难度。
2. DNSSEC 依赖 DS/DNSKEY/RRSIG 建立从根开始的信任链。
3. DoH 可能把 DNS 观察点集中到少数提供商，需要单独评估隐私模型。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：DNSSEC 与 DoH/DoT 的安全目标完全不同

### 第一性原理

- Cache poisoning 试图让 resolver 接受伪造 DNS data；transaction ID/source-port entropy 等提高伪造难度，DNSSEC 则提供可验证的签名链。
- DNSSEC 保护 data origin authentication 与 integrity（以及 authenticated denial），**不加密 query**。
- DoH/DoT 加密 Client↔Resolver transport，防本地链路旁观/篡改，但如果 resolver 本身恶意，它仍知道并能控制自己返回什么（除非 Client同时 DNSSEC validate）。

### Amplification

DNS UDP 可被源地址 spoof 利用：攻击者发送小 query、伪造 victim IP，使大量 resolver/authority 把更大 response 发给 victim。BCP 包括 source address validation、限制开放递归、response rate limiting 等。

### 安全边界

DoH 还改变企业可观测/策略路径，可能绕过本地 DNS control；安全讨论要区分 confidentiality、integrity、resolver trust、endpoint policy。

### 线上案例推演

公司网络 DoH 开启后传统 DNS firewall 失去可见性，不代表 DNSSEC 失效；这是“加密到外部 resolver”改变控制点，应在 endpoint/browser/resolver policy 层治理。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 DNS Security 说明关键状态、字段或数据路径。
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

### 追问 1：DoH 是否能防恶意 Resolver？

**参考回答**：DNSSEC验证 DNS数据的真实性/完整性，不加密查询内容；DoH/DoT保护客户端到 Resolver的传输通道，但不自动证明 Resolver本身可信。DNS amplification利用 UDP源地址伪造和“大响应/小请求”放大 DDoS。

### 追问 2：DNSSEC 能隐藏用户查询内容吗？

**参考回答**：DNSSEC验证 DNS数据的真实性/完整性，不加密查询内容；DoH/DoT保护客户端到 Resolver的传输通道，但不自动证明 Resolver本身可信。DNS amplification利用 UDP源地址伪造和“大响应/小请求”放大 DDoS。 SSE是基于HTTP的单向文本事件流，天然适合服务端推送和自动重连；WebSocket提供双向消息通道，L7代理必须显式支持升级/隧道。HTTP/2/3 streaming是传输能力，SSE是其上具体事件格式与语义。

### 追问 3：什么是 DNS amplification attack？

**参考回答**：DNSSEC验证 DNS数据的真实性/完整性，不加密查询内容；DoH/DoT保护客户端到 Resolver的传输通道，但不自动证明 Resolver本身可信。DNS amplification利用 UDP源地址伪造和“大响应/小请求”放大 DDoS。

## 高频易错点（PDF 原内容）

- ❌ 把 DoH 当作 DNSSEC 的替代。
- ❌ 认为 HTTPS 页面就不需要可信 DNS。

## 动手验证 / 抓包实验（PDF 原内容）

用 `dig +dnssec` 查看带 RRSIG 的记录；比较普通 DNS 与 DoH 的抓包可见性。

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

- [RFC 1034 - Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 1035 - Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [053. 输入域名后，DNS 完整解析链路是什么？](053-dns-resolution-path.md)
- [055. 为什么“DNS 使用 UDP”是错误或不完整答案？](055-dns-udp-and-tcp.md)
- [057. DNS TTL 与 Negative Caching 是什么？](057-dns-ttl-negative-cache.md)

## 复习卡片

- **一句话**：缓存投毒试图把伪造 DNS 数据写入 Resolver，使域名解析到攻击者地址。DNSSEC 通过签名链验证 DNS 数据来源与完整性；DoH/DoT 主要加密客户端到 Resolver 的传输，防止链路窃听/篡改，但本身不证明上游 DNS 数据真实。
- **必须会解释**：DNS Security。
- **必须避免**：把 DoH 当作 DNSSEC 的替代。
- **必须会验证**：用 `dig +dnssec` 查看带 RRSIG 的记录；比较普通 DNS 与 DoH 的抓包可见性。
