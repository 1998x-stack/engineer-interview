---
id: Q021
title: "画出 Scrapy 的架构。"
chapter: 3
difficulty: "★★☆☆☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q021 画出 Scrapy 的架构。

> **难度：** ★★☆☆☆  
> **章节：** 第三章  Scrapy、异步与并发  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- Engine
- Scheduler
- Downloader / Middleware / Spider / Pipeline

## 60-90 秒推荐回答

核心数据流是 Spider 产生 Request，Engine 交给 Scheduler；可调度请求再经 Downloader Middleware 到 Downloader；Response 回到 Engine，再经 Spider Middleware 交给 Spider；Spider 输出的新 Request 回到 Scheduler，Item 进入 Item Pipeline。

面试要说清楚 Engine 是协调者，Scheduler 管 frontier，Downloader 负责网络，Spider 负责解析和发现，Pipeline 负责数据后处理。

```text
Spider → Engine → Scheduler
   ↑         ↓
Item ← Spider ← Response ← Downloader ← Middleware
```

## 原理深挖

理解架构后，很多问题都有明确落点：代理/重试放 downloader middleware，字段校验放 pipeline，URL 发现逻辑放 spider。

### Scrapy 数据流

- Engine 控制组件间流动，Scheduler 提供待抓 Request，Downloader 负责 I/O，Spider 解析并产生 Item/Request，Pipeline 负责验证和持久化。
- 面试画图时标出 middleware 所在边界，能体现你理解横切逻辑的位置。

### GitHub 增强版：进一步理解

1. Scrapy 的优势来自事件驱动 I/O 与组件解耦，不是“线程更多”。对 CPU 密集解析、模型推理、OCR 等任务，应从 Reactor/Event Loop 中剥离。
2. 把 Scheduler 看作单机 URL Frontier，把 Downloader Middleware 看作 HTTP 横切面，把 Item Pipeline 看作数据工程边界；职责清晰后才容易扩展到分布式。
3. 吞吐调优必须同时看并发、远端延迟、下载槽位、连接复用、解析 CPU、输出背压，单独把 CONCURRENT_REQUESTS 调大经常只会把瓶颈转移。

## 高级面试扩展

### 1. 核心边界

Scrapy/异步题的核心不是背类名，而是理解 **事件循环不能被阻塞**、Scheduler/Downloader/Pipeline 的职责边界，以及并发、吞吐、远端压力三者不是同一个指标。

针对 **画出 Scrapy 的架构。**，面试时建议先明确讨论边界：Engine、Scheduler、Downloader / Middleware / Spider / Pipeline。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Spider → Engine → Scheduler → Downloader → Response → Spider → Item Pipeline`，其中网络等待由事件驱动复用；CPU 密集、阻塞数据库调用必须从 reactor/event-loop 热路径移出。

### 3. 本题进一步深挖

1. 高分回答应能解释 Engine 负责数据流协调，Scheduler 管 Request 队列/去重，Downloader 处理网络，Middleware 提供横切能力，Spider 负责业务解析，Pipeline 负责 item 后处理。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 并发 vs 远端压力 | 提高 in-flight 提升吞吐 | 必须有 per-host budget/AutoThrottle |
| 单进程简单 vs 隔离 | 事件循环高效 | CPU/阻塞任务需线程/进程/外部 worker |
| 内存队列 vs 持久化 | 快 | 重启恢复和大 frontier 需要持久化 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| Event-loop Block | callback 做 CPU/同步 I/O | profiling event-loop lag，移出热路径 |
| 队列失衡 | 下载快、Pipeline 慢 | queue lag + backpressure |
| 重启丢状态 | Scheduler/Item 未 checkpoint | 持久化 frontier + 幂等 sink |

### 6. 如何验证方案

用可控延迟/错误率的 mock server 做并发压测，记录 event-loop lag、in-flight、per-host QPS、queue lag、CPU 与 item latency。

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

> 构造一个 downloader 很快但 parser/sink 很慢的压测，观察 event-loop lag 与 queue lag，并给出 backpressure 和任务拆分方案。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] I/O 与 CPU 工作负载分离
- [ ] 中间件职责单一且可测试
- [ ] Scheduler/dupefilter 可恢复
- [ ] 并发调整必须观察远端与下游

### 建议监控的指标

- `in-flight requests`
- `download slot latency`
- `reactor lag`
- `parse CPU`
- `item pipeline latency`
## 常见误区与 Gotchas

- 把 Scheduler 当简单队列。
- 把所有逻辑都塞进 Spider。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：重试应该放在哪一层？

**参考回答：** 网络级临时错误放 Downloader Middleware/Retry 层更合适；业务语义失败（例如页面状态不完整、需要稍后 recrawl）应由 Spider/Scheduler 重新调度，避免混淆“传输重试”和“业务再抓”。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：URL 去重器和 Scheduler 的关系是什么？

**参考回答：** DupeFilter 通常在 Scheduler 接受请求时决定是否入队，Scheduler 管优先级/持久化/出队。去重是 frontier 的准入策略之一，不等同于整个 Scheduler。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 Engine。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> Scrapy 的价值是把网络、调度、解析、数据处理拆成可组合的阶段。

## 延伸阅读

- [Scrapy 2.18 - Architecture](https://docs.scrapy.org/en/latest/topics/architecture.html)
- [Scrapy - Downloader Middleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html)
- [Scrapy - AutoThrottle](https://docs.scrapy.org/en/latest/topics/autothrottle.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q020 HTML parser 应该选择严格还是容错？](../02-html-dom-extraction/Q020-HTML-parser-应该选择严格还是容错.md) | [Q022 Scrapy 为什么通常比 requests + ThreadPool 更适合高并发抓取？](Q022-Scrapy-为什么通常比-requests-+-ThreadPool-更适合高并发抓取.md) →
