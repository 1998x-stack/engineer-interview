# 网络故障定位框架

## 1. 先把“慢/失败”拆成可测量阶段

```text
DNS → TCP/QUIC connect → TLS → TTFB → download → client/application
```

不要先猜根因。先为每一段建立 timing 和 error rate。

## 2. 四类证据

- **应用证据**：trace、upstream latency、thread/connection pool。
- **Socket/TCP 证据**：`ss -ti`、状态分布、retransmission、window。
- **网络证据**：mtr、双端 tcpdump、MTU、route/NAT。
- **主机证据**：softirq、NIC drop、RSS/RPS、CPU affinity、conntrack。

## 3. 标准故障闭环

```text
现象 → 可证伪假设 → 最便宜的观测 → 缩小范围 → 强证据验证 → 根因 → 修复 → 回归验证
```

## 4. 常见错误

- TIME_WAIT 多就直接调 sysctl。
- ping 不通就宣布服务网络不通。
- Wireshark 标记 Retransmission 就宣布运营商丢包。
- CPU 不高就排除主机网络栈。
- 502/504 不区分 upstream invalid response 和 timeout。
