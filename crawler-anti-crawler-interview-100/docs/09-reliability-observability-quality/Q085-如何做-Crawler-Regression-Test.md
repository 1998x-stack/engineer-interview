---
id: Q085
title: "如何做 Crawler Regression Test？"
chapter: 9
difficulty: "★★★☆☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q085 如何做 Crawler Regression Test？

> **难度：** ★★★☆☆  
> **章节：** 第九章  稳定性、可观测性与数据质量  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- HTML fixtures
- golden output
- parser diff

## 60-90 秒推荐回答

保存覆盖典型模板和边界情况的 HTML fixtures，Parser 修改后离线运行新旧版本，对结构化输出、字段值、数量和异常进行差异比较。

测试应固定 raw input，避免回归测试本身依赖实时网站。

## 原理深挖

对选择器易变站点，可把真实线上样本定期匿名化后加入 fixture corpus，形成逐步扩充的回归集。


### GitHub 增强版：进一步理解

1. Crawler 的生产 SLO 应围绕“有效数据”而不是“请求成功”：fetch_success、parse_success、required-field completeness、freshness lag、duplicate rate、queue age 需要共同观察。
2. 最危险的故障往往不是 crash，而是 silent data corruption。每个 parser 都应有 fixture 回归、分布监控和 canary 发布。
3. 排障需要把系统分为入口、网络、远端、解析、浏览器、队列、存储七层，通过指标和 trace 缩小范围，而不是凭经验先猜“被反爬”。
4. Parser regression 应对 golden HTML 运行确定性断言，并比较新旧字段分布。

## 高级面试扩展

### 1. 核心边界

可靠性题的核心是：**系统必须能发现“自己看起来成功但数据已经错了”**。因此 transport success、parse success、semantic validity、business usefulness 应拆成不同 SLO。

针对 **如何做 Crawler Regression Test？**，面试时建议先明确讨论边界：HTML fixtures、golden output、parser diff。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Fetch Metrics → Parse/Schema Metrics → Data-quality Signals → Trace/Logs → Alert → Quarantine/Replay`。监控必须贯穿 URL 的端到端 lineage。

### 3. 本题进一步深挖

1. golden file 不应由实现者无审查地“更新通过”。建议差异审查、样本分层、时间/随机字段归一化，并保留历史 parser 版本的 expected output。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 灵敏度 vs 告警噪声 | 阈值低能早发现 | A/B 实验和自然波动会误报 |
| Fail-open vs Fail-closed | 继续产出保持覆盖 | 可能传播静默坏数据 |
| 保留原始数据 vs 成本 | 可重放/审计 | 存储与隐私治理成本 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| 200 假成功 | 登录页/错误模板 | semantic validator + template fingerprint |
| Silent Corruption | 字段空值但任务成功 | field distribution SLO + quarantine |
| Retry Storm | 故障期间放大压力 | error-class policy + exponential backoff/jitter/circuit breaker |

### 6. 如何验证方案

对 parser drift、目标站 429/503、DNS、DB 慢、对象存储慢、browser crash 注入故障；验证告警是否先于业务数据事故。

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

> 设计一次 parser 改版的 canary + data-quality SLO，要求在“服务仍返回 200、字段开始静默缺失”时 10 分钟内发现。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] 定义传输/解析/数据三层 SLO
- [ ] 全链路 trace + structured error
- [ ] fixture 回归 + canary
- [ ] Retry 有预算且带 jitter
- [ ] DLQ 可 replay

### 建议监控的指标

- `fetch success`
- `parse success`
- `data completeness`
- `freshness lag`
- `DLQ rate`
- `queue age`

### 示例 / 伪代码

```text
trace spans:
queue_wait -> dns -> connect -> tls -> ttfb -> download
          -> parse -> validate -> dedup -> store

metrics should correlate by: host, page_type, spider_version, parser_version
```

## 常见误区与 Gotchas

- 测试直接访问线上页面，结果不可重复。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：如何处理时间字段这种天然变化值？

**参考回答：** golden 比较前对 `now`、随机 ID、动态价格/计数等字段做规范化/掩码，或断言格式/范围而非精确值；固定 clock 可进一步提高可复现。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：golden file 更新流程怎么防止“把 bug 更新成基线”？

**参考回答：** 更新 golden 必须伴随 diff review、变更原因和代表页面抽样；CI 不允许测试失败后“一键接受全部”，否则容易把 bug 固化成新基线。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 HTML fixtures。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> Parser 应像普通软件一样有固定输入、确定输出和回归集。

## 延伸阅读

- [OpenTelemetry - Documentation](https://opentelemetry.io/docs/)
- [Google SRE Book - Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q084 什么叫 Silent Data Corruption？](Q084-什么叫-Silent-Data-Corruption.md) | [Q086 如何做 Canary Crawling？](Q086-如何做-Canary-Crawling.md) →
