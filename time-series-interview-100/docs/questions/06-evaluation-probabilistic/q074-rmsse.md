---
id: q074
title: "RMSSE 是什么？"
chapter: 6
difficulty: "★★★☆☆"
frequency: "★★★★☆"
tags: ["RMSSE", "M5", "scaled error"]
source: "PDF 2026.09"
---

# Q074 RMSSE 是什么？

> **章节：** 回测、指标与概率预测  
> **难度：** ★★★☆☆ ｜ **频率：** ★★★★☆  
> **关键词：** RMSSE / M5 / scaled error

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

RMSSE 是 squared-error 版本的 scaled metric，保持跨序列可比性并对大误差更敏感。

## PDF 基线：核心公式 / 结构

$$
RMSSE=sqrt(MSE_model / MSE_naive_scale)
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

M5 使用 WRMSSE 将层级不同节点按业务销售权重聚合，体现“metric 要反映业务价值”。

### PDF 易错点

> 只记缩写，不理解 scaling denominator。

### PDF 高级加分点

> （PDF 未给独立高级加分点。）

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

评估是高级时序面试的分水岭。一个没有时间正确性的高分模型，通常比一个朴素但可复现的 baseline 更危险。

- 从本题继续追问时，优先沿着‘假设 -> 统计直觉 -> 回测 -> 工程约束’展开。
- 评估是高级时序面试的分水岭。一个没有时间正确性的高分模型，通常比一个朴素但可复现的 baseline 更危险。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. WRMSSE 权重来自什么？

**回答方向：** 围绕本章主线回答：评估是高级时序面试的分水岭。一个没有时间正确性的高分模型，通常比一个朴素但可复现的 baseline 更危险，并落到假设、验证与工程边界。

### 2. 为什么不是 MAPE？

**回答方向：** 回答时不要停在现象层。先说明其改变的统计/信息条件，再指出对验证或部署的影响。可结合本题核心：RMSSE 是 squared-error 版本的 scaled metric，保持跨序列可比性并对大误差更敏感。


### 4. 工程检查清单

- [ ] 每个 fold 内重新 fit 全部 preprocessing。
- [ ] 指标至少拆成 horizon × segment。
- [ ] 点预测与概率预测使用不同但一致的 scoring rule。


## 最小可运行示例

```python
from ts_interview.metrics import rmsse

score = rmsse(y_true, y_pred, y_train, seasonality=7)
```

<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. RMSSE 是 squared-error 版本的 scaled metric，分子测测试 RMSE，分母来自训练期 naive difference 的平方平均。
2. 它对大误差更敏感，并适合跨不同 scale series 聚合。
3. M5 的 WRMSSE 进一步按 hierarchy 和销售价值加权。

### 2. 一条可复用的推理链

回答 **“RMSSE 是什么？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 把 RMSSE denominator 用测试集计算，造成泄漏。
- **边界 2：** 忽略 aggregation weights 使高价值节点与低价值节点同权。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

零售层级中 top-level、store、SKU 各层都可算 RMSSE，再按业务权重聚合。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

对层级预测，metric 本身定义了“哪些层更重要”，模型选择要与该权重保持一致。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 评价协议 Checklist

- [ ] 复刻 production cutoff/retrain cadence
- [ ] 预处理必须 fold-local fit
- [ ] 点预测、概率预测和业务损失分别评价

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** RMSSE 是 squared-error 版本的 scaled metric，保持跨序列可比性并对大误差更敏感。
>
> **第二层解释机制。** M5 使用 WRMSSE 将层级不同节点按业务销售权重聚合，体现“metric 要反映业务价值”。
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

> **结论：** RMSSE 是 squared-error 版本的 scaled metric，保持跨序列可比性并对大误差更敏感。  
> **原理：** M5 使用 WRMSSE 将层级不同节点按业务销售权重聚合，体现“metric 要反映业务价值”。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q073 为什么 MASE 很重要？](../06-evaluation-probabilistic/q073-mase.md)
- [Q075 Quantile Loss 如何实现概率预测？](../06-evaluation-probabilistic/q075-quantile-pinball-loss.md)

## 延伸阅读

- [FPP - Time series cross-validation](https://otexts.com/fpp3/tscv.html)
- [FPP - Prediction intervals](https://otexts.com/fpp3/prediction-intervals.html)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
