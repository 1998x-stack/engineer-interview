---
id: 11
title: "NAT 到底做了什么？SNAT、DNAT、PAT 有什么区别？"
chapter: "第二章 IP、NAT 与路由"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["NAT", "端口映射"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 011. NAT 到底做了什么？SNAT、DNAT、PAT 有什么区别？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：NAT / 端口映射  
> **本章**：[第二章 IP、NAT 与路由](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **NAT / 端口映射** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> NAT 改写报文中的 IP 地址，PAT/NAPT 还改写端口，并维护连接映射状态。SNAT 常用于内网访问公网；DNAT 常用于公网入口映射到内网服务；家庭路由器最常见的是多个私网连接共享一个公网 IP 的 NAPT。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. NAT 设备通常需要同步更新 IP/TCP/UDP 校验和。
2. 状态型 NAT 依赖连接跟踪，因此会消耗表项并可能成为性能瓶颈。
3. NAT 打破端到端寻址，使 P2P、入站连接、故障定位更复杂。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 把控制平面和转发平面分开：路由协议决定“学到什么路由”，FIB 决定“某个包下一跳去哪”。
- 任何 NAT/路由问题都先写出五元组、路由表命中项和下一跳，避免靠口头直觉猜。
- 公网故障常有非对称路径、ECMP、NAT/conntrack 和 ICMP 策略，单点抓包不能自动代表端到端事实。

<!-- V2-ENRICHMENT-START -->
## V2 深入：NAT 是有状态地址/端口重写系统，不只是“私网转公网”

### 第一性原理

- SNAT 改写源地址，DNAT 改写目的地址；PAT/NAPT 进一步利用传输层端口，让多个内部 flow 共享有限公网地址。
- 典型 NAT 需要维护 flow mapping 和反向映射，因此是有状态中间盒；容量受 table entry、端口空间、timeout、CPU/内存约束。
- NAT 改写 IP/port 后必须保持校验和/连接跟踪一致，返回流量才能正确映射回内部 endpoint。

### 五元组与状态

常见连接跟踪以协议、源/目的 IP、源/目的 port 为基础区分 flow。不同 NAT 行为对 endpoint-independent/dependent mapping/filtering 的处理不同，这也是 P2P traversal 难度差异的来源。

NAT 与 proxy 不同：NAT 通常仍在转发同一个网络/传输会话的包并改 header；L7 reverse proxy 会终止客户端连接、理解应用协议并新建到 upstream 的连接。

### 容量与故障模式

- 公网 SNAT 端口有限，短连接爆发会造成 ephemeral-port/PAT exhaustion。
- conntrack table 满时可能表现为新连接随机超时，而已有连接继续正常。
- NAT gateway 同样需要处理 TIME_WAIT/UDP timeout/连接状态，不能只看后端服务器连接数。

### 线上案例推演

如果某批客户端“老连接正常，新连接大量超时”，同时 NAT gateway conntrack/port usage 接近上限，应优先验证 NAT 容量，而不是把所有 SYN timeout 归因服务器 backlog。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“NAT 到底做了什么？SNAT、DNAT、PAT 有什么区别？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 NAT、端口映射 说明关键状态、字段或数据路径。
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

### 追问 1：NAT 表满会有什么现象？

**参考回答**：状态型 NAT/PAT 会改写地址和/或端口，并维护连接映射；容量不足时常见现象是新建连接失败、端口/conntrack 耗尽，而已有连接未必立刻全部中断。

### 追问 2：四元组/五元组如何用于 NAT 映射？

**参考回答**：状态型 NAT/PAT 会改写地址和/或端口，并维护连接映射；容量不足时常见现象是新建连接失败、端口/conntrack 耗尽，而已有连接未必立刻全部中断。

### 追问 3：NAT 与反向代理的区别是什么？

**参考回答**：NAT工作在网络/传输寻址层面，反向代理终止并重新建立上层连接，能理解 HTTP/TLS 等应用语义；两者的状态、可观测性和故障边界不同。

## 高频易错点（PDF 原内容）

- ❌ 把 NAT 说成“只改 IP，不改端口”。
- ❌ 认为 NAT 天然等价于安全防火墙。

## 动手验证 / 抓包实验（PDF 原内容）

用 `iptables/nftables` 做一次 SNAT/DNAT 实验，并查看 conntrack 表。

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

- [RFC 3022 - Traditional IP Network Address Translator](https://www.rfc-editor.org/rfc/rfc3022.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [012. NAT 为什么让 P2P 变难？STUN、TURN、ICE 分别做什么？](012-nat-traversal-stun-turn-ice.md)
- [045. TCP 半连接队列、全连接队列与 listen(backlog) 有什么关系？](../04-tcp-performance-congestion/045-syn-queue-accept-queue-backlog.md)
- [096. 大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？](../10-troubleshooting-system-design/096-syn-recv-troubleshooting.md)

## 复习卡片

- **一句话**：NAT 改写报文中的 IP 地址，PAT/NAPT 还改写端口，并维护连接映射状态。SNAT 常用于内网访问公网；DNAT 常用于公网入口映射到内网服务；家庭路由器最常见的是多个私网连接共享一个公网 IP 的 NAPT。
- **必须会解释**：NAT / 端口映射。
- **必须避免**：把 NAT 说成“只改 IP，不改端口”。
- **必须会验证**：用 `iptables/nftables` 做一次 SNAT/DNAT 实验，并查看 conntrack 表。
