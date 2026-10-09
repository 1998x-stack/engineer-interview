---
id: 97
title: "网络服务 CPU 很高但业务线程不忙，可能是什么？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "高级"
frequency: "★★★★☆"
tags: ["Softirq", "PPS", "NIC"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 097. 网络服务 CPU 很高但业务线程不忙，可能是什么？

> **定位**：高级 · **面试频率**：★★★★☆ · **标签**：Softirq / PPS / NIC  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Softirq / PPS / NIC** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 优先看软中断、每秒包数、NIC RX/TX queues、iptables/nft/conntrack、GRO、重传和 IRQ affinity。大量小包会使 CPU 花在 per-packet 协议处理上，即使业务 QPS 不高；单 RX queue 还可能形成单核热点。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. Mbps 低不代表 PPS 低，64B tiny packet 可以打满 CPU。
2. `ksoftirqd` 高、NET_RX softirq 高是网络栈热点线索。
3. RSS/RPS/XPS、GRO/GSO、irqbalance 都会影响多核扩展。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
## V2 深入：网络 CPU 高常发生在 softirq/packet processing，而不是业务线程

### 第一性原理

每 packet 都有固定协议栈成本。大量小包、retrans、conntrack/firewall、单 RX queue 热点可让 ksoftirqd/NAPI 吃满 CPU，即使 application handler 很轻。

### 观察路径

看 `/proc/softirqs`、`mpstat -P ALL`、`perf top`、NIC rx/tx/drop、ethtool queue/interrupt、RSS/RPS/RFS 配置、packet rate（PPS）而不只看 Mbps。1Gbps 的 64B packets 与 1Gbps 大 packets CPU成本完全不同。

### 常见优化方向

RSS 多队列 + IRQ affinity、RPS/RFS、GRO、batching、减少 iptables/conntrack 热路径、XDP/eBPF prefilter、合理 socket sharding；每个方向都应基于 profile/瓶颈证明。

### 线上案例推演

总 CPU 60%但 CPU3 `NET_RX` 100%，NIC RSS indirection 只映射 CPU3：扩业务 pod 无效，修 RX queue/IRQ distribution 后 p99 恢复。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“网络服务 CPU 很高但业务线程不忙，可能是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Softirq、PPS、NIC 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `curl -w`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `curl -w` |
| 辅助 | `ss -s` |
| 性能/路径 | `mtr` |
| 深挖 | `tcpdump -w out.pcap` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：如何区分包率问题与 TLS 加密问题？

**参考回答**：包率型瓶颈常表现为softirq/IRQ/NIC queue/PPS升高，TLS瓶颈更偏用户态/crypto CPU、握手率和指令热点。conntrack表满或锁竞争可导致新流丢弃/延迟，即使业务线程本身并不忙。

### 追问 2：conntrack 表满/锁竞争会怎样？

**参考回答**：SACK允许接收端报告非连续已收区间，减少大窗口多丢包时的无谓重传；RACK更依赖时间/发送顺序判断丢包，避免把固定 dupACK 数当作唯一信号。Spurious retransmission则是误判丢包导致的多余重传。 包率型瓶颈常表现为softirq/IRQ/NIC queue/PPS升高，TLS瓶颈更偏用户态/crypto CPU、握手率和指令热点。conntrack表满或锁竞争可导致新流丢弃/延迟，即使业务线程本身并不忙。

### 追问 3：NUMA 跨节点内存访问为何影响 NIC 性能？

**参考回答**：RSS由NIC硬件按flow hash选择RX队列/CPU，RPS在内核软件层把协议处理分配到CPU；单队列会把中断/协议处理压到少数CPU。NUMA下NIC、IRQ、应用线程和内存跨节点会增加延迟与带宽成本。

## 高频易错点（PDF 原内容）

- ❌ 只看 top 中业务进程 CPU。
- ❌ 用带宽 Mbps 代替 PPS 判断网络负载。

## 动手验证 / 抓包实验（PDF 原内容）

收集 `mpstat -P ALL`、`/proc/softirqs`、`ethtool -S`、pps、perf top，定位 CPU 花在哪里。

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

- [Linux Kernel Documentation - Scaling in the Linux Networking Stack](https://docs.kernel.org/networking/scaling.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [090. 一个 Packet 从 NIC 到应用 recv() 大致经过哪些 Linux 网络栈阶段？](../09-linux-socket-io/090-linux-packet-receive-path.md)
- [093. 服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？](093-latency-high-cpu-qps-stable.md)
- [099. 设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？](099-million-tcp-connections.md)

## 复习卡片

- **一句话**：优先看软中断、每秒包数、NIC RX/TX queues、iptables/nft/conntrack、GRO、重传和 IRQ affinity。大量小包会使 CPU 花在 per-packet 协议处理上，即使业务 QPS 不高；单 RX queue 还可能形成单核热点。
- **必须会解释**：Softirq / PPS / NIC。
- **必须避免**：只看 top 中业务进程 CPU。
- **必须会验证**：收集 `mpstat -P ALL`、`/proc/softirqs`、`ethtool -S`、pps、perf top，定位 CPU 花在哪里。
