---
id: 58
title: "DNS 如何做负载均衡？它的局限是什么？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["DNS LB", "GSLB"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 058. DNS 如何做负载均衡？它的局限是什么？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：DNS LB / GSLB  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **DNS LB / GSLB** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> DNS 可返回多个 A/AAAA，或基于地域、网络、健康状态、权重动态返回不同地址，实现粗粒度全局流量调度。局限是 Resolver 缓存、TTL、客户端未必按预期轮询，以及 Resolver 位置并不总等于用户位置。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. DNS 适合做全局入口调度，不擅长每请求级精确负载均衡。
2. 健康切换速度受 TTL 与缓存行为影响。
3. EDNS Client Subnet 能改善地理判断，但带来隐私与缓存碎片问题。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：DNS Load Balancing 是“解析时选入口”，不是实时 per-request 调度器

### 第一性原理

- DNS 可以返回多 A/AAAA、按 resolver/EDNS Client Subnet/Geo/health 策略返回不同 endpoint，实现粗粒度全局调度。
- DNS decision 被 cache，且 recursive resolver 的位置不一定等于真实 Client，因此无法像 L4/L7 LB 那样针对每次 request 精确看当前 connection/load。
- Client 可能保留旧 DNS answer 或连接，因此 DNS failover 有天然传播延迟。

### 与 L4/L7 配合

常见架构：DNS/GSLB 先把用户引到 region/POP，再由 Anycast/L4/L7 在站点内选择具体 backend。不同层解决不同时间尺度与故障域，不是互斥方案。

### GeoDNS vs Anycast

GeoDNS 更容易显式按国家/ASN/容量做策略，但受 DNS cache；Anycast 由 routing path 选择、切换透明但控制粒度不同。大型 CDN 常组合使用。

### 线上案例推演

健康检查已经摘掉故障 IP，但仍有用户打旧地址，第一步查 answer TTL/recursive cache 与现有 keep-alive connection，而不是认为健康检查系统“没生效”。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“DNS 如何做负载均衡？它的局限是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 DNS LB、GSLB 说明关键状态、字段或数据路径。
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

### 追问 1：DNS LB 与 L4/L7 LB 如何配合？

**参考回答**：常见是 DNS/GSLB 先选择 region/POP，站点内再用 Anycast/L4/L7 选具体 backend；DNS 处理分钟/秒级入口，连接级 LB 做更实时调度。

### 追问 2：为什么健康检查正常但部分用户仍访问旧 IP？

**参考回答**：DNS answer 已被 resolver/client cache，且已有 keep-alive connection 可继续复用旧 IP，所以健康检查摘除不会瞬间让所有现有流量消失。

### 追问 3：Anycast 与 GeoDNS 如何选择？

**参考回答**：GeoDNS 便于显式地域/容量策略但受缓存；Anycast 路由透明、切换快但依赖 BGP policy。大型系统常组合而非二选一。

## 高频易错点（PDF 原内容）

- ❌ 认为返回多个 IP 就会严格平均流量。
- ❌ 忽略客户端/Resolver 缓存导致的长尾。

## 动手验证 / 抓包实验（PDF 原内容）

配置一个测试域返回两个地址，用不同 resolver 与 TTL 观察缓存、顺序和客户端选择。

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

- [020. Anycast 是什么？为什么 DNS/CDN 常用？](../02-ip-nat-routing/020-anycast-dns-cdn.md)
- [053. 输入域名后，DNS 完整解析链路是什么？](053-dns-resolution-path.md)
- [060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？](060-cdn-acceleration.md)

## 复习卡片

- **一句话**：DNS 可返回多个 A/AAAA，或基于地域、网络、健康状态、权重动态返回不同地址，实现粗粒度全局流量调度。局限是 Resolver 缓存、TTL、客户端未必按预期轮询，以及 Resolver 位置并不总等于用户位置。
- **必须会解释**：DNS LB / GSLB。
- **必须避免**：认为返回多个 IP 就会严格平均流量。
- **必须会验证**：配置一个测试域返回两个地址，用不同 resolver 与 TTL 观察缓存、顺序和客户端选择。
