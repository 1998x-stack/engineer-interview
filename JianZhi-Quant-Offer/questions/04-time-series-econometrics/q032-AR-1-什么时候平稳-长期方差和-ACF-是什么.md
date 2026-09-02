---
id: q032
title: "AR(1) 什么时候平稳？长期方差和 ACF 是什么？"
chapter: "D. 时间序列与计量"
difficulty: "★★☆"
tags: ["AR(1)", "ACF", "稳定性"]
source_type: "高可信重构题型"
version: "2.0"
---

# 032. AR(1) 什么时候平稳？长期方差和 ACF 是什么？

[← Q031](q031-什么叫弱平稳-weak-stationarity.md) · [总索引](../../docs/100-question-index.md) · [Q033 →](q033-Random-Walk-为什么-non-stationary.md)

> **难度**：★★☆  
> **标签**：AR(1)｜ACF｜稳定性  
> **题型口径**：高可信重构题型  
> **所属模块**：D. 时间序列与计量  
> **本题能力主线**：时间序列与计量

## 题目

AR(1) 什么时候平稳？长期方差和 ACF 是什么？

---

## 1. 面试官到底在考什么

本题表面属于 **AR(1), ACF, 稳定性**，但真正考察的是：你能否把口头问题迅速变成一个**定义清楚、假设透明、可推导、可验证**的模型。

本章统一的高质量作答原则是：**先判断平稳性和时间可用性，再讨论预测；把 serial dependence、heteroskedasticity、非同步采样和 regime change 视为一等公民。**

面试官通常会观察四件事：

1. 你是否先明确随机变量 / 状态 / 时间信息集，而不是立即套公式；
2. 你是否知道结论依赖哪些假设，以及假设被破坏后会发生什么；
3. 你能否给出一条简洁主解，同时知道替代方法与扩展；
4. 你能否把数学结果翻译成量化研究或工程上的可验证结论。

## 2. 先给结论（30 秒版本）

X_t=φX_{t-1}+ε_t 在 |φ|<1 时协方差平稳；若 Var(ε)=σ²，则 Var(X)=σ²/(1-φ²)，ρ(k)=φ^k。

**推荐面试表达：** 用 MA(∞) 展开解释 |φ|<1，比只背条件更扎实。

如果只有 30 秒，优先说清楚：**定义 → 关键式子/算法 → 结论 → 一个最重要的坑**。不要先铺背景。

## 3. Formalization：变量、假设与数学对象

AR(1) $X_t=c+\phi X_{t-1}+\epsilon_t$ 在 $|\phi|<1$ 时有稳态均值 $\mu=c/(1-\phi)$、方差 $\sigma_\epsilon^2/(1-\phi^2)$、ACF $\rho_k=\phi^k$。

### 专业建模检查表

1. 先锁定时间轴：feature timestamp、observation timestamp、label horizon 与数据发布时刻必须严格有序。
2. 检查 stationarity / integration order / structural break；对 non-stationary level 直接回归很容易产生伪回归。
3. 明确依赖结构：ACF/PACF、异方差、seasonality、overlapping labels 与 asynchronous sampling 都会改变标准误和验证方式。
4. 模型选择与超参数只能使用历史训练窗口；validation 必须保持 chronological order。
5. 任何“历史上稳定”的关系都要做 rolling parameter、subperiod 与 regime sensitivity 检查。

## 4. 标准推导：从第一原则得到答案

递归展开 X_t=Σ_{j≥0} φ^j ε_{t-j}，只有 |φ|<1 时平方可和，才得到稳定的无限 MA 表示。

### 第二视角：如何验证主解

解析时间序列模型之外，再做 rolling/expanding OOS；理论上的平稳参数如果在滚动窗口剧烈变化，就应把 structural break 当一等问题。

对本题尤其值得继续追问的是：**AR(1) 的 |φ|<1 同时保证冲击衰减和有限长期方差；φ 越接近 1，有限样本中越容易与 unit root 混淆。**

一个成熟回答应能说明：如果解析解、数值实验和经验数据三者不一致，优先检查哪一层假设，而不是简单选择“看起来最漂亮”的结果。

## 5. Why：为什么这个方法有效

AR(1) 的 |φ|<1 同时保证冲击衰减和有限长期方差；φ 越接近 1，有限样本中越容易与 unit root 混淆。

这一层是区分“会做题”和“理解题”的关键。面试官继续追问时，最常见的方向不是让你重复公式，而是问：**为什么这个结构成立、什么情况下失效、能否推广**。

### 高级面试层：从答案到研究判断

- **本题的高级抽象**：AR(1) 的 |φ|<1 同时保证冲击衰减和有限长期方差；φ 越接近 1，有限样本中越容易与 unit root 混淆。
- **最值得保留的原始面试表达**：用 MA(∞) 展开解释 |φ|<1，比只背条件更扎实。
- **研究者视角**：不要只问“公式是否正确”，还要问“这个结论对哪些 perturbation 稳定、什么观测会证伪它、实现中哪一层最容易引入偏差”。

## 6. 量化金融 / 工程语境中的对应问题

AR(1) 是 mean persistence 的最小模型。估到 $\phi\approx1$ 时，小样本偏差和 unit-root 区分会很难；不要直接把 half-life 当稳定事实。

把本题迁移到真实研究时，建议统一问四个问题：

1. **Data generating process**：数据是怎么产生的？
2. **Information set**：在决策时刻真正可用的信息是什么？
3. **Estimator / algorithm**：我们估计/计算的对象是什么？
4. **Validation**：用什么反事实、OOS、replay 或 simulation 能证伪它？

### 实际落地检查清单

- 采用 chronological walk-forward，而不是随机切分。
- 监控 rolling coefficients/ACF/volatility/regime stability。
- 处理 timestamp alignment、publication lag 和 asynchronous sampling。

## 7. 边界条件、失效场景与模型风险

本题所在模块最容易出现以下系统性错误：

- 先建模后检查 stationarity/PIT
- 随机切分或忽略重叠窗口依赖
- 把统计相关直接解释为稳定经济机制

结合本题，还要特别注意原始题解中的这些陷阱：

- **错误 1**：把 φ≤1 当作条件，漏掉负数绝对值。

一个专业回答不应该只说“答案是 X”，而应至少能补一句：**“这个结论依赖于……；如果……不成立，我会改用……”**。

## 8. 追问树：不只列问题，还要会接

### 追问 1：φ≈1 时 finite sample 有什么问题？

**回答方向：** 当 $\phi$ 接近 1，OLS 存在显著 finite-sample bias，常规渐近近似变差，且与 unit root 的区分统计功效低。

### 追问 2：φ<0 的 ACF 形状？

**回答方向：** $\phi<0$ 时 $\rho_k=\phi^k$，ACF 正负交替并按 $|\phi|^k$ 衰减。

### 面试现场的追问策略

- 第一次追问：先给结论与关键理由，不要重新从头讲整题；
- 第二次追问：主动指出新假设改变了哪一部分模型；
- 开放追问：给一个 baseline，再给一个更严格/更工程化版本，并说明验证方式。

## 9. 高频错误：错误为什么会发生

- **错误 1**：把 φ≤1 当作条件，漏掉负数绝对值。

这些错误通常源于**忽略时间顺序、非平稳性和相关误差**；修复方法是先审计 timestamp/DGP，再选择模型和标准误。

## 10. 3 分钟专业回答模板

可以按下面顺序组织：

> **第一步，定义。** 我先明确本题的变量/状态和信息条件。  
> **第二步，主解。** 用最短的推导得到核心结论：X_t=φX_{t-1}+ε_t 在 |φ|<1 时协方差平稳；若 Var(ε)=σ²，则 Var(X)=σ²/(1-φ²)，ρ(k)=φ^k。  
> **第三步，解释。** 关键结构是：AR(1) 的 |φ|<1 同时保证冲击衰减和有限长期方差；φ 越接近 1，有限样本中越容易与 unit root 混淆。  
> **第四步，边界。** 如果存在 unit root、structural break、异方差、overlap 或非同步采样，我会先修正 DGP/验证协议，再解释系数和显著性。  
> **第五步，迁移。** 迁移到真实时间序列时，我会先锁 timestamp 和 walk-forward protocol，再讨论 stationarity、预测增益与 regime robustness。

这比“先堆术语、最后给答案”更符合顶级 Quant Research / Algorithm 面试的交流方式。

## 11. 自测与延伸练习

1. 不看答案，用 30 秒给出本题结论与最重要假设。
2. 不看推导，重新写出关键等式 / 状态 / 目标函数。
3. 回答全部追问，并明确哪些答案是精确结论、哪些只是近似或建模选择。
4. 为本题设计一个最小 simulation / numerical check，验证主结论。
5. 说明一个真实量化场景中会导致本题假设失效的例子。

## 12. 关联题目

- [031. 什么叫弱平稳（weak stationarity）？](q031-什么叫弱平稳-weak-stationarity.md)
- [033. Random Walk 为什么 non-stationary？](q033-Random-Walk-为什么-non-stationary.md)
- [037. Granger Causality 是真正的因果吗？](q037-Granger-Causality-是真正的因果吗.md)

## 13. 延伸阅读

- Hamilton, *Time Series Analysis*；Tsay, *Analysis of Financial Time Series*
- [本仓库知识地图](../../docs/knowledge-map.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
- [官方题型与岗位能力依据](../../references/official-sources.md)

## 14. 来源与内容边界

- **PDF 来源内容**：本题题干、基础答案、原始推导、追问、高频错误与面试表达，来自仓库所附 Professional Edition PDF / `questions.json` 的结构化转录。
- **V2 扩展内容**：Formalization、量化语境、追问回答方向、模型风险、工程验证与延伸阅读，是本次仓库专业化扩写；它们用于教学与面试训练，不应被误认为某家公司未公开的内部标准答案。
- `source_type: 高可信重构题型` 只表示题目来源口径。

---

[← Q031](q031-什么叫弱平稳-weak-stationarity.md) · [总索引](../../docs/100-question-index.md) · [Q033 →](q033-Random-Walk-为什么-non-stationary.md)
