---
id: 60
title: "CDN 为什么能加速？缓存命中率为什么只是其中一部分？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["CDN", "Edge", "Origin"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：CDN / Edge / Origin  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **CDN / Edge / Origin** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> CDN 通过分布式边缘节点把内容与连接终止点靠近用户，减少 RTT、跨洲链路与源站压力。除缓存命中外，还通过 Anycast/DNS 调度、TLS session reuse、HTTP/2/3、压缩、连接复用、Origin Shield 等优化动态和静态流量。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. Cache Hit 可直接从 edge 返回；Miss 仍可复用 edge→origin 长连接和优化路由。
2. Origin Shield 让多个 edge miss 汇聚到更少的上游请求，降低源站惊群。
3. 动态 API 也可能从就近 TLS termination、连接池和全局网络中获益。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：CDN 的性能收益来自“距离 + 连接 + 缓存 + 源站保护”的组合

### 第一性原理

- Edge cache 命中可以直接消除跨洲 RTT 和 origin compute，但即使 miss，CDN 仍可通过更好 peering、connection reuse、TLS termination、origin shielding 改善路径。
- Cache hit ratio 是总体平均指标；真正应看 byte hit ratio、object class、regional hit、origin offload 与 tail latency。
- CDN 调度通常结合 DNS/Anycast/POP health/capacity，不是简单“用户连地理最近机器”。

### Cache Key

Key 一般至少含 scheme/host/path，并根据 query/header/cookie/Vary 做变化。若把所有 Cookie/Query 都纳入，容易碎片化导致 hit ratio 低；若忽略真正影响内容的用户信息，又可能产生私有数据串缓存。

### Origin Shield

多 edge miss 如果都直打 origin 会形成 thundering herd；shield/层级缓存把 miss 合并到少量上游节点，降低源站连接和带宽压力。

### 线上案例推演

CDN hit ratio 90% 但 origin 仍被打爆，可能剩余 10% 是大对象/高计算动态请求，或 query/cookie 造成热门 URL 实际碎片化。需要按 cache status、bytes、key cardinality 分解，而不是只看一个百分比。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“CDN 为什么能加速？缓存命中率为什么只是其中一部分？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 CDN、Edge、Origin 说明关键状态、字段或数据路径。
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

### 追问 1：CDN Cache Key 如何设计？

**参考回答**：缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。

### 追问 2：为什么 Cookie/Query 参数会破坏命中率？

**参考回答**：缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。 Secure限制Cookie仅经安全通道发送，HttpOnly禁止脚本直接读取，SameSite限制跨站携带。Session横向扩展可用共享存储/粘性会话；JWT撤销困难是因为自包含 token在过期前不依赖中心状态，通常需短 TTL/黑名单/版本号等补偿。

### 追问 3：如何避免缓存用户私有数据？

**参考回答**：缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。

## 高频易错点（PDF 原内容）

- ❌ 把 CDN 简化成“静态文件复制”。
- ❌ 只追求 hit ratio，忽略错误 cache key 的数据泄漏风险。

## 动手验证 / 抓包实验（PDF 原内容）

对同一资源用 `curl -I` 多次请求，观察 Age、Via/X-Cache、Server-Timing 等缓存相关头。

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

- 本题以 PDF 原始题解与同章权威协议索引为主；详见 [`references/README.md`](../../references/README.md)。

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [020. Anycast 是什么？为什么 DNS/CDN 常用？](../02-ip-nat-routing/020-anycast-dns-cdn.md)
- [058. DNS 如何做负载均衡？它的局限是什么？](058-dns-load-balancing.md)
- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](../10-troubleshooting-system-design/091-url-to-page-full-path.md)

## 复习卡片

- **一句话**：CDN 通过分布式边缘节点把内容与连接终止点靠近用户，减少 RTT、跨洲链路与源站压力。除缓存命中外，还通过 Anycast/DNS 调度、TLS session reuse、HTTP/2/3、压缩、连接复用、Origin Shield 等优化动态和静态流量。
- **必须会解释**：CDN / Edge / Origin。
- **必须避免**：把 CDN 简化成“静态文件复制”。
- **必须会验证**：对同一资源用 `curl -I` 多次请求，观察 Age、Via/X-Cache、Server-Timing 等缓存相关头。
