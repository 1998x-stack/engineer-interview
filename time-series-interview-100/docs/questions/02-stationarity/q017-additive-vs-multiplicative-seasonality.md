---
id: q017
title: "Additive Seasonality 和 Multiplicative Seasonality 怎么判断？"
chapter: 2
difficulty: "★★☆☆☆"
frequency: "★★★★☆"
tags: ["加性", "乘性", "季节振幅"]
source: "PDF 2026.09"
---

# Q017 Additive Seasonality 和 Multiplicative Seasonality 怎么判断？

> **章节：** 平稳性、差分、分解与预处理  
> **难度：** ★★☆☆☆ ｜ **频率：** ★★★★☆  
> **关键词：** 加性 / 乘性 / 季节振幅

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

若季节振幅大致不随 level 改变，倾向加性；若 level 越高季节波动越大，倾向乘性。

## PDF 基线：核心公式 / 结构

$$
Additive:y=T+S+R; Multiplicative:y=T×S×R
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

log 变换常把乘性结构转为加性结构。实践中不应只肉眼判断，还应通过残差和 out-of-sample 结果选择。

### PDF 易错点

> 以“增长型序列一定乘性”做机械判断。

### PDF 高级加分点

> （PDF 未给独立高级加分点。）

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

先诊断再变换。所有变换都必须回答两个问题：它改变了什么统计性质？它是否使用了未来信息？

- 从本题继续追问时，优先沿着‘假设 -> 统计直觉 -> 回测 -> 工程约束’展开。
- 先诊断再变换。所有变换都必须回答两个问题：它改变了什么统计性质？它是否使用了未来信息？

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. 零值下 multiplicative 怎么办？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。

### 2. ETS 中 error/trend/seasonal 如何组合？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。


### 4. 工程检查清单

- [ ] 所有拟合型变换（scaler、Box-Cox 参数、插值模型）必须在训练窗内拟合。
- [ ] 同时检查 level、difference、seasonal difference 与 break；不要只看单个单位根检验。
- [ ] 记录变换后的反变换方式以及 bias correction。


<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. 加性季节性适合季节振幅大致固定；乘性季节性适合振幅与 level 成比例。
2. 可通过 seasonal subseries plot 或不同 level 下的 seasonal amplitude 检查，而不是凭肉眼一句话。
3. log transformation 常把乘性 $T_tS_tE_t$ 转成加性 log-space 结构。

### 2. 一条可复用的推理链

回答 **“Additive Seasonality 和 Multiplicative Seasonality 怎么判断？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 看到增长趋势就自动使用 multiplicative。
- **边界 2：** 忽略含零/负值时乘性模型的定义和数值问题。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

航空客流类序列随总体规模增长，旺季与淡季差距也扩大，是经典乘性季节性特征。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

现代 ETS 用 error/trend/seasonality 三组件组合，不应只把 Holt-Winters 简化成“加法或乘法二选一”。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 平稳化决策 Checklist

- [ ] 区分 deterministic vs stochastic trend
- [ ] 选择最小必要差分/变换
- [ ] 检查变换后残差与逆变换偏差

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** 若季节振幅大致不随 level 改变，倾向加性；若 level 越高季节波动越大，倾向乘性。
>
> **第二层解释机制。** log 变换常把乘性结构转为加性结构。实践中不应只肉眼判断，还应通过残差和 out-of-sample 结果选择。
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

> **结论：** 若季节振幅大致不随 level 改变，倾向加性；若 level 越高季节波动越大，倾向乘性。  
> **原理：** log 变换常把乘性结构转为加性结构。实践中不应只肉眼判断，还应通过残差和 out-of-sample 结果选择。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q016 Log / Box-Cox Transformation 为什么有用？](../02-stationarity/q016-log-boxcox-transform.md)
- [Q018 STL 是什么？](../02-stationarity/q018-stl-decomposition.md)

## 延伸阅读

- [FPP - Stationarity and differencing](https://otexts.com/fpp3/stationarity.html)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
