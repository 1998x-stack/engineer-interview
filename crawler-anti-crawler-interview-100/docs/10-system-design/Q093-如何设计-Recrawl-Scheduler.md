---
id: Q093
title: "如何设计 Recrawl Scheduler？"
chapter: 10
difficulty: "★★★★★"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q093 如何设计 Recrawl Scheduler？

> **难度：** ★★★★★  
> **章节：** 第十章  高级系统设计  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- 变化率估计
- 条件请求
- SLA

## 60-90 秒推荐回答

不同 URL 变化频率差异巨大。保存 last_fetch、last_change、ETag、Last-Modified、content hash 和历史变化间隔，估计 P(change | URL, Δt)。

长期不变页面逐步延长间隔，频繁变化页面缩短间隔；同时受业务 freshness SLA 和站点访问预算限制。

## 原理深挖

可以用 hazard rate/指数移动平均近似变化率；重要页面即使变化率低，也可能因 SLA 要求维持最小抓取频率。

### 变化率驱动 Recrawl

- 对每个 URL/cluster 建立 change history；连续稳定页面逐渐拉长 interval，频繁变化页面缩短。
- 可将条件请求结果、content hash 变化和业务价值一起用于 next_fetch_time。

**关键表达式 / 心智模型：**

```text
next_interval = clamp(base_interval / expected_change_rate, min_interval, max_interval)
```

### GitHub 增强版：进一步理解

1. 系统设计题先做量级估算，再画控制平面、状态平面、数据平面。没有容量数字的架构图很难判断是否真的可行。
2. 任何大规模 crawler 都必须同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance 七个目标；只回答吞吐不完整。
3. 优秀答案会明确失败模式与降级策略：队列爆炸、热点域名、浏览器 OOM、远端 429/503、parser drift、存储延迟、策略变更分别如何处理。

## 高级面试扩展

### 1. 核心边界

系统设计题不能只画组件。先给假设和量级，再定义目标函数与硬约束，然后拆 Control/State/Data Plane；最后用故障模式、SLO 和成本验证设计。

针对 **如何设计 Recrawl Scheduler？**，面试时建议先明确讨论边界：变化率估计、条件请求、SLA。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Capacity Estimate → Goals/Constraints → URL/Policy State → Scheduler/Fetcher → Raw/Parse/Quality → Recrawl → Observability/Compliance`。架构要同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance。

### 3. 本题进一步深挖

1. Scheduler 是 URL frontier 的单机版本：优先级、去重、持久化和出队策略都在这里体现。BFS/DFS 不是理论标签，实际由请求 priority、队列实现及并发共同决定。

2. recrawl 优先级可以基于 change hazard：重要度高且历史变化频繁的页面更早抓；条件请求降低 body 成本，但不会让调度和请求成本变成零。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| Coverage vs Freshness | 抓更多新 URL | 重要页面更新频率可能下降 |
| HTTP vs Browser | HTTP 成本低 | 动态页面需高成本 render |
| 一致性 vs 扩展性 | 全局状态准确 | 跨地域/十亿级协调昂贵 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| 容量低估 | 只算平均 QPS | 加入 peak/retry/browser fallback/retention |
| 全局扩容放大 host QPS | worker 增加但预算未集中 | host-aware global budget |
| 状态不可重建 | 无 raw/provenance/checkpoint | 数据与状态分层、可 replay |

### 6. 如何验证方案

用容量模型 + 压测 + chaos + replay 验证。要求能回答“机器翻倍后谁先成为瓶颈”“某层完全故障时怎么降级”“恢复后是否会造成重复/漏抓”。

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

> 先做容量估算，再画 Control/State/Data Plane；给出三种故障（热点站、存储慢、浏览器池崩溃）的降级与恢复路径。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] 先估算容量与峰值
- [ ] 画 control/state/data planes
- [ ] 列出 SLO 与约束
- [ ] 明确故障模式与降级
- [ ] 计算成本并设计扩缩容

### 建议监控的指标

- `useful pages/s`
- `cost per useful page`
- `freshness SLA`
- `host-budget violations`
- `replay recovery time`
## 常见误区与 Gotchas

- 固定“每天全量重抓”。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：如何处理突发新闻页？

**参考回答：** 突发新闻页可由站点/页面类型事件提升 priority、缩短 recrawl interval，并设置短期 burst budget；热度下降后指数回落，防长期占用抓取预算。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：内容 hash 变化但正文没变（广告变了）怎么办？

**参考回答：** 对正文做规范化 content hash/DOM main-content extraction，忽略广告/推荐等高变块；raw hash 变化但 normalized body 不变时无需触发全部下游重处理。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 3：条件请求如何降低成本？

**参考回答：** 条件请求在未变化时节省 body、带宽和解析，但仍消耗一次请求/连接和远端校验；所以它降低 cost，不替代 recrawl scheduler。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 变化率估计。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> Recrawl 是变化概率、页面价值和访问预算的联合调度。

## 延伸阅读

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [RFC 9309 - Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Scrapy architecture](https://docs.scrapy.org/en/latest/topics/architecture.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q092 设计一个搜索引擎 Web Crawler。](Q092-设计一个搜索引擎-Web-Crawler.md) | [Q094 如何检测 Crawl Trap？](Q094-如何检测-Crawl-Trap.md) →
