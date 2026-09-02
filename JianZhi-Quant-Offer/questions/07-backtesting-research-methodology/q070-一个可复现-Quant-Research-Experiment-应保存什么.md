---
id: q070
title: "一个可复现 Quant Research Experiment 应保存什么？"
chapter: "G. 数据、回测与研究方法论"
difficulty: "★★☆"
tags: ["Reproducibility", "lineage", "MLOps"]
source_type: "高可信重构题型"
version: "2.0"
---

# 070. 一个可复现 Quant Research Experiment 应保存什么？

[← Q069](q069-如何判断-improvement-是真-signal-还是-research-overfitting.md) · [总索引](../../docs/100-question-index.md) · [Q071 →](../08-portfolio-risk-optimization/q071-推导-Minimum-Variance-Portfolio.md)

> **难度**：★★☆  
> **标签**：Reproducibility｜lineage｜MLOps  
> **题型口径**：高可信重构题型  
> **所属模块**：G. 数据、回测与研究方法论  
> **本题能力主线**：回测与研究方法论

## 题目

一个可复现 Quant Research Experiment 应保存什么？

---

## 1. 面试官到底在考什么

本题表面属于 **Reproducibility, lineage, MLOps**，但真正考察的是：你能否把口头问题迅速变成一个**定义清楚、假设透明、可推导、可验证**的模型。

本章统一的高质量作答原则是：**先证明实验没有泄漏、幸存者偏差和成本幻觉，再谈 alpha；把每一次试验本身也视为需要记录和审计的数据。**

面试官通常会观察四件事：

1. 你是否先明确随机变量 / 状态 / 时间信息集，而不是立即套公式；
2. 你是否知道结论依赖哪些假设，以及假设被破坏后会发生什么；
3. 你能否给出一条简洁主解，同时知道替代方法与扩展；
4. 你能否把数学结果翻译成量化研究或工程上的可验证结论。

## 2. 先给结论（30 秒版本）

至少保存 dataset/universe/version、timestamps、feature code commit、label、split、model config、seed、cost model、metrics、environment、artifacts。

**推荐面试表达：** 提出“research lineage + immutable manifest”会很加分。

如果只有 30 秒，优先说清楚：**定义 → 关键式子/算法 → 结论 → 一个最重要的坑**。不要先铺背景。

## 3. Formalization：变量、假设与数学对象

可复现实验需要同时版本化 data、code、config、environment 与 artifacts。尤其要保存 universe/PIT snapshot、label definition、split schedule、random seed、cost/fill model 与所有超参。

### 专业建模检查表

1. 第一原则是 point-in-time：任何在决策时刻尚不可获得的信息都必须被排除，包括后修订数据、未来 universe 与未来 corporate-action 信息。
2. 把研究流程本身纳入审计：尝试过多少特征、参数、样本区间、universe 和 cost assumption，都影响最终显著性。
3. 区分 gross predictive edge 与 net implementable edge；spread、impact、fees、latency、fill 与 capacity 是模型的一部分。
4. 验证必须有 untouched holdout / walk-forward，并对不同 regime、资产群、时间尺度做 stability analysis。
5. 确保实验可重现：dataset snapshot、code commit、config、seed、cost model 与 evaluation artifact 都要可追踪。

## 4. 标准推导：从第一原则得到答案

更成熟系统应做到从任何结果反向追踪到原始数据快照与代码，支持“同输入同版本确定性重放”。

### 第二视角：如何验证主解

把 backtest 看成一个可证伪的软件实验：构造 placebo、延迟特征、打乱标签、提高成本、改变 universe 与 subperiod，观察结论是否按预期退化。

对本题尤其值得继续追问的是：**可复现研究需要把数据版本、时间口径、代码 commit、环境、随机种子、split、成本模型和 artifacts 一起固化。**

一个成熟回答应能说明：如果解析解、数值实验和经验数据三者不一致，优先检查哪一层假设，而不是简单选择“看起来最漂亮”的结果。

## 5. Why：为什么这个方法有效

可复现研究需要把数据版本、时间口径、代码 commit、环境、随机种子、split、成本模型和 artifacts 一起固化。

这一层是区分“会做题”和“理解题”的关键。面试官继续追问时，最常见的方向不是让你重复公式，而是问：**为什么这个结构成立、什么情况下失效、能否推广**。

### 高级面试层：从答案到研究判断

- **本题的高级抽象**：可复现研究需要把数据版本、时间口径、代码 commit、环境、随机种子、split、成本模型和 artifacts 一起固化。
- **最值得保留的原始面试表达**：提出“research lineage + immutable manifest”会很加分。
- **研究者视角**：不要只问“公式是否正确”，还要问“这个结论对哪些 perturbation 稳定、什么观测会证伪它、实现中哪一层最容易引入偏差”。

## 6. 量化金融 / 工程语境中的对应问题

目标是“给定 commit + manifest，可以重建同一训练矩阵和主要指标”。只保存 notebook 和最终 CSV 不够。

把本题迁移到真实研究时，建议统一问四个问题：

1. **Data generating process**：数据是怎么产生的？
2. **Information set**：在决策时刻真正可用的信息是什么？
3. **Estimator / algorithm**：我们估计/计算的对象是什么？
4. **Validation**：用什么反事实、OOS、replay 或 simulation 能证伪它？

### 实际落地检查清单

- 建立 PIT data manifest 与不可变 dataset snapshot。
- 用 audit tree 逐项排除 leakage、selection、cost 和 execution 偏差。
- 用 independent reimplementation 或 golden replay 复核关键结果。

## 7. 边界条件、失效场景与模型风险

本题所在模块最容易出现以下系统性错误：

- 只看最终回测曲线、不审计数据血缘
- holdout 被反复查看导致 research overfit
- cost/fill/universe 假设与实际部署不一致

结合本题，还要特别注意原始题解中的这些陷阱：

- **错误 1**：只保存 notebook 和最终 CSV。

一个专业回答不应该只说“答案是 X”，而应至少能补一句：**“这个结论依赖于……；如果……不成立，我会改用……”**。

## 8. 追问树：不只列问题，还要会接

### 追问 1：随机 GPU 算子怎么做可复现？

**回答方向：** 固定随机种子还不够；启用 deterministic kernels、固定库/驱动版本、记录硬件与非确定算子，必要时接受速度换确定性。

### 追问 2：数据 revision 后如何对比？

**回答方向：** 保存数据 snapshot/hash 与 transformation manifest；revision 后用 diff 量化哪些记录变化，并在旧/新版本分别重跑关键指标做 attribution。

### 面试现场的追问策略

- 第一次追问：先给结论与关键理由，不要重新从头讲整题；
- 第二次追问：主动指出新假设改变了哪一部分模型；
- 开放追问：给一个 baseline，再给一个更严格/更工程化版本，并说明验证方式。

## 9. 高频错误：错误为什么会发生

- **错误 1**：只保存 notebook 和最终 CSV。

这些错误通常源于**未来信息、样本选择、成本遗漏或研究者自由度**；修复方法是 PIT + audit trail + untouched OOS。

## 10. 3 分钟专业回答模板

可以按下面顺序组织：

> **第一步，定义。** 我先明确本题的变量/状态和信息条件。  
> **第二步，主解。** 用最短的推导得到核心结论：至少保存 dataset/universe/version、timestamps、feature code commit、label、split、model config、seed、cost model、metrics、environment、artifacts。  
> **第三步，解释。** 关键结构是：可复现研究需要把数据版本、时间口径、代码 commit、环境、随机种子、split、成本模型和 artifacts 一起固化。  
> **第四步，边界。** 如果 PIT、universe、cost、selection 或 execution 假设改变，Sharpe/PnL 需要重算；任何无法重现的收益都不进入结论。  
> **第五步，迁移。** 迁移到策略研究时，我会建立 PIT 数据血缘、研究日志、成本模型和独立 OOS，使结果能够被复现并被证伪。

这比“先堆术语、最后给答案”更符合顶级 Quant Research / Algorithm 面试的交流方式。

## 11. 自测与延伸练习

1. 不看答案，用 30 秒给出本题结论与最重要假设。
2. 不看推导，重新写出关键等式 / 状态 / 目标函数。
3. 回答全部追问，并明确哪些答案是精确结论、哪些只是近似或建模选择。
4. 为本题设计一个最小 simulation / numerical check，验证主结论。
5. 说明一个真实量化场景中会导致本题假设失效的例子。

## 12. 关联题目

- [069. 如何判断 improvement 是真 signal 还是 research overfitting？](q069-如何判断-improvement-是真-signal-还是-research-overfitting.md)
- [071. 推导 Minimum-Variance Portfolio。](../08-portfolio-risk-optimization/q071-推导-Minimum-Variance-Portfolio.md)
- [065. 为什么 transaction cost 不能简单固定减 1bp？](q065-为什么-transaction-cost-不能简单固定减-1bp.md)

## 13. 延伸阅读

- Bailey et al. 关于 backtest overfitting 的系列工作；López de Prado, *Advances in Financial Machine Learning*
- [本仓库知识地图](../../docs/knowledge-map.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
- [官方题型与岗位能力依据](../../references/official-sources.md)

## 14. 来源与内容边界

- **PDF 来源内容**：本题题干、基础答案、原始推导、追问、高频错误与面试表达，来自仓库所附 Professional Edition PDF / `questions.json` 的结构化转录。
- **V2 扩展内容**：Formalization、量化语境、追问回答方向、模型风险、工程验证与延伸阅读，是本次仓库专业化扩写；它们用于教学与面试训练，不应被误认为某家公司未公开的内部标准答案。
- `source_type: 高可信重构题型` 只表示题目来源口径。

---

[← Q069](q069-如何判断-improvement-是真-signal-还是-research-overfitting.md) · [总索引](../../docs/100-question-index.md) · [Q071 →](../08-portfolio-risk-optimization/q071-推导-Minimum-Variance-Portfolio.md)
