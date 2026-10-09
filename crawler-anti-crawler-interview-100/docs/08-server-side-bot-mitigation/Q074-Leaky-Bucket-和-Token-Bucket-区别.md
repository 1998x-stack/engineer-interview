---
id: Q074
title: "Leaky Bucket 和 Token Bucket 区别？"
chapter: 8
difficulty: "★★☆☆☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q074 Leaky Bucket 和 Token Bucket 区别？

> **难度：** ★★☆☆☆  
> **章节：** 第八章  服务端防爬体系  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- 流量整形
- burst
- 队列模型

## 60-90 秒推荐回答

Token Bucket 允许积累额度后突发；Leaky Bucket 更强调以稳定速率“漏出”流量，输入突发被排队或丢弃。

因此前者常用于“允许合理 burst 的配额”，后者常用于“平滑输出”的 traffic shaping。

## 原理深挖

实际系统可以把两者组合：入口 token bucket 控制预算，下游 leaky/queue 控制平滑发送。

### 整形与突发

- Token Bucket 允许可控 burst；Leaky Bucket 更强调恒定流出/平滑。
- 不要只背定义，要结合登录接口、搜索 API、异步队列等业务说明为什么选。

### GitHub 增强版：进一步理解

1. 防爬策略的核心是成本与风险分层：低风险允许，中风险限速/挑战，高置信滥用才阻断。把所有自动化请求一刀切会造成高昂误杀成本。
2. Rate Limit 必须选对维度：IP、account、session、API key、tenant、endpoint、ASN 都可能是 key；单 IP 在 NAT/移动网络下通常不够。
3. 规则引擎与模型应输出可解释的 policy input，并保留 shadow/canary/rollback 能力，否则误杀发生时无法安全迭代。

## 高级面试扩展

### 1. 核心边界

服务端防爬的本质是 **资源保护与风险治理**，不是“识别到 bot 就封”。Rate Limit、WAF、Bot Score、Challenge、Block 是不同层级的控制器，需要按业务成本和置信度组合。

针对 **Leaky Bucket 和 Token Bucket 区别？**，面试时建议先明确讨论边界：流量整形、burst、队列模型。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Identity/Endpoint/Cost → Rate/Feature State → Rule/Model → Policy → Allow/Throttle/Challenge/Block`。限流算法只解决速率问题，不能单独完成身份识别。

### 3. 本题进一步深挖

1. Token Bucket 由容量 B 与补充速率 r 决定：允许短时 burst≤B、长期平均≤r。分布式实现难点不是公式，而是跨节点 token ownership 和时间一致性。

2. Leaky Bucket 更像固定速率排水/整形，适合保护怕突发的下游；Token Bucket 更适合允许合法 burst 的 API。队列满时需明确 drop/reject/backpressure 策略。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 保护强度 vs 可用性 | 严格限制降低滥用 | 合法高频客户受损 |
| 局部限流 vs 全局准确 | 边缘本地快 | 跨地域预算需要协调 |
| 规则可解释 vs 模型覆盖 | 规则稳定清晰 | 复杂攻击模式需要模型 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| Key 选错 | 只按 IP 导致 NAT 误伤 | IP/account/session/endpoint/cost 多维预算 |
| 限流状态不原子 | 竞态突破配额 | Lua/事务/原子数据结构 |
| 策略突变 | 新规则直接阻断 | shadow/canary + rollback + exemption |

### 6. 如何验证方案

用突发、均匀、分布式、多租户流量做限流验证；检查边界窗口、故障模式、跨地域状态和策略回滚。

建议至少覆盖三类验证：

- **Correctness**：协议/算法/业务语义是否正确；
- **Resilience**：超时、重试、进程崩溃、依赖变慢时是否可恢复；
- **Scale**：数据量或并发扩大 10 倍时，状态、内存、网络和远端预算哪个先成为瓶颈。

### 7. 高级候选人的回答结构

1. **先给定义/结论**：20 秒内回答题面，不绕圈。
2. **讲机制**：用状态机、数据流或关键公式解释为什么。
3. **讲 Trade-off**：至少指出一个“收益 ↔ 代价”。
4. **落到生产**：给出一个指标、一个失败模式、一个验证方式。
5. **主动给边界**：说明什么规模/场景下需要换方案。

### 8. 实战演练

> 为一个昂贵 API 设计 account+IP+endpoint 多维限流与 shadow policy，说明 fail-open/fail-closed、跨节点原子性和监控指标。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] 选择合适限流算法与 key
- [ ] 风险分层动作而非一刀切
- [ ] 保护高成本 endpoint
- [ ] 策略支持 shadow/canary/rollback
- [ ] 监控用户体验成本

### 建议监控的指标

- `allow/throttle/challenge/block rates`
- `rate-limit rejection rate`
- `challenge completion`
- `policy latency`
- `rule/model disagreement`

### 示例 / 伪代码

```text
request -> feature extraction -> risk score -> policy engine
                                   |
             allow / throttle / challenge / block

注意：检测与策略解耦，且必须监控 false positive 与用户体验成本。
```

## 常见误区与 Gotchas

- 认为两者只是名字不同。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：如果 Search 后端怕突发，哪个更合适？

**参考回答：** 如果后端最怕瞬时突发，Leaky Bucket/有界队列平滑输出更直接；若业务允许短 burst 且只关心长期平均，Token Bucket 更合适。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：队列满时 Leaky Bucket 应如何处理？

**参考回答：** 队列满时必须明确丢弃/429/优先级淘汰策略；不能无限排队，因为那只是把过载从 QPS 转成巨大延迟和内存。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 流量整形。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> Token Bucket 允许积累额度，Leaky Bucket 强调平滑输出。

## 延伸阅读

- [Redis - Rate Limiter](https://redis.io/docs/latest/develop/use-cases/rate-limiter/)
- [Cloudflare - Bot Management](https://developers.cloudflare.com/bots/get-started/bot-management/)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q073 Token Bucket 原理是什么？](Q073-Token-Bucket-原理是什么.md) | [Q075 只按 IP Rate Limit 有什么问题？](Q075-只按-IP-Rate-Limit-有什么问题.md) →
