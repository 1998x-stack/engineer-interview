# -*- coding: utf-8 -*-
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BLOCKS={
'01-link-layer-foundations': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **端到端目标 vs 当前一跳**：IP 回答“最终去哪”，MAC/邻居解析回答“这一跳交给谁”。
- **封装不是装饰**：不同层 header 决定不同设备能做什么；抓包点不同会看到不同 offload/封装形态。
- **二层广播域必须可控**：ARP、VLAN、MAC table、环路与广播风暴是一组连续问题，不要分开背。

### 本章白板题

1. 画出同网段通信与跨网段通信的 Ethernet/IP header 差异。
2. 给定 MTU 1500、IPv4/TCP options，计算实际 MSS，并解释 TSO 为何让本机抓包看起来“超 MTU”。
3. 画一个 VLAN trunk/access 场景，说明 ARP broadcast 能到哪里、为什么。

### 最小实验组合

`ip addr` → `ip route` → `ip neigh` → `arping`/`ping` → `tcpdump -e -nn` → `tracepath`。目标是能从路由选择一直证明到实际二层目的 MAC。''',
'02-ip-nat-routing': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **Route lookup 先于邻居解析**：先决定 next-hop，再 ARP/NDP；NAT/ACL/conntrack 是中间盒附加状态。
- **路由不是“最短路”一个词**：数据平面 LPM、IGP cost、BGP policy、ECMP 分别处在不同层次。
- **公网可达性是整条路径属性**：NAT、PMTU、ICMP、BGP、Anycast 都可能让“地址正确”仍不可用。

### 本章白板题

1. 给出三条重叠 CIDR route，现场做 Longest Prefix Match。
2. 画 SNAT/PAT 五元组变化与 return mapping。
3. 对比 OSPF、eBGP/iBGP、Anycast/GSLB，说明谁解决“内部路径”“跨 AS 策略”“全局入口”。

### 最小实验组合

`ip route get`、`tracepath`、`traceroute -T -p 443`、`conntrack`（有权限时）、`tcpdump icmp or icmp6`。实验重点是 PMTU black hole 与 NAT state，而不是只看 ping。''',
'03-tcp-connection-reliability': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **TCP 是两个方向的有序字节序号空间**：SYN/FIN、SEQ/ACK、half-close、四次挥手都从这里推导。
- **传输确认 ≠ 业务确认**：`send()`、TCP ACK、peer `read()`、业务 commit 是四个不同里程碑。
- **状态机 + 时间线是唯一稳定的答题方式**：握手/重传/TIME_WAIT/CLOSE_WAIT 都应落到状态与 packet evidence。

### 本章白板题

1. 画三次握手，标 ISN、ACK、MSS/WS/SACK options 与状态迁移。
2. 画“第三 ACK 丢失 + Client 带数据”的时间线。
3. 给出一个订单请求连接 reset 场景，解释为什么 TCP 无法提供 Exactly Once。

### 最小实验组合

`ss -tanpi`、`tcpdump -nn -S`、Wireshark Seq/Ack/SACK、`nstat -az`。实验必须能把抓包中的 Seq/Ack 与 socket 状态一一对应。''',
'04-tcp-performance-congestion': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **吞吐由多重上限共同决定**：application data、`rwnd`、`cwnd`、BDP、pacing、socket/qdisc/device queue 都可能限制。
- **流控保护 receiver，拥塞控制保护 network**：zero-window 与 loss/ECN/RTT growth 的信号必须分开。
- **拥塞算法是 operating-point 策略**：Reno/CUBIC/BBR 的核心区别是如何探测容量、识别拥塞、恢复发送。

### 本章白板题

1. 计算 10Gbps × 80ms 的 BDP，并解释 window 不够时为何零丢包也跑不满。
2. 在同一图上画 rwnd/cwnd/ssthresh/flight size。
3. 对比 Reno、CUBIC、BBR 的增长/减速信号与 queue 行为。

### 最小实验组合

`ss -tin`、`tc qdisc/netem`、`iperf3`、`nstat`。至少做一次高 RTT + loss 实验，观察 cwnd/retrans/throughput，而不是只背公式。''',
'05-udp-quic-http3': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **UDP 只是 datagram substrate**：QUIC 的可靠性、stream、TLS、流控、拥塞控制都在 QUIC 层实现。
- **HTTP/3 的关键不是“UDP 更快”**：真正价值是 QUIC stream 独立重组、用户态演进、Connection ID/迁移与集成 TLS。
- **没有协议能消除所有等待**：HTTP/3 仍有单 stream ordering、QPACK dependency 和 connection-wide congestion control。

### 本章白板题

1. 从零列出“可靠 UDP”必须补齐的机制，并解释为什么这会演化成完整 transport protocol。
2. 画 HTTP/2/TCP 与 HTTP/3/QUIC 的 stream→packet mapping，说明 HOL 差异。
3. 画 Wi-Fi→5G migration，标 Connection ID 与 path validation。

### 最小实验组合

`curl --http2/--http3`、Wireshark QUIC、qlog、`tc netem loss/delay`。关注 tail latency 与 stream completion，而不是只测无损 LAN 峰值。''',
'06-dns-cdn': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **DNS 是缓存化的委派数据库**：Recursive/Iterative、Referral、TTL/negative cache、CNAME 链必须连成一条解析路径。
- **DNSSEC 与加密 DNS 分工不同**：前者验证 data，DoH/DoT 保护 Client↔Resolver transport。
- **CDN 是全局调度 + 边缘连接 + 缓存体系**：hit ratio 只是结果指标，不代表所有性能收益。

### 本章白板题

1. 画 stub→recursive→root→TLD→authoritative 完整链，并插入 cache/CNAME。
2. 解释为什么 DNS 改记录不能保证 TTL 秒后所有流量立即切换。
3. 设计 CDN cache key，列出 Cookie/Query/Vary 造成的缓存碎片化与泄漏风险。

### 最小实验组合

`dig +trace`、`dig +tcp`、指定 resolver/authoritative 查询、`curl -I` 查看 Age/Via/Cache-Status（若提供）。要求能区分 DNS cache、连接复用和 CDN object cache。''',
'07-http': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **HTTP Semantics 与 wire format 分离**：GET/POST/status/cache 语义跨 HTTP/1.1、2、3 共享；framing/streaming 机制不同。
- **缓存题先问 cache key/freshness/validation/shared scope**，不要把 `no-cache` 解释成“不能缓存”。
- **多路复用不等于无队头阻塞**：HTTP/2 stream 与 TCP byte stream 是两个层次。

### 本章白板题

1. 画 HTTP/1.1 message framing，解释 Content-Length/chunked 以及 CL.TE 风险。
2. 给出 GET/PUT/DELETE/POST，分别判断 safe/idempotent/cacheable 与业务重试策略。
3. 画 HTTP/2 stream/frame 与 TCP、HTTP/3 stream 与 QUIC 的对应关系。

### 最小实验组合

`curl -v/--http2/--http3`、浏览器 DevTools、`nghttp`/Wireshark HTTP2（可用时）。至少验证一次 ETag/304 和 Cache-Control revalidation。''',
'08-tls-https-pki': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **认证、密钥建立、数据保护分工明确**：Certificate/CertificateVerify、(EC)DHE、HKDF、AEAD 各自解决不同问题。
- **证书可信 ≠ hostname 正确**：chain、trust anchor、SAN、validity、usage、CT/revocation 是多个独立检查。
- **0-RTT 用历史状态换延迟**：Replay Risk 必须由应用幂等/anti-replay 共同治理。

### 本章白板题

1. 画 TLS 1.3 full handshake，标明从何时开始加密、CertificateVerify/Finished 各证明什么。
2. 画 Root→Intermediate→Leaf 验证链，并解释为什么 Server 不应把“自己发的 Root”当信任来源。
3. 给出转账、静态 GET、幂等查询三种请求，判断是否适合 0-RTT。

### 规范更新（2026）

TLS 1.3 现行规范为 **RFC 9846**，它兼容地取代 RFC 8446，并收紧 key-share reuse、旧版本协商等要求；学习资料若仍引用 RFC 8446，应以 RFC 9846 为当前规范对照更新。''',
'09-linux-socket-io': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **Readiness 不是 Completion**：epoll 告诉“现在可做 IO”，应用仍要正确处理 partial read/write/EAGAIN。
- **Event loop 正确性优先于 API 名字**：ET/LT、nonblocking、EPOLLOUT、ONESHOT 都服务于 fd 状态机与所有权。
- **网络栈瓶颈可能在 softirq/NIC queue**：业务线程不忙并不代表机器网络处理还有余量。

### 本章白板题

1. 画 `socket→bind→listen→accept4→recv/send→close`，标 listener/connected fd 区别。
2. 写 ET read loop 伪代码，包含 EAGAIN/EOF/error/SSL WANT_READ-WANT_WRITE。
3. 画 NIC RX→NAPI→GRO→IP/TCP→socket queue→recv，并解释 RSS/RPS/RFS。

### 最小实验组合

`strace -e network`、`ss`、`perf top`、`/proc/softirqs`、`ethtool -l/-x/-S`、`tcpdump`。目标是把 syscall、socket queue、softirq 和 packet timeline 连起来。''',
'10-troubleshooting-system-design': '''## V2 本章深度训练框架

### 必须形成的心智模型

- **先 decomposition，再 hypothesis，再证据**：DNS/connect/TLS/TTFB/body/render；不要“先猜网卡/先调 sysctl”。
- **单一指标无法定根因**：连接状态、RTT/retrans、队列、softirq、trace、双端抓包必须互相印证。
- **系统设计先做容量方程**：FD、bytes/conn、PPS、带宽、TLS、NAT/LB state、重连风暴、发布 headroom。

### 本章白板题

1. 画 `https://example.com` 冷连接与热连接两条完整路径，指出哪些阶段可被 cache/connection reuse 跳过。
2. 给“p99 上升但 CPU/QPS 不变”建立至少 5 个可证伪假设并列下一条观测。
3. 设计 1M long connections 容量表并推演一次 30% 实例同时重启的 reconnect storm。

### 故障面试答题模板

`现象 → 影响范围 → 时间线 → 分层拆解 → 2~3 个优先假设 → 指标/抓包验证 → 排除/确认 → 缓解 → 根因修复 → 防复发监控`。高级答案一定包含“哪些证据还不能证明什么”。''',
}
START='<!-- CHAPTER-V2-START -->'; END='<!-- CHAPTER-V2-END -->'
for d,b in BLOCKS.items():
    p=ROOT/'questions'/d/'README.md'
    txt=p.read_text(encoding='utf-8')
    import re
    txt=re.sub(re.escape(START)+r'.*?'+re.escape(END)+r'\n*','',txt,flags=re.S)
    anchor='\n## 题目目录\n'
    if anchor not in txt: raise RuntimeError(p)
    txt=txt.replace(anchor,f'\n{START}\n{b.strip()}\n{END}\n'+anchor,1)
    p.write_text(txt,encoding='utf-8')
print('updated',len(BLOCKS),'chapter readmes')
