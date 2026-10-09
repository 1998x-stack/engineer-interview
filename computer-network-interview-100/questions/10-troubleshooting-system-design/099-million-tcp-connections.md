---
id: 99
title: "设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "系统设计"
frequency: "★★★★★"
tags: ["Million Connections", "Capacity Planning"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 099. 设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？

> **定位**：系统设计 · **面试频率**：★★★★★ · **标签**：Million Connections / Capacity Planning  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Million Connections / Capacity Planning** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 先做资源模型而不是先说 epoll：FD 上限、每连接内核/用户内存、socket buffers、心跳包率、TLS 状态、event-loop 分片、accept/worker 架构、RSS/多核、NAT/LB、连接迁移与滚动发布。百万连接的关键常是内存与 PPS，而非纯连接计数。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 若每连接总状态 20KB，100 万连接就是约 20GB，还没算 page cache、应用和内核额外开销。
2. 30 秒一次心跳意味着约 33k heartbeat/s；若双向、多包，PPS 更高。
3. 滚动发布要 connection draining，否则一次重启会制造重连风暴。

## 二次深化：工程上还必须知道什么

百万连接不是 epoll API 题，而是容量工程：FD、socket 内存、TCP buffer、心跳 PPS、TLS state、NAT/conntrack、端口空间、重连风暴与滚动发布共同决定可用规模。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
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
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Million Connections、Capacity Planning 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `curl -w`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ss -s; ss -tan | wc -l` |
| 辅助 | `cat /proc/sys/fs/file-nr; ulimit -n` |
| 性能/路径 | `slabtop / /proc/net/sockstat` |
| 深挖 | `perf + NIC/softirq/heartbeat PPS` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：SO_REUSEPORT 如何分摊监听？

**参考回答**：`SO_REUSEPORT` 允许多个 listener 在同一 address:port 接收连接，内核按 hash/BPF 等策略分流，可把 accept/event loop 按 CPU shard，减少单 acceptor 热点。

### 追问 2：如何做长连接负载均衡和会话迁移？

**参考回答**：长连接通常先在 L4/L7 LB 做 connection ownership；迁移/发布依赖 connection draining、客户端重连/Connection ID（QUIC）或业务会话重新绑定。TCP 本身不能把一个已建立连接无损搬到另一普通 backend。

### 追问 3：为什么连接数大但活跃率低仍可能内存很高？

**参考回答**：空闲连接仍有 socket 结构、协议状态、send/receive buffer 最小占用、timer、TLS/应用对象；所以 active rate 低只减少动态 CPU/PPS，不消除固定内存成本。

## 高频易错点（PDF 原内容）

- ❌ 只回答“epoll 能支持百万连接”。
- ❌ 忽略客户端/网关端口和 NAT 表限制。

## 动手验证 / 抓包实验（PDF 原内容）

建立容量表：FD、bytes/conn、heartbeat PPS、TLS memory、CPU/packet、accept rate、reconnect storm，并做 2x safety margin。

### 实验验收标准

能给出“现象 → 假设 → 指标/抓包 → 排除/确认 → 根因”的完整闭环。

建议把实验结果记录成：**命令/抓包过滤器 → 观察到的字段/状态 → 与理论的对应关系 → 仍不能证明的部分**。这比只保存一张截图更接近线上排障习惯。

## 面试评分 Rubric

| 等级 | 表现 |
|---|---|
| 1/5 | 只会名词或结论，无法解释字段/状态/时序。 |
| 2/5 | 能复述主流程，但遇到异常路径或 Why 追问容易断。 |
| 3/5 | 能解释核心机制，并回答至少两个追问。 |
| 4/5 | 能说明设计取舍、边界条件，并结合 Linux/抓包证据。 |
| 5/5 | 能从业务现象反推协议/内核机制，主动指出不确定性并设计验证实验。 |

## 权威资料 / 延伸阅读

- [RFC 9293 - Transmission Control Protocol (TCP)](https://www.rfc-editor.org/rfc/rfc9293.html)
- [Linux Kernel Documentation - Scaling in the Linux Networking Stack](https://docs.kernel.org/networking/scaling.html)
- [Linux Kernel Documentation - IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [045. TCP 半连接队列、全连接队列与 listen(backlog) 有什么关系？](../04-tcp-performance-congestion/045-syn-queue-accept-queue-backlog.md)
- [090. 一个 Packet 从 NIC 到应用 recv() 大致经过哪些 Linux 网络栈阶段？](../09-linux-socket-io/090-linux-packet-receive-path.md)
- [097. 网络服务 CPU 很高但业务线程不忙，可能是什么？](097-network-cpu-softirq.md)

## 复习卡片

- **一句话**：先做资源模型而不是先说 epoll：FD 上限、每连接内核/用户内存、socket buffers、心跳包率、TLS 状态、event-loop 分片、accept/worker 架构、RSS/多核、NAT/LB、连接迁移与滚动发布。百万连接的关键常是内存与 PPS，而非纯连接计数。
- **必须会解释**：Million Connections / Capacity Planning。
- **必须避免**：只回答“epoll 能支持百万连接”。
- **必须会验证**：建立容量表：FD、bytes/conn、heartbeat PPS、TLS memory、CPU/packet、accept rate、reconnect storm，并做 2x safety margin。
