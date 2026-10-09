---
id: q069
title: "常见 Data Leakage 有哪些？"
chapter: 6
difficulty: "★★★★★"
frequency: "★★★★★"
tags: ["泄漏", "point-in-time"]
source: "PDF 2026.09"
---

# Q069 常见 Data Leakage 有哪些？

> **章节：** 回测、指标与概率预测  
> **难度：** ★★★★★ ｜ **频率：** ★★★★★  
> **关键词：** 泄漏 / point-in-time

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

常见泄漏：random split、rolling 含目标、全数据 scaler/encoder、future actual covariate、全时期聚合、后验修订数据、未来类别统计、publication delay 未模拟。

## PDF 基线：核心公式 / 结构

$$
Feature(t) must be computable using data available by t
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

高级面试要明确“event time ≠ availability time”。金融、宏观、供应链数据经常晚到或修订，必须维护 point-in-time feature store。

### PDF 易错点

> 只把“用了未来 target”才叫泄漏。

### PDF 高级加分点

> point-in-time correctness 是高级时序工程面试最高频的隐性考点之一。

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

评估是高级时序面试的分水岭。一个没有时间正确性的高分模型，通常比一个朴素但可复现的 baseline 更危险。

- 高级 leakage 包括 feature publication delay、事后修订数据、全局 target encoding、跨实体聚合中的未来值。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. target encoding 怎么防泄漏？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。

### 2. revised macro data 怎么回测？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。


### 4. 工程检查清单

- [ ] 每个 fold 内重新 fit 全部 preprocessing。
- [ ] 指标至少拆成 horizon × segment。
- [ ] 点预测与概率预测使用不同但一致的 scoring rule。


<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. 时序 leakage 可分 target leakage、feature leakage、preprocessing leakage、entity leakage、revision leakage、publication-delay leakage。
2. point-in-time correct join 要求使用 `event_time <= cutoff` 且 `available_time <= cutoff`，两者不是同一列。
3. 未来聚合特征、全量 normalization、后验异常标签、最终修订宏观数据都很危险。

### 2. 一条可复用的推理链

回答 **“常见 Data Leakage 有哪些？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 只检查 feature timestamp，不检查数据真正发布时间。
- **边界 2：** 回测数据库使用当前最新快照重建过去。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

宏观指标 1 月值在 2 月中旬才发布；预测 2 月 1 日时不能使用它，即使 event_date=1 月。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

成熟系统要维护 bitemporal data：event time + knowledge/ingestion time。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 评价协议 Checklist

- [ ] 复刻 production cutoff/retrain cadence
- [ ] 预处理必须 fold-local fit
- [ ] 点预测、概率预测和业务损失分别评价

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 7. 可运行代码 / 伪代码

```text
合法特征条件（概念）：
feature.event_time     <= cutoff
feature.available_time <= cutoff
source_snapshot_time   <= cutoff

任何一个条件不满足，都可能发生 look-ahead。
```

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** 常见泄漏：random split、rolling 含目标、全数据 scaler/encoder、future actual covariate、全时期聚合、后验修订数据、未来类别统计、publication delay 未模拟。
>
> **第二层解释机制。** 高级面试要明确“event time ≠ availability time”。金融、宏观、供应链数据经常晚到或修订，必须维护 point-in-time feature store。
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

> **结论：** 常见泄漏：random split、rolling 含目标、全数据 scaler/encoder、future actual covariate、全时期聚合、后验修订数据、未来类别统计、publication delay 未模拟。  
> **原理：** 高级面试要明确“event time ≠ availability time”。金融、宏观、供应链数据经常晚到或修订，必须维护 point-in-time feature store。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q068 为什么必须按 Forecast Horizon 评估？](../06-evaluation-probabilistic/q068-evaluate-by-horizon.md)
- [Q070 RMSE 和 MAE 有什么区别？](../06-evaluation-probabilistic/q070-rmse-vs-mae.md)
- [Q096 如何 Debug 一个“离线 RMSE 极好，上线完全失效”的 forecasting pipeline？](../09-system-design/q096-debug-offline-good-online-bad.md)

## 延伸阅读

- [FPP - Time series cross-validation](https://otexts.com/fpp3/tscv.html)
- [FPP - Prediction intervals](https://otexts.com/fpp3/prediction-intervals.html)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
