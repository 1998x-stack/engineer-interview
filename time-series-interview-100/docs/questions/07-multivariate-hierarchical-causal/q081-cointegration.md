---
id: q081
title: "什么是 Cointegration？"
chapter: 7
difficulty: "★★★★★"
frequency: "★★★★★"
tags: ["协整", "I(1)", "长期均衡"]
source: "PDF 2026.09"
---

# Q081 什么是 Cointegration？

> **章节：** 多变量、协整、层级与因果  
> **难度：** ★★★★★ ｜ **频率：** ★★★★★  
> **关键词：** 协整 / I(1) / 长期均衡

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

多个非平稳序列若存在某线性组合平稳，说明它们共享长期 equilibrium relationship。

## PDF 基线：核心公式 / 结构

$$
x_t,y_t~I(1), y_t-βx_t~I(0)
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

协整允许“level 非平稳但组合有长期约束”，因此不能简单对所有变量一阶差分后丢掉长期信息。

### PDF 易错点

> 看高相关系数就说协整。

### PDF 高级加分点

> （PDF 未给独立高级加分点。）

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

多变量问题要区分预测相关、长期均衡、层级约束和因果效应，这四类问题经常被错误混用。

- 协整的核心是非平稳序列的某个线性组合平稳，表示长期均衡约束。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. Engle-Granger 与 Johansen 区别？

**回答方向：** 按‘定义/假设 -> 表达能力 -> 失败模式 -> 适用场景 -> 如何验证’五个维度比较，避免只列优缺点。

### 2. 协整秩是什么？

**回答方向：** 围绕本章主线回答：多变量问题要区分预测相关、长期均衡、层级约束和因果效应，这四类问题经常被错误混用，并落到假设、验证与工程边界。


### 4. 工程检查清单

- [ ] 先确认变量是否平稳/协整再做 VAR/回归。
- [ ] 层级系统必须检查 coherence。
- [ ] 任何因果结论都需要额外识别假设，不能由预测相关直接推出。


<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. 若 $x_t,y_t$ 各自 I(1)，但某线性组合 $y_t-\beta x_t$ 为 I(0)，则存在 cointegration。
2. 协整表示长期 equilibrium constraint，即短期可偏离但不能无限漂离。
3. Engle-Granger 适合简单两变量，Johansen 可处理多重协整向量。

### 2. 一条可复用的推理链

回答 **“什么是 Cointegration？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 两个趋势变量回归 R² 高就说协整。
- **边界 2：** 对所有 I(1) 变量先差分，丢失长期关系。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

价格与某成本指数可能长期共同移动，spread 平稳则可能协整。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

协整 rank 决定 VECM 中 error-correction terms 数量。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 多变量与约束 Checklist

- [ ] 先检查 stationarity/cointegration/aggregation constraints
- [ ] 区分预测关系与因果关系
- [ ] 验证跨变量信息在预测时真实可用

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** 多个非平稳序列若存在某线性组合平稳，说明它们共享长期 equilibrium relationship。
>
> **第二层解释机制。** 协整允许“level 非平稳但组合有长期约束”，因此不能简单对所有变量一阶差分后丢掉长期信息。
>
> **第三层补边界。** 这个结论只有在数据生成机制、信息可用性和验证协议匹配时才有意义；我会主动检查本题上面列出的失败模式。
>
> **第四层落到工程。** 最后我会用与生产一致的 rolling backtest、强 baseline 和 horizon/segment 分解指标验证，并记录 point-in-time feature lineage，确保离线提升可以复现到线上。

### 9. 自测：面试前必须能脱口而出的 4 个问题

- **定义题：** 不看笔记，能否用 20 秒给出一句准确答案？
- **推导题：** 能否写出本题最关键公式，并解释每个符号的统计/业务含义？
- **反例题：** 能否给出一个模型表面合理、实际会失败的案例？
- **工程题：** 能否说明如何在不泄漏未来的前提下验证，并给出 fallback？
<!-- V2_DEEP_DIVE_END -->

## 面试表达模板

> **结论：** 多个非平稳序列若存在某线性组合平稳，说明它们共享长期 equilibrium relationship。  
> **原理：** 协整允许“level 非平稳但组合有长期约束”，因此不能简单对所有变量一阶差分后丢掉长期信息。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q080 什么是 Granger Causality？](../07-multivariate-hierarchical-causal/q080-granger-causality.md)
- [Q082 什么是 Spurious Regression？](../07-multivariate-hierarchical-causal/q082-spurious-regression.md)
- [Q083 Error Correction Model 为什么重要？](../07-multivariate-hierarchical-causal/q083-error-correction-model.md)

## 延伸阅读

- [FPP - Hierarchical forecasting](https://otexts.com/fpp3/hierarchical.html)
- [FPP - Forecast reconciliation](https://otexts.com/fpp3/reconciliation.html)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
