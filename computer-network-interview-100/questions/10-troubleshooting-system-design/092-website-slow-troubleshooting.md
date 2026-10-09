---
id: 92
title: "用户说“网站突然很慢”，你如何系统化拆解而不是猜？"
chapter: "第十章 综合故障定位与系统设计"
difficulty: "工程"
frequency: "★★★★★"
tags: ["Latency", "Troubleshooting"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 092. 用户说“网站突然很慢”，你如何系统化拆解而不是猜？

> **定位**：工程 · **面试频率**：★★★★★ · **标签**：Latency / Troubleshooting  
> **本章**：[第十章 综合故障定位与系统设计](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Latency / Troubleshooting** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 先把总延迟拆成 DNS、connect、TLS、TTFB、download、client rendering，再定位网络 RTT/loss、CDN hit、LB、应用、数据库和前端。建立分层时间线比“先重启服务器”更可靠。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. `curl -w` 可快速分解 name lookup/connect/appconnect/starttransfer/total。
2. TTFB 高偏向服务器/上游处理或网络往返；download 高偏向响应体、带宽、丢包。
3. 浏览器慢但 curl 快，可能是 JS、主线程、资源依赖和渲染。

## 二次深化：工程上还必须知道什么

建议固定使用“DNS → connect → TLS → TTFB → download → client”分段法。先测量每段，再深入。这样可以把“网站慢”从主观现象转成可以证伪的假设集合。

### 本章共同的工程视角

- 故障定位先做 latency/error decomposition，再从应用层向下验证，禁止“先猜网卡/先调 sysctl”。
- 单一指标几乎从不够：连接状态、重传、RTT、队列、softirq、应用 trace 与两端抓包应形成证据链。
- 系统设计题先做资源模型（FD、内存、PPS、带宽、端口、TLS、重连风暴），然后才讨论 epoll/线程模型。

<!-- V2-ENRICHMENT-START -->
## V2 深入：“网站很慢”首先要把总延迟做 decomposition

### 第一性原理

用近似模型 `T_total = DNS + connect + TLS + request queue + upstream/app + first-byte transfer + body transfer + browser/render`。第一步是确定变慢的是哪个区间，再提出机制假设。

### 证据优先级

- Client：`curl -w`/browser waterfall 分解 lookup/connect/appconnect/starttransfer/total。
- Network：RTT、loss、retrans、path、PMTU。
- Edge/LB：queue、upstream connect、5xx/timeout。
- Service：trace、thread pool、GC、DB/cache/downstream。
- Frontend：resource waterfall、main-thread/render。

### 避免平均数陷阱

“平均 latency 正常”不能排除 p99；按 region/ISP/protocol/version/POP/instance 分桶常能迅速识别局部故障。网络问题尤其可能只影响某 AS/path。

### 线上案例推演

只有某 ISP p99 从 200ms 升到 2s，服务端 CPU/DB 正常；应优先比较该 ISP route/retrans/edge POP，而不是全局扩容数据库。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“用户说“网站突然很慢”，你如何系统化拆解而不是猜？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Latency、Troubleshooting 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `curl -w`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `curl -w DNS/connect/TLS/TTFB/total` |
| 辅助 | `mtr / dig` |
| 性能/路径 | `ss -ti / retrans counters` |
| 深挖 | `distributed trace + CDN/upstream metrics` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：怎么判断 DNS 慢还是 connect 慢？

**参考回答**：证书验证要建立到本地信任锚的有效链；缺失中间证书会让不能自动补链的客户端失败。自签名证书默认不在信任库中所以报错。Certificate Transparency通过公开可审计日志提高错误/恶意签发的可发现性。

### 追问 2：p99 上升但 p50 正常通常看什么？

**参考回答**：p99上升而p50稳定通常说明只影响尾部请求的排队、GC、重试、冷缓存、跨区或少量坏路径。Little's Law可用 L=λW 理解在到达率不变时等待时间上升如何对应系统中在途/排队数量增长。CDN miss storm会同时推高回源QPS、TTFB和源站队列。

### 追问 3：CDN miss storm 会怎样体现？

**参考回答**：p99上升而p50稳定通常说明只影响尾部请求的排队、GC、重试、冷缓存、跨区或少量坏路径。Little's Law可用 L=λW 理解在到达率不变时等待时间上升如何对应系统中在途/排队数量增长。CDN miss storm会同时推高回源QPS、TTFB和源站队列。

## 高频易错点（PDF 原内容）

- ❌ 只看 CPU/QPS。
- ❌ 只用 ping 判断整个网站性能。

## 动手验证 / 抓包实验（PDF 原内容）

为一个请求同时收集 curl timing、traceroute/mtr、应用 tracing、DB slow query，构建 waterfall。

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

- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](091-url-to-page-full-path.md)
- [093. 服务延迟升高但 CPU、QPS 都没变化，你优先怀疑什么？](093-latency-high-cpu-qps-stable.md)
- [100. 给你一份 tcpdump/Wireshark 抓包，如何系统判断 TCP 问题？](100-tcpdump-wireshark-analysis.md)

## 复习卡片

- **一句话**：先把总延迟拆成 DNS、connect、TLS、TTFB、download、client rendering，再定位网络 RTT/loss、CDN hit、LB、应用、数据库和前端。建立分层时间线比“先重启服务器”更可靠。
- **必须会解释**：Latency / Troubleshooting。
- **必须避免**：只看 CPU/QPS。
- **必须会验证**：为一个请求同时收集 curl timing、traceroute/mtr、应用 tracing、DB slow query，构建 waterfall。
