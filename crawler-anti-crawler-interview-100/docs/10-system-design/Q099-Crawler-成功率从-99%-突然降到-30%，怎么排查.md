---
id: Q099
title: "Crawler 成功率从 99% 突然降到 30%，怎么排查？"
chapter: 10
difficulty: "★★★★★"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q099 Crawler 成功率从 99% 突然降到 30%，怎么排查？

> **难度：** ★★★★★  
> **章节：** 第十章  高级系统设计  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- 分层排障
- 指标证据
- 不要先入为主

## 60-90 秒推荐回答

按层排查：①基础设施 DNS/network/CPU/queue/DB；②HTTP 状态分布、redirect、response length、latency；③页面模板/HTML 变化；④Parser selector/schema；⑤Browser JS error/timeout/crash；⑥robots、rate-limit、授权/访问策略变化。

每一步都通过指标和样本证据缩小范围，而不是一上来修改 Header、代理或自动化行为。

## 原理深挖

先对“成功率”的定义做分解：fetch success、parse success、item validation success。三者下降的根因完全不同。

### 事故排查顺序

- 先确定是基础设施、HTTP、页面、Parser、Browser 还是 Policy 层；每一步都用指标证据排除。
- 若 200 比例没变但 items/page 暴跌，优先怀疑模板/解析；若 429/503 激增则优先看访问预算与远端容量。

### GitHub 增强版：进一步理解

1. 系统设计题先做量级估算，再画控制平面、状态平面、数据平面。没有容量数字的架构图很难判断是否真的可行。
2. 任何大规模 crawler 都必须同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance 七个目标；只回答吞吐不完整。
3. 优秀答案会明确失败模式与降级策略：队列爆炸、热点域名、浏览器 OOM、远端 429/503、parser drift、存储延迟、策略变更分别如何处理。

## 高级面试扩展

### 1. 核心边界

系统设计题不能只画组件。先给假设和量级，再定义目标函数与硬约束，然后拆 Control/State/Data Plane；最后用故障模式、SLO 和成本验证设计。

针对 **Crawler 成功率从 99% 突然降到 30%，怎么排查？**，面试时建议先明确讨论边界：分层排障、指标证据、不要先入为主。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Capacity Estimate → Goals/Constraints → URL/Policy State → Scheduler/Fetcher → Raw/Parse/Quality → Recrawl → Observability/Compliance`。架构要同时回答 coverage、freshness、politeness、cost、fault tolerance、quality、compliance。

### 3. 本题进一步深挖

1. 排障先区分 single-site vs global、transport vs parser vs storage。全站同时下降优先看基础设施/发布/共享依赖；单站下降优先看站点模板、政策、网络和域名级指标。

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

- 把所有 403 都归因于反爬升级。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：如果只有一个站点下降怎么判断？

**参考回答：** 单站下降优先比较该 host 的 status/latency/redirect/template/robots/policy 与历史；若基础设施其他站正常，根因更可能是站点特有改版、网络或访问策略。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：如果所有站点同时下降最可能看哪里？

**参考回答：** 所有站点同时下降先看共享层：发布、DNS/代理、出口网络、Scheduler、存储、数据库、CPU/内存、证书/依赖。全局共同变化通常不是单站反爬。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 3：怎样做自动 root-cause hints？

**参考回答：** 建立规则/统计 root-cause graph：例如 connect_error 全局升高→网络；200 正常但 field_missing 升高→parser/template；单 host 429→host budget/policy，并附证据指标。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 分层排障。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> 故障排查先分层定义成功，再用指标定位，不要凭经验猜。

## 延伸阅读

- [Google SRE Book](https://sre.google/sre-book/table-of-contents/)
- [RFC 9309 - Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Scrapy architecture](https://docs.scrapy.org/en/latest/topics/architecture.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q098 设计一个企业级反爬系统。](Q098-设计一个企业级反爬系统.md) | [Q100 终极题：设计一个十亿级 URL、可增量更新、合规、稳定且不压垮目标网站的爬虫平台。](Q100-终极题：设计一个十亿级-URL、可增量更新、合规、稳定且不压垮目标网站的爬虫平台.md) →
