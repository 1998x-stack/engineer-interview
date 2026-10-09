# 第二章 IP、NAT 与路由

从本机路由选择扩展到自治系统与全局流量调度。

## 本章能力目标

- 把控制平面和转发平面分开：路由协议决定“学到什么路由”，FIB 决定“某个包下一跳去哪”。
- 任何 NAT/路由问题都先写出五元组、路由表命中项和下一跳，避免靠口头直觉猜。
- 公网故障常有非对称路径、ECMP、NAT/conntrack 和 ICMP 策略，单点抓包不能自动代表端到端事实。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **Route lookup 先于邻居解析**：先决定 next-hop，再 ARP/NDP；NAT/ACL/conntrack 是中间盒附加状态。
- **路由不是“最短路”一个词**：数据平面 LPM、IGP cost、BGP policy、ECMP 分别处在不同层次。
- **公网可达性是整条路径属性**：NAT、PMTU、ICMP、BGP、Anycast 都可能让“地址正确”仍不可用。

### 本章白板题

1. 给出三条重叠 CIDR route，现场做 Longest Prefix Match。
2. 画 SNAT/PAT 五元组变化与 return mapping。
3. 对比 OSPF、eBGP/iBGP、Anycast/GSLB，说明谁解决“内部路径”“跨 AS 策略”“全局入口”。

### 最小实验组合

`ip route get`、`tracepath`、`traceroute -T -p 443`、`conntrack`（有权限时）、`tcpdump icmp or icmp6`。实验重点是 PMTU black hole 与 NAT state，而不是只看 ping。
<!-- CHAPTER-V2-END -->

## 题目目录

- [011. NAT 到底做了什么？SNAT、DNAT、PAT 有什么区别？](011-nat-snat-dnat-pat.md) · 进阶 · ★★★★★
- [012. NAT 为什么让 P2P 变难？STUN、TURN、ICE 分别做什么？](012-nat-traversal-stun-turn-ice.md) · 进阶 · ★★★☆☆
- [013. DHCP 的 DORA 流程是什么？为什么客户端一开始没有 IP 也能通信？](013-dhcp-dora.md) · 基础 · ★★★★☆
- [014. IPv4 与 IPv6 除了地址长度，还有哪些关键差异？](014-ipv4-vs-ipv6.md) · 进阶 · ★★★★☆
- [015. IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？](015-ip-fragmentation-pmtud.md) · 进阶 · ★★★★★
- [016. TTL / Hop Limit 为什么存在？路由环路是怎么形成的？](016-ttl-hop-limit-routing-loop.md) · 基础 · ★★★★☆
- [017. 路由器为什么使用最长前缀匹配？](017-longest-prefix-match.md) · 进阶 · ★★★★★
- [018. OSPF 与 BGP 的定位和核心思想有什么不同？](018-ospf-vs-bgp.md) · 进阶 · ★★★★☆
- [019. BGP 的 AS_PATH、LOCAL_PREF、MED 分别解决什么？](019-bgp-as-path-local-pref-med.md) · 进阶 · ★★★☆☆
- [020. Anycast 是什么？为什么 DNS/CDN 常用？](020-anycast-dns-cdn.md) · 进阶 · ★★★☆☆

## 推荐实践工具

- `ip route`
- `ip route get <dst>`
- `traceroute / mtr`
- `conntrack -S`

[← 返回全书目录](../../README.md)
