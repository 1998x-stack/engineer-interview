---
id: Q092
title: "设计一个搜索引擎 Web Crawler。"
chapter: 10
difficulty: "★★★★★"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q092 设计一个搜索引擎 Web Crawler。

> **难度：** ★★★★★  
> **章节：** 第十章  高级系统设计  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- coverage
- freshness
- importance/crawl traps/spam

## 60-90 秒推荐回答

搜索引擎 crawler 同时优化新网页发现和已知网页新鲜度。URL 来自 seed、页面链接、sitemap、历史库和 recrawl。

调度可抽象 Priority(u)=α·Importance+β·Freshness-γ·Cost-δ·Risk，并受到 host politeness、robots、容量和重复预算约束。

还要处理 canonical、crawl trap、spam、duplicate、redirect graph 和 change-rate learning。

## 原理深挖

“抓全网”不是现实目标，必须在有限带宽下最大化索引价值。可用 PageRank/站点质量、历史变化概率和查询需求共同定义 crawl value。

### 搜索 crawler 目标函数

- 搜索 crawler 同时优化 coverage、freshness、importance 与 cost；Frontier 优先级应融合 Page importance 与 recrawl urgency。
- 还需处理 crawl trap、spam、canonical、duplicate、robots 与 per-host budget。

### GitHub 增强版：进一步理解

1. 系统设计题先做量级估算，再画控制平面、状态平面、数据平面。没有容量数字的架构图很难判断是否真的可行。
2. 任何大规模 crawler 都必须同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance 七个目标；只回答吞吐不完整。
3. 优秀答案会明确失败模式与降级策略：队列爆炸、热点域名、浏览器 OOM、远端 429/503、parser drift、存储延迟、策略变更分别如何处理。

## 高级面试扩展

### 1. 核心边界

系统设计题不能只画组件。先给假设和量级，再定义目标函数与硬约束，然后拆 Control/State/Data Plane；最后用故障模式、SLO 和成本验证设计。

针对 **设计一个搜索引擎 Web Crawler。**，面试时建议先明确讨论边界：coverage、freshness、importance/crawl traps/spam。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Capacity Estimate → Goals/Constraints → URL/Policy State → Scheduler/Fetcher → Raw/Parse/Quality → Recrawl → Observability/Compliance`。架构要同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance。

### 3. 本题进一步深挖

1. 搜索 crawler 的目标函数同时含 discovery coverage 与 recrawl freshness；新 URL 和 recrawl URL 要共享预算并按 importance/change probability 调度，还需 crawl-trap/spam/canonical 去重。

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

- 只讲 BFS/DFS。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：新 URL 与 recrawl URL 如何争夺预算？

**参考回答：** 建立 discovery 与 recrawl 两类预算/优先级队列，使用价值函数统一竞争；可给重要 recrawl 保底配额，防新 URL 爆炸导致已有索引长期陈旧。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：如何估页面 change probability？

**参考回答：** 用历史 change/no-change 序列估 hazard rate，并加入页面类型、站点规律、ETag/lastmod 等特征；更新频繁且重要的页面 recrawl 更密。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 3：如何防 infinite calendar trap？

**参考回答：** 对 URL template/参数 cardinality、深度、路径重复和内容相似度设置 pattern budget；日历等无限空间先限速/限深，再抽样确认后封禁 pattern。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 coverage。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> 搜索 crawler 是受资源约束的 coverage × freshness 优化问题。

## 延伸阅读

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [RFC 9309 - Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Scrapy architecture](https://docs.scrapy.org/en/latest/topics/architecture.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q091 设计一个每天抓取 1 亿网页的系统。](Q091-设计一个每天抓取-1-亿网页的系统.md) | [Q093 如何设计 Recrawl Scheduler？](Q093-如何设计-Recrawl-Scheduler.md) →
