---
id: 96
title: "大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "工程"
frequency: "★★★★★"
tags: ["SYN_RECV", "Backlog"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 096. 大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？

> **定位**：工程 · **面试频率**：★★★★★ · **标签**：SYN_RECV / Backlog  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **SYN_RECV / Backlog** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 同时看 SYN arrival rate、SYN+ACK retrans、半连接队列、syncookie counters、NIC/drop、LB、防火墙、CPU softirq 与正常流量基线。如果握手完成率下降且源地址异常分散，可能是攻击；若链路丢包高则可能正常客户端 ACK 回不来；若 accept queue 满则是另一个应用问题。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 半连接与全连接队列要分别判断。
2. SYN flood 可用伪造源地址，而真实流量高峰通常能看到完整握手。
3. 边缘 LB/防火墙也可能先成为瓶颈，源主机指标看不到全部 SYN。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
## V2 深入：SYN_RECV 多只是现象，必须区分攻击、回程丢包与 listener 容量

### 第一性原理

SYN_RECV 表示 Server 已收到 SYN、发出 SYN+ACK并等待最终 ACK。它可能因为：伪造源 SYN flood；真实 Client 的 ACK/SYN+ACK path 丢包；SYN backlog pressure；Client故障。

### 证据矩阵

- 攻击：源分布异常、SYN rate 极高、ACK completion 比例低、边缘带宽/pps 高。
- 网络丢包：特定 region/ASN，SYN+ACK retrans 高，双方抓包不对称。
- 容量：listen overflow/syn backlog 指标、CPU/softirq、conntrack full。
- accept queue 问题：握手已完成，SYN_RECV 不一定高，listen established queue/worker 排队高。

### Syncookies 的定位

它是 SYN queue pressure 时的防护/降级机制，不应把所有新连接问题都“开 syncookies”解决。

### 线上案例推演

只有一个运营商 SYN_RECV 高且服务端反复发 SYN+ACK，其他地区正常，更像 return path/ACL 问题；全网随机伪造源 + PPS 爆炸才更像 SYN Flood。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“大量 SYN_RECV 且新连接失败，应如何判断是攻击、丢包还是容量问题？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 SYN_RECV、Backlog 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `curl -w`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ss -ant state syn-recv` |
| 辅助 | `nstat / netstat TCP counters` |
| 性能/路径 | `server + client tcpdump` |
| 深挖 | `SYN backlog / syncookie metrics` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：如何从抓包判断 SYN+ACK 是否离开服务器？

**参考回答**：服务器端抓包看到SYN+ACK只能证明它到达该抓包点；两端抓包可进一步区分出站丢失/回程问题。syncookies计数增长说明半连接资源受到压力，但单纯增大backlog若应用accept/CPU/网络仍是瓶颈只会延后失败。

### 追问 2：syncookies counter 说明什么？

**参考回答**：SYN queue保存尚未完成握手的半连接状态，accept queue保存已完成握手、等待应用 accept() 的连接。SYN cookies通常是在半连接资源受压时的防御/降级机制，不能替代正常容量规划。 缓存正确性取决于 cache key 与共享范围。Cookie/Query/Vary会扩大对象变体，降低命中率；private/no-store等策略防止共享缓存保存敏感响应。s-maxage用于共享缓存，stale-while-revalidate允许短时间返回过期对象并后台刷新。

### 追问 3：为什么 SYN backlog 调大也可能治标不治本？

**参考回答**：SYN queue保存尚未完成握手的半连接状态，accept queue保存已完成握手、等待应用 accept() 的连接。SYN cookies通常是在半连接资源受压时的防御/降级机制，不能替代正常容量规划。 服务器端抓包看到SYN+ACK只能证明它到达该抓包点；两端抓包可进一步区分出站丢失/回程问题。syncookies计数增长说明半连接资源受到压力，但单纯增大backlog若应用accept/CPU/网络仍是瓶颈只会延后失败。

## 高频易错点（PDF 原内容）

- ❌ 看到 SYN_RECV 就只会说 DDoS。
- ❌ 把 accept 慢与握手失败混为一谈。

## 动手验证 / 抓包实验（PDF 原内容）

构造诊断矩阵：SYN rate、SYN-ACK retrans、ACK rate、listen queue、syncookie、drop counters，对每种组合给出结论。

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

- [Linux Kernel Documentation - IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [030. SYN Flood 怎么攻击？SYN Cookies 是什么，为什么不是万能方案？](../03-tcp-connection-reliability/030-syn-flood-syn-cookies.md)
- [045. TCP 半连接队列、全连接队列与 listen(backlog) 有什么关系？](../04-tcp-performance-congestion/045-syn-queue-accept-queue-backlog.md)
- [100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？](100-tcpdump-wireshark-analysis.md)

## 复习卡片

- **一句话**：同时看 SYN arrival rate、SYN+ACK retrans、半连接队列、syncookie counters、NIC/drop、LB、防火墙、CPU softirq 与正常流量基线。如果握手完成率下降且源地址异常分散，可能是攻击；若链路丢包高则可能正常客户端 ACK 回不来；若 accept queue 满则是另一个应用问题。
- **必须会解释**：SYN_RECV / Backlog。
- **必须避免**：看到 SYN_RECV 就只会说 DDoS。
- **必须会验证**：构造诊断矩阵：SYN rate、SYN-ACK retrans、ACK rate、listen queue、syncookie、drop counters，对每种组合给出结论。
