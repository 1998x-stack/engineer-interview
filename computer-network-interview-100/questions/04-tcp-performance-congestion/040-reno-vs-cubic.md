---
id: 40
title: "TCP Reno 与 CUBIC 的核心差异是什么？"
chapter: "第四章 TCP 性能、窗口与拥塞控制"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["Reno", "CUBIC"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 040. TCP Reno 与 CUBIC 的核心差异是什么？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：Reno / CUBIC  
> **本章**：[第四章 TCP 性能、窗口与拥塞控制](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **Reno / CUBIC** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> Reno 在拥塞避免阶段近似线性增窗，适合早期较低 BDP 网络；CUBIC 以距离上次拥塞点的时间为变量使用三次函数增长，在高带宽、高 RTT 链路上更快恢复到先前窗口附近，同时保持一定稳定性。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. CUBIC 仍是 loss-based congestion control，丢包通常触发窗口降低。
2. 其曲线在上次最大窗口附近增长较慢，远离该点时增长更积极。
3. Linux 长期广泛使用 CUBIC，现代标准已将其规范化。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- 吞吐取决于窗口、RTT、丢包、排队和拥塞算法，不能只用“带宽大”解释性能。
- 先区分 rwnd（接收端能力）和 cwnd（网络承载估计），再讨论实际 in-flight 上限。
- 拥塞控制算法的目标是动态探测路径可用容量；不同算法对 loss、RTT 与 queue 的解释不同。

<!-- V2-ENRICHMENT-START -->
## V2 深入：Reno 用 ACK-clock 线性探测，CUBIC 用“距上次拥塞事件的时间”构造三次函数

### 第一性原理

- Reno congestion avoidance 的 additive increase 在高 BDP 路径上从一次 loss 恢复到大 window 可能非常慢。
- CUBIC 以此前拥塞窗口附近为参考，用 cubic function 随时间增长：远离旧最大值时增长更快，接近时更平缓以提高稳定性。
- CUBIC 仍是 loss/ECN 响应型拥塞控制，并需与 Reno 流量保持合理 coexistence。

### 为什么适合长肥网络

高带宽、长 RTT 意味着达到满 BDP 需要很大的 cwnd。Reno 每 RTT 小幅增长会耗费大量时间；CUBIC 的增长主要以 elapsed time 表达，降低对 RTT 的直接敏感度并提升 scalability。

### Bufferbloat 边界

Loss-based 算法通常持续增大发送直到 queue/loss/ECN 提示拥塞；若 bottleneck buffer 过大且 AQM 不佳，可能形成高 standing queue/RTT，即 bufferbloat。CUBIC 本身并不能保证低延迟。

### 规范状态

CUBIC 已由 RFC 9438 标准化，并更新 RFC 5681 对更激进增长行为的约束；回答时不要继续把 RFC 8312 当当前主规范。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“TCP Reno 与 CUBIC 的核心差异是什么？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 Reno、CUBIC 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `ss -ti`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `ss -ti` |
| 辅助 | `tc qdisc` |
| 性能/路径 | `iperf3` |
| 深挖 | `nstat -az | grep -i retrans` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：CUBIC 为什么比 Reno 更适合长肥网络？

**参考回答**：Reno拥塞避免近似按 RTT线性增长，CUBIC以立方函数随距上次拥塞点的时间调节窗口，更适合高 BDP 链路，同时保留 Reno-friendly 兼容区域。

### 追问 2：CUBIC 如何与 Reno-friendly 行为兼容？

**参考回答**：Reno拥塞避免近似按 RTT线性增长，CUBIC以立方函数随距上次拥塞点的时间调节窗口，更适合高 BDP 链路，同时保留 Reno-friendly 兼容区域。

### 追问 3：为什么 loss-based 容易造成 bufferbloat？

**参考回答**：BBR基于 delivery rate、RTT 和 loss 建立路径模型，并通过 pacing 与 in-flight 上限控制发送。它试图避免把“必须先把队列灌满直到丢包”当成唯一容量探测方式，但与其他算法竞争时仍需讨论公平性。

## 高频易错点（PDF 原内容）

- ❌ 把 CUBIC 说成“按三次方每 RTT 增长”。
- ❌ 认为 CUBIC 不依赖丢包信号。

## 动手验证 / 抓包实验（PDF 原内容）

查看 `sysctl net.ipv4.tcp_congestion_control`；在可控环境切换 reno/cubic 比较高 RTT 下吞吐。

### 实验验收标准

能把吞吐/延迟变化与 RTT、cwnd/rwnd、loss、queue 之一建立可验证联系。

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
- [RFC 5681 - TCP Congestion Control](https://www.rfc-editor.org/rfc/rfc5681.html)
- [RFC 9438 - CUBIC for Fast Long-Distance Networks](https://www.rfc-editor.org/rfc/rfc9438.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [037. Slow Start 为什么叫“慢启动”，它的增长其实有多快？](037-tcp-slow-start.md)
- [041. BBR 与 CUBIC 的核心思想差在哪里？](041-bbr-vs-cubic.md)
- [044. BDP 是什么？为什么高带宽长 RTT 链路需要大窗口？](044-bandwidth-delay-product.md)

## 复习卡片

- **一句话**：Reno 在拥塞避免阶段近似线性增窗，适合早期较低 BDP 网络；CUBIC 以距离上次拥塞点的时间为变量使用三次函数增长，在高带宽、高 RTT 链路上更快恢复到先前窗口附近，同时保持一定稳定性。
- **必须会解释**：Reno / CUBIC。
- **必须避免**：把 CUBIC 说成“按三次方每 RTT 增长”。
- **必须会验证**：查看 `sysctl net.ipv4.tcp_congestion_control`；在可控环境切换 reno/cubic 比较高 RTT 下吞吐。
