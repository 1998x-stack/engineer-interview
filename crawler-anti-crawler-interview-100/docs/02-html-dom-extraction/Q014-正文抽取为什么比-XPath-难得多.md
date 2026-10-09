---
id: Q014
title: "正文抽取为什么比 XPath 难得多？"
chapter: 2
difficulty: "★★★☆☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q014 正文抽取为什么比 XPath 难得多？

> **难度：** ★★★☆☆  
> **章节：** 第二章  HTML、DOM 与数据抽取  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- 正文/模板分类
- 文本密度与链接密度
- 通用抽取算法

## 60-90 秒推荐回答

页面里同时存在导航、正文、广告、推荐、评论和页脚。真正问题不是找到 p 标签，而是判断每个 block 是否属于 main content。

通用抽取器会结合文本密度、链接密度、DOM 深度、标签类型、标点、段落长度和模板频率等信号，把问题建模为 block classification。

## 原理深挖

新闻、论坛、文档站、代码页面的“正文”定义不同，因此通用抽取器仍需域级评测。生产系统应保留 raw HTML，支持离线重新抽取。

### 正文抽取是分类问题

- 可将 DOM block 的文本密度、链接密度、标签、位置、长度作为特征估计 main-content probability。
- 抽取器的评估不只看字符 recall，还应看 boilerplate precision、结构保真和下游字段完整率。

### GitHub 增强版：进一步理解

1. Extraction 的真正对象不是 DOM 节点，而是业务实体。先定义 schema、字段语义和冲突优先级，再写 selector；否则页面一改版就会把结构问题变成数据污染。
2. 稳定性优先级通常是：结构化数据(JSON-LD/嵌入 JSON) > 语义属性(data-*/ARIA/稳定 id) > 相对 DOM 结构 > 绝对路径。
3. 任何核心字段都应有 validation 与 drift metric；“返回空字符串继续入库”是典型 silent corruption。
4. Selector 的稳定性优先于“短”；最好用 fixture 回归证明规则面对模板变化仍正确。

## 高级面试扩展

### 1. 核心边界

数据抽取不是“selector 能选到值”就结束，而是把不稳定网页映射为稳定业务 Schema。应区分 **结构定位问题**、**语义解释问题**、**数据质量问题**：三者需要不同的监控和修复方式。

针对 **正文抽取为什么比 XPath 难得多？**，面试时建议先明确讨论边界：正文/模板分类、文本密度与链接密度、通用抽取算法。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Raw HTML/DOM/JSON-LD → Parse → Candidate Extraction → Semantic Resolution → Schema Validation → Quarantine/Store`。生产系统必须允许“解析成功但语义不可信”的中间状态。

### 3. 本题进一步深挖

1. Selector 稳定性通常来自语义属性（data-*、ARIA、schema、稳定 label）和相对结构，而不是 DOM 绝对层级。建议对 selector 建 fixture 回归集，并让 fallback 有明确优先级和命中统计。

2. 正文抽取本质是 block classification/segmentation：文本密度、链接密度、标签结构、重复模板频率等共同决定正文概率。评价应同时看 precision、recall、结构保真和 boilerplate leakage。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 精度 vs 召回 | 严格 selector/规则降低误抓 | 页面变体会增加漏抓 |
| 稳定性 vs 特异性 | 使用语义属性/结构化数据 | 过度泛化可能选中错误实体 |
| 实时修复 vs 可复现 | 在线 fallback 快 | 保留 raw 才能离线重放和审计 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| Selector Drift | class/DOM 层级变化 | field missing-rate + fixture regression |
| 语义歧义 | 多个价格/时间/实体 | 业务 Schema 显式建模，不压成单一 string |
| 模板污染 | 导航/页脚进入正文 | 正文质量指标 + boilerplate 频率检测 |

### 6. 如何验证方案

维护代表性 HTML fixtures、golden structured output、字段级强/弱校验和 DOM 变体测试；改 parser 时跑差异报告，而不是直接覆盖基线。

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

> 准备 20 个不同模板/异常页面的 HTML fixture，设计字段级验证和 fallback 策略，并说明如何区分 genuine missing 与 parser drift。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] 先定义 schema 再写 selector
- [ ] 准备页面 fixture 与边界样本
- [ ] 必填字段失败进入 quarantine
- [ ] 监控字段分布与模板漂移

### 建议监控的指标

- `required-field completeness`
- `selector success rate`
- `items/page`
- `text length distribution`
- `quarantine rate`

### 示例 / 伪代码

```python
def validate_item(item):
    assert item.get("source_url")
    assert item.get("observed_at")
    assert item.get("title") and len(item["title"]) < 500
    assert item.get("body") and len(item["body"]) > 100
    return item
```

重点不是这几行代码，而是“解析失败必须可见，不能静默写空字段”。

## 常见误区与 Gotchas

- 把所有 p 拼起来当正文。
- 只看正文非空，不评估 boilerplate 污染率。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：如何衡量正文抽取质量？

**参考回答：** 用人工标注的正文块/文档 gold set 测 precision、recall、boilerplate leakage、结构保真；再看正文长度分布、链接密度和下游搜索/训练效果，避免只看“提取非空”。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：为什么模板污染会影响内容去重？

**参考回答：** 模板文本会让不同页面共享大量相同 n-gram，导致内容指纹被模板主导，增加近重复误判/聚类噪声。通常应先做正文/boilerplate 清理再内容去重。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 正文/模板分类。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> 正文抽取是页面语义分类问题，不是标签遍历问题。

## 延伸阅读

- [MDN - HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Schema.org](https://schema.org/)
- [lxml documentation](https://lxml.de/)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q013 DOM Tree 与原始 HTML 为什么可能不同？](Q013-DOM-Tree-与原始-HTML-为什么可能不同.md) | [Q015 页面结构变化后，如何避免大规模产出空数据？](Q015-页面结构变化后，如何避免大规模产出空数据.md) →
