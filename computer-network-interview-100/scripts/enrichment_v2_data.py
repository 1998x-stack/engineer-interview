# -*- coding: utf-8 -*-
"""Question-specific V2 enrichment blocks.

Generated for the repository's second, deeper edition. Each block is intentionally
question-specific; the updater inserts it into the corresponding Markdown file.
"""
PACKS = {}
PACKS.update({
1: r'''
## V2 深入：分层模型不是“背七层”，而是定位责任边界

### 第一性原理

- **分层的价值是隔离变化**：应用不需要知道以太网如何重传/交换，TCP 也不需要知道 HTTP 方法语义；层与层之间通过稳定接口协作。
- **封装与解封装是一条数据路径，不是七个独立世界**：同一份应用数据会依次成为 transport payload、IP payload、link-layer payload；排障时要反向确认到底在哪一层出现异常。
- **OSI 是教学抽象，Internet 协议族才是工程事实**：TLS、QUIC、VPN、隧道等现代协议经常跨越传统层次，因此面试时应回答“它提供什么能力、依赖什么下层”，而不是争论唯一层号。

### 协议栈级展开

典型 Linux 用户态到网络的路径可以抽象成：`HTTP/gRPC → TLS（可选）→ TCP/UDP/QUIC → IPv4/IPv6 → Ethernet/Wi-Fi → NIC`。每一层都会增加自己的控制信息，但并非每个中间设备都会看到所有层：二层交换机通常只需理解 L2，普通路由器核心转发决策基于 L3，而 L7 代理会终止上层连接并重新发起新的下游连接。

面试中尤其要区分 **endpoint protocol stack** 与 **middlebox**。例如 NAT 会修改 IP/port 并重算相关校验和；TLS 终止代理会解密并重新加密；普通路由器则不会“把 HTTP 请求重新封装一次”。

### 工程边界与反例

- MPLS、VXLAN、GRE、IPsec 会形成“外层协议包裹内层协议”的隧道，因此真实网络常是多层嵌套，而不是一条平直的七层栈。
- QUIC 基于 UDP 承载，却向应用暴露 stream、可靠性、流控、拥塞控制和安全握手；只用“UDP 属于传输层”无法解释其能力边界。
- 抓包位置会改变你看到的层次：在应用代理前后、容器 veth、宿主机、物理 NIC 上抓到的包可能不同。

### 线上案例推演

如果用户报告“HTTPS 访问慢”，不要直接归因 HTTP。先拆成 DNS、连接建立、TLS、请求处理、响应传输；若 `curl` 显示 connect 很快但 TLS handshake 慢，问题层次已经从 TCP connect 缩小到 TLS/CPU/证书链/网络 RTT，而不是继续盲查交换机。
''',
2: r'''
## V2 深入：`send()` 到 NIC 之间真正发生了什么

### 第一性原理

- `send()` 的成功语义通常只是**内核接受了多少用户数据**，不是“已上网线”，更不是“对端应用已收到”。
- TCP 是字节流：应用写入的数据先进入 socket send buffer，TCP 根据 MSS、拥塞窗口、接收窗口、pacing、TSO/GSO 等条件决定何时怎样分段。
- 发送路径同时受协议状态和设备队列影响：用户态、socket buffer、qdisc、驱动 ring、NIC/DMA 都可能成为排队点。

### Linux 发送路径拆解

可以把路径记成：`copy_from_user/zero-copy → socket send buffer → TCP segmentation/拥塞控制 → IP route → qdisc → driver TX ring → DMA → NIC`。启用 TSO/GSO 后，内核可能保留较大的“逻辑 skb”，把最终分段交给更靠近网卡的位置完成，因此在不同抓包点看到的 packet size 不一定一致。

TCP 的发送还受 `cwnd`、`rwnd`、Nagle、pacing、retransmission queue 等共同约束。应用即使连续 `write()` 很多数据，也可能因为 peer zero-window、拥塞窗口太小或 qdisc backlog 而暂时无法真正出接口。

### 工程边界与观测误区

- 本机 `tcpdump` 看到超 MTU 的大 segment，不一定是线上真的发出了 jumbo packet，可能只是抓包点位于 GSO/TSO 分段之前。
- `send()` 短写是合法行为；nonblocking socket 还可能返回 `EAGAIN`，应用必须维护未发送偏移量。
- 路由器每一跳会重新构造对应链路层帧，但 IP payload/目的地址通常保持端到端语义（NAT/隧道等除外）。

### 线上案例推演

若应用 QPS 正常但发送延迟飙升，先看 socket send queue、TCP retrans、cwnd/RTT、qdisc drops 和 NIC TX statistics。若 `ss -tin` 显示 send-q 持续增长而应用 CPU 很低，问题可能在网络/对端消费/拥塞，而不是业务计算。
''',
3: r'''
## V2 深入：Hub、Switch、Router 的区别本质是“转发依据与广播边界”

### 第一性原理

- Hub 近似物理层中继，不理解目的 MAC；Switch 学习 `MAC → port` 并在一个二层广播域内转发；Router 根据 IP 前缀选择下一跳并隔离二层广播域。
- 交换机的 MAC 表是**从源 MAC 学出来的**，不是通过 ARP 构建的。ARP 是端主机/三层设备进行 IP→链路地址解析的协议。
- Router 每转发一跳都需要为下一链路重新生成 L2 header，因此同一个 IP packet 的源/目的 MAC 可以逐跳变化。

### 二层交换细节

未知单播、广播以及某些组播在二层可能被 flood 到 VLAN 内多个端口；一旦交换机学习到目的 MAC 所在端口，普通单播即可定向转发。MAC aging、STP、VLAN、LAG 等机制都是为了让这个二层转发域在存在冗余链路和规模扩展时仍然可控。

Router 则进行 L3 forwarding：查 FIB、最长前缀匹配、更新 TTL/Hop Limit，并把包交给下一跳接口。它通常不会把一个 VLAN 中的 L2 broadcast 原样转发到另一个三层网段。

### 工程边界与反例

- “三层交换机”并不改变逻辑层次，它只是用硬件 ASIC 高速实现 L3 forwarding。
- VXLAN/EVPN 可以在三层网络上延伸二层逻辑网络，但这是一种 overlay，不代表物理 underlay 失去了路由层。
- ARP flood 与 unknown-unicast flood 是不同原因，排障时应区分。

### 线上案例推演

同 VLAN 大量广播导致 CPU/带宽异常时，先确认广播类型、MAC flap、ARP storm、环路/STP 状态；如果跨 VLAN 互通失败，则应转向网关/SVI/路由/ACL，而不是继续只查交换机 MAC 表。
''',
4: r'''
## V2 深入：IP 标识“端到端目标”，MAC 标识“当前链路下一跳”

### 第一性原理

- IP 地址服务于可路由的网络层命名；MAC 地址主要服务当前 L2 链路上的帧交付。
- 访问跨网段目标时，本机 L2 目的通常是**默认网关的 MAC**，而 IP 目的仍是远端服务器；这正是“逐跳链路 + 端到端网络层”的组合。
- 路由器转发后会为下一条链路重新选择 L2 地址，因此 MAC 不是互联网端到端标识。

### 数据路径示例

主机 `192.168.1.10/24` 访问 `8.8.8.8` 时，先用路由表判断目标不在 `192.168.1.0/24`，于是下一跳为 `192.168.1.1`。ARP/NDP 解析的是网关链路地址，构造的帧是 `dst MAC = gateway`，但 IP header 仍是 `dst IP = 8.8.8.8`。下一跳路由器收到后移除该 L2 header，再为新的 egress link 构造新的 L2 header。

### 边界与容易混淆的点

- MAC“全球唯一”不是协议正确性的绝对前提：虚拟机、容器、克隆镜像、手工配置都可能产生重复 MAC，真正要求是在相关二层域内避免冲突。
- NAT 会改变网络层/传输层地址映射，但并不把 MAC 变成跨互联网标识。
- 在点对点链路或某些隧道里，链路层不一定使用传统 48-bit Ethernet MAC；“每个 IP packet 都必须有 MAC”也是错误结论。

### 线上案例推演

如果同网段主机互 ping 失败但网关可达，重点看 ARP table、duplicate IP/MAC、VLAN、port isolation；如果公网目标不可达且 ARP 网关正常，则问题大概率已越过 L2，应查路由/NAT/ACL/上游。
''',
5: r'''
## V2 深入：ARP 是“下一跳地址解析”，不是“寻找互联网目标”

### 第一性原理

- ARP 将本地链路上的 IPv4 地址解析为链路层地址；它不会跨路由器广播到整个互联网。
- 发送端先查路由表决定 next-hop，再决定 ARP 谁：同网段解析目标主机，跨网段解析网关。
- ARP cache 是有状态缓存，条目有生命周期；缓存错误、冲突和欺骗都会直接影响 L2 交付。

### 协议行为

ARP Request 通常以 Ethernet broadcast 发送，询问“谁拥有某 IPv4 地址”；目标主机返回 ARP Reply，发送者把 IP→MAC 映射缓存下来。Gratuitous ARP 可以在没有显式请求时宣布自己的映射，常用于地址冲突检测、HA VIP 漂移后刷新邻居缓存等场景。

IPv6 不再使用 ARP，而使用 ICMPv6 Neighbor Discovery（NDP），同时融合邻居解析、Router Discovery、DAD 等能力。

### 安全与工程边界

- ARP 没有原生强认证，攻击者可能伪造 reply 进行 ARP spoofing/MITM；交换网络可通过 DHCP snooping + Dynamic ARP Inspection 等降低风险。
- Proxy ARP 会让设备替另一个 IP 回 ARP，可能让“看起来同链路”的通信实际经过路由设备。
- 容器/云网络可能使用 proxy ARP、EVPN、neighbor suppression 等优化，不应假设每次都真的在物理网段广播。

### 线上案例推演

出现“偶发访问到错误主机”时，结合 `ip neigh`、交换机 MAC table 与抓包检查同一 IP 是否在不同 MAC 间抖动；如果 HA VIP 切换后部分客户端仍访问旧节点，Gratuitous ARP 是否被过滤/缓存未刷新就是关键假设。
''',
6: r'''
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
''',
7: r'''
## V2 深入：CIDR 的本质是把地址空间变成可聚合的前缀集合

### 第一性原理

- 前缀长度决定“网络部分有多少 bit”，并用于本机 on-link 判断与路由聚合。
- 路由选择不是“看前三段 IP 是否相同”，而是对 destination 与候选 prefix 做 bit-level prefix matching。
- CIDR 同时解决地址分配灵活性与路由表聚合问题，是现代 IP 路由的基础。

### 特殊前缀

`/32` 表示单个 IPv4 host route；`/31` 可用于点对点链路（没有传统意义上的网络/广播地址浪费）；默认路由是 `/0`。所以“每个 subnet 固定减 2 个地址”并不是所有前缀的普遍法则。

云平台还会为网关、DNS、平台基础设施等保留地址，能分配给用户的数量取决于平台约束，而不是只算 `2^(host bits)-2`。

### 与路由系统的关系

CIDR 允许把多个更具体前缀汇总成 aggregate，降低全球路由表规模；但若某个更具体 prefix 被单独发布，Longest Prefix Match 会优先选它，这也是流量工程和 prefix hijack 分析的基础。

### 线上案例推演

如果新加的 `/24` 路由没有生效，不能只看“有没有默认路由”；需要同时检查是否存在更具体 `/25`、policy routing、VRF、rule priority，以及最终 FIB 实际选择。
''',
8: r'''
## V2 深入：ping 测的是 ICMP Echo 路径，不是“整个网络是否正常”

### 第一性原理

- ping 主要用 ICMP Echo Request/Reply 验证特定 IP 层可达性和 RTT；它没有建立 TCP connection，也没有验证服务进程。
- ICMP 是网络控制与错误反馈的重要组成，不只是 ping 工具；PMTUD、Destination Unreachable、Time Exceeded 都依赖 ICMP/ICMPv6。
- 网络设备和主机可以独立对 ICMP 做过滤或限速，因此 ping 结果不能直接等价于业务协议结果。

### 为什么 RTT 不能机械等价

ICMP 与 TCP/QUIC 可能经过不同 ACL、QoS、ECMP hash、处理优先级；某些路由器对控制平面 ICMP reply 严格限速，但正常 forwarding 不受影响。因此 ping RTT 高并不一定代表数据平面转发同样高延迟。

反过来，ping 正常也只说明这一类 packet 的路径可用，不代表 DNS、TLS、HTTP、服务端线程池、数据库都正常。

### 工程化使用

- 用 ping 作为**低成本 baseline**，不要作为根因结论。
- 需要验证 TCP 端口时使用 `nc`/`curl`/TCP traceroute；需要判断路径 loss/latency 时结合 `mtr` 与两端 telemetry。
- 云环境中 security group 允许 TCP/443 而禁 ICMP 非常常见。

### 线上案例推演

如果用户说“ping 服务器 10ms，但 API 2s”，应立即把问题从基础 IP RTT 转向 DNS/connect/TLS/TTFB/application decomposition；继续无限 ping 不会增加诊断信息。
''',
9: r'''
## V2 深入：traceroute 利用的是 TTL/Hop Limit 的逐跳失效反馈

### 第一性原理

- IPv4 TTL / IPv6 Hop Limit 每经一个转发节点递减；到 0 时路由器丢包并通常返回 ICMP Time Exceeded。
- traceroute 通过发送 TTL=1、2、3… 的 probe，逐步让不同 hop 成为“第一个过期点”，从返回 ICMP 的源地址推断路径。
- 它观察的是 **probe 的去程 + ICMP 回程组合结果**，并不是精确还原所有转发设备的绝对拓扑。

### 实现差异

传统 Unix traceroute 常用高端口 UDP probe；Windows `tracert` 常用 ICMP Echo；也可以用 TCP/443 probe，以穿过只允许 Web 流量的防火墙。不同 probe 的五元组会导致 ECMP hash 不同，因此路径可能不一样。

`mtr` 在 traceroute 基础上持续探测并统计每 hop latency/loss，但中间 hop ICMP rate-limit 会制造“这个 hop 丢包很高、后续却正常”的假象。

### 边界与反例

- 去程和回程可以完全不对称；看到某个 ICMP source 不代表业务回程经过同一路由。
- MPLS、隧道、ICMP filtering 会隐藏某些 hop。
- 单个中间 hop 不 reply 并不等于它丢弃了 transit traffic。

### 线上案例推演

跨地域延迟突增时，比较故障前后的 TCP traceroute/MTR、BGP path 与业务 RTT。如果只某中间 hop 不响应而最终目标 RTT 正常，不应误判该路由器为丢包根因。
''',
10: r'''
## V2 深入：VLAN 的核心是把一个物理二层基础设施切成多个逻辑广播域

### 第一性原理

- VLAN 给 Ethernet frame 增加逻辑二层分区，使同一交换基础设施中的不同 VLAN 彼此不直接共享广播域。
- 不同 VLAN 之间若要通信，需要经过 L3 routing（SVI/router-on-a-stick 等），因此 ARP broadcast 默认不会跨 VLAN。
- VLAN 解决的是二层隔离与扩展，不是加密；同 VLAN/不同 VLAN 都仍需考虑 ACL、身份和上层安全。

### 802.1Q 与端口模型

Access port 通常把未标记流量归入一个 VLAN；Trunk port 可以携带多个带 802.1Q tag 的 VLAN。Native VLAN/untagged 行为若两端配置不一致，可能产生 VLAN hopping、流量串域或难以排查的单向通信问题。

STP 仍在每个逻辑二层拓扑里解决环路，而 VLAN 数量过大也会带来 MAC table、broadcast/ARP、STP 控制面的扩展问题。

### VLAN 与 VXLAN

VLAN ID 只有 12 bit，规模与跨三层扩展能力有限；VXLAN 使用 VNI 在 IP underlay 上构建大规模 L2/L3 overlay，常结合 EVPN 控制平面。两者都是逻辑分段，但技术层次和规模目标不同。

### 线上案例推演

“同交换机两台机器互相不通”时先确认它们是否真的属于同 VLAN、PVID/tag 配置是否一致、是否有 port isolation；若不同 VLAN，则应检查默认网关/SVI/ACL，而不是期待 ARP 跨 VLAN 生效。
''',
11: r'''
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
''',
12: r'''
## V2 深入：STUN、TURN、ICE 是“发现候选、验证路径、必要时中继”的组合

### 第一性原理

- STUN 帮 endpoint 发现外部看到的 server-reflexive address，并可用于 connectivity check；它不是万能打洞服务。
- TURN 提供 relay candidate：当双方无法直接建立可用路径时，通过中继服务器转发，代价是额外带宽和时延。
- ICE 负责收集 host/server-reflexive/relay 等候选、形成 candidate pair、做连通性检查并选择可用路径。

### 为什么不能只靠 STUN

NAT mapping/filtering 行为、企业防火墙、对称 NAT、UDP blocked 等都可能使直连失败。ICE 的价值正是**尝试多种候选并择优**，TURN 则是“保证能通”的兜底，而不是性能最优路径。

WebRTC 中还需要考虑 ICE restart、trickle ICE、IPv4/IPv6 双栈、多网卡和 network handover，因此真实连接建立比“STUN 拿公网 IP→UDP hole punching”复杂得多。

### IPv6 也不代表问题消失

IPv6 减少地址转换需求，但防火墙、隐私地址、多归属、企业策略、中继需求仍然存在；ICE 还能承担路径选择与连通性验证，因此不会因为 IPv6 普及而自动失去价值。

### 线上案例推演

若一部分企业用户 WebRTC 永远走 TURN，而家庭网络可 P2P，优先按网络类型统计 ICE candidate pair 选择、STUN timeout、UDP/TCP/TLS TURN fallback，而不是只查媒体编码。
''',
13: r'''
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
''',
14: r'''
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
''',
15: r'''
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
''',
16: r'''
## V2 深入：TTL/Hop Limit 是分布式路由系统的“最终保险丝”

### 第一性原理

- 路由协议可能暂时收敛不一致形成 loop；TTL/Hop Limit 保证 packet 不会无限循环消耗网络资源。
- 每个 L3 hop 递减，归零后 router 丢弃，并通常返回 ICMP Time Exceeded；这与 TCP RST 完全不同层。
- TTL 是 packet 字段，不是应用连接超时，也不是“真实秒数寿命”的可靠计时器。

### 路由环路如何发生

静态路由误配、IGP/BGP 收敛期间的瞬时不一致、互相 redistribution、policy routing 都可能导致 A→B→C→A。环路不仅让请求失败，还会瞬时放大 PPS/链路利用率，因此 TTL 是必要的故障隔离机制。

不同 OS 常使用不同初始 TTL/Hop Limit，这可以辅助被动 fingerprint，但不能当作安全身份验证，因为值可配置且路径 hop 数未知。

### 线上案例推演

如果抓包看到同一 flow 的 ICMP Time Exceeded、traceroute 出现 hop 循环，应把根因转向 routing policy/route convergence，而不是继续调 TCP retransmission。观察 TTL 逐跳减少可以直接证明 packet 在循环路径里被消耗。
''',
17: r'''
## V2 深入：Longest Prefix Match 决定“候选路由里谁更具体”

### 第一性原理

- 路由查找首先在能够匹配 destination 的前缀中选择**最长前缀**；它表示“更具体的目标范围”。
- metric、administrative distance、BGP attributes 等通常是在路由协议产生/安装候选 route 时参与选择，不应和数据平面 LPM 混成一个步骤。
- RIB 是控制平面学习/选择的路由视图，FIB 是为高速 forwarding 下发/优化后的数据平面表。

### 例子

如果同时存在 `0.0.0.0/0 → A`、`10.0.0.0/8 → B`、`10.1.0.0/16 → C`，访问 `10.1.2.3` 选 `/16`。这也是为什么更具体 prefix leak/hijack 能吸引流量：数据平面天然偏好更具体前缀。

### ECMP 与乱序

多个等价 next-hop 可做 ECMP，但通常按 flow hash 让同一 flow 稳定落在同一路径，避免逐包 load balancing 导致 TCP reordering。硬件 FIB 常用 TCAM/trie 等结构加速 LPM。

### 线上案例推演

“明明有默认路由却不走默认网关”时，第一步就是查更具体 route。若 `ip route get <dst>` 与预期不同，继续查 policy rule/VRF/FIB，而不是从 DNS 开始排查。
''',
18: r'''
## V2 深入：OSPF 优化自治系统内部收敛，BGP表达跨自治系统策略

### 第一性原理

- OSPF 是 link-state IGP：在一个管理域内传播拓扑信息、运行 SPF，目标是快速、一致地计算内部路径。
- BGP 是 path-vector/policy protocol：跨 AS 传播可达前缀和属性，核心不是物理最短，而是商业与运营策略可控。
- 互联网不能简单用一个全局 OSPF：拓扑规模、故障泛洪、信任边界、策略需求都不允许。

### 收敛与扩展

OSPF 通过 area 限制 LSDB/flooding 范围，BGP 则用增量 UPDATE、route policy、aggregation 和 route reflector 等扩展。BGP 的收敛通常更保守，因为跨组织策略和 path exploration 比一个园区内 SPF 更复杂。

### iBGP / eBGP

eBGP 在不同 AS 之间交换路由；iBGP 在同一 AS 内分发外部路由和策略。iBGP 本身不等于 IGP，通常仍依赖 OSPF/IS-IS 提供 next-hop reachability。

### 线上案例推演

如果内部机房链路故障后路由几秒内切换，更多是 IGP/FIB 问题；如果只有某 ISP/地区用户绕路数分钟甚至更久，需检查 BGP announcement、policy、community、upstream path，而不是只看 OSPF。
''',
19: r'''
## V2 深入：BGP Attributes 是“策略语言”，不是单一最短路径权重

### 第一性原理

- `LOCAL_PREF` 常用于一个 AS 内表达“出站更喜欢哪个出口”，通常更高优先。
- `AS_PATH` 既用于 loop prevention，也参与 route selection，但不是唯一决定因素。
- `MED` 常用于向邻居表达“进入我这个 AS 更希望走哪个入口”，但其比较范围/策略受实现和运营配置影响。

### Community 与运营策略

BGP community 让 operator 给 route 打标签，再批量应用 local-pref、no-export、blackhole、region 等 policy。现实网络里，大量流量工程不靠手工改每条 prefix，而靠 community 驱动策略。

### Route leak 与 hijack

Hijack 通常指错误/恶意 origin 或更具体 prefix 抢占；route leak 更多是合法学到的 route 被不当传播到不该传播的邻居，破坏 valley-free 等政策边界。两者都可能导致大规模绕路/黑洞，但根因和治理方式不同。

### 线上案例推演

若用户从欧洲访问亚洲服务突然绕到北美，检查 BGP looking glass/AS_PATH 只是一部分；还要结合 local-pref、community、provider policy 和是否有更具体 announcement，不能机械说“AS_PATH 最短就会被选”。
''',
20: r'''
## V2 深入：Anycast 把“同一个服务地址”交给路由系统做粗粒度就近选择

### 第一性原理

- 多个站点从不同位置宣布同一 prefix，BGP 将客户端流量送到当前策略下的某个可达实例。
- Anycast 的“近”是路由策略意义上的近，不保证地理最近或 RTT 最低。
- 它特别适合无状态/易复制的边缘入口，例如 DNS、CDN edge、DDoS 吸收点。

### 与 DNS GSLB 的差异

DNS GSLB 在解析阶段返回不同 endpoint，可做更细粒度地域/健康/容量策略，但受 resolver cache/TTL 影响；Anycast 在 L3 routing 层持续起作用，切换可更透明，却受 BGP convergence 和 routing policy 约束。大型系统常组合二者。

### 有状态服务的挑战

TCP/QUIC connection 建立后若路由突然漂移到另一个 POP，新节点可能没有 connection state。解决方式包括 routing stability、state replication、connection ID/LB coordination 或让 Anycast 只承载可容错入口。

### 线上案例推演

若同一 Anycast IP 只有某 ISP 用户延迟突增，服务实例本身可能完全健康。应查该 ISP 到 prefix 的 BGP path/peering 和 POP ingress 分布，而不是只查全局平均服务器 CPU。
''',
})
PACKS.update({
21: r'''
## V2 深入：TCP/UDP 的区别是“服务抽象”，不是两个形容词

### 第一性原理

- TCP 向应用提供**有序可靠字节流**与连接状态；UDP 提供**无连接数据报**，保留消息边界但不内建可靠、排序、流控与拥塞恢复语义。
- TCP 的可靠性来自序号、ACK、重传、接收重组和校验等状态；这些能力带来额外延迟、内存和 head-of-line 约束。
- UDP 的“简单”意味着上层可以自行选择需要哪些机制，而不是“UDP 天生更快”。QUIC 正是在 UDP 之上重新构建现代传输能力。

### 选型维度

面试中应从 **可靠性要求、时延预算、消息边界、拥塞控制、连接迁移、部署兼容性**回答，而不是背“视频用 UDP、网页用 TCP”。实时媒体可以容忍部分过期 packet 丢失，因此常选择 UDP + 自定义恢复/FEC；文件传输则通常需要完整可靠交付。

### 边界与反例

- UDP checksum/链路 CRC 不提供应用语义可靠性；TCP 可靠也不等于业务 Exactly Once。
- DNS 普通请求常用 UDP，但大 response、zone transfer、DoT/DoH 等可以使用其他 transport。
- QUIC 的拥塞控制、可靠 stream 和 TLS 安全都是 QUIC 自己提供，不是 UDP 获得了这些能力。

### 线上案例推演

若 UDP 业务“偶发音视频花屏”，应观察 packet loss、jitter、reordering、应用 jitter buffer/FEC；把它当 TCP retransmission 问题会走错诊断路径。
''',
22: r'''
## V2 深入：三次握手真正建立的是双方的序号空间、能力与状态

### 第一性原理

- Client SYN 声明自己的 ISN 与 TCP options；Server SYN+ACK 同时确认 Client ISN 并声明自己的 ISN；第三次 ACK 证明 Client 已收到 Server 的序号空间。
- SYN 消耗一个 sequence number，因此对 SYN 的累计确认是 `ISN+1`。
- MSS、Window Scale、SACK Permitted、Timestamp 等 option 只能/主要在 SYN 阶段协商，连接建立后不能随意“重新协商”。

### 状态机级细节

Client 常经历 `CLOSED → SYN-SENT → ESTABLISHED`；Server 常经历 `LISTEN → SYN-RECEIVED → ESTABLISHED`。握手 packet 丢失不会立即失败，而由 retransmission timer 驱动重发。第三个 ACK 可以是纯 ACK，也可以与第一批 application data 同 segment 携带。

### 为什么旧 SYN 是问题

TCP 连接以四元组与序号空间区分新旧数据。如果网络中延迟的旧 SYN/segment 被误当成新连接的一部分，可能污染新状态。握手的双向确认与 ISN 机制让双方能验证“这次连接”的序号上下文。

### 线上案例推演

抓包看到 `SYN → SYN,ACK → ACK` 很快但应用 `accept()` 很慢，说明协议握手与应用 accept queue 消费是两个阶段；此时应查 accept queue/worker，而不是继续解释三次握手本身。
''',
23: r'''
## V2 深入：“为什么三次”应从最小充分信息交换来回答

### 第一性原理

要建立双向可靠字节流，双方都需要知道：①对方选择了什么初始序号；②自己发出的序号信息确实被对方收到。两次交互后 Server 已确认 Client 的 SYN，但 Client 对 Server SYN 的确认还没有回到 Server，因此三次是常规 active/passive open 下同步双方状态的最小自然流程。

### 为什么不是“验证双方收发能力”一句话

“收发能力”过于模糊：网络路径可能在握手后马上变化，三次握手也无法永久证明链路可靠。它真正能证明的是**这些具体 handshake message 已经按序号/ACK 语义到达，从而允许状态机安全推进**。

### 四次是否更安全

没有必要把 Server 的 SYN 与 ACK 拆成两个 packet，它们可以合并成 SYN+ACK，因此一般是三次。特殊 simultaneous open 等路径可能呈现不同 packet 组合，但不改变双方需要同步序号与确认的核心不变量。

### 线上案例推演

面试官问“第二次 SYN+ACK 丢了怎么办”，应立即回到状态机和 timer：Client 没看到 SYN+ACK 仍在 SYN-SENT，Server 仍在 SYN-RECEIVED，双方会按各自重传逻辑继续尝试，而不是说“握手自动变两次”。
''',
24: r'''
## V2 深入：最后 ACK 丢失不代表后续带 ACK 的数据也无效

### 第一性原理

- TCP 状态推进依赖 ACK 是否确认了正确的 SYN sequence，而不是要求“第三个 packet 必须是一个没有 payload 的纯 ACK”。
- Client 在收到 SYN+ACK 后通常可认为本端连接已建立并发送数据；该 data segment 会携带 ACK flag/ack number。
- Server 若仍处于 SYN-RECEIVED，收到一个可接受的 ACK（即使同时带 data）可以完成 handshake，再处理数据。

### 重传与队列

若 Server 一直收不到有效 ACK，会重传 SYN+ACK；超出重试策略后才回收半连接状态。完成握手后，连接才进入 established/accept queue，应用 `accept()` 消费的是已经完成协议握手的 socket。

### `connect()` 的语义

Blocking `connect()` 成功表示本地 TCP stack 完成了连接建立语义，不等于服务端应用已经 `accept()` 或准备好处理请求。Nonblocking connect 则通常通过 writable event + `getsockopt(SO_ERROR)` 判断最终结果。

### 线上案例推演

如果 packet trace 中最后纯 ACK 丢失但紧接着 Client 发 HTTP request，Server 仍响应正常，这并不矛盾；HTTP request 所在 TCP segment 自带有效 ACK，足以让 Server 完成状态推进。
''',
25: r'''
## V2 深入：FIN 只关闭一个发送方向，TCP 才会出现“通常四次”

### 第一性原理

- TCP 是 full-duplex，两端发送方向独立；FIN 的语义是“我之后不再发送新的字节”，不是“整个连接立刻消失”。
- 收到 FIN 的一方先 ACK 是传输层确认，它的应用仍可能有未发送完的数据，因此自己的 FIN 可以稍后再发。
- 当 ACK 与本端 FIN 恰好能合并时，抓包可能表现为三段而非严格四个 packet。

### FIN 与 RST

FIN 是有序 sequence-space 事件，允许接收方读完已排队数据后得到 EOF；RST 更接近异常终止，可能使未读/未确认数据被丢弃并让应用得到 connection reset。`shutdown(SHUT_WR)` 是显式 half-close；`close()` 还涉及 fd 生命周期与 linger 行为。

### 状态机视角

主动关闭方可能经历 `FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT`；被动关闭方常经历 `CLOSE_WAIT → LAST_ACK`。TIME_WAIT 与 CLOSE_WAIT 的根因完全不同：一个是协议正确性状态，一个常反映应用未 close。

### 线上案例推演

若抓包显示 peer FIN 后本机立即 ACK，但 socket 长时间 CLOSE_WAIT，网络已经完成对端关闭通知，问题应转向本地应用为什么没有 close，而不是怀疑 FIN 丢包。
''',
26: r'''
## V2 深入：TIME_WAIT 同时保护“最后 ACK”与“旧序号空间”

### 第一性原理

- 主动关闭方最后发送 ACK 后不能立即忘记连接：若该 ACK 丢失，对端会重传 FIN，需要有人重新 ACK。
- 同一四元组可能以后复用；等待足够时间让旧 duplicate segment 从网络中消失，降低其污染新连接序号空间的风险。
- `2MSL` 是经典协议推导中的时间尺度，不应简单理解成所有 OS 都固定一个完全相同的秒数参数。

### 谁进入 TIME_WAIT

通常是执行 active close 的 endpoint，因此“服务器很多 TIME_WAIT”首先说明服务器在大量连接中主动关闭，不代表服务器一定有 bug。反向代理主动关闭 upstream、短连接 client、健康检查都可能制造大量 TIME_WAIT。

### Linux 调优边界

调 sysctl 前应先看连接复用率、close 方向、端口空间和 NAT。粗暴缩短/绕过 TIME_WAIT 可能隐藏架构问题；现代内核对 TIME_WAIT 使用轻量结构，其内存成本也不能按完整 established socket 机械估计。

### 线上案例推演

若业务每秒创建数万 outbound 短连接且本机 ephemeral port 接近耗尽，根因优先是连接池/HTTP keep-alive/上游复用设计，而不是“TIME_WAIT 数字看起来大”。
''',
27: r'''
## V2 深入：TIME_WAIT 排障必须先区分“状态多”与“资源真的耗尽”

### 第一性原理

看到几十万 TIME_WAIT 时先回答四个问题：谁主动关闭？新建连接速率多少？是否出现端口/NAT table/CPU/内存瓶颈？连接为什么不能复用？只有后两者出现实际症状时才是容量故障。

### 资源模型

Client 主动发起 outbound connection 时更容易受 local ephemeral-port space 与目标四元组复用约束；Server listener 的 FD 上限问题则主要与 active established sockets 相关。NAT gateway 还可能先于后端耗尽 PAT port/conntrack。

HTTP/2/HTTP/3 multiplexing 允许多个 request 共用一条长连接，能显著降低 connection churn；但一条连接承载过多流也有 failure blast radius 和负载均衡粒度 trade-off。

### 排障证据链

用 `ss -s` 看整体状态，按 remote endpoint 聚合 TIME_WAIT，查看应用 connection pool metrics、`ip_local_port_range`、NAT/conntrack 使用率和新建连接失败码。不要把 `ulimit -n` 当唯一指标，因为 TIME_WAIT 并不等价于进程持有一个普通 open fd。

### 线上案例推演

发布后 TIME_WAIT 激增但业务无 error、端口利用低，可能只是实例滚动关闭连接；如果同时出现 `EADDRNOTAVAIL`/connect timeout，则必须进一步验证 ephemeral port 或 NAT 端口耗尽。
''',
28: r'''
## V2 深入：CLOSE_WAIT 的一句话诊断是“内核已收到 FIN，应用还没把 socket 关掉”

### 第一性原理

- Peer FIN 到达后，本地 TCP ACK 并进入 CLOSE_WAIT；这个状态等待的是**本地应用调用 close/shutdown**，不是等待网络继续做某个神秘握手。
- 因此大量长期 CLOSE_WAIT 高度指向 fd 生命周期、异常路径、连接池、阻塞线程等应用问题。
- 与之配对的 peer 可能处于 FIN_WAIT_2，等待本端最终 FIN。

### 为什么会泄漏

常见原因包括 HTTP response body 未关闭、异常返回绕过 defer/finally/RAII、worker 卡死、业务对象仍持有 socket、连接池状态机错误。即使 peer 已经结束，fd 仍占用内核与进程资源。

### 定位方法

先按 PID/fd/remote 聚合，再用 `lsof`、`ss -tanp`、语言 runtime stack/heap profile 找持有连接的调用栈；如果 CLOSE_WAIT 数量与某 API/异常率同步增长，基本可建立因果链。

### 线上案例推演

Java 服务某异常分支没有关闭 response stream，数小时后 CLOSE_WAIT 与 FD 数持续线性增长直到 `Too many open files`。这类故障调 TCP keepalive 无法解决，必须修资源释放路径。
''',
29: r'''
## V2 深入：Half-close 让“发送完成”和“接收完成”成为两个独立事件

### 第一性原理

- `shutdown(SHUT_WR)` 发送 FIN，告诉 peer 本端不会再发送，但本端仍可以 `read()` peer 后续 response。
- 收到 peer FIN 后，应用把缓冲数据读完，再读通常得到 EOF（`read()` 返回 0），这不是 error。
- 这种语义适合“请求体以 EOF 结束、仍等待服务端结果”等协议设计。

### `close()`、`shutdown()` 与引用

`close(fd)` 是描述符生命周期操作；若多个 fd/reference 指向同一 socket，实际 protocol close 语义还与引用计数有关。`SO_LINGER` 可以改变 close 在有未发送数据时的阻塞/复位行为，因此不能把 `close()` 永远等同“优雅 FIN”。

### RST 为什么不同

RST 表示连接状态异常/无效，接收端通常得到 reset error，而不是先消费全部有序数据再 EOF；因此无法替代 half-close 的协议语义。

### 线上案例推演

自定义 RPC 若 Client 发完 request 后需要告诉 Server“请求完整结束”但还要继续收 response，可以用 length framing，也可以设计 half-close；若使用 RST 作为“结束标记”，很容易把正常关闭变成错误路径。
''',
30: r'''
## V2 深入：SYN Flood 攻击的是“握手前状态与资源”，SYN Cookies 是降级型防护

### 第一性原理

- 攻击者大量发送 SYN、伪造源或不完成最后 ACK，使服务端在 SYN-RECEIVED 保留大量半连接状态并重传 SYN+ACK。
- SYN queue 与 accept queue 不同：前者保存未完成握手，后者保存已完成握手、等待应用 `accept()` 的连接。
- SYN Cookies 在压力下把一部分本应保存在 server state 的信息编码进 SYN+ACK sequence，从最终 ACK 恢复/验证，从而降低半连接状态消耗。

### 为什么不是万能方案

Cookies 只针对一类 handshake state exhaustion；攻击仍可能消耗带宽、CPU、NIC、firewall/conntrack，且某些 TCP option/扩展能力在 cookie 路径下可能受限制或需要额外机制。因此正常容量不足时应扩 backlog/应用处理，而不是把 syncookies 当常态性能方案。

### 与 ACK/全连接攻击区分

ACK flood、建立完整连接后的 request flood、TLS handshake flood 都攻击不同资源层。只看 SYN_RECV 数量不够，应结合 SYN rate、SYN+ACK retrans、listen overflow、conntrack/NIC drops、CPU softirq。

### 线上案例推演

新连接失败但 SYN queue 不满、accept queue 满且 worker CPU 高，根因不是 SYN Flood；这是已完成握手后应用消费不及时，应查 accept/worker/backpressure。
''',
31: r'''
## V2 深入：TCP Seq/Ack 的单位是“字节序号”，不是 packet 编号

### 第一性原理

- `SEQ` 标识该 segment payload 在发送方向字节流中的起始位置；ACK 是**累计确认**，表示“下一个期望的字节序号”。
- ACK 可以一次跨过大量字节，因为一个 ACK 可以累计确认此前连续收到的整个区间。
- SYN 和 FIN 也各自占一个 sequence-space 位置，所以即使没有 payload 也会影响 ACK number。

### 乱序与 SACK

若收到后面的 segment 但前面有 gap，累计 ACK 通常停在 gap 左边并产生 duplicate ACK；SACK option 可以额外告诉 sender 哪些非连续 block 已经缓存，从而精确重传缺失范围。

### 抓包工具的相对序号

真实 TCP sequence 是 32-bit 并从随机/伪随机 ISN 开始，不方便人工阅读；Wireshark 常默认显示 relative sequence numbers，把首个序号映射到 0/1。分析 wraparound、PAWS 等高级问题时要知道这是显示层抽象。

### 线上案例推演

如果看到 ACK 持续不前但 SACK blocks 在变化，说明 receiver 仍收到后续数据，只是 sequence gap 未补齐；这比单看“有 retransmission”更能判断 loss/reordering 位置。
''',
32: r'''
## V2 深入：TCP 可靠的是字节流交付，不是业务事务语义

### 第一性原理

TCP 的可靠性由 checksum、sequence/ACK、重传、乱序重组、duplicate suppression、流控和拥塞控制等共同组成。它保证在连接有效时向应用提供有序字节流，但**无法告诉 Client 某个业务操作是否已经 commit**。

### “最后请求是否执行”难题

Client 发送支付请求后连接 reset：请求可能没到 Server、到达但未被应用读、应用已处理但 response 丢失、数据库已 commit 但 ACK 未回。TCP 无法区分这些业务状态，因此需要 request ID、idempotency key、事务状态查询等应用协议设计。

### SACK/重传的边界

SACK 提升丢包恢复效率，但不会改变 cumulative ACK 的基本语义；TCP checksum 也不是端到端内容真实性机制，不能替代 TLS/application checksum。

### 线上案例推演

订单 API 因 timeout 自动重试却产生重复扣款，本质不是“TCP 不可靠”，而是业务把 transport uncertainty 错当成“请求一定未执行”。正确方案是幂等 key + 原子状态持久化。
''',
33: r'''
## V2 深入：RTO、Fast Retransmit、SACK 是不同层次的丢失恢复信号

### 第一性原理

- RTO 是“长时间没有足够进展”的 timer-based fallback，依据 SRTT/RTTVAR 估计并指数退避。
- Fast Retransmit 利用重复 ACK/SACK 等更早推断 gap，不必等 RTO。
- SACK 告诉 sender receiver 已拥有哪些非连续 byte ranges，减少一次窗口内多丢包时的盲目重传。

### 为什么“3 dupACK”不是物理定律

它是经典算法中的启发式阈值，用于在 loss 与 reordering 之间折中。现代 TCP 还可能使用 RACK 基于 packet transmission time/ACK evidence 推断 loss，不再只依赖 duplicate ACK 计数。

### Spurious Retransmission

大幅 reordering、突然 RTT spike、RTO 估计不准都可能导致 segment 实际未丢却被重传。性能分析要结合 original/retrans timestamp、DSACK/RACK 指标，而不是见 retrans 就说链路真的丢包。

### 线上案例推演

高延迟跨洲链路有少量乱序，Wireshark 标大量 Fast Retransmission，但接口 drop 很低。应进一步检查 SACK/DSACK、reordering depth 和 RACK，而不是直接要求运营商“修丢包”。
''',
34: r'''
## V2 深入：滑动窗口把“可靠性”与“流水线并行”结合起来

### 第一性原理

- Stop-and-wait 每个 RTT 只能推进极少数据；滑动窗口允许多个未确认字节同时 in-flight，吞吐上限才可能接近 BDP。
- Sender usable window 同时受 peer advertised `rwnd` 与本地 congestion-control `cwnd` 约束，并随 ACK/应用消费/网络状态动态变化。
- Window Scale 只能在 SYN 中协商，因为双方必须从连接开始就一致解释 16-bit Window 字段的缩放因子。

### Zero Window 与 Persist

如果 receiver application 读得太慢，receive buffer 满，peer 可通告 zero window。Sender 不能继续正常推进数据，但会使用 persist/window probe 机制避免“窗口更新丢失后双方永久等待”。

### Socket buffer 与窗口

`SO_RCVBUF`/autotuning 决定接收 buffer 能力，但 advertised rwnd 还受协议实现和当前 buffer occupation 影响；“把 buffer 调大”也不等价于吞吐一定提高，cwnd/RTT/应用处理仍可能是瓶颈。

### 线上案例推演

`ss -tin` 若显示 `rcv_space`/window 小、peer zero-window，且应用线程消费慢，增加带宽无效；瓶颈在 receiver backpressure。
''',
35: r'''
## V2 深入：“粘包/拆包”是应用错误地把 TCP read 边界当消息边界

### 第一性原理

- TCP 只保证有序 byte stream：一次 `write()` 可能被拆成多个 segment，多次 `write()` 也可能在 receiver 一次 `read()` 中同时出现。
- 因此应用协议必须显式 framing，不能用 `recv()` 返回一次就假设得到一个完整业务 message。
- UDP 保留 datagram boundary，所以不存在同一种语义问题，但 datagram 仍可能截断/丢失/乱序。

### Framing 方案

常见有固定长度、delimiter、length-prefix、TLV、自描述 framing。Length-prefix parser 应维护 `READ_HEADER → parse length → READ_BODY → emit frame` 状态，并防御恶意超大 length 导致内存 DoS。

Protobuf 定义 message serialization，却不会自动告诉 raw TCP stream 下一条 protobuf 从哪个 byte 开始；gRPC 会在 protobuf 之外再增加自己的 message framing。

### 工程边界

TLS 同样是 stream abstraction；`SSL_read()` 也不与上层业务 message 一一对应。高性能 parser 通常需要 incremental buffer、partial header/body、multiple frames per read。

### 线上案例推演

线上偶发 JSON parse error，只在高 QPS 出现，很可能是应用默认“一次 read=一条 JSON”。通过人为把 packet 分片或一次发送多条消息即可稳定复现，这比调 MTU 更能验证根因。
''',
36: r'''
## V2 深入：Flow Control 保护接收端，Congestion Control 保护共享网络

### 第一性原理

- `rwnd` 反映 receiver buffer/消费能力，防止 sender 把接收端内存淹没；这是端到端 flow control。
- `cwnd`/pacing 根据网络 congestion signal 控制 in-flight/发送速率，防止路径 queue/loss 崩溃；这是 congestion control。
- 实际发送通常受到两者更严格者约束，近似理解为 `in_flight ≤ min(rwnd, cwnd)`。

### 信号归类

Zero Window 是 flow-control 信号；loss/ECN/RTT growth 等主要用于 congestion signal。应用读取慢会减少可用 receive buffer，导致 rwnd 下降，但并不意味着网络拥塞。

### 为什么必须分开

如果混淆两者，就会对 zero-window 去调 CUBIC/BBR，或对拥塞丢包只增大 receiver buffer。排障必须同时看 `cwnd`、`rtt`、retrans 与 advertised window/send-q/recv-q。

### 线上案例推演

吞吐低时若 `cwnd` 很大、无 retrans，但 peer advertised window 极小，网络容量并不是瓶颈；应查对端应用或 receive buffer。
''',
37: r'''
## V2 深入：Slow Start 的“慢”是相对于一开始就按未知容量全速发送

### 第一性原理

- Slow Start 从相对较小的 initial congestion window 出发，通过 ACK clock 快速增加 cwnd；理想化看每 RTT 近似指数增长。
- 其目标是在不知道 path capacity 的前提下快速探测，同时避免直接向网络注入一个巨大 burst。
- 达到 ssthresh、检测 congestion 或由现代算法的 startup detector 判断后进入更保守增长阶段。

### 为什么短请求敏感

如果 response 只有几 RTT 就结束，连接可能大部分生命周期都处于 startup，初始窗口与 RTT 对 TTFB/下载完成时间影响很大。Connection reuse/HTTP2/QUIC resumption 可以避免每个小请求重新从冷启动状态开始。

### 现代边界

CUBIC 可结合 HyStart++ 更早发现 delay increase，BBR 的 startup 又是另一种容量探测逻辑；因此面试时区分“经典 RFC 5681 slow start”与“某算法的具体 startup 实现”。

### 线上案例推演

高 RTT 用户下载很多几十 KB 对象明显慢，而大文件最终吞吐正常，可能是每个新连接 startup/handshake 成本占比过高；优先验证连接复用和 RTT，而不是只看峰值带宽。
''',
38: r'''
## V2 深入：Fast Retransmit 负责“发现并重传”，Fast Recovery 负责“如何继续发”

### 第一性原理

- Duplicate ACK 表明 receiver 仍在收到后续数据，却缺前面的 gap，因此 sender 可以在 RTO 前推断 loss 并重传。
- Fast Recovery 的目标是在单个/少量 loss 后不要完全把管道清空，而是根据 ACK 继续估计网络中仍有多少数据在飞。
- Reno/NewReno/PRR 等对 loss recovery 中 cwnd/发送额度的计算不同，不能把所有现代 TCP 都说成同一个“3 dupACK 后 cwnd/2”公式。

### NewReno 与多丢包

Reno 在一个 window 多 packet loss 时恢复效率差；NewReno 借 partial ACK 改进，而 SACK/现代 recovery 能更明确知道多个 hole。PRR 进一步控制 recovery 期间发多少新数据，使发送更贴近目标 ssthresh。

### 线上案例推演

抓包中大量 duplicate ACK 后快速重传，但 connection 没有明显停顿，说明 fast recovery 在工作；若频繁触发 RTO 则影响通常更重，应继续查严重 loss、ACK path 或 RTT variance。
''',
39: r'''
## V2 深入：`rwnd/cwnd/ssthresh` 分别描述接收容量、网络容量估计和增长阶段边界

### 第一性原理

- `rwnd` 来自 peer，代表 flow-control ceiling；`cwnd` 在 sender 本地，是 congestion-control state；`ssthresh` 是经典 TCP 决定 startup/avoidance 行为的状态变量。
- 发送受 `min(rwnd,cwnd)` 近似约束，但还受 application data、pacing、TSO、qdisc、socket buffer 等限制。
- `ssthresh` 不是接收窗口，也不是“网络带宽大小”。

### 高 BDP 与 Window Scale

TCP header 原始 Window 字段只有 16 bit，若不协商 scaling，在高 BDP 路径上 rwnd ceiling 可能严重限制吞吐。Window Scale 在 SYN 中双向协商，并且每个方向的 scale factor 可以不同。

### 诊断思路

`cwnd` 大但吞吐低：检查 application-limited、rwnd、loss、pacing、CPU、send buffer；`rwnd` 大也不代表应用消费快，因为 kernel receive buffer/autotuning 可能暂时吸收数据。

### 线上案例推演

1Gbps/100ms path 的 BDP 约 12.5MB；若 effective receive window 只有几百 KB，即使零丢包和巨大 cwnd，也无法跑满链路。
''',
40: r'''
## V2 深入：Reno 用 ACK-clock 线性探测，CUBIC 用“距上次拥塞事件的时间”构造三次函数

### 第一性原理

- Reno congestion avoidance 的 additive increase 在高 BDP 路径上从一次 loss 恢复到大 window 可能非常慢。
- CUBIC 以此前拥塞窗口附近为参考，用 cubic function 随时间增长：远离旧最大值时增长更快，接近时更平缓以提高稳定性。
- CUBIC 仍是 loss/ECN 响应型拥塞控制，并需与 Reno 流量保持合理 coexistence。

### 为什么适合长肥网络

高带宽、长 RTT 意味着达到满 BDP 需要很大的 cwnd。Reno 每 RTT 小幅增长会耗费大量时间；CUBIC 的增长主要以 elapsed time 表达，降低对 RTT 的直接敏感度并提升 scalability。

### Bufferbloat 边界

Loss-based 算法通常持续增大发送直到 queue/loss/ECN 提示拥塞；若 bottleneck buffer 过大且 AQM 不佳，可能形成高 standing queue/RTT，即 bufferbloat。CUBIC 本身并不能保证低延迟。

### 规范状态

CUBIC 已由 RFC 9438 标准化，并更新 RFC 5681 对更激进增长行为的约束；回答时不要继续把 RFC 8312 当当前主规范。
''',
41: r'''
## V2 深入：BBR 尝试建模瓶颈，而 CUBIC 主要从 loss/ECN 反馈调窗口

### 第一性原理

- BBR 估计 bottleneck bandwidth 与 propagation RTT，目标是在接近 BDP 的 in-flight 下用 pacing 控制发送，而不是必须把 queue 填到 loss 才知道容量。
- Pacing 很关键：即使平均速率相同，burst 发送也会瞬间形成 queue/drop；BBR 用 pacing rate 把 packet 更均匀地送入路径。
- CUBIC 更典型地根据 congestion event 减窗、再按 cubic growth 探测。

### BBR 与低延迟不是同义词

模型估计有误、多个 flow 竞争、ACK aggregation/policer、版本策略都会影响 queue 和公平性。BBR 的目标不是“永不丢包”或“永远最低 RTT”，而是通过模型控制 operating point。

### 公平性问题

不同 congestion controller 竞争时，共享 bottleneck 上的 throughput/queue 占用取决于算法响应方式、RTT、AQM 等；不能用单 flow benchmark 推导全网公平。

### 2026 规范状态

截至 2026-09-02，IETF CCWG 的 BBR 文档仍是 `draft-ietf-ccwg-bbr-06` Active Internet-Draft，不应写成已发布 RFC。工程实现还要明确具体 BBR 版本/内核实现。
''',
42: r'''
## V2 深入：Nagle 针对 tinygram，`TCP_NODELAY` 是延迟/吞吐取舍开关

### 第一性原理

- Nagle 的经典目标是在存在未确认小数据时合并新的小 write，避免大量 tiny TCP segments 浪费带宽/处理开销。
- 交互式 RPC 常更怕几十毫秒额外等待，因此设置 `TCP_NODELAY`，但这并不取消 TCP buffering、congestion control 或调度延迟。
- Delayed ACK 与 Nagle 相互作用时可能放大小消息延迟，因此需要理解双方算法，而不是只背一个 socket option。

### 应用层 batching

现代 RPC framework 往往自己做 coalescing/batching/writev，因为应用更知道 message boundary 和 latency budget。这样可以在关闭 Nagle 的同时仍避免每个字段都变成一个 packet。

### 边界与反例

一次 `write(<MSS)` 不代表内核一定立即上线：cwnd/rwnd、qdisc、pacing、scheduler、TLS record 都可能延迟。`TCP_NODELAY` 只改变 Nagle 相关发送决策。

### 线上案例推演

小 RPC p99 恰好常出现约一个 delayed-ACK timer 量级延迟时，可以 A/B `TCP_NODELAY`、抓包看 small segment/ACK timing，并检查框架 batching，而不是只增加线程数。
''',
43: r'''
## V2 深入：`TCP_NODELAY` 只控制 Nagle，不是“低延迟模式”总开关

### 第一性原理

开启 `TCP_NODELAY` 后，小 write 不再因为 Nagle 的“等待未确认数据/合并”规则而被延迟；但 TCP 仍然要遵守发送窗口、拥塞控制、重传、qdisc 与 NIC scheduling。

### 与 `TCP_CORK`/writev 的关系

Linux `TCP_CORK` 倾向暂时阻止不完整 frame 发送以便应用组装较大 segment，适合明确知道“接下来还有 header/body”的场景；`writev` 则可以一次 syscall 提交多个 buffer，减少 syscall/copy/小 write，而不改变协议本身。

### 为什么游戏仍可能不用 TCP

即使 NODELAY，TCP 仍提供严格有序 stream：某个 packet loss 会阻塞其后的字节交付。对位置更新这类“旧数据过期”的实时业务，UDP/QUIC datagram 可能更匹配语义。

### 线上案例推演

开启 NODELAY 后平均 latency 降了但 PPS/CPU 暴涨，说明原先 Nagle 在帮你聚合小写；下一步应在应用层做 batching/writev，而不是简单在“延迟”和“CPU”之间二选一。
''',
44: r'''
## V2 深入：BDP 是“填满路径需要多少在途数据”的第一性尺度

### 第一性原理

`BDP = bottleneck bandwidth × RTT`。如果 in-flight/window 长期明显小于 BDP，sender 即使无丢包也无法保持 bottleneck 持续忙；如果远大于真实 BDP，多余数据往往进入 queue，增加 latency。

### 数值直觉

1Gbps × 100ms ≈ 100Mbit ≈ 12.5MB。要跑满这样的单 TCP flow，cwnd、rwnd、socket buffers 等必须允许约这个量级的数据同时在飞。卫星/跨洋网络因 RTT 高，BDP 特别大。

### 多连接为什么“看起来更快”

多个 TCP connection 各有独立 cwnd/window，历史上可绕过单连接窗口或更快聚合带宽，但也可能增加公平性问题、握手开销和网络拥塞。HTTP/2/3 更强调复用单连接，现代 stack 通过 Window Scale/autotuning 改善单流能力。

### QUIC 同样受 BDP

QUIC 虽非 TCP，但可靠 stream 与 congestion control 仍需足够 in-flight 才能利用高 BDP path；“UDP 没窗口所以不受 BDP”是错误理解。
''',
45: r'''
## V2 深入：listener 不是一个队列，握手队列和 accept queue 代表不同阶段

### 第一性原理

- 未完成三次握手的连接占 SYN/half-open 状态；握手完成后连接进入等待应用 `accept()` 的 accept queue。
- `listen(backlog)` 与内核 `somaxconn`、`tcp_max_syn_backlog` 等共同影响容量，但具体语义是 OS 实现相关，不能把一个数字简单等于“所有 TCP 连接上限”。
- SYN queue 满与 accept queue 满的现象/解决方法不同：前者关注握手攻击/丢包/容量，后者关注应用 accept 消费速度。

### 如何判断哪个队列满

结合 listen overflow/drop counters、SYN_RECV 数、handshake completion、`ss -lnt` queue 指标、SYN/SYN+ACK retrans 抓包。若客户端握手已完成却迟迟无法被应用处理，worker/accept starvation 更可疑。

### `SO_REUSEPORT`

多个 listener 可以在同一地址/端口上由内核分流 connection，减少单 acceptor 锁/CPU 热点并改善 NUMA locality，但负载分配、BPF selector、连接迁移/滚动发布仍需设计。

### 线上案例推演

流量峰值时 SYN_RECV 不高但 listen overflow 增长、CPU worker 满，说明客户端已经能握手，瓶颈是 accept queue/应用消费；开 syncookies 不会修复这个问题。
''',
})
PACKS.update({
46: r'''
## V2 深入：自己做“可靠 UDP”意味着重新面对传输协议的全部难题

### 第一性原理

- UDP 只提供 datagram delivery 与 checksum 等基础能力；若要可靠传输，必须自己定义 packet number/sequence、ACK、重传、乱序缓存、duplicate detection。
- 可靠性之外还必须处理 flow control 与 congestion control，否则一个“可靠”协议可能把 receiver 或共享网络打爆。
- 一旦加入连接身份、path validation、MTU、加密、key update、版本协商、多路复用，复杂度已经接近完整现代 transport protocol。

### 为什么 RUDP 难

Loss detection 不能只设固定 timeout：RTT 会变化、ACK 会丢、packet 会乱序。重传还要避免 ambiguous ACK；receiver buffer 需要上限；packet number wrap/重放/伪造需要安全处理；拥塞控制要能与其他 Internet traffic 公平共存。

### 什么时候值得定制

非常专用、封闭网络或游戏/媒体等业务可能只需要部分可靠性，例如关键状态可靠、位置更新可丢弃；这时自定义 protocol 的价值在于语义优化，而不是“比 TCP 随便快”。公网通用可靠传输更应优先成熟 QUIC/SCTP/现有库。

### 线上案例推演

自研 UDP 传输压测很快、上线后跨网丢包导致带宽暴涨，通常是重传算法没有拥塞退避；“丢了就立刻重发”会让真正拥塞更严重，形成正反馈。
''',
47: r'''
## V2 深入：UDP 保留 datagram 边界，但应用仍必须处理截断与大小限制

### 第一性原理

- 一次 UDP send 形成一个 datagram，receiver 一次接收对应一个 datagram 语义；多个 send 不会像 TCP stream 那样自然合并成一个无边界字节流。
- 如果应用 receive buffer 小于 datagram，具体 API 通常返回截断数据并丢弃剩余部分/提供 truncation 标志；无法像 TCP 下一次 read 继续拿“后半包”。
- Datagram boundary 不等于可靠：UDP 仍可 loss、duplicate、reorder。

### 大包问题

UDP datagram 过大更易触发 IP fragmentation 或超过 path MTU；DNS/QUIC 等协议都会主动控制 datagram size。EDNS0 扩展 DNS UDP payload 能力，但遇到 truncation/网络限制仍可能 fallback 到 TCP。

### 与 QUIC 的关系

一个 UDP datagram 可以承载一个或多个 QUIC packet（视版本/packet type），而 QUIC stream 的 message/byte-stream 语义建立在 QUIC 层，不是 UDP 自身提供。

### 线上案例推演

如果 UDP 应用小消息正常、偶发大消息完全消失，检查 application recv buffer、IP fragmentation/PMTU 和 firewall fragment policy；不要把它归结为“UDP 粘包”。
''',
48: r'''
## V2 深入：QUIC 选择 UDP 的核心是可部署性与协议演进速度

### 第一性原理

- 直接修改 TCP 意味着依赖 OS kernel、middlebox、NAT/firewall 对新 option/behavior 的支持，部署周期很长且容易遭遇 protocol ossification。
- UDP 是互联网中广泛可穿越的最小 datagram substrate，QUIC 把传输状态机放到用户态，使应用/库可以更快升级版本和 congestion/loss-recovery 实现。
- QUIC 自己提供 security、connection ID、stream、flow control、loss recovery、congestion control，UDP 只是承载层。

### Protocol Ossification

长期中间盒往往假设 TCP header/handshake 固定，对未知 option 或新行为丢弃/篡改，导致即使端点支持新功能也无法可靠部署。QUIC 大量加密 transport metadata、使用版本协商与可变 connection ID，目的之一就是降低未来协议被网络“固定死”的风险。

### UDP 被封锁怎么办

真实客户端必须支持 fallback，例如 HTTP/3 失败后回 HTTP/2/TCP；QUIC 不是假设所有网络都允许 UDP，而是将失败检测与替代路径纳入部署策略。

### 线上案例推演

某企业网络 HTTP/3 success rate 显著低于家庭网络，可按 UDP/443 reachability、NAT timeout、middlebox policy 分组，并验证是否快速 fallback；不能因为平均 HTTP/3 更快就强制只启用 QUIC。
''',
49: r'''
## V2 深入：HTTP/2 的多路复用止于 TCP byte stream，HTTP/3 把独立性下沉到 transport stream

### 第一性原理

- HTTP/2 的 stream 是 HTTP framing 层概念，但所有 frame 最终按一个 TCP ordered byte stream 交付。
- TCP sequence gap 出现时，后续已到达字节也不能越过缺口交给 HTTP/2 parser，因此无关 stream 会一起等待。
- QUIC 为每个 stream 维护独立 offset/reassembly，某 stream 丢 packet 后，其他 stream 的完整数据仍可交付。

### 仍然存在的 HOL

HTTP/3 不会消除所有“等待”：同一个 QUIC stream 内仍需有序；QPACK dynamic table 可能产生 header dependency；一个 UDP datagram 若同时承载多个 stream frame 丢失，这些 frame 都需恢复。它解决的是 TCP 单一字节序列造成的**跨流 transport HOL**。

### Congestion Control 仍共享

同一 QUIC connection 的多个 stream 通常共享 path 与 congestion controller，所以 congestion event 会影响整体发送速率；“不跨流 HOL”不等于每个 stream 拥有独立带宽。

### 线上案例推演

在 2% loss + 高 RTT 环境并发下载多个资源，HTTP/2 某 TCP loss 可能让所有 stream 的应用交付暂停；HTTP/3 通常能让未受影响 stream 继续推进，差异更容易反映在 tail latency 而非无损局域网峰值。
''',
50: r'''
## V2 深入：Connection ID 把“连接身份”从固定四元组中解耦出来

### 第一性原理

- TCP connection 通常与源/目的 IP/port 强绑定；Wi-Fi→5G 导致 local address 变化时，原四元组无法继续代表同一 TCP flow。
- QUIC 使用 Connection ID 识别逻辑连接，并通过 PATH_CHALLENGE/PATH_RESPONSE 等 path validation 验证新地址可达，支持 NAT rebinding 和主动 migration。
- Connection migration 不等于 multipath：标准迁移通常是把活动路径切到新 path；MPTCP/MPQUIC 类方案才强调多 path 同时使用。

### 安全与负载均衡

若攻击者仅伪造新源地址，path validation 防止服务器立即把大量数据发往 victim，降低 amplification/connection hijack 风险。Load balancer 则可能需要从 CID 中编码/查找 backend routing 信息，否则四元组变化后 packet 可能被 hash 到错误 server。

### 隐私边界

长期使用固定 CID 会成为跨网络追踪信号，所以 QUIC 支持发放/轮换多个 Connection ID；面试回答可指出 migration、routing 与 privacy 三者存在 trade-off。

### 线上案例推演

移动 App 从 Wi-Fi 切 5G 后 TCP WebSocket 重连，而 QUIC session 能继续时，用户感知收益来自避免完整连接/认证重建；若 LB 不理解 CID，迁移反而可能导致 packet 落到无状态 backend。
''',
51: r'''
## V2 深入：QUIC 减少的是“传输 + TLS 串行建连成本”，0-RTT 则用历史信任换延迟

### 第一性原理

- QUIC 把 TLS 1.3 handshake 集成到 transport 建连，不再先完成 TCP 三次握手再开始 TLS，因此首次安全可用数据路径减少串行 RTT。
- 恢复连接可使用 PSK/session ticket，并在满足条件时发送 0-RTT early data；Server 仍可能拒绝 early data，Client 必须能重放到 1-RTT 路径。
- 0-RTT early data 具有 replay 风险，因此只适用于可安全重复、服务器有 anti-replay 策略的操作。

### Retry 为什么可能增加 RTT

QUIC Server 可先发送 Retry，要求 Client 证明源地址可达/携带 token，降低 spoofed-source amplification，但代价是额外 round trip。是否启用取决于 DDoS/地址验证与 latency trade-off。

### Session ticket 的边界

Ticket 是恢复凭据，不等于“永久 session”；有过期、key rotation、跨机房共享/隔离、安全策略问题。0-RTT 还不能依赖本次 handshake 新协商出来的所有参数。

### 线上案例推演

静态 GET 在恢复连接中使用 0-RTT通常风险较低；创建订单/转账即使 HTTP 方法写成 POST/GET 都不应只看方法名，真正标准是操作是否可重放与服务端能否防重复执行。
''',
52: r'''
## V2 深入：QUIC 把 flow control 与 congestion control 重新实现了一遍，而且是分层的

### 第一性原理

- QUIC stream flow control 限制单 stream 可发送多少，connection-level flow control 限制所有 stream 的 aggregate，二者共同保护 receiver memory/consumption。
- Congestion control 则限制对网络的发送压力，QUIC RFC 9002 给出 loss detection 与 NewReno-like baseline，也允许实现其他合规算法。
- QUIC ACK 确认的是 packet number ranges；可靠 stream 的 byte offsets 与 packet number 解耦，因此 packet 被重传时通常以新 packet number 携带同一 stream data。

### 为什么这很重要

TCP 的 packet sequence 与 byte sequence 紧密绑定；QUIC 分离“哪次 packet transmission”与“stream 哪段数据”，能更清晰测 RTT、避免 retransmission ambiguity，并支持 packet-level ACK ranges。

### CUBIC/BBR

QUIC 可以使用 CUBIC、BBR 等 congestion controller，只要满足互联网拥塞控制安全要求；不能因为底层 UDP 没有内建 CC 就让应用任意发送。

### 线上案例推演

HTTP/3 某 stream 停住时，要同时检查 stream MAX_STREAM_DATA、connection MAX_DATA、congestion window、loss recovery；只看 UDP socket send buffer不足以解释 QUIC 层 backpressure。
''',
53: r'''
## V2 深入：DNS 解析是一条多级缓存 + 委派链，不是每次都从 Root 开始

### 第一性原理

典型客户端把问题交给 recursive resolver；resolver 若无缓存，依据 Root → TLD → authoritative referral 逐步找到权威答案。浏览器、OS、local stub、递归 resolver、应用自身都可能缓存，因此真实请求常在前几层就命中。

### CNAME 与额外查询

若名字返回 CNAME，resolver 还需解析 canonical target；长 CNAME chain 增加 lookup latency、失败点与 DNS packet size，也影响 CDN/证书/运营管理。最终 A/AAAA 还会进入连接 Happy Eyeballs 等后续过程。

### TTL 与真实一致性

TTL 是 DNS cache 的协议性过期上限/指导，但本地实现可能有最小/最大 TTL、prefetch、serve-stale、application cache 等策略，因此“权威改完 TTL 秒后全球必然完全一致”过于绝对。

### 线上案例推演

域名切流后只有部分 ISP 用户仍命中旧 IP，应按 resolver/ASN 收集实际 answer 与 TTL，确认是不是 recursive cache，而不是只在权威 DNS 控制台反复查看新记录。
''',
54: r'''
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
''',
55: r'''
## V2 深入：DNS 的 transport 选择取决于场景，不是“53 端口=UDP”

### 第一性原理

- 经典 DNS query 常优先 UDP 以减少 connection overhead，但 DNS 同样定义 TCP transport。
- UDP response 若设置 TC（Truncated）bit，传统 resolver 可用 TCP 重试；AXFR/IXFR 等 zone transfer 也依赖有序可靠 transport。
- EDNS0 扩展可用 UDP payload size，但 path MTU、fragmentation 和 middlebox 使“越大越好”并不成立。

### 现代加密 DNS

DoT 在 TLS 上承载 DNS，DoH 在 HTTPS 上承载 DNS；它们保护 Client→Resolver 传输的机密性/完整性，不等于 DNSSEC。DNSSEC 验证 DNS data 的来源/完整性链，不能隐藏 query 内容。

### 工程边界

防火墙若只允许 UDP/53 而禁 TCP/53，会产生“小 DNS 正常、大/特殊查询失败”的隐蔽问题。递归 resolver 应监控 TCP fallback/TC rate/DNSSEC validation failure。

### 线上案例推演

新增大量 DNSSEC record 后部分用户解析失败，抓包发现 UDP response truncated 但 TCP/53 被防火墙丢弃；这不是权威 record 本身错误，而是 transport fallback 被阻断。
''',
56: r'''
## V2 深入：DNS Record Type 描述的是不同“命名关系”，不是同一种 IP 映射

### 第一性原理

- A/AAAA：name → IPv4/IPv6 address；CNAME：alias → canonical name；MX：domain → mail exchanger；NS：zone delegation/authoritative server；TXT：通用文本载体。
- DNS lookup 不是“最终一定得到 A”：不同应用主动请求不同 RR type，并按协议解释 priority/target/metadata。
- MX/NS target 通常还需进一步解析 A/AAAA，形成依赖链。

### 常见扩展

SRV 描述 service priority/weight/port/target；CAA 限制哪些 CA 被授权为该域签发证书。TXT 被 SPF、DKIM/验证等广泛复用，但并非结构化数据库的理想替代。

### Apex 与 CNAME

Zone apex 需要同时存在 SOA/NS 等记录，传统 DNS 语义下不能简单把 apex 做普通 CNAME；云 DNS 的 ALIAS/ANAME 类能力属于 provider-specific flattening，不等于协议出现了一个标准 CNAME 例外。

### 线上案例推演

邮件收不到时不能只 `dig A domain`；应查 MX target、priority、目标 A/AAAA、SPF/DKIM TXT、反向 DNS 等完整邮件 DNS 链。
''',
57: r'''
## V2 深入：TTL 控制缓存新鲜度，Negative Caching 控制“不存在答案”的记忆

### 第一性原理

- Positive response 的 TTL 决定 resolver 可缓存该 RR 多久；TTL 较长减少 authoritative QPS/延迟，较短提升切流速度但增加解析负载。
- NXDOMAIN/NODATA 等 negative result 也需要缓存，否则不存在名字会持续打到 authority；RFC 2308 定义了相关机制。
- SERVFAIL 与 NXDOMAIN 语义不同：前者是解析失败，后者是权威意义上的名字不存在，不能简单同等长期缓存。

### 为什么 TTL=0 仍未必“瞬时一致”

终端应用、浏览器、JVM、OS、代理可能有独立缓存策略；连接池还可能继续复用旧 IP 上已经建立的 TCP connection。所以 DNS TTL 只是切流路径的一部分。

### CDN TTL 设计

GSLB/CDN 常在健康故障切换速度、resolver load、缓存命中和流量稳定性之间选 TTL；极短 TTL 也受 recursive resolver 最小缓存策略影响。

### 线上案例推演

权威 TTL 已降到 30 秒但发布后 10 分钟仍有旧流量，先分辨是 DNS answer 旧、Client DNS cache 旧，还是 HTTP keep-alive/QUIC connection 仍复用旧 endpoint。
''',
58: r'''
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
''',
59: r'''
## V2 深入：DNSSEC 与 DoH/DoT 的安全目标完全不同

### 第一性原理

- Cache poisoning 试图让 resolver 接受伪造 DNS data；transaction ID/source-port entropy 等提高伪造难度，DNSSEC 则提供可验证的签名链。
- DNSSEC 保护 data origin authentication 与 integrity（以及 authenticated denial），**不加密 query**。
- DoH/DoT 加密 Client↔Resolver transport，防本地链路旁观/篡改，但如果 resolver 本身恶意，它仍知道并能控制自己返回什么（除非 Client同时 DNSSEC validate）。

### Amplification

DNS UDP 可被源地址 spoof 利用：攻击者发送小 query、伪造 victim IP，使大量 resolver/authority 把更大 response 发给 victim。BCP 包括 source address validation、限制开放递归、response rate limiting 等。

### 安全边界

DoH 还改变企业可观测/策略路径，可能绕过本地 DNS control；安全讨论要区分 confidentiality、integrity、resolver trust、endpoint policy。

### 线上案例推演

公司网络 DoH 开启后传统 DNS firewall 失去可见性，不代表 DNSSEC 失效；这是“加密到外部 resolver”改变控制点，应在 endpoint/browser/resolver policy 层治理。
''',
60: r'''
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
''',
})
PACKS.update({
61: r'''
## V2 深入：HTTP/1.1 报文必须同时理解“语义”和“framing”

### 第一性原理

- HTTP 语义由 method、target、status、header fields、representation 等组成；HTTP/1.1 的文本报文只是承载这些语义的一种 messaging syntax。
- Request 由 request-line + fields + 可选 content 组成；Response 由 status-line + fields + 可选 content 组成。是否有 body 不能只看“有没有 Content-Length”，还受 method/status 语义约束。
- Parser 必须严格处理 message boundary，否则容易出现 request smuggling、desync 等安全/代理一致性问题。

### 特殊 body 语义

HEAD 的响应应表现得像对应 GET 的 metadata，但没有实际 response content；1xx、204、304 等状态对 content/framing 有特殊规则。CONNECT 成功后连接语义又转为 tunnel，不能继续用普通 message body 规则机械解析。

### Request Target

HTTP/1.1 存在 origin-form、absolute-form、authority-form、asterisk-form 等 request-target 形式，分别对应 origin server、proxy、CONNECT、OPTIONS * 等场景。面试高级回答可指出 proxy 请求与普通 origin 请求的 request-line 不完全相同。

### 线上案例推演

若自研 proxy 对 204 response 仍按错误 Content-Length 等待 body，连接可能卡死并污染后续 keep-alive message boundary；这类问题属于 HTTP framing/parser，而不是 TCP 丢包。
''',
62: r'''
## V2 深入：GET/POST 的关键是 method semantics，URL/body 只是常见用法

### 第一性原理

- `safe` 表示客户端请求的语义是只读/不期望改变服务器状态；`idempotent` 表示相同请求重复执行一次或多次，对预期服务器状态的效果相同；`cacheable` 是缓存规范/响应指示决定的另一维度。
- GET 是 safe、idempotent；PUT/DELETE 语义上 idempotent 但不 safe；POST 一般不保证 idempotent。
- Method 语义影响 retry、cache、crawler、proxy 行为，因此不能只根据“GET 参数在 URL，POST 参数在 body”回答。

### 幂等不是“响应完全一样”

DELETE 第一次返回 204、第二次可能 404，但资源最终状态仍是“被删除”，所以语义可以是 idempotent。支付 POST 可通过 Idempotency-Key 把业务操作设计成可安全重试，但这是应用层额外协议，不会把 POST 标准语义改成天生幂等。

### GET Body

规范并未把“GET 绝对不能有 content”简单定义成语法错误，但其语义缺乏通用定义，许多 server/proxy/cache 不支持或忽略，因此工程上不应依赖。

### 线上案例推演

客户端 timeout 自动 retry 一个创建订单 POST，若没有幂等 key，transport uncertainty 可能变成重复订单；面试应把 HTTP method semantics 与业务 exactly-once 设计连起来。
''',
63: r'''
## V2 深入：Status Code 体现“这次 HTTP 交互处在哪个故障层”

### 第一性原理

- 301/308 是永久重定向语义；302/307 是临时语义。307/308 明确保留 method/content，而历史 user-agent 对 301/302 的 POST 可能改成 GET，因此实际行为需要理解兼容历史。
- 401 表示需要/缺失有效 authentication credentials，通常伴随 `WWW-Authenticate`；403 表示服务器理解身份/请求但拒绝授权或策略不允许。
- 502 是 gateway/proxy 从 upstream 获得无效/失败 response；504 是 gateway 等 upstream 超时；408 是**当前 server 等 client request 超时**，责任方向不同。

### 代理链思维

Client → CDN → L7 LB → service → downstream。某层返回 502/504 时，必须知道谁是“gateway”，它的 upstream 是谁。502 可以来自 connection reset、protocol parse failure、TLS to upstream failure 等，并不等于 upstream 返回了一个 HTTP 500。

### 线上案例推演

用户看到 504，而 service access log 没有对应 request，问题可能发生在 LB→service 建连/排队前；若 service 收到并处理 10s 而 LB timeout 5s，则 service 最后返回 200 也无法改变客户端已经收到 504 的事实。
''',
64: r'''
## V2 深入：HTTP Stateless 指每个请求语义可独立解释，不代表应用不能有状态

### 第一性原理

- HTTP 本身不要求服务器为协议正确性保留“上一个请求执行到哪”的隐式会话；应用需要用户状态时通过 Cookie、Authorization、URL/token 等显式携带关联信息。
- Session 常把状态保存在 server-side store，Cookie 只携带 opaque session ID；token/JWT 可把部分 claim 携带在客户端，但带来撤销/更新/泄漏风险。
- “无状态服务”与“HTTP 无状态协议”不是同义词：服务仍可访问数据库、cache、session store。

### Cookie 安全属性

`Secure` 限制安全 transport 发送；`HttpOnly` 降低脚本读取 cookie 的能力；`SameSite` 控制 cross-site request 场景，有助于 CSRF 风险治理。它们解决不同威胁，不应合成一句“Cookie 加密”。

### 水平扩展

Server-side session 可以通过 shared store、consistent routing/sticky session 或 session replication 扩展；JWT 免集中 session lookup，但撤销、key rotation、权限变更需要额外机制。

### 线上案例推演

多实例扩容后用户随机掉登录，如果 session 只存在单机内存且 LB 没有粘性/共享 store，就属于应用会话架构问题，而非 HTTP keep-alive 故障。
''',
65: r'''
## V2 深入：HTTP Persistent Connection 是“协议复用连接”，TCP 长连接只是底层连接存活

### 第一性原理

- TCP 只知道一个 byte-stream connection；HTTP persistent connection 定义多个 request/response 如何在同一 transport connection 上连续使用。
- HTTP/1.1 默认持久连接减少 TCP/TLS handshake、slow-start 与 socket churn；连接池进一步跨业务请求复用这些 connection。
- TCP Keepalive 是内核空闲连接探测机制，HTTP `Keep-Alive`/persistent semantics 是应用协议层概念，完全不同。

### Connection Pool 的生命周期

长期 idle connection 可能被 NAT/LB/server timeout silently 删除；Client pool 必须有 max idle/lifetime、health/retry 逻辑。连接无限长也会阻碍 backend rebalancing、证书/key rotation、故障恢复。

### HTTP/2 连接数量

HTTP/2 multiplexing 显著减少需要的并发 TCP connection，但 browser 仍可能因不同 origin、proxy、connection coalescing 条件、故障隔离等维护多连接；“HTTP/2 全浏览器只一条 TCP”不准确。

### 线上案例推演

服务端 keep-alive timeout 60s，而 Client pool 复用 10 分钟 idle socket，会频繁出现第一请求 reset；调 TCP keepalive 未必有用，更应让 pool lifetime 与中间盒/Server timeout 协调。
''',
66: r'''
## V2 深入：HTTP/1.1 Framing 必须知道 message content 到哪里结束

### 第一性原理

- `Content-Length` 明确 content 长度；chunked transfer coding 把未知总长度的 content 分成 chunk 并用终止 chunk 标记结束。
- HTTP/1.1 persistent connection 不能依赖“server close 就代表 body 结束”作为所有 response 的默认方式，否则无法高效复用连接。
- HTTP/2/3 使用 binary frame/stream boundary，不再使用 HTTP/1.1 `Transfer-Encoding: chunked` 作为 message framing。

### Request Smuggling

若前置 proxy 与 backend 对 `Content-Length`/`Transfer-Encoding` 冲突的解释不同，攻击者可制造 CL.TE/TE.CL desync，让后续 bytes 被不同组件当成不同 request。这说明 framing 不是纯性能细节，也是安全边界。

### Trailers

Chunked encoding 可以在 body 后发送 trailer fields（前提是语义允许）；HTTP/2/3 也有 trailer field sections，但机制不是 chunked。

### 线上案例推演

反向代理升级后偶发“一个用户收到另一个请求的响应”，若发生在 keep-alive connection 复用，必须排查 HTTP parser/framing 一致性和 request smuggling，而不是先怀疑 TCP 粘包。
''',
67: r'''
## V2 深入：Cache-Control 要分“能否存”“何时算新鲜”“过期后是否可复用”

### 第一性原理

- `max-age` 控制 freshness lifetime；`no-cache` 通常允许存储但 reuse 前必须 revalidate；`no-store` 要求不要存储；`private` 限制 shared cache 复用；`must-revalidate` 收紧 stale response 使用。
- Shared cache 还可使用 `s-maxage` 覆盖共享缓存的新鲜度策略，而 private browser cache 不按同样方式解释。
- `Vary` 参与 cache key 选择，告诉 cache 哪些 request fields 会改变 response representation。

### Stale 策略

`stale-while-revalidate` 允许在后台更新时暂时服务 stale，减少用户 tail latency；`stale-if-error` 类策略在 origin 故障时提升可用性。是否可用要看具体规范/实现和业务一致性要求。

### Cookie/授权边界

带 Authorization/Cookie 的 response 是否可共享缓存必须非常谨慎；错误 cache key 或错误 `public/private` 可能造成严重用户数据泄漏。

### 线上案例推演

部署后发现 CDN hit ratio 极低，检查 `Vary`、Set-Cookie、Cache-Control、query normalization；如果 `no-cache` 被团队误写成“绝对不能缓存”，就会错误理解实际 revalidation 流量。
''',
68: r'''
## V2 深入：Conditional Request 把“是否变化”与“重新传 body”分离

### 第一性原理

- ETag 是 server 给 representation 的 opaque validator；Client 用 `If-None-Match` 验证缓存副本，未变化可返回 304，不再传 body。
- Last-Modified/If-Modified-Since 基于时间，是较弱/粒度有限 validator；ETag 可以表达更精确版本。
- `If-Match` 是前置条件：只有当前 entity tag 匹配才执行，可用于 optimistic concurrency、防 lost update。

### Strong vs Weak Validator

ETag 可以是 strong/weak；strong validator 要求 representation byte-equivalent 等更严格语义，weak 更适合“语义等价但字节可能不同”的缓存验证。不能把 ETag 简单等于 MD5。

### 分布式坑

如果多个实例用 inode/mtime/随机值生成 ETag，同一内容在不同 server 可能 ETag 不一致，导致缓存抖动。更可靠方式是稳定 content hash、version ID 或统一生成策略。

### 线上案例推演

静态文件每次都 200 而非 304，检查 CDN 是否剥离 ETag、压缩版本是否导致不同 validator、多个 origin 是否一致；不要只看浏览器缓存开关。
''',
69: r'''
## V2 深入：HTTP/2 改的是 wire format 和并发模型，不改 HTTP 核心语义

### 第一性原理

- HTTP/2 使用 binary framing，把一个 connection 划分为多个 stream，并允许 frame interleaving；method/status/cache 等 HTTP 语义仍来自共同 HTTP Semantics。
- HPACK 压缩重复 header fields，显著降低多 request header overhead；stream-level flow control 允许 receiver 对并发 stream/connection 做 backpressure。
- HTTP/2 仍运行在 TCP 上，因此 transport reliability/order 和 congestion control 是 connection-wide TCP 提供的。

### Stream ID 与生命周期

Client/server 发起 stream 的 ID 规则、HEADERS/DATA/RST_STREAM/GOAWAY 等 frame 构成独立 stream 状态机。高级面试不必背所有 frame bit，但应知道 GOAWAY 用于 graceful shutdown/迁移未处理 stream。

### Server Push

Server Push 规范上存在，但浏览器生态实际大幅减少/禁用，原因包括缓存重复、调度复杂度与收益有限；不能把“HTTP/2 有 Server Push”当今天最重要卖点。

### 线上案例推演

HTTP/2 上一个 backend connection 承载几百 stream，单 connection reset 会同时影响很多 request；多路复用降低连接成本，也扩大单连接故障 blast radius。
''',
70: r'''
## V2 深入：HTTP/2 的 HOL 根源是 TCP 的“全连接统一序号空间”

### 第一性原理

- HTTP/2 stream 彼此有 stream ID，但 frame bytes 最终进入一个 TCP sequence space。
- TCP 必须按字节顺序交给上层；某 segment 丢失后，即使后续 segment 已到达 kernel，也不能越过 gap 交给 HTTP/2 parser。
- 这会让本来属于不同 HTTP stream 的数据一起等待，形成跨 stream transport-level HOL。

### HTTP/3 的改善边界

QUIC stream offset 独立，未丢数据的 stream 可继续交付；但同 stream 内仍有 ordering，QPACK dynamic dependency 也可能阻塞 header，connection-level congestion control 仍共享。

### Packet 包含多个 frame

QUIC 一个 packet 可以携带多个 stream frame；packet 丢失时这些 frame 都需要重新发送，但它们不会要求其他未涉及且完整的 stream data 等待同一 byte gap。

### 线上案例推演

无损 LAN 比较 HTTP/2/3 很可能差异小；要验证 HOL，应在 tc/netem 注入 controlled loss/RTT，并看并发 stream completion distribution 而不是只看总吞吐。
''',
71: r'''
## V2 深入：QPACK 的设计目标是“保留动态压缩收益但避免把跨流顺序依赖带进 QUIC”

### 第一性原理

- HPACK 利用 HTTP/2 在单 TCP byte stream 上的整体顺序，可安全维护动态 header table state；直接搬到 HTTP/3 会让 header block 等待丢失的 table update，重新产生 HOL。
- QPACK 将 encoder/decoder instruction 放在独立 unidirectional streams，并允许 request stream 引用 table entries，同时设置 blocked stream 上限来控制依赖。
- Static table 提供无动态依赖的常见 header 压缩，dynamic table 以复杂度换更高压缩率。

### QPACK 仍可能阻塞

若 request header 引用 decoder 尚未收到的 dynamic entry，该 stream 仍会 blocked；QPACK 不是“完全无等待”，而是让这种阻塞可显式管理、限制，不扩散为 TCP 全连接 byte gap。

### 安全边界

Header compression 的大小/时间差异可能形成侧信道（历史上如 CRIME/BREACH 类风险），敏感 header 与 attacker-controlled data 的压缩策略需要谨慎。

### 线上案例推演

HTTP/3 request header latency 异常而 DATA stream 正常时，可看 QPACK blocked stream/encoder instructions，而不是把所有 delay 归因 UDP loss。
''',
72: r'''
## V2 深入：WebSocket、SSE、Long Polling 的核心区别是通信方向、消息模型与基础设施成本

### 第一性原理

- Long Polling 仍是 request/response：Server 延迟响应，Client 收到后重新发请求，兼容性高但有重复 header/connection scheduling 开销。
- SSE 是 server→client 的事件流，基于 HTTP streaming、文本 event format，天然有 Event ID/reconnect 语义，适合通知/LLM token stream 等单向推送。
- WebSocket 建立持久双向消息通道，适合 chat/collaboration/game control，但 proxy idle timeout、backpressure、connection lifecycle 更复杂。

### HTTP/2/3 时代

SSE 可以在 HTTP/2/3 stream 上承载；“HTTP/2 有 streaming 所以 SSE 消失”错误。WebSocket 在 HTTP/2 可通过 Extended CONNECT 等机制启动，基础设施是否支持要看 proxy/gateway 实现。

### 选型问题

考虑双向性、消息频率、二进制需求、浏览器 API、断线重连、proxy/CDN 支持、连接规模、鉴权与 backpressure，而不是只按“实时程度”选。

### 线上案例推演

若仅 Server 持续推送 AI token，SSE 往往比 WebSocket 简化得多；若 Client 也高频发送协作操作，则 full-duplex WebSocket/双向 streaming RPC 更合适。
''',
73: r'''
## V2 深入：gRPC 借 HTTP/2 解决 transport concerns，但自己定义 RPC/message 语义

### 第一性原理

- gRPC 利用 HTTP/2 stream multiplexing、flow control、binary framing 与长期 connection，承载 unary/client-streaming/server-streaming/bidi-streaming RPC。
- Protobuf 序列化只定义 message bytes；gRPC 仍需要 message length/compression flag framing，因为一个 HTTP/2 DATA stream 可以连续承载多条 protobuf message。
- gRPC status/trailer、deadline、metadata、service/method path 构成独立 RPC contract，不等同 REST resource semantics。

### Trade-off

gRPC schema/codegen/二进制效率/streaming 很强，但 browser/debug/cache/公共 HTTP ecosystem 兼容性与 REST 不同。内部服务和对外 API 的最佳选择可能不同。

### HTTP/3

gRPC 可以映射到 HTTP/3 的研究/实现方向，但实际 production support 取决于语言 runtime、proxy、load balancer 与规范生态，不能只因 HTTP/3 存在就说 gRPC 已全面迁移。

### 线上案例推演

一个 gRPC stream 卡住时同时看 HTTP/2 flow-control window、TCP cwnd/rwnd 与应用 consumer；只调 protobuf size 不一定解决 backpressure。
''',
74: r'''
## V2 深入：HTTPS 的本质是把 HTTP 放进经过认证与加密的安全通道

### 第一性原理

- TLS 提供 confidentiality、integrity，并通过证书/PSK 等机制提供 peer authentication；HTTP 的 method/status/cache 语义本身没有因此变化。
- TLS 防网络窃听/篡改，不防应用 SQL injection、XSS、越权、恶意合法用户；安全层次必须分开。
- Server private key/handshake key exchange 用于认证和建立 traffic secrets，真正 bulk data 使用 AEAD symmetric encryption。

### “HTTPS 能隐藏什么”

Payload/path/query/header 在 TLS 内通常加密，但 destination IP 仍需路由可见；传统 SNI 可能暴露 hostname，ECH 目标是加密 ClientHello 中的敏感域名信息，但部署还受 DNS/客户端/服务端生态影响。

### 企业 TLS Inspection

若 endpoint 信任企业安装的 root CA，企业 proxy 可以与 Client/Server 各建立一条 TLS connection，对中间内容解密再转发。这不是 TLS 被“破解”，而是信任模型加入了新的受信 CA/终止点。

### 2026 规范更新

TLS 1.3 当前主规范为 RFC 9846，它以兼容方式取代 RFC 8446并收紧若干要求；仓库后续 TLS 题统一以 RFC 9846 为首要参考。
''',
75: r'''
## V2 深入：TLS 1.3 面试要掌握消息流、Key Schedule 与“谁证明了什么”

### 第一性原理

- ClientHello 提供 supported_versions、cipher suites、key_share、signature algorithms、SNI/ALPN 等；ServerHello 选择参数与 key_share 后，双方可基于 (EC)DHE 派生 handshake secrets。
- ServerHello 后大部分 handshake message 已加密；Server 通过 Certificate + CertificateVerify 证明对证书私钥的控制，Finished 用 transcript-derived MAC 证明握手 transcript 与 secrets 一致。
- Client 验证证书链/身份后发送自己的 Finished，随后双方使用 application traffic secrets 保护数据。

### Key Schedule 心智模型

TLS 1.3 使用 HKDF 做强 key separation：early/handshake/application 等不同阶段 secret 分离，并结合 transcript hash。不要背每个 label 字符串，但要理解“不是直接把 ECDHE shared secret 当 AES key”。

### 1-RTT 与 TLS 1.2

TLS 1.3 移除了 static RSA key exchange、精简 cipher suite，使 full handshake 通常更少往返并默认具备 public-key forward secrecy；0-RTT 属于恢复连接的额外模式，不是所有 TLS 1.3 第一次连接都 0 RTT。

### 2026 规范提示

RFC 9846 是 TLS 1.3 当前规范，保持协议版本 1.3 与 RFC 8446 wire compatibility，但收紧 key-share reuse、旧版本协商等要求。
''',
76: r'''
## V2 深入：证书验证是“建立可信公钥到目标服务身份的链”

### 第一性原理

浏览器验证通常包含：构建到本地 trust anchor 的 certificate chain、验证签名/Basic Constraints/Key Usage、有效期、目标 hostname（SAN）匹配，以及实现相关的 revocation/CT/policy 检查。只验证“证书没过期”远远不够。

### Chain Building

Server 通常发送 leaf + 必要 intermediate，不应依赖 Client 一定能在线下载缺失 intermediate。Root CA 一般已经存在 Client trust store，不需要也不应把“Server 发来的 root”当成信任来源。

### Hostname 与证书

合法 CA 签发给 `other.example` 的证书即使链完全可信，也不能用于 `api.example`，除非 SAN 覆盖。Identity verification 是 TLS 与具体应用协议集成的一部分。

### CT/Revocation

Certificate Transparency 提供公开可审计签发日志，提高误签/恶意签发可发现性；OCSP/CRL 类机制处理撤销，但浏览器实际策略有性能/隐私/soft-fail trade-off。

### 线上案例推演

“Chrome 正常、老 Java 客户端失败”常见于 intermediate chain 缺失、root store 差异、algorithm support、hostname policy 不同；不能看到一个客户端成功就断言证书配置绝对正确。
''',
77: r'''
## V2 深入：TLS 混合密码体系把“身份/密钥建立”与“高速数据保护”分开

### 第一性原理

- 非对称密码学用于签名、身份认证和 ephemeral key agreement；计算成本高且不适合直接加密大量 application data。
- (EC)DHE 产生 shared secret，HKDF 从其与 transcript 派生多个 traffic secrets；AEAD（如 AES-GCM/ChaCha20-Poly1305）用对称 key 高效保护 record。
- Server public key 不是 AES key：二者算法类型、密钥空间、用途和安全证明都不同。

### RSA 签名 vs RSA Key Exchange

历史 TLS 可用 RSA 加密 premaster secret 做 key exchange，但 TLS 1.3移除了 static RSA key exchange；RSA 仍可作为证书签名/CertificateVerify 的签名算法之一。回答“TLS 1.3 用 RSA 加密 AES key”是不准确的。

### HKDF

HKDF Extract/Expand 提供 entropy extraction 与 domain-separated key derivation，使 handshake/application/resumption/exporter keys 相互隔离，降低一个 key/用途泄漏影响其他阶段。

### 线上案例推演

TLS CPU 成本高时，不能简单说“非对称加密每个 packet 都很慢”；大部分 data records 已走 symmetric AEAD，瓶颈可能是 handshake rate、certificate signature、AEAD throughput 或 kernel/user copy。
''',
78: r'''
## V2 深入：Forward Secrecy 保护的是“长期密钥未来泄露后，历史会话仍难被解密”

### 第一性原理

- ECDHE 每次 handshake 生成 ephemeral key pair；双方从私钥×对方公钥计算同一 shared secret，但 passive observer 只有 public values。
- Server certificate private key用于签名 handshake，证明身份；它不直接等于 ECDHE ephemeral private key。
- 若长期证书私钥未来泄露，攻击者仅凭过去录制的 traffic/handshake 不应能恢复过去的 ephemeral shared secrets。

### PFS 不解决什么

PFS 不能阻止**当前**有能力冒充身份/控制 endpoint 的 active MITM；也不能保护已经攻陷终端内存中的当前 plaintext/traffic key。它主要减少 long-term key compromise 对历史流量的追溯影响。

### PSK 边界

TLS 1.3 resumption PSK 可以与 DHE 组合获得 forward secrecy；纯 PSK 模式的安全属性不同，回答应区分 handshake mode。

### 线上案例推演

公司要求“即使明年服务器证书私钥泄漏，今天抓到的流量也不能解密”，这正是 forward secrecy 的设计目标，而不是靠更长 RSA key 简单实现。
''',
79: r'''
## V2 深入：SNI 选择“你要哪个虚拟服务”，ALPN 选择“这个 TLS 连接上跑哪个应用协议”

### 第一性原理

- SNI 是 ClientHello extension，告诉 shared IP 上的 TLS endpoint 目标 server name，以便选择正确 certificate/virtual host。
- ALPN 在 TLS handshake 中协商应用协议，如 `h2`、`http/1.1`，避免握手后再猜协议。
- 一个是 host identity/routing hint，一个是 application protocol negotiation，不能混为一谈。

### 没有 SNI

共享 IP 仍可配置 default certificate/site，或不同 IP 分配不同域名；但大规模 virtual hosting 会很受限。证书 SAN 多域名也不能完全替代正确 SNI routing。

### ECH 与可见性

ECH 目标是保护 ClientHello 中包括真实 SNI 在内的敏感信息，但 destination IP 仍需路由；DNS/流量特征也可能泄露信息。因此 ECH 不是“隐藏访问目标的一切”。

### 线上案例推演

TLS handshake 成功却协商成 `http/1.1` 而非 `h2`，应查 ALPN/client/server/proxy support；证书选错域名则优先查 SNI/vhost，而不是把两种错误混在一起。
''',
80: r'''
## V2 深入：0-RTT 的核心矛盾是“数据在服务端证明连接新鲜性之前就可能被处理”

### 第一性原理

- Client 使用此前 resumption PSK/ticket 加密 early data；攻击者可以捕获并在可行条件下重放相同 early data，Server 必须自行判断是否安全接受。
- TLS 不能自动知道“这条 HTTP 请求是否会扣款”，所以 application protocol/Server 必须限制 early data 到 replay-safe 操作或实现 anti-replay/idempotency。
- 0-RTT early data 的 security properties 弱于普通 1-RTT data，且不具备本次 handshake DHE 后才产生的同等 forward secrecy。

### GET 也不自动安全

HTTP GET 语义应 safe，但现实系统可能错误地让 GET 触发 side effect；是否允许 0-RTT 应基于实际业务 semantics，而不是只检查 method string。

### 多机房 anti-replay

严格全局 replay cache 需要跨 POP 同步，成本高且增加 latency；系统常结合 ticket lifetime、single-use token、request idempotency、局部 anti-replay window 等做 trade-off。

### 2026 规范提示

TLS 1.3 的现行参考应更新到 RFC 9846；QUIC 0-RTT 使用 TLS 1.3 early-data 机制，但还要遵守 QUIC transport parameter/connection semantics。
''',
})
PACKS.update({
81: r'''
## V2 深入：TCP Server 系统调用链要同时理解“监听 socket”和“已连接 socket”

### 第一性原理

- `socket()` 创建 endpoint；`bind()` 绑定本地地址；`listen()` 把 socket 变成 listener；`accept()`/`accept4()` 返回**新的 connected socket**，listener 本身继续接收后续连接。
- TCP 三次握手主要由内核完成，应用通常在握手完成后从 accept queue 取连接；因此“Client 已 ESTABLISHED”与“Server application 已 accept”不是同一时间点。
- `recv()/send()` 操作 connected socket；关闭 listener 不等于自动优雅关闭所有已经 accept 的连接。

### `accept4` 与 fd flags

`accept4()` 可以原子设置 `SOCK_NONBLOCK`/`SOCK_CLOEXEC`，避免 accept 后再 `fcntl()` 之间的 race。高并发服务应把 fd ownership、close-on-exec、nonblocking 设置视为资源正确性问题。

### Reuse 选项

`SO_REUSEADDR` 主要涉及地址重绑定/特定 bind 语义；`SO_REUSEPORT` 允许多个 socket 绑定同一地址端口并由内核分流，常用于多核 listener。两者不是“都用来绕过端口占用”的同义开关。

### 线上案例推演

连接握手正常但 accept latency 很高时，抓包只会显示 ESTABLISHED；必须结合 listener queue、event loop、worker scheduling，证明 bottleneck 在应用 accept path。
''',
82: r'''
## V2 深入：Nonblocking 改变的是 syscall“等待行为”，不改变 socket 协议语义

### 第一性原理

- Blocking `read()` 在当前无数据且连接未结束时可睡眠等待；nonblocking 则立即返回 `EAGAIN/EWOULDBLOCK`。
- EOF 是 `read()==0`，表示 peer 已 orderly close 发送方向；EAGAIN 表示“现在没有数据，但以后可能有”，两者必须严格区分。
- Nonblocking 并不让 IO 自动完成，它通常与 readiness mechanism（epoll/kqueue）配合，应用仍需显式 read/write。

### Nonblocking connect

`connect()` 可能返回 `EINPROGRESS`；之后 writable event 只表示连接尝试“完成了某种结果”，必须用 `getsockopt(SO_ERROR)` 判断成功或具体错误。

### Write readiness

大多数时间 socket send buffer 都有空间，如果永久订阅 writable event，event loop 可能被持续唤醒形成 busy loop。常见做法是只有发生 partial write/EAGAIN、确实有 pending output 时才开启 EPOLLOUT。

### 线上案例推演

事件循环 CPU 100% 而业务 QPS 很低，检查是否所有连接永久注册 EPOLLOUT；这类 bug 不是网络拥塞，而是 readiness subscription 设计错误。
''',
83: r'''
## V2 深入：Readiness 与 Completion 是理解 IO 模型的真正主线

### 第一性原理

- Readiness 模型告诉应用“现在做 read/write 大概率不会因等待数据而阻塞”，应用随后自己执行 syscall；select/poll/epoll/kqueue 属于这一思路。
- Completion 模型更接近“提交 IO 操作，完成后通知结果/bytes”，应用不必在 readiness 后再发起同一个同步 copy syscall；io_uring/IOCP 更接近 completion-oriented 设计。
- “异步”这个词常被混用，面试中应具体说清谁等待、谁执行、何时 copy、谁收到 completion。

### Reactor vs Proactor

Reactor：event loop 收到 readiness，再调用 handler 执行 IO；Proactor：先提交异步 IO，completion event 再交给 handler。真实框架可能混合使用，不必把所有 API 强行归为教科书五类。

### 文件 IO 为什么特殊

Regular file 常不存在 socket 那种“等网络数据到达”的 readiness；page fault/storage latency 仍可能阻塞。io_uring 能异步提交 read/write/fsync 等，对 file IO 更自然。

### 线上案例推演

网络服务 epoll event loop 偶发 100ms stall，如果 handler 同步读磁盘，epoll 本身没有问题；readiness 只管理 socket，blocking file IO 把整个 reactor 卡住。
''',
84: r'''
## V2 深入：select/poll/epoll 的差异是“兴趣集合如何维护、就绪集合如何返回”

### 第一性原理

- select 每轮传 fd bitset，并受接口/FD_SETSIZE 等限制；poll 使用 pollfd array，无同样 bitset 上限，但每轮仍需传/扫描集合。
- epoll 在 kernel 中维护长期 interest set，`epoll_ctl` 用于增删改，`epoll_wait` 返回 ready events；因此大量 idle connection 场景减少重复扫描/复制成本。
- epoll 性能不是“所有操作严格 O(1)”的口号；ready-list、wakeup、lock/cache、事件风暴、应用 handler 才决定实际吞吐。

### 何时 poll 足够

fd 数量小、活跃比例高、代码跨平台/简单工具场景，poll 的简洁性可能比复杂 event loop 更重要；没有必要为了几十个 fd 强行 epoll。

### epoll_ctl

正常设计不是每次 wait 前重建全部 fd；connection 建立/兴趣变化时才 ctl。频繁无意义 MOD/DEL/ADD 会增加 syscall 与锁开销。

### 线上案例推演

百万 idle connection 只有千级活跃时，select/poll 每轮扫描成本明显；但如果 handler 每个事件做重 CPU 计算，换 epoll 也不会自动提升业务吞吐。
''',
85: r'''
## V2 深入：LT 报“状态仍为真”，ET 报“状态发生边沿变化”

### 第一性原理

- LT 下，只要 receive buffer 仍可读，后续 `epoll_wait` 仍可能继续报告 readable；遗漏一次 read 通常还有机会再次收到事件。
- ET 下，应用应在收到 edge 后循环处理到 `EAGAIN`，把当前可消费状态 drain 掉；只读一次可能留下数据却没有新的 edge，造成连接“假死”。
- ET 的正确性依赖 nonblocking + 循环 drain + 完整 partial-read/write 状态机。

### EPOLLONESHOT

多线程 worker 处理同一个 fd 时，可用 ONESHOT 防止同一 fd 同时被多个线程重复处理；handler 完成后需要 rearm。它解决的是并发事件所有权，不等于 ET 本身。

### ET 不一定更快

LT 的额外重复 wakeup 在正确 drain 的服务里也可能很少；ET 则增加状态机复杂度。选型应根据 workload、框架成熟度，而不是把 ET 当高级版必选。

### 线上案例推演

ET server 在大 response/请求 burst 下偶发永不继续读，最常见 bug 就是每次 event 只 `recv()` 一次；抓包显示数据已到本机、recv-q 非空但应用不再醒来。
''',
86: r'''
## V2 深入：ET + blocking 最大风险是“为了 drain 而把 event loop 永久卡住”

### 第一性原理

- ET handler 通常需要 `while (read() > 0) ...` 直到 EAGAIN；若 socket blocking，当最后一次 read 没有新数据时就可能睡眠，整个 reactor 被单连接阻塞。
- Nonblocking 让“当前状态已经 drain 完”通过 EAGAIN 明确返回，使线程能回到 epoll_wait 服务其他连接。
- LT 也通常推荐 nonblocking，因为 readiness 与真正 syscall 之间存在 race，多线程/事件变化仍可能让 blocking 调用卡住。

### 为什么 FIONREAD 不能代替循环读

读取“当前可用字节数”与实际 read 之间仍有并发/协议变化，且 TLS/stream parser 需要处理 partial data；以 EAGAIN 作为 kernel authoritative boundary 更稳健。

### ET + TLS

`SSL_read()` 有自己的 record/buffer 状态，可能出现 `SSL_ERROR_WANT_READ/WANT_WRITE`；TLS library 已经读取到用户态的 decrypted/record data 也可能不再对应新的 kernel EPOLLIN。必须按 TLS state machine 驱动，而不是只把 raw recv loop 套在 SSL 上。

### 线上案例推演

ET + OpenSSL 服务 CPU 不高但连接偶发卡住，检查是否正确处理 WANT_WRITE/SSL pending data 与 epoll interest；“socket 没新 EPOLLIN”不代表 TLS library 内部没有可读明文。
''',
87: r'''
## V2 深入：Regular File 不适合 epoll，因为“可读”并不代表底层存储 IO 已完成

### 第一性原理

- Socket readability 是随网络数据到达变化的状态；regular file 在语义上通常随时可发起 read，真正延迟可能发生在 page cache miss/磁盘访问。
- Linux epoll 不是通用 file completion API，regular file 通常不能像 socket 一样作为有意义的 readiness source 加入。
- 将慢磁盘 read 放在 epoll event loop 线程中，仍可能阻塞整个网络 reactor。

### io_uring 的不同抽象

io_uring 允许提交 read/write/fsync 等请求并获取 completion，适合把实际 storage operation 的完成纳入异步流水；也可以与网络 IO 统一事件驱动，但编程模型不是“epoll 的更快版本”这么简单。

### Direct I/O

O_DIRECT 绕过/减少 page cache 路径并引入 alignment 等限制，不会自动把同步 read 变成异步；应用仍需异步 submission/completion 或 thread pool 避免 event-loop stall。

### 线上案例推演

静态文件服务 epoll 线程偶发 latency spike，如果 handler 同步 open/read 冷文件，perf/iostat 显示 storage wait，就应使用 sendfile/page cache、async file IO 或 worker pool，而不是调整 epoll ET/LT。
''',
88: r'''
## V2 深入：`send()`、TCP ACK、对端 `read()`、业务 commit 是四个完全不同的里程碑

### 第一性原理

1. `send()` 成功：本机 kernel 接受了 N bytes（可能只是进 send buffer）。
2. 对端 TCP ACK：对端 TCP stack 确认相应字节范围已接收，不代表 application 已 read。
3. 对端 application read：业务进程拿到了 bytes，不代表处理成功。
4. DB/业务 commit：只有应用级 response/幂等状态才能表达。

### Crash 场景

本机 `send()` 后进程 crash，kernel 可能仍有机会发送已排队数据，也可能 connection 被关闭/未完全交付；Client 无法仅凭本地 return value 推断远端执行状态。

### 支付重试设计

为有 side effect 请求使用唯一 idempotency key，Server 原子记录 operation/result；Client timeout 后重试相同 key，Server 返回原结果或状态。Transport retry 与 business retry 必须解耦。

### 线上案例推演

“Client timeout 后用户再次点击导致重复订单”不是把 socket timeout 调长就彻底解决；需要让协议对 ambiguous outcome 有可查询/幂等语义。
''',
89: r'''
## V2 深入：Zero Copy 的目标是减少 CPU copy/上下文切换，不是让数据物理上从未移动

### 第一性原理

传统文件发送可能经历 storage→page cache→user buffer→socket buffer/NIC，多次 copy 与 syscall。`sendfile()` 可让 kernel 在 file/socket 路径直接转移数据，减少 user-space round trip；`splice()` 在支持的 fd/pipeline 间移动 page references/pipe buffers；`mmap()` 用虚拟内存映射减少显式 read copy，但仍有 page fault/cache 行为。

### DMA 的作用

NIC/storage DMA 可以在设备与内存之间搬运数据而不让 CPU逐字节复制；“zero-copy”通常指 CPU/user-kernel copy 优化，内存/总线上的数据传输依然存在。

### HTTPS 难点

TLS encryption 传统上需要把 plaintext 交给 TLS stack 处理，不能简单把 file pages 原封不动 sendfile 到 NIC；kTLS/硬件 offload 等可重新打通部分 zero-copy 路径，具体取决于 kernel/cipher/NIC。

### 线上案例推演

静态大文件服务 CPU 主要耗在 memcpy/syscall，可比较 read+write 与 sendfile 的 CPU cycles/context switches；如果 bottleneck 已是 NIC 带宽，zero-copy 只降 CPU，不会突破线速。
''',
90: r'''
## V2 深入：NIC→recv() 是一条多核、批处理、协议状态机共同作用的数据路径

### 第一性原理

典型路径：NIC RX ring/DMA → interrupt/NAPI poll → driver 构造/处理 skb → GRO → L2/L3 → netfilter/routing → TCP/UDP → socket receive queue → application `recv()`。每一层都有队列、CPU 与 drop point。

### RSS / RPS / RFS / XPS

- RSS：NIC 硬件按 flow hash 把 packet 分散到多个 RX queue/CPU。
- RPS：内核软件把收包处理分发到其他 CPU。
- RFS：进一步尝试让 flow processing 靠近消费该 socket 的 application CPU，改善 cache locality。
- XPS：发送方向选择 TX queue/CPU 的策略。

### GRO/LRO

GRO 在 stack 较早阶段合并同 flow packet，减少 per-packet protocol overhead；LRO 更偏 NIC/driver，可能影响转发/抓包语义。高 PPS 小包场景常是 CPU bottleneck，而不是带宽 Mbps bottleneck。

### 线上案例推演

总 CPU 40% 但单核 softirq 100%、NIC 只有一个 RX queue 时，吞吐已被单核 packet processing 卡住；增加业务线程没有帮助，应查 RSS queue/IRQ affinity/RPS。
''',
91: r'''
## V2 深入：URL 全流程题的最高分答案是“给出一条可观测的分层时间线”

### 第一性原理

把一次访问拆成：URL/缓存策略 → DNS → route/neighbor → transport connect（TCP 或 QUIC）→ TLS/ALPN → HTTP request → CDN/LB/proxy → service/downstream → response → browser parse/render。每一步都有独立失败模式和观测信号。

### 现代浏览器细节

浏览器可能先查 Service Worker/HTTP cache；DNS 可能使用 DoH；连接可能复用已有 HTTP/2/QUIC connection而没有新的 TCP/TLS handshake；HTTP/3 可通过 Alt-Svc/HTTPS RR 等获知；因此“每次输入 URL 都严格 DNS→TCP三次握手→TLS”只是冷连接简化模型。

### 页面显示不是网络结束

HTML response 到达后还有 parser、preload scanner、CSSOM/DOM、JS、字体/图片子资源、layout/paint/composite；Web performance 题应区分 TTFB 与 LCP/INP 等浏览器阶段。

### 线上案例推演

`curl` TTFB 50ms但浏览器 LCP 3s，网络后端不一定慢；需要看 waterfall、render-blocking CSS/JS、图片和主线程，而不是继续优化 TCP handshake。
''',
92: r'''
## V2 深入：“网站很慢”首先要把总延迟做 decomposition

### 第一性原理

用近似模型 `T_total = DNS + connect + TLS + request queue + upstream/app + first-byte transfer + body transfer + browser/render`。第一步是确定变慢的是哪个区间，再提出机制假设。

### 证据优先级

- Client：`curl -w`/browser waterfall 分解 lookup/connect/appconnect/starttransfer/total。
- Network：RTT、loss、retrans、path、PMTU。
- Edge/LB：queue、upstream connect、5xx/timeout。
- Service：trace、thread pool、GC、DB/cache/downstream。
- Frontend：resource waterfall、main-thread/render。

### 避免平均数陷阱

“平均 latency 正常”不能排除 p99；按 region/ISP/protocol/version/POP/instance 分桶常能迅速识别局部故障。网络问题尤其可能只影响某 AS/path。

### 线上案例推演

只有某 ISP p99 从 200ms 升到 2s，服务端 CPU/DB 正常；应优先比较该 ISP route/retrans/edge POP，而不是全局扩容数据库。
''',
93: r'''
## V2 深入：CPU/QPS 不变而 latency 上升，优先想“等待时间”而不是“计算量”

### 第一性原理

Latency 可以花在 network RTT/loss/retrans、queue、lock、connection pool、DNS、downstream、storage IO 上，这些都会让 wall-clock 变长而 CPU 不一定升高。Little's Law 还能导致同 QPS 下 concurrent in-flight 增加。

### 网络假设

RTT 上升、packet loss 触发 RTO、PMTU black hole、route change、NAT/conntrack pressure、receiver zero-window 都可能表现为等待。`ss -tin` 的 rtt/retrans/cwnd/send-q 与 trace timing 能帮助区分。

### 应用等待假设

DB connection pool 等待、thread semaphore、RPC upstream timeout、GC pause、DNS resolver 卡顿也会让 CPU 空闲但请求排队。必须有 queue time/trace span，而不是只看 host CPU。

### 线上案例推演

QPS 1000 始终不变，平均 service CPU 30%，p99 从 100ms 到 5s，同时 active request 数暴涨：这是典型等待/queue 膨胀信号，下一步应找哪个 span time 增加。
''',
94: r'''
## V2 深入：TIME_WAIT 排障是一套“连接生命周期 + 资源容量”调查

### 第一性原理

先判断 active closer，再按 remote endpoint/进程/协议统计 connection churn；接着验证是否真的出现 ephemeral port、NAT/conntrack、CPU/memory 或 connect error。没有资源症状时，TIME_WAIT 多可能只是 workload 特征。

### 推荐流程

1. `ss -s`/状态分布与新建连接速率。
2. 按 destination 聚合，定位哪个 upstream 产生短连接。
3. 检查 HTTP/RPC pool reuse、keepalive、max lifetime。
4. 检查 local port range、`EADDRNOTAVAIL`、NAT port usage。
5. 最后才评估内核参数，并明确版本/风险。

### 常见架构根因

每 request 新建 DB/HTTP connection、代理关闭策略不一致、发布/健康检查造成 connection churn、LB idle timeout 比 pool lifetime 短。

### 线上案例推演

某服务引入新 HTTP client 后每请求都 new client，TIME_WAIT 从 2k 升到 300k并出现 connect failure；复用 connection pool 后恢复。这比调 `tcp_tw_reuse` 更接近根因修复。
''',
95: r'''
## V2 深入：CLOSE_WAIT 排障必须落到“哪个对象为什么没有 close fd”

### 第一性原理

CLOSE_WAIT 已经证明 peer FIN 到达且 kernel 完成 ACK；剩下的是 local application lifecycle。核心不是网络重传，而是资源所有权。

### 推荐流程

1. `ss -tanp state close-wait` 找 PID/remote。
2. `lsof -p`/fd count 看是否持续增长。
3. 按调用路径/endpoint 与异常率关联。
4. 抓 thread dump/goroutine/heap profile 找持有连接的对象。
5. 修复 finally/defer/RAII、body close、pool return，并加泄漏监控。

### FIN_WAIT_2 关联

对端已经主动 close并收到本端 ACK 后，可能处于 FIN_WAIT_2 等待本端 FIN；因此一端大量 CLOSE_WAIT 可能同时给 peer 制造大量 FIN_WAIT_2。

### 线上案例推演

只在 downstream 500 error 时 CLOSE_WAIT 增长，通常说明 error path 没释放 response body/socket。优先 code review异常分支，而不是网络设备。
''',
96: r'''
## V2 深入：SYN_RECV 多只是现象，必须区分攻击、回程丢包与 listener 容量

### 第一性原理

SYN_RECV 表示 Server 已收到 SYN、发出 SYN+ACK并等待最终 ACK。它可能因为：伪造源 SYN flood；真实 Client 的 ACK/SYN+ACK path 丢包；SYN backlog pressure；Client故障。

### 证据矩阵

- 攻击：源分布异常、SYN rate 极高、ACK completion 比例低、边缘带宽/pps 高。
- 网络丢包：特定 region/ASN，SYN+ACK retrans 高，双方抓包不对称。
- 容量：listen overflow/syn backlog 指标、CPU/softirq、conntrack full。
- accept queue 问题：握手已完成，SYN_RECV 不一定高，listen established queue/worker 排队高。

### Syncookies 的定位

它是 SYN queue pressure 时的防护/降级机制，不应把所有新连接问题都“开 syncookies”解决。

### 线上案例推演

只有一个运营商 SYN_RECV 高且服务端反复发 SYN+ACK，其他地区正常，更像 return path/ACL 问题；全网随机伪造源 + PPS 爆炸才更像 SYN Flood。
''',
97: r'''
## V2 深入：网络 CPU 高常发生在 softirq/packet processing，而不是业务线程

### 第一性原理

每 packet 都有固定协议栈成本。大量小包、retrans、conntrack/firewall、单 RX queue 热点可让 ksoftirqd/NAPI 吃满 CPU，即使 application handler 很轻。

### 观察路径

看 `/proc/softirqs`、`mpstat -P ALL`、`perf top`、NIC rx/tx/drop、ethtool queue/interrupt、RSS/RPS/RFS 配置、packet rate（PPS）而不只看 Mbps。1Gbps 的 64B packets 与 1Gbps 大 packets CPU成本完全不同。

### 常见优化方向

RSS 多队列 + IRQ affinity、RPS/RFS、GRO、batching、减少 iptables/conntrack 热路径、XDP/eBPF prefilter、合理 socket sharding；每个方向都应基于 profile/瓶颈证明。

### 线上案例推演

总 CPU 60%但 CPU3 `NET_RX` 100%，NIC RSS indirection 只映射 CPU3：扩业务 pod 无效，修 RX queue/IRQ distribution 后 p99 恢复。
''',
98: r'''
## V2 深入：L4 与 L7 LB 的根本区别是“是否终止并理解应用协议”

### 第一性原理

- L4 根据 IP/port/protocol/connection state 做转发或连接代理，协议通用、开销低、可承载任意 TCP/UDP。
- L7 终止 HTTP/TLS（取决于部署），可按 Host/path/header/cookie/RPC metadata 路由，并做 auth、rate limit、retry、cache、observability。
- 功能越上层，控制力越强，但 CPU/memory、配置复杂度、failure mode 也越多。

### TLS 与连接拓扑

L7 若 TLS termination，会形成 Client→LB 与 LB→Backend 两条独立 transport connection；因此 502/504、TCP state、MTU、keepalive 都要分前后两段看。L4 DSR/NAT 模式则可能保持不同的数据路径。

### 选型

需要路径路由、灰度、WAF、HTTP metrics → L7；需要超高吞吐、非 HTTP、保留端到端 TLS/低开销 → L4；大型系统常 L4 入口 + L7 service mesh/gateway 组合。

### 线上案例推演

L7 proxy CPU 已满、backend 很空，改 backend instance 无效；若只是简单 TCP forwarding，可以评估把部分功能下沉 L4，或优化 TLS/HTTP parser/connection reuse。
''',
99: r'''
## V2 深入：百万连接首先是一张资源预算表，其次才是 epoll 选择题

### 第一性原理

必须量化：`FD + kernel socket memory + app connection object + TLS state + receive/send buffers + heartbeat PPS + active traffic bandwidth/PPS + event-loop CPU + LB/NAT state`。连接“空闲”只降低动态 traffic，不消除固定 per-connection state。

### 粗算示例

若端到端每连接平均占 12KB（只是示例，需实测），1M 就是约 12GB；30s heartbeat 是约 33k heartbeat/s，每个 heartbeat 若产生 request+response 与 TCP ACK，实际 PPS 更高。TLS 会额外增加 session/crypto buffer/state。

### 多核与 listener 架构

`SO_REUSEPORT`/多 event loop 可让 connection ownership 按 CPU shard，结合 RSS/RFS 提高 cache locality。需要避免一个 global lock/单 acceptor/单 timer wheel 成为百万规模热点。

### 生命周期与发布

真正危险的是 reconnect storm：一个实例重启导致几十万客户端同时 DNS/connect/TLS/auth。必须有 connection draining、jittered reconnect、backoff、LB health、capacity headroom；否则 steady-state 能扛 1M 也扛不住瞬时重连。

### NAT/端口与负载均衡

如果 Client/Proxy 通过有限 SNAT 出口连接同一 backend，可能先耗尽源端口/NAT entries；百万 backend connection capacity 不代表整条链路每层都支持百万 state。
''',
100: r'''
## V2 深入：抓包分析的核心是构造“序号—ACK—时间—窗口—应用事件”证据链

### 第一性原理

不要先相信 Wireshark 的彩色 `Retransmission` 标签，而是先定位 connection、方向和时间线：握手是否完整？谁先发数据？SEQ range？ACK 是否推进？是否 SACK？window 是否收缩？RST/FIN 来自谁？

### 常见模式

- `SYN` repeated、无 SYN+ACK：去程/服务端 listener/firewall。
- `SYN→SYN+ACK` repeated、无 ACK：回程/Client/源地址 spoof。
- Duplicate ACK + SACK + retrans：sequence gap/loss/reordering。
- Zero Window/Window Update：receiver/application backpressure。
- RST：需要看 sequence/时点判断是无 listener、abortive close、中间盒还是应用 reset。
- 连接正常但 HTTP 无 response：转向应用/proxy/upstream，不要继续只看握手。

### 抓包局限

单端抓包无法确定某 packet 是否真的到达对端；TSO/GRO 会影响本机包形态；镜像口可能丢包；Wireshark expert heuristic 可能把 reordering 标成 retrans。因此关键故障要尽量双端 capture + host counters + trace。

### 面试现场方法

按五步答：①找四/五元组与 handshake；②画 Seq/Ack timeline；③标 RTT/retrans/SACK/window；④关联应用 request/response；⑤提出至少两个假设并说明下一条证据如何区分。高级答案的价值在“证明”，不是背过滤器。
''',
})

assert set(PACKS) == set(range(1, 101)), (len(PACKS), sorted(set(range(1,101)) - set(PACKS)))
