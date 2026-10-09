---
id: 6
title: "MTU 与 MSS 有什么区别？为什么常见 MSS 是 1460？"
chapter: "第一章 网络分层、链路与二层基础"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["MTU", "MSS", "分段"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 006. MTU 与 MSS 有什么区别？为什么常见 MSS 是 1460？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：MTU / MSS / 分段  
> **本章**：[第一章 网络分层、链路与二层基础](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **MTU / MSS / 分段** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> MTU 是链路层可承载的最大网络层 Packet 大小；MSS 是 TCP 连接中协商的最大 TCP Payload。典型以太网 MTU 1500、IPv4 无选项 20B、TCP 无选项 20B，因此常见 MSS≈1460，但真实值受 IPv6、隧道、VPN、TCP 选项和路径 MTU 影响。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. MSS 由 TCP SYN 中的 MSS option 通告，用于避免生成过大的 TCP Segment。
2. IPv6 基础头 40B，因此同一 MTU 下可用 TCP payload 与 IPv4 不同。
3. 隧道会增加额外封装，导致“物理链路 MTU 1500，但内层可用 MTU 更小”。

## 二次深化：工程上还必须知道什么

计算 MSS 时必须把“路径上最小可用 MTU”与“本机接口 MTU”分开。实际云网络、VXLAN、WireGuard/IPsec 等封装都会吞掉额外头部；抓包看到超大 TCP segment 还可能是 TSO/GSO 导致的主机侧观测假象。

### 本章共同的工程视角

- 始终区分“最终目的”与“当前下一跳”：IP 负责跨网络寻址，二层地址负责当前链路交付。
- 回答时要把数据单位说清楚：Application Data → Segment/Datagram → IP Packet → Frame。
- 遇到“为什么”题，不只背协议名称，要解释分层如何降低耦合、让每一层独立演进。

<!-- V2-ENRICHMENT-START -->
## V2 深入：MTU 决定网络包边界，MSS 是 TCP 对 payload 的协商约束

### 第一性原理

- MTU 是某条链路能承载的最大网络层 packet 大小；MSS 是 TCP 对端声明自己愿意接收的最大 TCP segment payload。
- 常见以太网 MTU 1500 下，IPv4 20B + TCP 20B 的无 option 情况得到 MSS 1460；加入 IPv6、TCP option、隧道封装后可用空间会变化。
- MSS 主要帮助 TCP 避免产生需要 IP fragmentation 的 segment，但真正端到端可用上限取决于 Path MTU。

### 隧道与 Offload

VPN、VXLAN、GRE、IPsec 会增加外层 header，若底层仍为 1500 MTU，内层 MTU 往往需要降低。所谓 MSS clamping 就是在边界设备修改 SYN 中 MSS，避免端点按照过大的 MSS 发送。

Linux 的 TSO/GSO/GRO 会把“协议逻辑分段”和“设备真正上线的 frame”解耦，所以在本机抓包看到 8KB、32KB 甚至更大的 TCP segment 并不能直接证明链路 MTU 大于 1500。

### 边界与反例

- IPv4 header 可能有 options，TCP header 也常带 Timestamp，因此 `1500-20-20=1460` 只是典型无 option 计算。
- Jumbo Frame 需要链路端到端设备一致支持，否则会形成 MTU mismatch。
- ICMP 被错误过滤会破坏 PMTUD，产生“大包黑洞”。

### 线上案例推演

“SSH 能连、短请求正常，但上传大 body 卡住”是典型 PMTU 假设。可以用 `tracepath`、DF ping、tcpdump 观察 MSS/ICMP Packet Too Big，并比较隧道前后的 MTU，而不是只调整应用 timeout。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“MTU 与 MSS 有什么区别？为什么常见 MSS 是 1460？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 MTU、MSS、分段 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `tcpdump -e -nn`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `tcpdump -e -nn` |
| 辅助 | `ip neigh` |
| 性能/路径 | `ip link` |
| 深挖 | `ip addr` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：MSS 与 Path MTU 是什么关系？

**参考回答**：Path MTU 是端到端路径上最小可承载 IP packet 尺寸；TCP MSS 应让 TCP payload 加 IP/TCP 头后不超过可用 PMTU，实际还会受隧道和 option 影响。

### 追问 2：为什么 VPN 常见 MTU 1400/1420？

**参考回答**：VPN/WireGuard/VXLAN/IPsec 等增加外层 header，若底层 MTU 仍约 1500，内层可用 MTU 必须降低，因此常见 1400/1420 等配置。

### 追问 3：抓包为什么偶尔看到超过 1500 字节的 TCP Segment？

**参考回答**：常见原因是 TSO/GSO：抓包点位于硬件分段之前，看到的是大逻辑 skb，而 NIC 最终会按 MTU 分段；不要据此断言链路支持超大 frame。

## 高频易错点（PDF 原内容）

- ❌ 把 MTU 当成“应用一次最多 send 的字节数”。
- ❌ 认为 1460 是所有网络的固定 MSS。

## 动手验证 / 抓包实验（PDF 原内容）

执行 `ip link` 查看 MTU；用 `ping -M do -s <size>` 探索无分片上限；抓 SYN 观察 MSS option。

### 实验验收标准

能在抓包或邻居/链路表中验证当前一跳的二层信息，并把它与最终 IP 目的地址区分开。

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

- [015. IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？](../02-ip-nat-routing/015-ip-fragmentation-pmtud.md)
- [044. BDP 是什么？为什么高带宽长 RTT 链路需要大窗口？](../04-tcp-performance-congestion/044-bandwidth-delay-product.md)
- [090. 一个 Packet 从 NIC 到应用 recv() 大致经过哪些 Linux 网络栈阶段？](../09-linux-socket-io/090-linux-packet-receive-path.md)

## 复习卡片

- **一句话**：MTU 是链路层可承载的最大网络层 Packet 大小；MSS 是 TCP 连接中协商的最大 TCP Payload。典型以太网 MTU 1500、IPv4 无选项 20B、TCP 无选项 20B，因此常见 MSS≈1460，但真实值受 IPv6、隧道、VPN、TCP 选项和路径 MTU 影响。
- **必须会解释**：MTU / MSS / 分段。
- **必须避免**：把 MTU 当成“应用一次最多 send 的字节数”。
- **必须会验证**：执行 `ip link` 查看 MTU；用 `ping -M do -s <size>` 探索无分片上限；抓 SYN 观察 MSS option。
