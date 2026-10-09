# -*- coding: utf-8 -*-
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
A={
2:[
"`send()` 成功只表示本机内核接受了相应字节，数据之后还要经过 socket send buffer、TCP/IP、qdisc、driver/NIC；可能尚未真正出接口，更不代表对端已收到。",
"TSO/GSO 允许内核在较高层保留大 skb，再由更靠近网卡的位置分段，所以本机某些抓包点会看到大于 MTU 的逻辑 TCP segment；线上的 Ethernet frame 仍受实际 MTU/设备 offload 约束。",
"路由器收到帧后去掉入接口二层头，完成 L3 查表/TTL 等处理，再为出接口与下一跳构造新的二层帧；因此 MAC 地址逐跳变化。"],
3:[
"ARP Request 是二层广播，交换机不知道目标 MAC 具体端口时会在同 VLAN 广播域内 flood；这不是交换机‘用 ARP 学 MAC’，MAC 表仍主要从收到帧的源 MAC 学习。",
"VLAN 把一个物理交换网络切成多个逻辑广播域；广播/ARP 默认只在本 VLAN 内传播，不同 VLAN 间通信必须经过三层转发。",
"普通路由器以 L3 为边界，不把一个接口收到的 Ethernet broadcast 原样转发到另一 IP subnet；需要跨网段的服务通常通过路由、relay 或显式应用机制实现。"],
4:[
"先查路由表。若目标不在本地 on-link prefix，ARP 的对象是下一跳网关 IP，而 IP header 的目标仍是公网服务器。",
"取决于 NAT 类型：SNAT 改源，DNAT 改目的。普通家庭出网 SNAT 通常不改变远端目标 IP；端口映射/反向 NAT 则可能改变目的地址/端口。",
"不一定。MAC 可被软件配置，虚机/容器/克隆都可能重复；协议真正要求是在相关二层域内不要产生冲突和错误转发。"],
6:[
"Path MTU 是端到端路径上最小可承载 IP packet 尺寸；TCP MSS 应让 TCP payload 加 IP/TCP 头后不超过可用 PMTU，实际还会受隧道和 option 影响。",
"VPN/WireGuard/VXLAN/IPsec 等增加外层 header，若底层 MTU 仍约 1500，内层可用 MTU 必须降低，因此常见 1400/1420 等配置。",
"常见原因是 TSO/GSO：抓包点位于硬件分段之前，看到的是大逻辑 skb，而 NIC 最终会按 MTU 分段；不要据此断言链路支持超大 frame。"],
7:[
"`/32` 是单主机路由；`/31` 可用于点对点链路并让两地址都可作为 endpoint，不按传统子网‘网络地址/广播地址’浪费。",
"云平台通常额外保留 gateway、DNS、平台基础设施等地址，所以可分配给用户的数量由平台规则决定，不只由 `2^(host bits)-2` 决定。",
"CIDR 产生可变长度前缀；转发时在所有匹配 destination 的 route 中选择最长前缀，因此更具体的路由会覆盖更粗的汇总路由。"],
12:[
"STUN 只能帮助发现外部映射并做连通性检查，企业防火墙/对称 NAT/UDP blocked 等仍可能让直连失败，所以需要 TURN relay 作为兜底。",
"不同 NAT 的 mapping/filtering 是否依赖 destination 会直接影响两个 endpoint 能否通过彼此观察到的映射做 hole punching；越‘对称/依赖对端’越难直连。",
"不会完全消失。IPv6 降低地址转换需求，但防火墙、多网卡、双栈、路径验证和中继需求仍存在，ICE 仍承担 candidate selection/connectivity check。"],
13:[
"DHCP broadcast 默认不跨三层网段，Relay 在客户端网段接收请求并单播/转发给中心 DHCP Server，同时携带网段信息，使 Server 选择正确地址池。",
"客户端会在租约周期内提前续租/重新绑定；若最终无法续租并过期，不能无限继续使用该地址，应重新进入获取流程。",
"静态 IP 是客户端本地手工配置；Reservation 是 DHCP Server 根据 MAC/client-id 等规则始终租给同一地址，仍保留集中租约/配置管理。"],
14:[
"IPv6 不使用 IPv4 broadcast 机制，许多发现/通知通过 multicast 完成，例如 NDP 的 solicited-node multicast，从而减少整个广播域无差别处理。",
"SLAAC 通过 Router Advertisement/prefix 自主生成地址；DHCPv6 由 Server 分配地址/参数。部署可使用 SLAAC、stateless DHCPv6、stateful DHCPv6 等组合。",
"双栈时某一地址族可能配置坏或路径慢；Happy Eyeballs 并行/交错尝试 IPv6/IPv4，目标是降低单栈故障造成的用户等待，而不是固定永远优先某一族。"],
16:[
"TTL/Hop Limit 属于 IP 层，归零表示 forwarding loop/路径过长，路由器通常回 ICMP Time Exceeded；TCP RST 是传输层连接状态错误，两者语义不同。",
"不同系统使用不同初始 TTL/Hop Limit 是实现默认值，不是协议要求；它可用于粗略 fingerprint，但可配置且经过多少 hop 未知。",
"环路会让同一 packet 在多条链路反复转发，持续消耗带宽/pps/设备队列；TTL 是最终上限，路由协议快速收敛才是根治。"],
21:[
"实时音视频中旧 packet 可能很快失去价值，应用更愿意自己控制重传/FEC/jitter buffer，避免 TCP 严格有序导致一个丢包阻塞后续媒体数据。",
"DNS 同时支持 UDP/TCP：普通小查询常用 UDP；truncation、大响应、zone transfer 等会用 TCP，现代还可用 DoT/DoH。",
"UDP 提供可部署的 datagram substrate，QUIC 在用户态自行实现可靠 stream、TLS、拥塞控制和迁移，避免直接修改内核 TCP 与 middlebox ossification。"],
22:[
"若最后 ACK 丢失，Server 仍在 SYN-RECEIVED 并可能重传 SYN+ACK；Client 收到后会再次 ACK。若 Client 随后发送带正确 ACK 的 data，Server 也可据此完成握手。",
"SYN/FIN 都属于同一 TCP sequence space，使控制事件与数据顺序具有统一的可确认语义；因此 SYN 会消耗一个序号并被 ACK 为 ISN+1。",
"TCP Fast Open 在具备有效 cookie 等条件时允许 SYN 携带早期数据，减少部分建连等待；它没有取消 TCP 状态机，还要处理重放、回退和中间盒兼容。"],
23:[
"Server 的 SYN 与对 Client SYN 的 ACK 可以合并成一个 SYN+ACK，所以无需机械拆成四次；三次已完成双方 ISN/ACK 同步。",
"Client 没收到 SYN+ACK 就仍在 SYN-SENT；Server 会按重传定时器重发 SYN+ACK，Client 也可能重发 SYN，直到成功或超时。",
"QUIC 将传输建立与 TLS 1.3 深度集成，并以 Connection ID/packet number 为核心，不复用 TCP 的 SYN/ACK 状态机，所以交互消息和 RTT 模型不同。"],
24:[
"Blocking `connect()` 通常在本地 TCP 认为连接建立成功后返回；这不保证 Server 应用已经 `accept()`，只代表本地 transport handshake 语义完成。",
"由操作系统 TCP 实现与相关重试/timeout 参数控制，不应把某个默认次数当协议永久常量；排障应查看 SYN+ACK retrans 与最终 timeout。",
"服务端收到可接受的最终 ACK 后，连接从半连接状态转为 established 并进入等待应用 accept 的队列；具体内部数据结构/时点是内核实现细节。"],
25:[
"ACK 与本端 FIN 可以合并，例如收到 peer FIN 后应用也已经没有数据要发，于是回一个 FIN+ACK，抓包就可能只看到三段。",
"`shutdown(SHUT_WR)` 只关闭发送方向，仍可读；`close()` 释放 fd/引用并触发完整 socket 生命周期，行为还受引用计数、linger 等影响。",
"FIN 是有序、优雅的单方向 EOF；RST 是异常/立即重置，接收端通常得到 connection reset，不提供优雅 half-close。"],
27:[
"端口耗尽常出现 `EADDRNOTAVAIL`/新 outbound connect 失败并伴随 ephemeral-port 使用高；FD 耗尽则是进程/系统 open file 数接近上限并出现 `EMFILE/ENFILE`。",
"HTTP/2 把多个并发 request multiplex 到少量 TCP 连接，显著降低每请求建连/关闭造成的 TIME_WAIT，但也增加单连接故障影响范围。",
"NAT/PAT 同样维护连接映射和源端口；短连接 churn 可能先耗尽 NAT 端口或 conntrack，即使后端服务器本身端口/FD 充足。"],
30:[
"SYN queue 保存未完成握手的半连接；accept queue 保存已完成握手、等待应用 accept 的连接。一个受攻击不代表另一个也满。",
"Linux syncookies 主要在 SYN queue pressure/overflow 等条件下作为 fallback，并非所有正常连接无条件使用；具体行为应结合内核版本和配置。",
"SYN Flood 打握手状态/带宽；ACK Flood 常是大量无状态/伪造 ACK 消耗 ACL/conntrack/CPU 或链路，两者 packet state 和防护点不同。"],
31:[
"ACK 是累计确认，所以一旦缺口补齐，可以从旧 ACK 一次跳到更大的 next-expected byte，等于同时确认此前连续的一大段字节。",
"乱序时 cumulative ACK 通常停在第一个缺口，后续每次收到更高序号数据可能产生 duplicate ACK，并可用 SACK 标出已收到的非连续 block。",
"真实 ISN/sequence 是 32-bit 且数值很大，工具为可读性常显示 relative sequence；分析 wraparound/精确报文时可切换绝对序号。"],
32:[
"TCP 只保证有序字节流，不知道‘支付一次’这类业务事务。timeout/reset 时 Client 不能确定请求是否已被应用/数据库执行，因此需要幂等键、状态查询等上层机制。",
"仅凭连接断开无法判定：请求可能没到、已到未处理、已处理但响应丢失。正确做法是让业务请求有唯一 ID，并能查询/重试同一语义结果。",
"大窗口中一次可能丢多个 segment；SACK 告诉 sender receiver 已缓存哪些非连续范围，使其更精确恢复缺口，避免只靠累计 ACK 重传过多数据。"],
36:[
"Zero Window 是接收端通告没有可用 receive-buffer 空间，属于 flow control；拥塞窗口可能仍很大。",
"ECN 是网络拥塞显式信号，属于 congestion-control 反馈；它不表示接收端应用 buffer 满。",
"应用读慢会让 receive buffer 占用增加，可通告 rwnd 逐渐缩小甚至 0，从而反压 sender。"],
37:[
"短 Web 请求可能在连接还没增长到稳定 cwnd 前就结束，因此 initial cwnd、RTT 和 connection reuse 对完成时间占比很高。",
"经典算法在拥塞事件后设置/更新 ssthresh，具体计算与 congestion controller/recovery 相关；不能把一个固定数值当永恒规则。",
"cwnd 实质约束在途数据量，实现常以字节维护并结合 MSS/SMSS 调整；教材用‘几个 MSS’只是方便表达增长规模。"],
39:[
"高 BDP 路径需要大 receive window；Window Scale 在 SYN 中协商把 16-bit窗口字段扩展解释到更大范围，否则 rwnd 会成为吞吐 ceiling。",
"可能 application-limited、peer rwnd 小、pacing/CPU/qdisc 限制、实际 RTT高或 loss recovery；`cwnd` 只是多个约束之一。",
"不代表。内核 receive buffer 可以暂时吸收大量数据，即使应用处理慢；必须结合 recv-q、应用消费率和 window 演化判断。"],
41:[
"BBR 的速率控制高度依赖 pacing，把估计可用带宽按时间平滑送入网络，避免相同平均速率形成大 burst/queue。",
"BBR 的目标 operating point 通常希望避免长期把瓶颈队列填满，但模型估计/竞争/版本行为仍可能形成 queue；它不是‘自动消灭 bufferbloat’。",
"取决于算法、版本、RTT、AQM/ECN、bottleneck 类型等；不同 controller coexistence 可能不公平，必须用共享瓶颈实验而非单 flow 结论。"],
44:[
"卫星链路 RTT 很高，即使带宽中等，`bandwidth × RTT` 仍会得到很大的 BDP，需要更多在途数据与更大的 buffer/window 才能跑满。",
"多个连接各自有独立 congestion/receive window，聚合后可能更快填满 path；但会增加连接成本并可能对其他 flow 不公平，不是理想通用解法。",
"需要。QUIC 也运行拥塞控制并维持 in-flight data，可靠 stream 想利用高带宽长 RTT 路径同样必须覆盖 BDP。"],
45:[
"看 SYN_RECV、SYN+ACK retrans、`tcp_max_syn_backlog`/syncookie counters 与 listen overflow；握手完成但应用处理慢更像 accept queue，未完成握手堆积更像 SYN queue。",
"即使 TCP handshake 很快，应用线程若忙/被阻塞就无法及时 `accept()`/处理，已完成连接会在 accept queue 堆积，最终新连接被丢弃/延迟。",
"`SO_REUSEPORT` 允许多个 listener 绑定同地址端口并由内核分流，可把 accept/network processing 分散到多个 CPU/event loop，减少单 listener 热点。"],
46:[
"因为你必须正确实现 loss detection、重传歧义、乱序、流控、拥塞控制、MTU、安全和状态迁移；实验室无丢包能跑不代表公网正确。",
"极低延迟媒体/游戏、封闭网络、只对部分 message 可靠等有特殊语义的场景可能值得定制，但仍应明确 congestion/fairness 与安全边界。",
"QUIC 已提供 packet number/ACK、loss recovery、stream reliability、flow/congestion control、TLS、Connection ID/迁移等大量通用能力。"],
48:[
"Protocol ossification 指中间盒长期假设某协议 header/行为固定，未知扩展被丢弃或改写，导致端点难以部署新 TCP 特性。",
"加密 transport metadata 可减少中间盒依赖/篡改内部字段，也保护隐私并给未来协议演进留下空间；仍需保留必要可路由/可管理信息。",
"Client 需要快速检测 QUIC/UDP 失败并 fallback 到 HTTP/2/TCP 等；生产部署必须监控 UDP reachability 与 fallback latency。"],
49:[
"QUIC 的 crypto data 有自己的有序 offset/状态依赖；消除的是 TCP 单字节流对所有 HTTP stream 的跨流阻塞，不是让每一种控制数据都无序。",
"不是。单个 QUIC stream 内仍要按 stream offset 有序交付，QPACK dynamic dependency 也可能阻塞；只是一个 stream 的 loss 不再天然阻塞所有其他 stream。",
"通常共享。多个 stream 共用同一 connection/path 的 congestion controller，所以网络拥塞会影响整体发送速率；独立的是 stream reassembly/flow-control 状态，不是每流独占网络容量。"],
50:[
"MPTCP 允许一个逻辑 TCP connection 同时使用多个 subflow/path；QUIC 标准 migration 主要强调四元组变化后把同一 connection 延续/切换到新 path，概念不同。",
"新 path 需要 PATH_CHALLENGE/PATH_RESPONSE 等验证，避免仅凭伪造源地址就把连接迁走或向 victim 放大流量；Connection ID 也不应被当作单独认证凭据。",
"传统五元组 hash 可能把迁移后的 packet 分到另一个 backend；LB 需要理解/路由 QUIC Connection ID 或保持共享状态，否则新节点没有原连接状态。"],
54:[
"Referral 是上级 DNS server 告诉 resolver‘这个 zone 应去问哪些 NS’，通常伴随 delegation/必要 glue，而不是直接给最终目标 record。",
"本地 recursive resolver 可提供缓存、内部 split DNS、DNSSEC 验证、访问策略与更低解析 RTT，也能减少每个终端直接访问外部 resolver。",
"软件可以同时实现两种角色，但运营上常分离以缩小攻击面/缓存污染风险，并明确哪些 zone 提供权威、哪些请求允许递归。"],
56:[
"Zone apex 必须同时承载 SOA/NS 等记录，而 CNAME 的语义要求该 owner name 不与其他普通 data 共存，因此传统上 apex 不能直接做普通 CNAME；云 ALIAS 是提供商扩展。",
"SRV 记录服务的 priority、weight、port 与 target，让客户端按服务发现语义选择 endpoint，而不仅得到 IP。",
"CAA 声明哪些 CA 被授权为域签发证书，CA 在签发流程中检查它以降低非授权签发风险。"],
58:[
"常见是 DNS/GSLB 先选择 region/POP，站点内再用 Anycast/L4/L7 选具体 backend；DNS 处理分钟/秒级入口，连接级 LB 做更实时调度。",
"DNS answer 已被 resolver/client cache，且已有 keep-alive connection 可继续复用旧 IP，所以健康检查摘除不会瞬间让所有现有流量消失。",
"GeoDNS 便于显式地域/容量策略但受缓存；Anycast 路由透明、切换快但依赖 BGP policy。大型系统常组合而非二选一。"],
70:[
"不会。HTTP/3 消除 TCP 单字节序列导致的跨 stream transport HOL，但单 stream 内 ordering、QPACK dynamic dependency 等仍可能等待。",
"该 packet 中的相关 stream frames 都需要通过新 QUIC packet 重发；但其他已完整到达的 stream data 不需要等待同一个 TCP sequence gap。",
"因为 QUIC reliable stream 暴露有序字节流语义：同一 stream 更高 offset 的字节不能在缺失低 offset 数据前按序交付给应用。"],
74:[
"传统 TLS 中 destination IP 仍可见，ClientHello 的 SNI 也可能暴露 hostname；ECH 目标是保护真实 ClientHello/SNI，但不能隐藏路由所需 IP，部署还依赖客户端/DNS/服务端。",
"不能。TLS 保护传输机密性/完整性/认证，不理解 SQL query 或应用授权逻辑；SQL injection 是应用输入处理问题。",
"如果终端信任企业安装的根 CA，代理可以分别与客户端/目标站建立 TLS connection 并签发临时证书完成合法 MITM；这改变了信任边界，不是破解密码算法。"],
81:[
"`accept4()` 可在创建 accepted fd 时原子设置 NONBLOCK/CLOEXEC，减少后续 `fcntl` syscall 和多线程/exec race。",
"`SO_REUSEADDR` 主要影响地址重绑定/特定 bind 语义；`SO_REUSEPORT` 允许多个 listener 同地址端口并由内核分流，常用于多核扩展。",
"可以。fork 后多个进程可继承同一个 listen fd；也可以分别用 SO_REUSEPORT 创建 listener。两种模型的负载分配和锁/队列行为不同。"],
83:[
"Reactor 等 readiness：事件到来后应用自己执行 read/write；Proactor 先提交异步操作，收到 completion 后处理结果。真实框架可能是混合模型。",
"Regular file 的‘readable’不表示磁盘 IO 已完成，page-cache miss 仍可能阻塞；io_uring 可以真正提交 file read/write 并以 completion 通知，更贴近存储 IO。",
"Signal-driven IO 的信号处理/状态管理、可移植性和复杂度不如 epoll/kqueue/event loop 生态，生产网络服务较少把它作为主模型。"],
86:[
"是。LT 也通常配 nonblocking，因为 readiness 与实际 syscall 之间存在 race，多线程或状态变化仍可能让 blocking read 卡住。",
"FIONREAD 只是某一瞬间可用字节的观测，查询和 read 之间会变化，也不能替代 partial parser/TLS 状态；循环 read 到 EAGAIN 是更可靠的完成条件。",
"TLS library 有内部 record/buffer 状态；应循环 `SSL_read` 并正确处理 WANT_READ/WANT_WRITE/`SSL_pending`，不能只根据 raw EPOLLIN 一次读完就结束。"],
94:[
"端口耗尽常伴随 outbound connect 的 `EADDRNOTAVAIL`/NAT port pressure；FD 耗尽出现 `EMFILE/ENFILE` 和 open-fd 接近限制。TIME_WAIT 本身并不等于进程仍持有普通 fd。",
"HTTP/2 多路复用让许多 request 共用少量连接，降低连接创建/关闭频率和 TIME_WAIT；但连接 lifetime/GOAWAY/负载均衡仍需合理设计。",
"NAT/PAT 也要维护四/五元组映射与源端口，短连接峰值可能先把 NAT table/port pool 打满，所以必须检查整条链路而非只看应用服务器。"],
99:[
"`SO_REUSEPORT` 允许多个 listener 在同一 address:port 接收连接，内核按 hash/BPF 等策略分流，可把 accept/event loop 按 CPU shard，减少单 acceptor 热点。",
"长连接通常先在 L4/L7 LB 做 connection ownership；迁移/发布依赖 connection draining、客户端重连/Connection ID（QUIC）或业务会话重新绑定。TCP 本身不能把一个已建立连接无损搬到另一普通 backend。",
"空闲连接仍有 socket 结构、协议状态、send/receive buffer 最小占用、timer、TLS/应用对象；所以 active rate 低只减少动态 CPU/PPS，不消除固定内存成本。"],
}

def replace_answers(section, answers):
    matches=list(re.finditer(r'\*\*参考回答\*\*：.*', section))
    if len(matches)!=3:
        return section, False
    out=[]; pos=0
    for m,ans in zip(matches,answers):
        out.append(section[pos:m.start()]); out.append('**参考回答**：'+ans); pos=m.end()
    out.append(section[pos:])
    return ''.join(out), True

for p in ROOT.glob('questions/*/*.md'):
    if p.name=='README.md': continue
    txt=p.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(\d+)',txt,re.M)
    if not m: continue
    qid=int(m.group(1))
    if qid not in A: continue
    secm=re.search(r'(## 面试官常见追问（PDF 原题 \+ 回答方向）\n.*?)(?=\n## 高频易错点)',txt,re.S)
    if not secm: raise RuntimeError(p)
    new,ok=replace_answers(secm.group(1),A[qid])
    if not ok: raise RuntimeError(f'expected 3 answers: {p}')
    txt=txt[:secm.start(1)]+new+txt[secm.end(1):]
    p.write_text(txt,encoding='utf-8')
print('fixed',len(A),'files')
