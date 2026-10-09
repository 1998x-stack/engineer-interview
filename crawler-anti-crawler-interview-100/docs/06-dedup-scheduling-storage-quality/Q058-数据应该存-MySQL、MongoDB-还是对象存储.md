---
id: Q058
title: "数据应该存 MySQL、MongoDB 还是对象存储？"
chapter: 6
difficulty: "★★★☆☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q058 数据应该存 MySQL、MongoDB 还是对象存储？

> **难度：** ★★★☆☆  
> **章节：** 第六章  去重、调度、存储与数据质量  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- 冷热分层
- 原始/规范化/服务层
- 数据生命周期

## 60-90 秒推荐回答

不存在一种存储适合全部阶段。Raw HTML/response body 适合对象存储；结构化分析结果适合 Parquet/Data Lake；需要事务和主键查询的业务实体适合 SQL；搜索服务适合倒排索引。

设计时先问访问模式、更新模式、保留周期、数据量与成本，而不是先选品牌。

## 原理深挖

一个常见三层是 Raw Zone（不可变原始数据）→ Curated Zone（规范化列式数据）→ Serving Layer（数据库/搜索）。


### GitHub 增强版：进一步理解

1. 去重至少分 URL identity、exact content、near duplicate 三层；它们解决的问题完全不同，不能用一个 Redis Set 代替全部语义。
2. 原始响应应作为可重放事实层保存，解析结果是可再生派生层。保留 fetch_time、headers、content_hash、parser_version，才能做离线重跑与审计。
3. 大规模数据系统应把“抓到多少”升级为“可用多少”：schema completeness、duplicate rate、freshness、provenance coverage 与 parser drift 都是质量指标。
4. 存储选型应按 raw/normalized/serving 分层，而不是试图用单一数据库承载所有生命周期。

## 高级面试扩展

### 1. 核心边界

去重与存储题必须先明确“重复”的定义：URL 相同、规范化 URL 相同、正文完全相同、近重复、语义重复是不同层次；不同层次允许的误判成本也不同。

针对 **数据应该存 MySQL、MongoDB 还是对象存储？**，面试时建议先明确讨论边界：冷热分层、原始/规范化/服务层、数据生命周期。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`Normalize URL → Seen/Dedup → Fetch → Raw Preserve → Content Fingerprint → Exact/Near Dedup → Structured Store + Provenance`。建议把 raw 与 derived 数据分层，支持重放。

### 3. 本题进一步深挖

1. 存储选型应按 raw/analytical/serving 分层：对象存储保存大 body，Parquet/Data Lake 适合扫描分析，OLTP/Document DB 保存业务实体，Search index 服务检索。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 内存 vs FPR | Bloom 极省空间 | 允许 false positive |
| 精确度 vs 计算 | MinHash/SimHash 降复杂度 | 是近似算法，需要阈值/候选索引 |
| 保留能力 vs 成本 | 长期 raw 便于审计重放 | 对象存储/生命周期成本高 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| 过度 Canonicalize | 误合并有意义 query | 字段白名单/域名规则 + 回归样本 |
| 去重误删 | FPR/阈值过激 | 抽样估 FPR/FNR，保留 cluster provenance |
| 小文件/Schema 漂移 | 分析层性能下降 | Parquet compaction + schema version |

### 6. 如何验证方案

建立成对重复/非重复 gold set，分别测 precision/recall；对 Bloom 做容量/FPR 压测，对存储做 replay 与 provenance 反查测试。

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

> 给 1,000 万 URL 和一批近重复正文，设计 URL canonicalization + Bloom/精确/近重复分层方案，并估算误判与内存。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] URL/内容/近重复分层
- [ ] 保留原始响应用于 replay
- [ ] 内容哈希与 parser_version 可追踪
- [ ] 大规模状态估算内存/磁盘
- [ ] 质量指标进入发布门禁

### 建议监控的指标

- `URL dedup hit rate`
- `exact/near-duplicate rate`
- `raw-to-structured coverage`
- `storage write p95`
- `provenance completeness`
## 常见误区与 Gotchas

- 把所有 HTML 塞 MySQL TEXT。
- 只存最终字段，无法重新处理。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：Parquet 为什么适合分析层？

**参考回答：** Parquet 列式、压缩、predicate pushdown 和统计元数据使它适合大规模分析扫描；不适合每条随机小更新的 OLTP 工作负载。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：对象存储上的小文件问题怎么解决？

**参考回答：** 设置目标文件大小（如数百 MB 量级）、批量写入并定期 compaction；按常用过滤字段合理 partition，避免过细分区产生百万小文件。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 冷热分层。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> 存储选型由数据生命周期和访问模式决定。

## 延伸阅读

- [Redis - Sorted Sets](https://redis.io/docs/latest/develop/data-types/sorted-sets/)
- [RFC 3986 - URI Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q057 什么时候使用 SimHash？](Q057-什么时候使用-SimHash.md) | [Q059 为什么原始 HTML 最好保留？](Q059-为什么原始-HTML-最好保留.md) →
