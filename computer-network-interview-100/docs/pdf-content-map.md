# PDF 内容映射

本文件用于证明 PDF 内容在 Repository 中的覆盖关系。

## 主体内容

### 第一章 网络分层、链路与二层基础

- 001. OSI 七层与 TCP/IP 模型如何对应？工程上为什么更常用 TCP/IP？ → [`questions/01-link-layer-foundations/001-osi-tcp-ip-model.md`](../questions/01-link-layer-foundations/001-osi-tcp-ip-model.md)
- 002. 一个应用层消息从 send() 到网卡发送经历了什么封装？ → [`questions/01-link-layer-foundations/002-send-to-nic-encapsulation.md`](../questions/01-link-layer-foundations/002-send-to-nic-encapsulation.md)
- 003. Hub、Switch、Router 的本质区别是什么？ → [`questions/01-link-layer-foundations/003-hub-switch-router.md`](../questions/01-link-layer-foundations/003-hub-switch-router.md)
- 004. MAC 地址和 IP 地址为什么要同时存在？ → [`questions/01-link-layer-foundations/004-mac-vs-ip.md`](../questions/01-link-layer-foundations/004-mac-vs-ip.md)
- 005. ARP 的工作原理是什么？跨网段通信时 ARP 查询谁？ → [`questions/01-link-layer-foundations/005-arp-next-hop.md`](../questions/01-link-layer-foundations/005-arp-next-hop.md)
- 006. MTU 与 MSS 有什么区别？为什么常见 MSS 是 1460？ → [`questions/01-link-layer-foundations/006-mtu-vs-mss.md`](../questions/01-link-layer-foundations/006-mtu-vs-mss.md)
- 007. 子网掩码 / CIDR 前缀到底解决什么问题？ → [`questions/01-link-layer-foundations/007-cidr-subnet-mask.md`](../questions/01-link-layer-foundations/007-cidr-subnet-mask.md)
- 008. ping 的完整原理是什么？ping 不通能否说明 TCP 也不通？ → [`questions/01-link-layer-foundations/008-ping-icmp.md`](../questions/01-link-layer-foundations/008-ping-icmp.md)
- 009. traceroute 为什么能看到中间路由器？ → [`questions/01-link-layer-foundations/009-traceroute-ttl.md`](../questions/01-link-layer-foundations/009-traceroute-ttl.md)
- 010. 为什么二层需要 VLAN？VLAN 与广播域是什么关系？ → [`questions/01-link-layer-foundations/010-vlan-broadcast-domain.md`](../questions/01-link-layer-foundations/010-vlan-broadcast-domain.md)

### 第二章 IP、NAT 与路由

- 011. NAT 到底做了什么？SNAT、DNAT、PAT 有什么区别？ → [`questions/02-ip-nat-routing/011-nat-snat-dnat-pat.md`](../questions/02-ip-nat-routing/011-nat-snat-dnat-pat.md)
- 012. NAT 为什么让 P2P 变难？STUN、TURN、ICE 分别做什么？ → [`questions/02-ip-nat-routing/012-nat-traversal-stun-turn-ice.md`](../questions/02-ip-nat-routing/012-nat-traversal-stun-turn-ice.md)
- 013. DHCP 的 DORA 流程是什么？为什么客户端一开始没有 IP 也能通信？ → [`questions/02-ip-nat-routing/013-dhcp-dora.md`](../questions/02-ip-nat-routing/013-dhcp-dora.md)
- 014. IPv4 与 IPv6 除了地址长度，还有哪些关键差异？ → [`questions/02-ip-nat-routing/014-ipv4-vs-ipv6.md`](../questions/02-ip-nat-routing/014-ipv4-vs-ipv6.md)
- 015. IP Fragmentation 为什么通常应该避免？Path MTU Discovery 如何工作？ → [`questions/02-ip-nat-routing/015-ip-fragmentation-pmtud.md`](../questions/02-ip-nat-routing/015-ip-fragmentation-pmtud.md)
- 016. TTL / Hop Limit 为什么存在？路由环路是怎么形成的？ → [`questions/02-ip-nat-routing/016-ttl-hop-limit-routing-loop.md`](../questions/02-ip-nat-routing/016-ttl-hop-limit-routing-loop.md)
- 017. 路由器为什么使用最长前缀匹配？ → [`questions/02-ip-nat-routing/017-longest-prefix-match.md`](../questions/02-ip-nat-routing/017-longest-prefix-match.md)
- 018. OSPF 与 BGP 的定位和核心思想有什么不同？ → [`questions/02-ip-nat-routing/018-ospf-vs-bgp.md`](../questions/02-ip-nat-routing/018-ospf-vs-bgp.md)
- 019. BGP 的 AS_PATH、LOCAL_PREF、MED 分别解决什么？ → [`questions/02-ip-nat-routing/019-bgp-as-path-local-pref-med.md`](../questions/02-ip-nat-routing/019-bgp-as-path-local-pref-med.md)
- 020. Anycast 是什么？为什么 DNS/CDN 常用？ → [`questions/02-ip-nat-routing/020-anycast-dns-cdn.md`](../questions/02-ip-nat-routing/020-anycast-dns-cdn.md)

### 第三章 TCP 连接、状态机与可靠性

- 021. TCP 与 UDP 的本质区别是什么？不要只说“可靠/不可靠”。 → [`questions/03-tcp-connection-reliability/021-tcp-vs-udp.md`](../questions/03-tcp-connection-reliability/021-tcp-vs-udp.md)
- 022. TCP 三次握手完整过程是什么？每一步同步了什么状态？ → [`questions/03-tcp-connection-reliability/022-tcp-three-way-handshake.md`](../questions/03-tcp-connection-reliability/022-tcp-three-way-handshake.md)
- 023. 为什么 TCP 需要三次握手，不能两次？ → [`questions/03-tcp-connection-reliability/023-why-three-way-handshake.md`](../questions/03-tcp-connection-reliability/023-why-three-way-handshake.md)
- 024. 第三次握手 ACK 丢失后，客户端立刻带数据发送，服务端能建立连接吗？ → [`questions/03-tcp-connection-reliability/024-third-ack-lost-with-data.md`](../questions/03-tcp-connection-reliability/024-third-ack-lost-with-data.md)
- 025. TCP 为什么通常需要四次挥手？FIN 与 ACK 的语义是什么？ → [`questions/03-tcp-connection-reliability/025-tcp-four-way-close.md`](../questions/03-tcp-connection-reliability/025-tcp-four-way-close.md)
- 026. TIME_WAIT 为什么存在？为什么经常讨论 2MSL？ → [`questions/03-tcp-connection-reliability/026-time-wait-2msl.md`](../questions/03-tcp-connection-reliability/026-time-wait-2msl.md)
- 027. 服务器几十万个 TIME_WAIT，应该怎么分析而不是直接改内核参数？ → [`questions/03-tcp-connection-reliability/027-time-wait-at-scale.md`](../questions/03-tcp-connection-reliability/027-time-wait-at-scale.md)
- 028. CLOSE_WAIT 大量堆积通常说明什么？ → [`questions/03-tcp-connection-reliability/028-close-wait-leak.md`](../questions/03-tcp-connection-reliability/028-close-wait-leak.md)
- 029. 什么是 TCP Half-close？什么时候有用？ → [`questions/03-tcp-connection-reliability/029-tcp-half-close.md`](../questions/03-tcp-connection-reliability/029-tcp-half-close.md)
- 030. SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？ → [`questions/03-tcp-connection-reliability/030-syn-flood-syn-cookies.md`](../questions/03-tcp-connection-reliability/030-syn-flood-syn-cookies.md)
- 031. TCP Sequence Number 与 ACK Number 到底在确认什么？ → [`questions/03-tcp-connection-reliability/031-tcp-seq-ack.md`](../questions/03-tcp-connection-reliability/031-tcp-seq-ack.md)
- 032. TCP 可靠性由哪些机制共同保证？ → [`questions/03-tcp-connection-reliability/032-tcp-reliability.md`](../questions/03-tcp-connection-reliability/032-tcp-reliability.md)
- 033. 超时重传、快速重传和 SACK 分别解决什么？ → [`questions/03-tcp-connection-reliability/033-rto-fast-retransmit-sack.md`](../questions/03-tcp-connection-reliability/033-rto-fast-retransmit-sack.md)
- 034. TCP 滑动窗口解决什么问题？发送窗口为什么不是固定大小？ → [`questions/03-tcp-connection-reliability/034-tcp-sliding-window.md`](../questions/03-tcp-connection-reliability/034-tcp-sliding-window.md)
- 035. 所谓 TCP “粘包/拆包”到底是什么？应用层怎样正确 framing？ → [`questions/03-tcp-connection-reliability/035-tcp-stream-framing.md`](../questions/03-tcp-connection-reliability/035-tcp-stream-framing.md)

### 第四章 TCP 性能、窗口与拥塞控制

- 036. Flow Control 与 Congestion Control 的区别是什么？ → [`questions/04-tcp-performance-congestion/036-flow-vs-congestion-control.md`](../questions/04-tcp-performance-congestion/036-flow-vs-congestion-control.md)
- 037. Slow Start 为什么叫“慢启动”，它的增长其实有多快？ → [`questions/04-tcp-performance-congestion/037-tcp-slow-start.md`](../questions/04-tcp-performance-congestion/037-tcp-slow-start.md)
- 038. Fast Retransmit 与 Fast Recovery 分别是什么？ → [`questions/04-tcp-performance-congestion/038-fast-retransmit-fast-recovery.md`](../questions/04-tcp-performance-congestion/038-fast-retransmit-fast-recovery.md)
- 039. rwnd、cwnd、ssthresh 三者是什么关系？ → [`questions/04-tcp-performance-congestion/039-rwnd-cwnd-ssthresh.md`](../questions/04-tcp-performance-congestion/039-rwnd-cwnd-ssthresh.md)
- 040. TCP Reno 与 CUBIC 的核心差异是什么？ → [`questions/04-tcp-performance-congestion/040-reno-vs-cubic.md`](../questions/04-tcp-performance-congestion/040-reno-vs-cubic.md)
- 041. BBR 与 CUBIC 的核心思想差在哪里？ → [`questions/04-tcp-performance-congestion/041-bbr-vs-cubic.md`](../questions/04-tcp-performance-congestion/041-bbr-vs-cubic.md)
- 042. Nagle Algorithm 解决什么？为什么交互式 RPC 常设置 TCP_NODELAY？ → [`questions/04-tcp-performance-congestion/042-nagle-tcp-nodelay.md`](../questions/04-tcp-performance-congestion/042-nagle-tcp-nodelay.md)
- 043. TCP_NODELAY 到底改变什么，不改变什么？ → [`questions/04-tcp-performance-congestion/043-tcp-nodelay-boundaries.md`](../questions/04-tcp-performance-congestion/043-tcp-nodelay-boundaries.md)
- 044. BDP 是什么？为什么高带宽长 RTT 链路需要大窗口？ → [`questions/04-tcp-performance-congestion/044-bandwidth-delay-product.md`](../questions/04-tcp-performance-congestion/044-bandwidth-delay-product.md)
- 045. TCP 半连接队列、全连接队列与 listen(backlog) 有什么关系？ → [`questions/04-tcp-performance-congestion/045-syn-queue-accept-queue-backlog.md`](../questions/04-tcp-performance-congestion/045-syn-queue-accept-queue-backlog.md)

### 第五章 UDP、QUIC 与 HTTP/3 传输基础

- 046. 如果基于 UDP 实现可靠传输，需要补哪些机制？ → [`questions/05-udp-quic-http3/046-reliable-udp-design.md`](../questions/05-udp-quic-http3/046-reliable-udp-design.md)
- 047. UDP 为什么不存在 TCP 那种“粘包”语义？ → [`questions/05-udp-quic-http3/047-udp-datagram-boundaries.md`](../questions/05-udp-quic-http3/047-udp-datagram-boundaries.md)
- 048. QUIC 为什么建立在 UDP 上，而不是直接改 TCP？ → [`questions/05-udp-quic-http3/048-why-quic-over-udp.md`](../questions/05-udp-quic-http3/048-why-quic-over-udp.md)
- 049. HTTP/2 已有多路复用，为什么 HTTP/3 仍需要 QUIC？ → [`questions/05-udp-quic-http3/049-http2-vs-http3-hol.md`](../questions/05-udp-quic-http3/049-http2-vs-http3-hol.md)
- 050. QUIC Connection Migration 为什么适合移动网络？ → [`questions/05-udp-quic-http3/050-quic-connection-migration.md`](../questions/05-udp-quic-http3/050-quic-connection-migration.md)
- 051. QUIC 为什么能减少首次/恢复连接延迟？0-RTT 的收益与风险是什么？ → [`questions/05-udp-quic-http3/051-quic-handshake-0rtt.md`](../questions/05-udp-quic-http3/051-quic-handshake-0rtt.md)
- 052. QUIC 使用 UDP，是否就不需要拥塞控制和流量控制？ → [`questions/05-udp-quic-http3/052-quic-flow-congestion-control.md`](../questions/05-udp-quic-http3/052-quic-flow-congestion-control.md)

### 第六章 DNS、全局调度与 CDN

- 053. 输入域名后，DNS 完整解析链路是什么？ → [`questions/06-dns-cdn/053-dns-resolution-path.md`](../questions/06-dns-cdn/053-dns-resolution-path.md)
- 054. DNS 递归查询与迭代查询有什么区别？ → [`questions/06-dns-cdn/054-dns-recursive-vs-iterative.md`](../questions/06-dns-cdn/054-dns-recursive-vs-iterative.md)
- 055. 为什么“DNS 使用 UDP”是错误或不完整答案？ → [`questions/06-dns-cdn/055-dns-udp-and-tcp.md`](../questions/06-dns-cdn/055-dns-udp-and-tcp.md)
- 056. A、AAAA、CNAME、MX、NS、TXT 分别表达什么？ → [`questions/06-dns-cdn/056-dns-record-types.md`](../questions/06-dns-cdn/056-dns-record-types.md)
- 057. DNS TTL 与 Negative Caching 是什么？ → [`questions/06-dns-cdn/057-dns-ttl-negative-cache.md`](../questions/06-dns-cdn/057-dns-ttl-negative-cache.md)
- 058. DNS 如何做负载均衡？它的局限是什么？ → [`questions/06-dns-cdn/058-dns-load-balancing.md`](../questions/06-dns-cdn/058-dns-load-balancing.md)
- 059. DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？ → [`questions/06-dns-cdn/059-dns-cache-poisoning-dnssec-doh-dot.md`](../questions/06-dns-cdn/059-dns-cache-poisoning-dnssec-doh-dot.md)
- 060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？ → [`questions/06-dns-cdn/060-cdn-acceleration.md`](../questions/06-dns-cdn/060-cdn-acceleration.md)

### 第七章 HTTP/1.1、HTTP/2 与应用层协议

- 061. HTTP/1.1 Request/Response 报文结构是什么？ → [`questions/07-http/061-http11-message-structure.md`](../questions/07-http/061-http11-message-structure.md)
- 062. GET 与 POST 真正的区别是什么？safe、idempotent、cacheable 如何区分？ → [`questions/07-http/062-get-vs-post-semantics.md`](../questions/07-http/062-get-vs-post-semantics.md)
- 063. 常见 HTTP 状态码中，301/302/307/308、401/403、502/504 怎么区分？ → [`questions/07-http/063-http-status-codes.md`](../questions/07-http/063-http-status-codes.md)
- 064. HTTP “无状态”是什么意思？Cookie、Session、Token 为什么出现？ → [`questions/07-http/064-http-stateless-cookie-session-token.md`](../questions/07-http/064-http-stateless-cookie-session-token.md)
- 065. HTTP Persistent Connection 与 TCP 长连接是什么关系？ → [`questions/07-http/065-http-persistent-connection.md`](../questions/07-http/065-http-persistent-connection.md)
- 066. Content-Length 与 chunked transfer encoding 解决什么？ → [`questions/07-http/066-content-length-chunked.md`](../questions/07-http/066-content-length-chunked.md)
- 067. Cache-Control 中 max-age、no-cache、no-store、private、must-revalidate 怎么理解？ → [`questions/07-http/067-cache-control.md`](../questions/07-http/067-cache-control.md)
- 068. ETag/If-None-Match 与 Last-Modified/If-Modified-Since 如何工作？ → [`questions/07-http/068-etag-last-modified.md`](../questions/07-http/068-etag-last-modified.md)
- 069. HTTP/1.1 与 HTTP/2 的核心差异是什么？ → [`questions/07-http/069-http11-vs-http2.md`](../questions/07-http/069-http11-vs-http2.md)
- 070. HTTP/2 为什么仍存在 Head-of-Line Blocking？ → [`questions/07-http/070-http2-head-of-line-blocking.md`](../questions/07-http/070-http2-head-of-line-blocking.md)
- 071. HPACK 与 QPACK 为什么不能完全相同？ → [`questions/07-http/071-hpack-vs-qpack.md`](../questions/07-http/071-hpack-vs-qpack.md)
- 072. WebSocket、SSE、Long Polling 应该怎么选？ → [`questions/07-http/072-websocket-sse-long-polling.md`](../questions/07-http/072-websocket-sse-long-polling.md)
- 073. gRPC 为什么常运行在 HTTP/2 上？ → [`questions/07-http/073-grpc-http2.md`](../questions/07-http/073-grpc-http2.md)

### 第八章 HTTPS、TLS 1.3 与 PKI

- 074. HTTP 与 HTTPS 的本质区别是什么？TLS 提供了哪些安全属性？ → [`questions/08-tls-https-pki/074-http-vs-https.md`](../questions/08-tls-https-pki/074-http-vs-https.md)
- 075. TLS 1.3 Handshake 需要掌握到什么程度？ → [`questions/08-tls-https-pki/075-tls13-handshake.md`](../questions/08-tls-https-pki/075-tls13-handshake.md)
- 076. 浏览器如何验证 HTTPS 证书？证书链、主机名、有效期各自是什么作用？ → [`questions/08-tls-https-pki/076-certificate-validation.md`](../questions/08-tls-https-pki/076-certificate-validation.md)
- 077. TLS 为什么同时使用非对称密码学和对称加密？ → [`questions/08-tls-https-pki/077-asymmetric-vs-symmetric-crypto.md`](../questions/08-tls-https-pki/077-asymmetric-vs-symmetric-crypto.md)
- 078. 什么是 Forward Secrecy？为什么 ECDHE 很重要？ → [`questions/08-tls-https-pki/078-forward-secrecy-ecdhe.md`](../questions/08-tls-https-pki/078-forward-secrecy-ecdhe.md)
- 079. SNI 与 ALPN 分别解决什么问题？ → [`questions/08-tls-https-pki/079-sni-vs-alpn.md`](../questions/08-tls-https-pki/079-sni-vs-alpn.md)
- 080. TLS 1.3 0-RTT 为什么有 Replay Risk？哪些业务不适合？ → [`questions/08-tls-https-pki/080-tls13-0rtt-replay.md`](../questions/08-tls-https-pki/080-tls13-0rtt-replay.md)

### 第九章 Socket、epoll 与 Linux 网络栈

- 081. 一个 TCP Server 从 socket() 到处理请求的系统调用流程是什么？ → [`questions/09-linux-socket-io/081-tcp-server-socket-syscalls.md`](../questions/09-linux-socket-io/081-tcp-server-socket-syscalls.md)
- 082. Blocking Socket 与 Non-blocking Socket 的核心区别是什么？ → [`questions/09-linux-socket-io/082-blocking-vs-nonblocking-socket.md`](../questions/09-linux-socket-io/082-blocking-vs-nonblocking-socket.md)
- 083. 经典五种 I/O Model 是什么？readiness 与 completion 的区别是什么？ → [`questions/09-linux-socket-io/083-five-io-models.md`](../questions/09-linux-socket-io/083-five-io-models.md)
- 084. select、poll、epoll 的核心差异是什么？ → [`questions/09-linux-socket-io/084-select-poll-epoll.md`](../questions/09-linux-socket-io/084-select-poll-epoll.md)
- 085. epoll LT 与 ET 有什么区别？ET 为什么要求“读到 EAGAIN”？ → [`questions/09-linux-socket-io/085-epoll-lt-vs-et.md`](../questions/09-linux-socket-io/085-epoll-lt-vs-et.md)
- 086. 为什么 epoll ET 几乎总与 nonblocking socket 搭配？ → [`questions/09-linux-socket-io/086-epoll-et-nonblocking.md`](../questions/09-linux-socket-io/086-epoll-et-nonblocking.md)
- 087. 为什么 epoll 对普通磁盘文件意义有限？ → [`questions/09-linux-socket-io/087-epoll-regular-files.md`](../questions/09-linux-socket-io/087-epoll-regular-files.md)
- 088. send() 返回成功，是否意味着对端已经收到或处理？ → [`questions/09-linux-socket-io/088-send-success-semantics.md`](../questions/09-linux-socket-io/088-send-success-semantics.md)
- 089. Zero Copy 的目标是什么？sendfile、splice、mmap 各自大致减少了什么？ → [`questions/09-linux-socket-io/089-zero-copy-sendfile-splice-mmap.md`](../questions/09-linux-socket-io/089-zero-copy-sendfile-splice-mmap.md)
- 090. 一个 Packet 从 NIC 到应用 recv() 大致经过哪些 Linux 网络栈阶段？ → [`questions/09-linux-socket-io/090-linux-packet-receive-path.md`](../questions/09-linux-socket-io/090-linux-packet-receive-path.md)

### 第十章 综合故障定位与系统设计

- 091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？ → [`questions/10-troubleshooting-system-design/091-url-to-page-full-path.md`](../questions/10-troubleshooting-system-design/091-url-to-page-full-path.md)
- 092. 用户说“网站突然很慢”，你如何系统化拆解而不是猜？ → [`questions/10-troubleshooting-system-design/092-website-slow-troubleshooting.md`](../questions/10-troubleshooting-system-design/092-website-slow-troubleshooting.md)
- 093. 服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？ → [`questions/10-troubleshooting-system-design/093-latency-high-cpu-qps-stable.md`](../questions/10-troubleshooting-system-design/093-latency-high-cpu-qps-stable.md)
- 094. 大量 TIME_WAIT 的完整排障流程是什么？ → [`questions/10-troubleshooting-system-design/094-time-wait-troubleshooting.md`](../questions/10-troubleshooting-system-design/094-time-wait-troubleshooting.md)
- 095. 大量 CLOSE_WAIT 的完整排障流程是什么？ → [`questions/10-troubleshooting-system-design/095-close-wait-troubleshooting.md`](../questions/10-troubleshooting-system-design/095-close-wait-troubleshooting.md)
- 096. 大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？ → [`questions/10-troubleshooting-system-design/096-syn-recv-troubleshooting.md`](../questions/10-troubleshooting-system-design/096-syn-recv-troubleshooting.md)
- 097. 网络服务 CPU 很高但业务线程不忙，可能是什么？ → [`questions/10-troubleshooting-system-design/097-network-cpu-softirq.md`](../questions/10-troubleshooting-system-design/097-network-cpu-softirq.md)
- 098. 四层负载均衡与七层负载均衡怎么选？ → [`questions/10-troubleshooting-system-design/098-l4-vs-l7-load-balancing.md`](../questions/10-troubleshooting-system-design/098-l4-vs-l7-load-balancing.md)
- 099. 设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？ → [`questions/10-troubleshooting-system-design/099-million-tcp-connections.md`](../questions/10-troubleshooting-system-design/099-million-tcp-connections.md)
- 100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？ → [`questions/10-troubleshooting-system-design/100-tcpdump-wireshark-analysis.md`](../questions/10-troubleshooting-system-design/100-tcpdump-wireshark-analysis.md)

## PDF 附录对应

- Top 20 与 7 天冲刺 → [`docs/top20.md`](top20.md) + [`docs/7-day-plan.md`](7-day-plan.md)
- Linux 网络排障命令速查 → [`docs/linux-network-cheatsheet.md`](linux-network-cheatsheet.md)
- 权威协议与实现参考 → [`references/README.md`](../references/README.md)
- 面试自评表 → 每个题目 Markdown 的 `面试评分 Rubric` + [`docs/self-assessment.md`](self-assessment.md)

## 完整性说明

题目元数据由生成 PDF 的同源结构化内容解析得到，并与 PDF 文本抽取的目录核对。仓库 CI 进一步强制检查题号 1-100 连续、文件数量为 100。
