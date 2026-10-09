---
id: q077
title: "Prediction Interval 怎么评价？"
chapter: 6
difficulty: "★★★★☆"
frequency: "★★★★★"
tags: ["coverage", "sharpness", "校准"]
source: "PDF 2026.09"
---

# Q077 Prediction Interval 怎么评价？

> **章节：** 回测、指标与概率预测  
> **难度：** ★★★★☆ ｜ **频率：** ★★★★★  
> **关键词：** coverage / sharpness / 校准

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

先看 90/95% interval 的 empirical coverage 是否接近 nominal，再看 interval width / sharpness；还应按horizon 和 segment 检查。

## PDF 基线：核心公式 / 结构

$$
Coverage≈nominal; width should be small conditional on calibration
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

区间过宽可轻易获得高 coverage，因此“校准 + 尽可能尖锐”才是目标。可用 interval score、Winkler score 或CRPS 综合。

### PDF 易错点

> 只报平均区间宽度或只报 coverage。

### PDF 高级加分点

> 概率模型应同时检查 calibration 与 sharpness，任何单一维度都可能被投机。

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

评估是高级时序面试的分水岭。一个没有时间正确性的高分模型，通常比一个朴素但可复现的 baseline 更危险。

- 概率预测至少同时看 coverage、sharpness、calibration-by-horizon；单独 coverage 可以被无限宽区间‘作弊’。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. 为什么远期区间应更宽？

**回答方向：** 回答时不要停在现象层。先说明其改变的统计/信息条件，再指出对验证或部署的影响。可结合本题核心：先看 90/95% interval 的 empirical coverage 是否接近 nominal，再看 interval width / sharpness；还应按horizon 和 segment 检查。

### 2. conformal prediction 如何用？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。


### 4. 工程检查清单

- [ ] 每个 fold 内重新 fit 全部 preprocessing。
- [ ] 指标至少拆成 horizon × segment。
- [ ] 点预测与概率预测使用不同但一致的 scoring rule。


## 最小可运行示例

```python
from ts_interview.metrics import interval_coverage, mean_interval_width

coverage = interval_coverage(y_true, lower, upper)
width = mean_interval_width(lower, upper)
```

<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. 区间评价至少包含 empirical coverage 与 width/sharpness；只追 coverage 会鼓励无限宽。
2. 应按 nominal level、horizon、segment 检查 calibration，例如 90% interval 是否长期约覆盖 90%。
3. distribution shift 下历史 calibration 可能失效，需要 conformal recalibration 或在线更新。

### 2. 一条可复用的推理链

回答 **“Prediction Interval 怎么评价？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 把 confidence interval 与 prediction interval 混为一谈。
- **边界 2：** 只汇总全局 coverage，掩盖某些 horizon/segment 极度失准。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

整体 P90 coverage=90%，但新品只有 60%、成熟品 96%，库存风险仍严重。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

区间分数（interval score/Winkler）把 miss penalty 与 width 统一成一个 proper-like objective。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 评价协议 Checklist

- [ ] 复刻 production cutoff/retrain cadence
- [ ] 预处理必须 fold-local fit
- [ ] 点预测、概率预测和业务损失分别评价

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** 先看 90/95% interval 的 empirical coverage 是否接近 nominal，再看 interval width / sharpness；还应按horizon 和 segment 检查。
>
> **第二层解释机制。** 区间过宽可轻易获得高 coverage，因此“校准 + 尽可能尖锐”才是目标。可用 interval score、Winkler score 或CRPS 综合。
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

> **结论：** 先看 90/95% interval 的 empirical coverage 是否接近 nominal，再看 interval width / sharpness；还应按horizon 和 segment 检查。  
> **原理：** 区间过宽可轻易获得高 coverage，因此“校准 + 尽可能尖锐”才是目标。可用 interval score、Winkler score 或CRPS 综合。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q076 CRPS 是什么？](../06-evaluation-probabilistic/q076-crps.md)
- [Q078 如果缺货成本比库存成本高 5 倍，该用什么 loss？](../06-evaluation-probabilistic/q078-asymmetric-business-loss.md)

## 延伸阅读

- [FPP - Time series cross-validation](https://otexts.com/fpp3/tscv.html)
- [FPP - Prediction intervals](https://otexts.com/fpp3/prediction-intervals.html)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
