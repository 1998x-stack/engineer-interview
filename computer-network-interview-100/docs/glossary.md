# 术语表

- **ACK**：Acknowledgment，确认号/确认语义取决于协议。
- **BDP**：Bandwidth-Delay Product，链路中维持满吞吐所需的在途数据量量级。
- **cwnd**：TCP congestion window，发送端根据拥塞控制维护。
- **rwnd**：receiver advertised window，接收端通告的接收能力。
- **MSS**：TCP Maximum Segment Size，最大 TCP payload 协商值。
- **MTU**：链路可承载的最大网络层 packet 大小。
- **HOL**：Head-of-Line Blocking，队头阻塞。
- **RTO**：Retransmission Timeout，重传超时。
- **SACK**：Selective Acknowledgment，选择确认。
- **PMTU**：Path MTU，端到端路径上可用的最小 MTU。
- **NAPI**：Linux 驱动收包机制之一，结合中断与 polling。
- **RSS/RPS/RFS**：硬件/软件接收流量分发与流亲和技术。
- **SNI**：TLS Server Name Indication。
- **ALPN**：TLS 中协商应用层协议。
- **PFS**：Forward Secrecy，长期密钥泄露不应直接解密过去会话。
