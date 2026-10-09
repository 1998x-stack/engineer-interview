# Linux 网络排障命令速查

| 目的 | 命令 | 主要看什么 |
|---|---|---|
| 连接/状态 | `ss -s; ss -tanp; ss -lnt; ss -ti` | 连接数、TCP 状态、监听、RTT/cwnd |
| 路由 | `ip route; ip route get <dst>` | 默认路由、LPM 最终命中 |
| 邻居 | `ip neigh` | ARP/NDP 邻居缓存 |
| DNS | `dig; dig +trace; resolvectl` | Resolver/权威链路/缓存 |
| 抓包 | `tcpdump -i any -nn -s0 -w out.pcap` | 生成 pcap 证据 |
| 链路 | `ping; traceroute; mtr` | RTT、路径、丢包线索 |
| NIC | `ethtool -S eth0; ethtool -l eth0` | drop/error/多队列 |
| CPU 网络 | `cat /proc/softirqs; cat /proc/interrupts` | NET_RX/IRQ 热点 |
| conntrack | `conntrack -S; conntrack -L` | NAT/状态表容量 |
| HTTP | `curl -w ... -v` | DNS/connect/TLS/TTFB/total |

## 使用原则

1. 先确认故障层次，再选择工具。
2. `ss`/指标回答“系统现在是什么状态”，`tcpdump` 回答“线上实际交换了什么”。
3. 单端抓包不能自动证明丢包位置；关键问题尽量两端同时抓。
4. 看到 checksum error/超大 segment 时先考虑 NIC offload 造成的本机观测差异。
