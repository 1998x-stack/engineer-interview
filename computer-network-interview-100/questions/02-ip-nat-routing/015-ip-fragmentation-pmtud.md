---
id: 15
title: "IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？"
chapter: "第二章 IP、NAT 与路由"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["分片", "PMTU"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 015. IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：分片 / PMTU  
> **本章**：[第二章 IP、NAT 与路由](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **分片 / PMTU** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> IP 分片会放大丢包代价、增加重组状态和中间设备兼容问题。现代传输更倾向让源端根据 Path MTU 控制报文大小。IPv4 可通过 DF + ICMP Fragmentation Needed，IPv6 则由路由器返回 Packet Too Big。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 一个 fragment 丢失就会使原始 IP datagram 无法完整重组。
2. 中间防火墙若错误丢弃必要 ICMP，可能导致 PMTU black hole。
3. TCP 常结合 MSS 控制，尽量不让正常 Segment 触发 IP fragmentation。

## 二次深化：工程上还必须知道什么

PMTU black hole 是经典线上故障：中间链路需要更小 MTU，但必要 ICMP 被过滤，结果可能表现为小请求正常、大响应卡住或 TLS/SSH 在特定阶段停滞。

### 本章共同的工程视角

- 把控制平面和转发平面分开：路由协议决定“学到什么路由”，FIB 决定“某个包下一跳去哪”。
- 任何 NAT/路由问题都先写出五元组、路由表命中项和下一跳，避免靠口头直觉猜。
- 公网故障常有非对称路径、ECMP、NAT/conntrack 和 ICMP 策略，单点抓包不能自动代表端到端事实。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Fragmentation 把“一次丢包影响”放大成“整份 datagram 重组失败”

### 第一性原理

- IP fragmentation 发生后，任一 fragment 丢失都可能使整个原始 datagram 无法重组，增加丢包放大、buffer/CPU 和安全复杂度。
- TCP 更希望通过 MSS/PMTUD 从源端避免产生超 Path MTU 的 packet，而不是依赖中途 fragmentation。
- IPv6 router 不进行 fragmentation；源端根据 ICMPv6 Packet Too Big 等信息调整发送大小。

### PMTUD 与黑洞

经典 IPv4 PMTUD 使用 DF + ICMP Fragmentation Needed；IPv6 使用 Packet Too Big。若中间防火墙丢弃这些 ICMP，端点可能反复发送过大 packet，从而出现**小包正常、大包超时**的 PMTU black hole。

Packetization Layer PMTUD（PLPMTUD）类思想会从传输/应用层主动探测可用尺寸，降低完全依赖 ICMP 的脆弱性。

### 工程边界

- VPN/VXLAN 使有效 PMTU 降低，是黑洞高发场景。
- TCP MSS 只约束 TCP payload，UDP/QUIC 仍必须自行控制 datagram size。
- “ping -s 小包通”无法证明大 packet path 正常。

### 线上案例推演

API header 很小正常、上传文件或 TLS 大 record 卡住时，抓包若反复重传相同大 segment且看不到对应 ACK/ICMP，应立即验证 PMTU/隧道 MTU，而不是只增加 TCP timeout。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 分片、PMTU 说明关键状态、字段或数据路径。
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

### 追问 1：什么是 PMTU black hole？

**参考回答**：MSS约束 TCP payload，Path MTU 约束端到端路径可承载的 IP packet。隧道/VPN增加外层头部会降低内层可用 MTU；必要 ICMP 被过滤时可能出现 PMTU black hole。

### 追问 2：为什么 “ping 通但大包 TCP 卡住” 可能与 MTU 有关？

**参考回答**：MSS约束 TCP payload，Path MTU 约束端到端路径可承载的 IP packet。隧道/VPN增加外层头部会降低内层可用 MTU；必要 ICMP 被过滤时可能出现 PMTU black hole。 ping主要验证 ICMP/IP 层可达性和 RTT；ICMP可能被策略丢弃，因此 ping 不通不等于 TCP/443 不通，ping 通也不等于应用健康。

### 追问 3：IPv6 的最小链路 MTU 有什么意义？

**参考回答**：MSS约束 TCP payload，Path MTU 约束端到端路径可承载的 IP packet。隧道/VPN增加外层头部会降低内层可用 MTU；必要 ICMP 被过滤时可能出现 PMTU black hole。

## 高频易错点（PDF 原内容）

- ❌ 认为 TCP 自身会做“IP 分片”。
- ❌ 把 TCP segmentation 与 IP fragmentation 当成同一件事。

## 动手验证 / 抓包实验（PDF 原内容）

用不同 payload 的 `ping -M do` 查最大无分片尺寸；再通过 VPN/隧道场景观察 PMTU 变化。

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

- [RFC 1191 - Path MTU Discovery](https://www.rfc-editor.org/rfc/rfc1191.html)
- [RFC 8201 - Path MTU Discovery for IPv6](https://www.rfc-editor.org/rfc/rfc8201.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [006. MTU 与 MSS 有什么区别？为什么常见 MSS 是 1460？](../01-link-layer-foundations/006-mtu-vs-mss.md)
- [014. IPv4 与 IPv6 除了地址长度，还有哪些关键差异？](014-ipv4-vs-ipv6.md)
- [100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？](../10-troubleshooting-system-design/100-tcpdump-wireshark-analysis.md)

## 复习卡片

- **一句话**：IP 分片会放大丢包代价、增加重组状态和中间设备兼容问题。现代传输更倾向让源端根据 Path MTU 控制报文大小。IPv4 可通过 DF + ICMP Fragmentation Needed，IPv6 则由路由器返回 Packet Too Big。
- **必须会解释**：分片 / PMTU。
- **必须避免**：认为 TCP 自身会做“IP 分片”。
- **必须会验证**：用不同 payload 的 `ping -M do` 查最大无分片尺寸；再通过 VPN/隧道场景观察 PMTU 变化。
