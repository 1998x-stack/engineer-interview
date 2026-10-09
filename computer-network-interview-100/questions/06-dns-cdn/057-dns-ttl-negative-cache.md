---
id: 57
title: "DNS TTL 与 Negative Caching 是什么？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["TTL", "NXDOMAIN"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 057. DNS TTL 与 Negative Caching 是什么？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：TTL / NXDOMAIN  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **TTL / NXDOMAIN** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> TTL 指定记录可被缓存的时间，降低权威 DNS 压力和查询延迟；负缓存则把 NXDOMAIN/NODATA 等“没有记录”的结果也缓存一段时间，避免持续重复查询不存在的名称。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. TTL 越长，缓存命中更高但变更收敛更慢。
2. 上线迁移常提前降低 TTL，而不是修改记录后才降低。
3. 负缓存过长会让刚创建的域名在部分用户处继续“查不到”。

## 二次深化：工程上还必须知道什么

负缓存是 DNS 一致性问题的重要一半：不存在的名字也会被缓存。上线新域名、切换记录前，如果先产生过 NXDOMAIN，客户端可能在一段时间内继续看到“仍不存在”。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：TTL 控制缓存新鲜度，Negative Caching 控制“不存在答案”的记忆

### 第一性原理

- Positive response 的 TTL 决定 resolver 可缓存该 RR 多久；TTL 较长减少 authoritative QPS/延迟，较短提升切流速度但增加解析负载。
- NXDOMAIN/NODATA 等 negative result 也需要缓存，否则不存在名字会持续打到 authority；RFC 2308 定义了相关机制。
- SERVFAIL 与 NXDOMAIN 语义不同：前者是解析失败，后者是权威意义上的名字不存在，不能简单同等长期缓存。

### 为什么 TTL=0 仍未必“瞬时一致”

终端应用、浏览器、JVM、OS、代理可能有独立缓存策略；连接池还可能继续复用旧 IP 上已经建立的 TCP connection。所以 DNS TTL 只是切流路径的一部分。

### CDN TTL 设计

GSLB/CDN 常在健康故障切换速度、resolver load、缓存命中和流量稳定性之间选 TTL；极短 TTL 也受 recursive resolver 最小缓存策略影响。

### 线上案例推演

权威 TTL 已降到 30 秒但发布后 10 分钟仍有旧流量，先分辨是 DNS answer 旧、Client DNS cache 旧，还是 HTTP keep-alive/QUIC connection 仍复用旧 endpoint。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“DNS TTL 与 Negative Caching 是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 TTL、NXDOMAIN 说明关键状态、字段或数据路径。
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

### 追问 1：为什么 TTL=0 也不一定全球立即一致？

**参考回答**：TTL/Hop Limit 属于 IP 层防环机制，耗尽时通常由路由器丢包并回 ICMP Time Exceeded，而不是生成 TCP RST；RST是 TCP 端点的连接语义。 DNS结果会经过多级缓存，因此修改不会瞬间全球一致。CNAME链增加查询/依赖层级；NXDOMAIN可按负缓存规则缓存，而 SERVFAIL通常不应被当成等价的“名字不存在”长期缓存。TTL=0也无法消除应用/代理自身缓存或在途并发。

### 追问 2：NXDOMAIN 与 SERVFAIL 能否同样缓存？

**参考回答**：DNS结果会经过多级缓存，因此修改不会瞬间全球一致。CNAME链增加查询/依赖层级；NXDOMAIN可按负缓存规则缓存，而 SERVFAIL通常不应被当成等价的“名字不存在”长期缓存。TTL=0也无法消除应用/代理自身缓存或在途并发。

### 追问 3：CDN 为什么会精细控制 DNS TTL？

**参考回答**：TTL/Hop Limit 属于 IP 层防环机制，耗尽时通常由路由器丢包并回 ICMP Time Exceeded，而不是生成 TCP RST；RST是 TCP 端点的连接语义。

## 高频易错点（PDF 原内容）

- ❌ 认为只有成功答案能缓存。
- ❌ 把 DNS TTL 与 IP 包 TTL 混淆。

## 动手验证 / 抓包实验（PDF 原内容）

先查询一个不存在的测试子域，再短时间重复查询，观察 Resolver 负缓存行为与 SOA 信息。

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
- [RFC 2308 - Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [053. 输入域名后，DNS 完整解析链路是什么？](053-dns-resolution-path.md)
- [058. DNS 如何做负载均衡？它的局限是什么？](058-dns-load-balancing.md)
- [059. DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？](059-dns-cache-poisoning-dnssec-doh-dot.md)

## 复习卡片

- **一句话**：TTL 指定记录可被缓存的时间，降低权威 DNS 压力和查询延迟；负缓存则把 NXDOMAIN/NODATA 等“没有记录”的结果也缓存一段时间，避免持续重复查询不存在的名称。
- **必须会解释**：TTL / NXDOMAIN。
- **必须避免**：认为只有成功答案能缓存。
- **必须会验证**：先查询一个不存在的测试子域，再短时间重复查询，观察 Resolver 负缓存行为与 SOA 信息。
