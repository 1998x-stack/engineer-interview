---
id: Q048
title: "如何保证 Worker Crash 后任务不丢？"
chapter: 5
difficulty: "★★★★☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q048 如何保证 Worker Crash 后任务不丢？

> **难度：** ★★★★☆  
> **章节：** 第五章  分布式爬虫  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- lease/visibility timeout
- ACK
- 重投与幂等

## 60-90 秒推荐回答

任务被 worker 获取时不是立刻从系统永久删除，而是获得一个 lease/visibility timeout；处理成功后 ACK，worker 崩溃则 lease 到期，任务重新可见。

这种机制天然是 at-least-once，所以存储和解析必须幂等。

## 原理深挖

对于长任务，需要 heartbeat/lease extension；否则仍在处理的任务可能被重复分配。

### Lease + ACK

- Worker 领取任务时写 lease_deadline；完成后 ACK；崩溃导致 lease 过期后任务重新可见。
- 结果写入必须幂等，因为“写成功但 ACK 丢失”会引发重复执行。

### GitHub 增强版：进一步理解

1. 分布式爬虫的核心不是“多机器下载”，而是把 Frontier、去重、host 状态、租约、优先级和失败恢复从单进程内存提升为分布式状态。
2. 任务语义通常选择 at-least-once + 幂等结果，而不是追求端到端 exactly-once。只要 Worker 可能在“抓取成功但 ACK 前”崩溃，重复执行就必须被接受和治理。
3. 按 host/domain 聚合调度有利于 politeness 与连接复用，但会引入热点倾斜；大站点需要虚拟分片，同时仍保持全局 per-host budget。

## 高级面试扩展

### 1. 核心边界

分布式爬虫的难点不是“把 downloader 扩成 N 台”，而是把 **Frontier、去重、host 预算、lease、优先级、失败恢复** 变成分布式状态，并保证扩容后目标站点 QPS 不被意外放大。

针对 **如何保证 Worker Crash 后任务不丢？**，面试时建议先明确讨论边界：lease/visibility timeout、ACK、重投与幂等。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Discovery → Normalize/Dedup → Distributed Frontier → Host-aware Scheduler → Lease → Fetch/Parse → ACK/Retry → Recrawl`。通常采用 at-least-once 执行语义 + 幂等结果。

### 3. 本题进一步深挖

1. lease 模型把任务从“出队即丢失”变成“暂时所有权”。worker 卡死/崩溃后 lease 到期重投；poison task 需要最大尝试次数和 DLQ，避免无限放大。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 一致性 vs 吞吐 | 全局强一致预算准确 | 中心化状态可能成瓶颈 |
| 分片局部性 vs 热点 | 按 host 便于 politeness | 大站点会 skew |
| 恢复能力 vs 状态成本 | lease/checkpoint 可恢复 | 增加持久化和协调开销 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| 热点分片 | 热门 host 占满 partition | virtual shard + 全局 host budget |
| Lease 丢失/重复 | worker crash/GC pause | lease timeout + 幂等 sink + poison-task limit |
| Backpressure 失效 | 下游慢仍持续抓 | queue age/lag 驱动 scheduler 降速 |

### 6. 如何验证方案

做 worker kill、网络分区、Redis/Kafka 故障、热点 host、慢 parser、存储抖动等 chaos test；验证重复率、丢任务率和 host-budget violation。

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

> 模拟 3 个 worker、一个热点 host、一个卡死 worker 和一个慢存储，验证 lease、host budget、requeue 和 backpressure 是否正确。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] Frontier 持久化并支持优先级/延迟
- [ ] 任务使用 lease + ACK
- [ ] 结果写入幂等
- [ ] 按 host 做全局 politeness
- [ ] 建立 backpressure

### 建议监控的指标

- `frontier depth`
- `oldest-task age`
- `lease timeout rate`
- `retry amplification`
- `per-host queue skew`

### 示例 / 伪代码

```text
READY --lease--> IN_FLIGHT --ack--> DONE
                    |
                    +-- lease timeout --> READY

关键不变量：Store 必须可幂等重放，因为 DONE 之前任何位置都可能崩溃。
```

## 常见误区与 Gotchas

- “pop 出队列”后立刻丢状态。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：Worker 卡死但没退出怎么办？

**参考回答：** lease + heartbeat：任务有过期时间，worker 周期续租；卡死即使进程不退出，只要 heartbeat 停止，lease 到期后可回收。设置最大 lease 延长防永久占用。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：如何处理 poison task 无限重投？

**参考回答：** 记录 attempt_count 和 error fingerprint；超过阈值进入 DLQ。若同类 poison task 批量出现，应按错误签名触发 circuit breaker/暂停 pattern，而不是无限重投。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 lease/visibility timeout。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> 可靠队列的核心是租约，而不是“拿走即删除”。

## 延伸阅读

- [Apache Kafka - Introduction](https://kafka.apache.org/documentation/)
- [Redis documentation](https://redis.io/docs/latest/)
- [Scrapy - Jobs: pause and resume](https://docs.scrapy.org/en/latest/topics/jobs.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q047 Redis 在分布式 crawler 中适合做什么？](Q047-Redis-在分布式-crawler-中适合做什么.md) | [Q049 为什么 Exactly-once Crawling 几乎没有必要？](Q049-为什么-Exactly-once-Crawling-几乎没有必要.md) →
