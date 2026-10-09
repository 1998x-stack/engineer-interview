---
id: 53
title: "输入域名后，DNS 完整解析链路是什么？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "基础"
frequency: "★★★★★"
tags: ["DNS", "Resolver", "Cache"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 053. 输入域名后，DNS 完整解析链路是什么？

> **定位**：基础 · **面试频率**：★★★★★ · **标签**：DNS / Resolver / Cache  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **DNS / Resolver / Cache** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 应用先检查浏览器/系统等本地缓存与 hosts，随后通常把查询交给递归 Resolver。若缓存未命中，Resolver 按 Root→TLD→Authoritative 的委派链获取最终记录并按 TTL 缓存。真实链路还可能包含 CNAME、多级 DNS、DoH/DoT 与负载调度。

## 核心时序 / 心智模型（PDF 原内容）

```text
Client
  ↓
Recursive Resolver
  ↓
Root → TLD → Authoritative
  ↓
Answer + TTL
  ↓
Cache
```

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. Root 不会返回所有域名 IP，而是告诉 Resolver 去问相应 TLD。
2. TLD 再返回目标域的权威服务器信息。
3. Resolver 的缓存使绝大多数查询无需每次走完整根链路。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：DNS 解析是一条多级缓存 + 委派链，不是每次都从 Root 开始

### 第一性原理

典型客户端把问题交给 recursive resolver；resolver 若无缓存，依据 Root → TLD → authoritative referral 逐步找到权威答案。浏览器、OS、local stub、递归 resolver、应用自身都可能缓存，因此真实请求常在前几层就命中。

### CNAME 与额外查询

若名字返回 CNAME，resolver 还需解析 canonical target；长 CNAME chain 增加 lookup latency、失败点与 DNS packet size，也影响 CDN/证书/运营管理。最终 A/AAAA 还会进入连接 Happy Eyeballs 等后续过程。

### TTL 与真实一致性

TTL 是 DNS cache 的协议性过期上限/指导，但本地实现可能有最小/最大 TTL、prefetch、serve-stale、application cache 等策略，因此“权威改完 TTL 秒后全球必然完全一致”过于绝对。

### 线上案例推演

域名切流后只有部分 ISP 用户仍命中旧 IP，应按 resolver/ASN 收集实际 answer 与 TTL，确认是不是 recursive cache，而不是只在权威 DNS 控制台反复查看新记录。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“输入域名后，DNS 完整解析链路是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 DNS、Resolver、Cache 说明关键状态、字段或数据路径。
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

### 追问 1：CNAME 链过长会造成什么？

**参考回答**：DNS结果会经过多级缓存，因此修改不会瞬间全球一致。CNAME链增加查询/依赖层级；NXDOMAIN可按负缓存规则缓存，而 SERVFAIL通常不应被当成等价的“名字不存在”长期缓存。TTL=0也无法消除应用/代理自身缓存或在途并发。

### 追问 2：为什么 DNS 修改不是瞬间生效？

**参考回答**：DNS结果会经过多级缓存，因此修改不会瞬间全球一致。CNAME链增加查询/依赖层级；NXDOMAIN可按负缓存规则缓存，而 SERVFAIL通常不应被当成等价的“名字不存在”长期缓存。TTL=0也无法消除应用/代理自身缓存或在途并发。

### 追问 3：浏览器和 OS 的缓存策略是否完全遵循同一个 TTL？

**参考回答**：TTL/Hop Limit 属于 IP 层防环机制，耗尽时通常由路由器丢包并回 ICMP Time Exceeded，而不是生成 TCP RST；RST是 TCP 端点的连接语义。

## 高频易错点（PDF 原内容）

- ❌ 说浏览器直接依次请求 Root/TLD。
- ❌ 忽略递归 Resolver 缓存。

## 动手验证 / 抓包实验（PDF 原内容）

使用 `dig +trace` 观察委派链，再用普通 `dig` 对比递归 Resolver 的结果与 TTL。

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

- [054. DNS 递归查询与迭代查询有什么区别？](054-dns-recursive-vs-iterative.md)
- [055. 为什么“DNS 使用 UDP”是错误或不完整答案？](055-dns-udp-and-tcp.md)
- [057. DNS TTL 与 Negative Caching 是什么？](057-dns-ttl-negative-cache.md)

## 复习卡片

- **一句话**：应用先检查浏览器/系统等本地缓存与 hosts，随后通常把查询交给递归 Resolver。若缓存未命中，Resolver 按 Root→TLD→Authoritative 的委派链获取最终记录并按 TTL 缓存。真实链路还可能包含 CNAME、多级 DNS、DoH/DoT 与负载调度。
- **必须会解释**：DNS / Resolver / Cache。
- **必须避免**：说浏览器直接依次请求 Root/TLD。
- **必须会验证**：使用 `dig +trace` 观察委派链，再用普通 `dig` 对比递归 Resolver 的结果与 TTL。
