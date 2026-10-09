# 权威协议与实现参考

协议题优先查 IETF/RFC；Linux 行为优先查 Kernel Documentation 和 man-pages。下面链接按仓库题目覆盖范围整理。

- [RFC 9293 - Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html)
- [RFC 5681 - TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681.html)
- [RFC 9438 - CUBIC for Fast Long-Distance Networks](https://www.rfc-editor.org/rfc/rfc9438.html)
- [IETF CCWG - draft-ietf-ccwg-bbr-06 (2026-07-06, Active Internet-Draft)](https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/)
- [RFC 8200 - Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200.html)
- [RFC 4861 - Neighbor Discovery for IPv6](https://www.rfc-editor.org/rfc/rfc4861.html)
- [RFC 1034 - Domain Names: Concepts and Facilities](https://www.rfc-editor.org/rfc/rfc1034.html)
- [RFC 1035 - Domain Names: Implementation and Specification](https://www.rfc-editor.org/rfc/rfc1035.html)
- [RFC 2308 - Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html)
- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [RFC 9111 - HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [RFC 9112 - HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html)
- [RFC 9113 - HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html)
- [RFC 9000 - QUIC: A UDP-Based Multiplexed and Secure Transport](https://www.rfc-editor.org/rfc/rfc9000.html)
- [RFC 9002 - QUIC Loss Detection and Congestion Control](https://www.rfc-editor.org/rfc/rfc9002.html)
- [RFC 9114 - HTTP/3](https://www.rfc-editor.org/rfc/rfc9114.html)
- [RFC 9846 - TLS 1.3 (current specification, obsoletes RFC 8446)](https://www.rfc-editor.org/rfc/rfc9846.html)
- [RFC 5280 - Internet X.509 PKI Certificate and CRL Profile](https://www.rfc-editor.org/rfc/rfc5280.html)
- [RFC 6066 - TLS Extensions (includes SNI)](https://www.rfc-editor.org/rfc/rfc6066.html)
- [RFC 7301 - Application-Layer Protocol Negotiation (ALPN)](https://www.rfc-editor.org/rfc/rfc7301.html)
- [RFC 4271 - BGP-4](https://www.rfc-editor.org/rfc/rfc4271.html)
- [RFC 2328 - OSPF Version 2](https://www.rfc-editor.org/rfc/rfc2328.html)
- [RFC 2131 - Dynamic Host Configuration Protocol](https://www.rfc-editor.org/rfc/rfc2131.html)
- [RFC 826 - Address Resolution Protocol](https://www.rfc-editor.org/rfc/rfc826.html)
- [RFC 4786 - Operation of Anycast Services](https://www.rfc-editor.org/rfc/rfc4786.html)
- [RFC 3022 - Traditional IP Network Address Translator](https://www.rfc-editor.org/rfc/rfc3022.html)
- [RFC 4787 - NAT Behavioral Requirements for Unicast UDP](https://www.rfc-editor.org/rfc/rfc4787.html)
- [RFC 8445 - ICE](https://www.rfc-editor.org/rfc/rfc8445.html)
- [RFC 8489 - STUN](https://www.rfc-editor.org/rfc/rfc8489.html)
- [RFC 8656 - TURN](https://www.rfc-editor.org/rfc/rfc8656.html)
- [RFC 1191 - Path MTU Discovery](https://www.rfc-editor.org/rfc/rfc1191.html)
- [RFC 8201 - Path MTU Discovery for IPv6](https://www.rfc-editor.org/rfc/rfc8201.html)
- [RFC 6455 - The WebSocket Protocol](https://www.rfc-editor.org/rfc/rfc6455.html)
- [Linux Kernel Documentation - Scaling in the Linux Networking Stack](https://docs.kernel.org/networking/scaling.html)
- [Linux Kernel Documentation - IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html)
- [Linux man-pages - epoll(7)](https://man7.org/linux/man-pages/man7/epoll.7.html)
- [Linux man-pages - socket(7)](https://man7.org/linux/man-pages/man7/socket.7.html)
- [Linux man-pages - tcp(7)](https://man7.org/linux/man-pages/man7/tcp.7.html)
- [Linux man-pages - sendfile(2)](https://man7.org/linux/man-pages/man2/sendfile.2.html)
- [Linux man-pages - splice(2)](https://man7.org/linux/man-pages/man2/splice.2.html)

### 深入主题补充

- [RFC 6298 - Computing TCP's Retransmission Timer](https://www.rfc-editor.org/rfc/rfc6298.html)
- [RFC 2018 - TCP Selective Acknowledgment Options](https://www.rfc-editor.org/rfc/rfc2018.html)
- [RFC 7323 - TCP Extensions for High Performance (Window Scale / Timestamps)](https://www.rfc-editor.org/rfc/rfc7323.html)
- [RFC 7413 - TCP Fast Open](https://www.rfc-editor.org/rfc/rfc7413.html)
- [RFC 9204 - QPACK: Field Compression for HTTP/3](https://www.rfc-editor.org/rfc/rfc9204.html)
- [RFC 4033 - DNS Security Introduction and Requirements](https://www.rfc-editor.org/rfc/rfc4033.html)
- [RFC 7858 - DNS over TLS](https://www.rfc-editor.org/rfc/rfc7858.html)
- [RFC 8484 - DNS Queries over HTTPS](https://www.rfc-editor.org/rfc/rfc8484.html)
- [RFC 9525 - Service Identity in TLS](https://www.rfc-editor.org/rfc/rfc9525.html)
- [RFC 9205 - Building Protocols with HTTP](https://www.rfc-editor.org/rfc/rfc9205.html)

## 2026 状态说明

- TLS 1.3：RFC 9846 已取代 RFC 8446，保持 TLS 1.3 版本号与兼容性，并收紧部分安全要求。
- BBR：`draft-ietf-ccwg-bbr-06` 于 2026-07-06 发布，当前仍是 IETF CCWG Active Internet-Draft，目标为 Experimental；不要将其写作已发布 RFC。
- HTTP：RFC 9110 明确 HTTP/1.1、HTTP/2、HTTP/3 共享共同语义且并未简单互相淘汰。
- Linux 多核网络：Kernel 文档明确区分 RSS（NIC 硬件队列选择）、RPS（软件协议处理 CPU 选择）与 RFS（进一步考虑应用 locality）。
