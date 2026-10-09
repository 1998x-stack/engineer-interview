---
id: 13
title: "DHCP 的 DORA 流程是什么？为什么客户端一开始没有 IP 也能通信？"
chapter: "第二章 IP、NAT 与路由"
difficulty: "基础"
frequency: "★★★★☆"
tags: ["DHCP", "地址分配"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 013. DHCP 的 DORA 流程是什么？为什么客户端一开始没有 IP 也能通信？

> **定位**：基础 · **面试频率**：★★★★☆ · **标签**：DHCP / 地址分配  
> **本章**：[第二章 IP、NAT 与路由](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **DHCP / 地址分配** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> DHCP 经典流程为 Discover→Offer→Request→ACK。客户端初始还没有可用地址，因此通过广播和特殊源/目的地址获取配置；服务端可下发 IP、Mask、Gateway、DNS、Lease 等。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. DHCP 基于 UDP，客户端/服务端使用固定端口。
2. 租约机制使地址可复用，客户端会在租期内提前续租。
3. 跨网段 DHCP 常通过 DHCP Relay，把广播请求转发到集中服务器。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 把控制平面和转发平面分开：路由协议决定“学到什么路由”，FIB 决定“某个包下一跳去哪”。
- 任何 NAT/路由问题都先写出五元组、路由表命中项和下一跳，避免靠口头直觉猜。
- 公网故障常有非对称路径、ECMP、NAT/conntrack 和 ICMP 策略，单点抓包不能自动代表端到端事实。

<!-- V2-ENRICHMENT-START -->
## V2 深入：DHCP 在“客户端还没有 IP”时靠广播与租约状态机启动网络身份

### 第一性原理

- 客户端初始不知道自己的 IP、服务器地址和网关，因此 Discover/Request 可以使用广播和特殊地址完成 bootstrap。
- DORA 不只是四个包名，而是一套租约选择与确认状态机：Discover → Offer → Request → ACK。
- DHCP 下发的不仅是地址，还可包括 subnet mask/prefix、default gateway、DNS、lease time 等网络配置。

### 租约生命周期

客户端不会等 lease 完全过期才行动，而会在租约周期中尝试续租/重新绑定；如果最终无法续租，地址不应被无限继续使用。DHCP Reservation 则是服务器根据 client identifier/MAC 等规则固定分配某地址，与客户端手工配置静态 IP 的控制面完全不同。

### DHCP Relay

广播通常不跨三层路由，因此大型网络在每个 subnet 都部署独立 DHCP server 并不现实。Relay agent 将本地客户端请求转给中心 DHCP server，并携带网段信息，使 server 能从正确 address pool 分配。

### 线上案例推演

“新机器拿不到 IP，但已有机器正常”时，应依次确认 L2/VLAN、DHCP Discover 是否发出、relay 是否转发、server pool 是否耗尽、Offer 是否回来、客户端是否 Request/ACK，而不是只重启 DHCP 服务。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“DHCP 的 DORA 流程是什么？为什么客户端一开始没有 IP 也能通信？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 DHCP、地址分配 说明关键状态、字段或数据路径。
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

### 追问 1：DHCP Relay 为什么需要？

**参考回答**：DHCP broadcast 默认不跨三层网段，Relay 在客户端网段接收请求并单播/转发给中心 DHCP Server，同时携带网段信息，使 Server 选择正确地址池。

### 追问 2：租约到期会怎样？

**参考回答**：客户端会在租约周期内提前续租/重新绑定；若最终无法续租并过期，不能无限继续使用该地址，应重新进入获取流程。

### 追问 3：静态 IP 与 DHCP Reservation 有何差别？

**参考回答**：静态 IP 是客户端本地手工配置；Reservation 是 DHCP Server 根据 MAC/client-id 等规则始终租给同一地址，仍保留集中租约/配置管理。

## 高频易错点（PDF 原内容）

- ❌ 把 DORA 当成 TCP 握手。
- ❌ 认为 DHCP 只下发 IP，不下发 DNS/Gateway。

## 动手验证 / 抓包实验（PDF 原内容）

抓取一次 DHCP renew 或在虚拟机重启网卡，观察 Discover/Offer/Request/ACK。

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

- [RFC 2131 - Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [012. NAT 为什么让 P2P 变难？STUN、TURN、ICE 分别做什么？](012-nat-traversal-stun-turn-ice.md)
- [014. IPv4 与 IPv6 除了地址长度，还有哪些关键差异？](014-ipv4-vs-ipv6.md)

## 复习卡片

- **一句话**：DHCP 经典流程为 Discover→Offer→Request→ACK。客户端初始还没有可用地址，因此通过广播和特殊源/目的地址获取配置；服务端可下发 IP、Mask、Gateway、DNS、Lease 等。
- **必须会解释**：DHCP / 地址分配。
- **必须避免**：把 DORA 当成 TCP 握手。
- **必须会验证**：抓取一次 DHCP renew 或在虚拟机重启网卡，观察 Discover/Offer/Request/ACK。
