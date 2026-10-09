---
id: q041
title: "什么是 Known Future Covariate？"
chapter: 4
difficulty: "★★★☆☆"
frequency: "★★★★★"
tags: ["协变量", "未来可用性"]
source: "PDF 2026.09"
---

# Q041 什么是 Known Future Covariate？

> **章节：** 机器学习与大规模 Global Forecasting  
> **难度：** ★★★☆☆ ｜ **频率：** ★★★★★  
> **关键词：** 协变量 / 未来可用性

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

known-future 是预测时已经确定的未来变量，如日历、既定促销、计划价格；observed-past 只能看到历史。

## PDF 基线：核心公式 / 结构

$$
x_{t+h} known at forecast origin
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

这是 TFT、Chronos-2、现代 global forecasting 的核心数据契约。错误标记 covariate availability 会直接导致线上崩溃。

### PDF 易错点

> 验证阶段用未来真实值代替当时可获得的预测值。

### PDF 高级加分点

> （PDF 未给独立高级加分点。）

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

机器学习预测的核心不是换模型，而是构造 point-in-time 正确的监督学习样本，并决定 local/global、多步策略与业务 covariates。

- Known-future 是由业务流程保证可见，不是‘模型可以预测到’。天气预报和真实未来天气应区分。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. 天气预报算 known future 吗？

**回答方向：** 围绕本章主线回答：机器学习预测的核心不是换模型，而是构造 point-in-time 正确的监督学习样本，并决定 local/global、多步策略与业务 covariates，并落到假设、验证与工程边界。

### 2. 计划价格临时变更怎么办？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。


### 4. 工程检查清单

- [ ] 特征构造统一遵循 point-in-time contract。
- [ ] 对每个 horizon 说明 recursive/direct/MIMO 策略。
- [ ] Global model 要评估跨实体泛化、cold start 与 scale normalization。


<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. Known future covariate 是在 forecast origin 时就能确定整个未来 horizon 的变量。
2. 要区分 known future、observed past-only、static covariate 和 forecasted future covariate。
3. 模型接口支持 future covariates 不代表业务数据真的可用，必须有 availability contract。

### 2. 一条可复用的推理链

回答 **“什么是 Known Future Covariate？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 把未来真实天气/未来实际价格当 known future。
- **边界 2：** 回测使用最终修订后的计划值，而生产时只能看到早期版本。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

节假日和已排期促销一般 known future；实际温度不是，但天气预报可以作为 forecasted covariate。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

对计划变量还要建 scenario risk：促销排期可能临时变更，模型应支持 what-if 或 fallback。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 监督学习流水线 Checklist

- [ ] 构造 point-in-time correct features
- [ ] 明确 future covariate availability
- [ ] 按 horizon/segment 做滚动回测

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** known-future 是预测时已经确定的未来变量，如日历、既定促销、计划价格；observed-past 只能看到历史。
>
> **第二层解释机制。** 这是 TFT、Chronos-2、现代 global forecasting 的核心数据契约。错误标记 covariate availability 会直接导致线上崩溃。
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

> **结论：** known-future 是预测时已经确定的未来变量，如日历、既定促销、计划价格；observed-past 只能看到历史。  
> **原理：** 这是 TFT、Chronos-2、现代 global forecasting 的核心数据契约。错误标记 covariate availability 会直接导致线上崩溃。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q040 如何编码周期性时间特征？](../04-machine-learning/q040-cyclical-feature-encoding.md)
- [Q042 Recursive、Direct、MIMO 多步预测有什么区别？](../04-machine-learning/q042-recursive-direct-mimo.md)

## 延伸阅读

- [M5 Accuracy competition paper](https://www.sciencedirect.com/science/article/pii/S0169207021001874)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
