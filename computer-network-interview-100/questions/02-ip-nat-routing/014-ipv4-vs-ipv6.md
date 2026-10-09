---
id: 14
title: "IPv4 与 IPv6 除了地址长度，还有哪些关键差异？"
chapter: "第二章 IP、NAT 与路由"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["IPv6", "NDP", "Header"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 014. IPv4 与 IPv6 除了地址长度，还有哪些关键差异？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：IPv6 / NDP / Header  
> **本章**：[第二章 IP、NAT 与路由](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **IPv6 / NDP / Header** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> IPv6 使用 128 位地址、固定基础头、扩展头体系、NDP 替代 ARP，并取消路由器中途分片；多播承担许多 IPv4 广播场景。其目标不只是“地址更多”，还包括更简洁的转发与更好的协议扩展性。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. IPv6 基础头没有 IPv4 header checksum，减少逐跳处理。
2. Fragment Extension Header 由源端添加，路由器不会替源主机分片。
3. NDP 基于 ICMPv6 完成邻居解析、路由器发现、地址自动配置等。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 把控制平面和转发平面分开：路由协议决定“学到什么路由”，FIB 决定“某个包下一跳去哪”。
- 任何 NAT/路由问题都先写出五元组、路由表命中项和下一跳，避免靠口头直觉猜。
- 公网故障常有非对称路径、ECMP、NAT/conntrack 和 ICMP 策略，单点抓包不能自动代表端到端事实。

<!-- V2-ENRICHMENT-START -->
## V2 深入：IPv6 是地址、邻居发现、分片与自动配置模型的系统性变化

### 第一性原理

- IPv6 使用 128-bit 地址，并简化基础 header；Router 不再执行中途 fragmentation，源节点负责适应 Path MTU。
- IPv6 没有 IPv4 ARP，使用 ICMPv6 Neighbor Discovery；也没有传统 L2 “IPv4 broadcast”语义，更多使用 multicast。
- 地址配置可以通过 SLAAC、DHCPv6 或组合方式完成，网络不必依赖 NAT 才能扩展地址空间。

### 双栈现实

现代网络常同时存在 A/AAAA，客户端必须在 IPv4/IPv6 可用性、DNS 返回、路径质量之间选择。Happy Eyeballs 的目标不是“永远优先 IPv6”，而是避免某一地址族配置坏掉时让用户等待很长超时。

IPv6 扩展 header、NDP、RA、DAD、privacy address 都会影响排障方法，因此仅把 IPv6 当“地址更长的 IPv4”会漏掉关键问题。

### 安全与运维边界

- “没有 NAT”不等于“没有防火墙”；IPv6 host 仍需 stateful firewall/security group。
- ICMPv6 对 NDP/PMTUD 等基础功能更关键，粗暴全禁 ICMPv6 会造成隐蔽故障。
- 双栈环境要分别监控 v4/v6 success rate 和 RTT。

### 线上案例推演

若只有部分移动网络用户访问慢，检查 AAAA、IPv6 path、PMTU/ICMPv6、Happy Eyeballs fallback；如果强制 `curl -4` 正常而 `curl -6` 失败，问题边界迅速缩小。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“IPv4 与 IPv6 除了地址长度，还有哪些关键差异？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 IPv6、NDP、Header 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `ip route`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ip route` |
| 辅助 | `ip route get <dst>` |
| 性能/路径 | `traceroute / mtr` |
| 深挖 | `conntrack -S` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：IPv6 为什么不需要广播？

**参考回答**：IPv6 不使用 IPv4 broadcast 机制，许多发现/通知通过 multicast 完成，例如 NDP 的 solicited-node multicast，从而减少整个广播域无差别处理。

### 追问 2：SLAAC 和 DHCPv6 如何区别？

**参考回答**：SLAAC 通过 Router Advertisement/prefix 自主生成地址；DHCPv6 由 Server 分配地址/参数。部署可使用 SLAAC、stateless DHCPv6、stateful DHCPv6 等组合。

### 追问 3：双栈环境为什么会出现 Happy Eyeballs？

**参考回答**：双栈时某一地址族可能配置坏或路径慢；Happy Eyeballs 并行/交错尝试 IPv6/IPv4，目标是降低单栈故障造成的用户等待，而不是固定永远优先某一族。

## 高频易错点（PDF 原内容）

- ❌ 认为 IPv6 天生自带加密。
- ❌ 认为 IPv6 完全不需要任何 NAT 场景。

## 动手验证 / 抓包实验（PDF 原内容）

执行 `ip -6 addr`、`ip -6 neigh`、`ping -6`，抓取 Neighbor Solicitation/Advertisement。

### 实验验收标准

能用路由表、路径探测或 conntrack 解释“为什么走这条路/为什么被改写”，而不是只给结论。

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

- [RFC 8200 - Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200.html)
- [RFC 4861 - Neighbor Discovery for IPv6](https://www.rfc-editor.org/rfc/rfc4861.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [005. ARP 的工作原理是什么？跨网段通信时 ARP 查询谁？](../01-link-layer-foundations/005-arp-next-hop.md)
- [015. IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？](015-ip-fragmentation-pmtud.md)
- [016. TTL / Hop Limit 为什么存在？路由环路是怎么形成的？](016-ttl-hop-limit-routing-loop.md)

## 复习卡片

- **一句话**：IPv6 使用 128 位地址、固定基础头、扩展头体系、NDP 替代 ARP，并取消路由器中途分片；多播承担许多 IPv4 广播场景。其目标不只是“地址更多”，还包括更简洁的转发与更好的协议扩展性。
- **必须会解释**：IPv6 / NDP / Header。
- **必须避免**：认为 IPv6 天生自带加密。
- **必须会验证**：执行 `ip -6 addr`、`ip -6 neigh`、`ping -6`，抓取 Neighbor Solicitation/Advertisement。
