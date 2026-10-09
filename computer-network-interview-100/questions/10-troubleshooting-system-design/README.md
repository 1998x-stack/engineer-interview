# 第十章 综合故障定位与系统设计

用分层方法处理真实线上问题与高并发架构题。

## 本章能力目标

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **先 decomposition，再 hypothesis，再证据**：DNS/connect/TLS/TTFB/body/render；不要“先猜网卡/先调 sysctl”。
- **单一指标无法定根因**：连接状态、RTT/retrans、队列、softirq、trace、双端抓包必须互相印证。
- **系统设计先做容量方程**：FD、bytes/conn、PPS、带宽、TLS、NAT/LB state、重连风暴、发布 headroom。

### 本章白板题

1. 画 `https://example.com` 冷连接与热连接两条完整路径，指出哪些阶段可被 cache/connection reuse 跳过。
2. 给“p99 上升但 CPU/QPS 不变”建立至少 5 个可证伪假设并列下一条观测。
3. 设计 1M long connections 容量表并推演一次 30% 实例同时重启的 reconnect storm。

### 故障面试答题模板

`现象 → 影响范围 → 时间线 → 分层拆解 → 2~3 个优先假设 → 指标/抓包验证 → 排除/确认 → 缓解 → 根因修复 → 防复发监控`。高级答案一定包含“哪些证据还不能证明什么”。
<!-- CHAPTER-V2-END -->

## 题目目录

- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](091-url-to-page-full-path.md) · 综合 · ★★★★★
- [092. 用户说“网站突然很慢”，你如何系统化拆解而不是猜？](092-website-slow-troubleshooting.md) · 工程 · ★★★★★
- [093. 服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？](093-latency-high-cpu-qps-stable.md) · 工程 · ★★★★★
- [094. 大量 TIME_WAIT 的完整排障流程是什么？](094-time-wait-troubleshooting.md) · 工程 · ★★★★★
- [095. 大量 CLOSE_WAIT 的完整排障流程是什么？](095-close-wait-troubleshooting.md) · 工程 · ★★★★★
- [096. 大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？](096-syn-recv-troubleshooting.md) · 工程 · ★★★★★
- [097. 网络服务 CPU 很高但业务线程不忙，可能是什么？](097-network-cpu-softirq.md) · 高级 · ★★★★☆
- [098. 四层负载均衡与七层负载均衡怎么选？](098-l4-vs-l7-load-balancing.md) · 系统设计 · ★★★★★
- [099. 设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？](099-million-tcp-connections.md) · 系统设计 · ★★★★★
- [100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？](100-tcpdump-wireshark-analysis.md) · 综合 · ★★★★★

## 推荐实践工具

- `curl -w`
- `ss -s`
- `mtr`
- `tcpdump -w out.pcap`

[← 返回全书目录](../../README.md)
