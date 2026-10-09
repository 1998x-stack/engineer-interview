# 第一章 网络分层、链路与二层基础

建立“逐层封装与当前一跳”的基本心智模型。

## 本章能力目标

- 始终区分“最终目的”与“当前下一跳”：IP 负责跨网络寻址，二层地址负责当前链路交付。
- 回答时要把数据单位说清楚：Application Data → Segment/Datagram → IP Packet → Frame。
- 遇到“为什么”题，不只背协议名称，要解释分层如何降低耦合、让每一层独立演进。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **端到端目标 vs 当前一跳**：IP 回答“最终去哪”，MAC/邻居解析回答“这一跳交给谁”。
- **封装不是装饰**：不同层 header 决定不同设备能做什么；抓包点不同会看到不同 offload/封装形态。
- **二层广播域必须可控**：ARP、VLAN、MAC table、环路与广播风暴是一组连续问题，不要分开背。

### 本章白板题

1. 画出同网段通信与跨网段通信的 Ethernet/IP header 差异。
2. 给定 MTU 1500、IPv4/TCP options，计算实际 MSS，并解释 TSO 为何让本机抓包看起来“超 MTU”。
3. 画一个 VLAN trunk/access 场景，说明 ARP broadcast 能到哪里、为什么。

### 最小实验组合

`ip addr` → `ip route` → `ip neigh` → `arping`/`ping` → `tcpdump -e -nn` → `tracepath`。目标是能从路由选择一直证明到实际二层目的 MAC。
<!-- CHAPTER-V2-END -->

## 题目目录

- [001. OSI 七层与 TCP/IP 模型如何对应？工程上为什么更常用 TCP/IP？](001-osi-tcp-ip-model.md) · 基础 · ★★★★★
- [002. 一个应用层消息从 send() 到网卡发送经历了什么封装？](002-send-to-nic-encapsulation.md) · 基础 · ★★★★☆
- [003. Hub、Switch、Router 的本质区别是什么？](003-hub-switch-router.md) · 基础 · ★★★★☆
- [004. MAC 地址和 IP 地址为什么要同时存在？](004-mac-vs-ip.md) · 基础 · ★★★★★
- [005. ARP 的工作原理是什么？跨网段通信时 ARP 查询谁？](005-arp-next-hop.md) · 基础 · ★★★★★
- [006. MTU 与 MSS 有什么区别？为什么常见 MSS 是 1460？](006-mtu-vs-mss.md) · 进阶 · ★★★★★
- [007. 子网掩码 / CIDR 前缀到底解决什么问题？](007-cidr-subnet-mask.md) · 基础 · ★★★★☆
- [008. ping 的完整原理是什么？ping 不通能否说明 TCP 也不通？](008-ping-icmp.md) · 基础 · ★★★★☆
- [009. traceroute 为什么能看到中间路由器？](009-traceroute-ttl.md) · 进阶 · ★★★★☆
- [010. 为什么二层需要 VLAN？VLAN 与广播域是什么关系？](010-vlan-broadcast-domain.md) · 进阶 · ★★★☆☆

## 推荐实践工具

- `tcpdump -e -nn`
- `ip neigh`
- `ip link`
- `ip addr`

[← 返回全书目录](../../README.md)
