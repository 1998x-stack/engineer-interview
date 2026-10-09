---
id: 98
title: "四层负载均衡与七层负载均衡怎么选？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "系统设计"
frequency: "★★★★★"
tags: ["L4", "L7", "Load Balancing"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 098. 四层负载均衡与七层负载均衡怎么选？

> **定位**：系统设计 · **面试频率**：★★★★★ · **标签**：L4 / L7 / Load Balancing  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **L4 / L7 / Load Balancing** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> L4 基于 IP/Port/协议转发，通用、开销低、可承载任意 TCP/UDP；L7 理解 HTTP/gRPC 等应用协议，可按 Host/Path/Header/Cookie 路由、做认证、重试、限流和可观测，但需要解析/终止协议并承担更多 CPU、内存与语义复杂度。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. TLS passthrough 更像 L4；TLS termination 后才能做多数 HTTP L7 路由。
2. L7 retry 必须理解请求幂等性，否则可能重复副作用。
3. 长连接和 HTTP/2 connection pooling 会让“连接均衡”与“请求均衡”出现差异。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
## V2 深入：L4 与 L7 LB 的根本区别是“是否终止并理解应用协议”

### 第一性原理

- L4 根据 IP/port/protocol/connection state 做转发或连接代理，协议通用、开销低、可承载任意 TCP/UDP。
- L7 终止 HTTP/TLS（取决于部署），可按 Host/path/header/cookie/RPC metadata 路由，并做 auth、rate limit、retry、cache、observability。
- 功能越上层，控制力越强，但 CPU/memory、配置复杂度、failure mode 也越多。

### TLS 与连接拓扑

L7 若 TLS termination，会形成 Client→LB 与 LB→Backend 两条独立 transport connection；因此 502/504、TCP state、MTU、keepalive 都要分前后两段看。L4 DSR/NAT 模式则可能保持不同的数据路径。

### 选型

需要路径路由、灰度、WAF、HTTP metrics → L7；需要超高吞吐、非 HTTP、保留端到端 TLS/低开销 → L4；大型系统常 L4 入口 + L7 service mesh/gateway 组合。

### 线上案例推演

L7 proxy CPU 已满、backend 很空，改 backend instance 无效；若只是简单 TCP forwarding，可以评估把部分功能下沉 L4，或优化 TLS/HTTP parser/connection reuse。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“四层负载均衡与七层负载均衡怎么选？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 L4、L7、Load Balancing 说明关键状态、字段或数据路径。
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

### 追问 1：NAT mode、DSR、proxy mode 有何区别？

**参考回答**：NAT模式由LB改写地址并保持状态，DSR通常让响应绕过LB降低回程压力，proxy模式由LB终止并重建连接。L7 LB理解HTTP语义，因此上游reset/timeout会映射成502/504等；一致性哈希适合需要稳定key→backend映射且节点会动态变化的场景。

### 追问 2：L7 LB 为什么可能产生 502/504？

**参考回答**：401表示请求缺少/无效的认证凭据并可触发认证挑战，403表示服务器理解身份/请求但拒绝授权。502是网关从上游得到无效/失败响应，504是等待上游超时，408是服务器等待客户端请求超时。 NAT模式由LB改写地址并保持状态，DSR通常让响应绕过LB降低回程压力，proxy模式由LB终止并重建连接。L7 LB理解HTTP语义，因此上游reset/timeout会映射成502/504等；一致性哈希适合需要稳定key→backend映射且节点会动态变化的场景。

### 追问 3：一致性哈希适合什么场景？

**参考回答**：NAT模式由LB改写地址并保持状态，DSR通常让响应绕过LB降低回程压力，proxy模式由LB终止并重建连接。L7 LB理解HTTP语义，因此上游reset/timeout会映射成502/504等；一致性哈希适合需要稳定key→backend映射且节点会动态变化的场景。

## 高频易错点（PDF 原内容）

- ❌ 说 L7 一定比 L4 更先进。
- ❌ 忽略 TLS termination 对证书与安全边界的影响。

## 动手验证 / 抓包实验（PDF 原内容）

画出 Client→L4 LB→L7 Proxy→Service 的链路，对每层列出可见字段、状态、故障码和监控。

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

- 本题以 PDF 原始题解与同章权威协议索引为主；详见 [`references/README.md`](../../references/README.md)。

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [020. Anycast 是什么？为什么 DNS/CDN 常用？](../02-ip-nat-routing/020-anycast-dns-cdn.md)
- [060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？](../06-dns-cdn/060-cdn-acceleration.md)
- [099. 设计支持 100 万 TCP 长连接的服务器，第一性约束有哪些？](099-million-tcp-connections.md)

## 复习卡片

- **一句话**：L4 基于 IP/Port/协议转发，通用、开销低、可承载任意 TCP/UDP；L7 理解 HTTP/gRPC 等应用协议，可按 Host/Path/Header/Cookie 路由、做认证、重试、限流和可观测，但需要解析/终止协议并承担更多 CPU、内存与语义复杂度。
- **必须会解释**：L4 / L7 / Load Balancing。
- **必须避免**：说 L7 一定比 L4 更先进。
- **必须会验证**：画出 Client→L4 LB→L7 Proxy→Service 的链路，对每层列出可见字段、状态、故障码和监控。
