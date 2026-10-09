---
id: Q100
title: "终极题：设计一个十亿级 URL、可增量更新、合规、稳定且不压垮目标网站的爬虫平台。"
chapter: 10
difficulty: "★★★★★"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q100 终极题：设计一个十亿级 URL、可增量更新、合规、稳定且不压垮目标网站的爬虫平台。

> **难度：** ★★★★★  
> **章节：** 第十章  高级系统设计  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- 全局架构
- 控制/状态/数据三平面
- 容量、合规、可恢复

## 60-90 秒推荐回答

整体链路：Seed Management → URL Normalize → Global Dedup → Distributed Frontier → Policy/robots evaluation → Domain-aware Scheduler → HTTP Fetcher / Browser Pool → Raw Data Lake → Parsing/Validation → Content Dedup/Entity Merge → Serving Storage。

状态面保存 URL history、robots、ETag/Last-Modified、last_fetch/last_change、host budget、failure score、dedup index；控制面管理策略、版本、限流、授权、删除请求和审计。

抓取层采用 at-least-once + idempotent store，错误走有预算的 retry/circuit breaker/DLQ；backpressure 从 storage/parser 反向控制 scheduler。

```text
Seed → Normalize → Dedup → Frontier → Policy → Host Scheduler
                                      ├→ HTTP Fetch
                                      └→ Browser Pool
                                                ↓
                                         Raw Data Lake
                                                ↓
                                 Parse → Validate → Dedup → Serve
```

## 原理深挖

容量上先估 10^9 URL 的 frontier 与 history 状态：即使每 URL 仅几十字节也是几十 GB 到数百 GB，必须分片持久化；raw body 更是 PB 级生命周期问题。

增量更新利用 ETag/Last-Modified/content hash 与 change-rate learning；调度目标可写成最大化 Σ Value(u)·Freshness(u)，约束每个 domain 的 RequestRate ≤ Budget。

合规上至少要区分 robots 协商、授权/许可、登录权限、数据保留/删除与审计，不把“技术可访问”当作“业务可采集”。

### 平台化设计

- 建议显式区分 Control Plane（配置/策略/发布）、State Plane（frontier/dedup/host state/lease）、Data Plane（fetch/parse/store）。
- 容量、politeness、recrawl、browser fallback、quality gates、compliance 与 replay 必须进入同一设计，而不是后补模块。

**关键表达式 / 心智模型：**

```text
objective = maximize(useful_fresh_data) subject to host_budget, compute_budget, storage_budget, policy_constraints
```

### GitHub 增强版：进一步理解

1. 系统设计题先做量级估算，再画控制平面、状态平面、数据平面。没有容量数字的架构图很难判断是否真的可行。
2. 任何大规模 crawler 都必须同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance 七个目标；只回答吞吐不完整。
3. 优秀答案会明确失败模式与降级策略：队列爆炸、热点域名、浏览器 OOM、远端 429/503、parser drift、存储延迟、策略变更分别如何处理。

## 高级面试扩展

### 1. 核心边界

系统设计题不能只画组件。先给假设和量级，再定义目标函数与硬约束，然后拆 Control/State/Data Plane；最后用故障模式、SLO 和成本验证设计。

针对 **终极题：设计一个十亿级 URL、可增量更新、合规、稳定且不压垮目标网站的爬虫平台。**，面试时建议先明确讨论边界：全局架构、控制/状态/数据三平面、容量、合规、可恢复。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Capacity Estimate → Goals/Constraints → URL/Policy State → Scheduler/Fetcher → Raw/Parse/Quality → Recrawl → Observability/Compliance`。架构要同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance。

### 3. 本题进一步深挖

1. 十亿级设计要显式估算 frontier/history/dedup state 与 raw retention。若每 URL 状态 100B，10^9 URL 就是约 100GB 原始状态（未含索引/副本）；raw body 往往才是 PB 级成本主项。

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

### 示例 / 伪代码

```text
capacity inputs:
  pages/day
  peak_factor
  avg_response_bytes
  retry_ratio
  browser_fallback_ratio
  parse_cpu_ms/page
  retention_days

outputs:
  peak fetch QPS
  network egress/ingress
  fetcher/browser/parser worker count
  raw storage/day
  frontier & dedup state size
```

## 常见误区与 Gotchas

- 系统设计只画组件，不写约束和状态。
- 全局扩容时忘记 host QPS 不能跟着倍增。
- 没有 raw provenance 和版本，无法审计/重放。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：Frontier 如何按 host 与时间双重调度？

**参考回答：** 用两层调度：host `next_eligible_at` 最小堆/时间轮决定可运行 host，host 内 priority queue 选 URL；抓完更新 token/eligible time 后重新入全局堆。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：如何做 10^9 URL 去重与扩容？

**参考回答：** URL 先 canonicalize，再用分片 Bloom/持久 KV 做 seen；十亿级需要按未来容量估 m/n、分代扩容和持久化。内容层再用 exact/MinHash 去重，二者不要混成一个索引。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 3：如何控制 PB 级 raw retention？

**参考回答：** 按 raw 价值/复现需求分层生命周期：热数据短期、冷对象存储中期、低价值只保留 hash/metadata；使用压缩、dedup、生命周期规则，并让删除请求可沿 provenance 传播。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 4：如何把 freshness SLA 映射成 recrawl priority？

**参考回答：** 把 freshness SLA 转成 stale-cost/priority：`priority ~ importance × expected_change × stale_age / fetch_cost`，为高等级页面设最大 stale age 硬约束，再由 recrawl scheduler 动态分配预算。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 全局架构。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> Web-scale crawler 是一个受站点预算、数据价值、freshness 和成本共同约束的分布式调度系统。

## 延伸阅读

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [RFC 9309 - Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Scrapy architecture](https://docs.scrapy.org/en/latest/topics/architecture.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q099 Crawler 成功率从 99% 突然降到 30%，怎么排查？](Q099-Crawler-成功率从-99%-突然降到-30%，怎么排查.md)
