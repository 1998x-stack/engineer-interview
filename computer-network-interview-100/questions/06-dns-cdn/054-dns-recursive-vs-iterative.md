---
id: 54
title: "DNS 递归查询与迭代查询有什么区别？"
chapter: "第六章 DNS、全局调度与 CDN"
difficulty: "基础"
frequency: "★★★★☆"
tags: ["Recursive", "Iterative"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 054. DNS 递归查询与迭代查询有什么区别？

> **定位**：基础 · **面试频率**：★★★★☆ · **标签**：Recursive / Iterative  
> **本章**：[第六章 DNS、全局调度与 CDN](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Recursive / Iterative** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 递归查询要求被询问者给出最终答案或失败；迭代查询允许服务器返回“我不知道最终答案，但你下一步去问这里”。典型互联网 DNS 中，终端向递归 Resolver 发递归请求，Resolver 再以迭代方式查询 Root/TLD/Authoritative。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 递归 Resolver 代替客户端承担多次查询与缓存。
2. 权威服务器通常只回答自己负责区域的数据，不帮你递归整个 DNS 树。
3. 开放递归 Resolver 如果配置不当会被滥用于反射放大攻击。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Recursive 与 Iterative 的区别是“谁负责继续把问题问下去”

### 第一性原理

- Recursive query 期望被询问者返回最终答案或错误；客户端 stub 通常把递归责任交给 recursive resolver。
- Iterative resolution 中 resolver 接受 referral（例如“去问这些 .com nameserver”），自己继续向下一层查询。
- Authoritative server 对自己负责 zone 给权威答案；recursive resolver 负责缓存和替客户端遍历委派链，两种角色逻辑不同。

### Referral

Root/TLD 通常返回 NS delegation 以及必要 glue record，而不是替 Client 一路递归到最终 A/AAAA。Glue 用于解决“要找 NS 地址却又需要先解析这个 NS 名字”的依赖问题。

### 企业 Resolver

企业部署本地 recursive resolver 可做 split-horizon、内部域、DNSSEC validation、缓存、审计与策略，但也形成集中故障点，需要 redundancy/anycast/health design。

### 线上案例推演

若 `dig @authoritative name` 正常而终端 resolver 返回 SERVFAIL，应把问题放在递归链、DNSSEC validation、cache/forwarder，而不是认为权威记录一定错。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“DNS 递归查询与迭代查询有什么区别？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Recursive、Iterative 说明关键状态、字段或数据路径。
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

### 追问 1：什么是 DNS Referral？

**参考回答**：Referral 是上级 DNS server 告诉 resolver‘这个 zone 应去问哪些 NS’，通常伴随 delegation/必要 glue，而不是直接给最终目标 record。

### 追问 2：为什么企业常部署本地递归 Resolver？

**参考回答**：本地 recursive resolver 可提供缓存、内部 split DNS、DNSSEC 验证、访问策略与更低解析 RTT，也能减少每个终端直接访问外部 resolver。

### 追问 3：Authoritative 与 Recursive 能否由同一软件提供？

**参考回答**：软件可以同时实现两种角色，但运营上常分离以缩小攻击面/缓存污染风险，并明确哪些 zone 提供权威、哪些请求允许递归。

## 高频易错点（PDF 原内容）

- ❌ 把“递归/迭代”与“UDP/TCP”混为一谈。
- ❌ 认为所有 DNS 服务器都会帮客户端递归。

## 动手验证 / 抓包实验（PDF 原内容）

用 `dig +norecurse` 查看某些服务器返回的 referral/权威行为。

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
- [058. DNS 如何做负载均衡？它的局限是什么？](058-dns-load-balancing.md)

## 复习卡片

- **一句话**：递归查询要求被询问者给出最终答案或失败；迭代查询允许服务器返回“我不知道最终答案，但你下一步去问这里”。典型互联网 DNS 中，终端向递归 Resolver 发递归请求，Resolver 再以迭代方式查询 Root/TLD/Authoritative。
- **必须会解释**：Recursive / Iterative。
- **必须避免**：把“递归/迭代”与“UDP/TCP”混为一谈。
- **必须会验证**：用 `dig +norecurse` 查看某些服务器返回的 referral/权威行为。
