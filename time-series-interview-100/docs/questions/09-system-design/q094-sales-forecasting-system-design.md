---
id: q094
title: "设计一个完整的销量预测系统。"
chapter: 9
difficulty: "★★★★★"
frequency: "★★★★★"
tags: ["系统设计", "销量", "回测", "部署"]
source: "PDF 2026.09"
---

# Q094 设计一个完整的销量预测系统。

> **章节：** 工业系统设计题  
> **难度：** ★★★★★ ｜ **频率：** ★★★★★  
> **关键词：** 系统设计 / 销量 / 回测 / 部署

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

先澄清预测粒度、horizon、更新频率、库存/补货决策和成本；再定义 point-in-time 数据集，建立 seasonal naive/ETS/GBDT baseline，做 rolling backtest，输出 quantiles，最后接入库存策略和监控。

## PDF 基线：核心公式 / 结构

$$
Objective→Data→Baseline→Backtest→Model→Uncertainty→Decision→Monitoring
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

高级答案会区分 demand 与 observed sales（缺货会 censor demand）、known-future promo、价格计划、商品层级，并设计 champion/challenger 与重训练机制。

### PDF 易错点

> 一上来选 LSTM/TFT，没有业务定义和基线。

### PDF 高级加分点

> 系统设计题的第一句话应是“先确认预测对象、horizon、粒度和决策成本”。

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

系统设计题先定义 decision，再定义 forecast。模型只是其中一层，还要覆盖数据契约、回测、部署、监控、fallback 与成本函数。

- 系统设计题先定义决策变量与成本，再反推预测粒度、horizon、quantile、更新频率和 SLA。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. 目标是销量还是真实需求？

**回答方向：** 围绕本章主线回答：系统设计题先定义 decision，再定义 forecast。模型只是其中一层，还要覆盖数据契约、回测、部署、监控、fallback 与成本函数，并落到假设、验证与工程边界。

### 2. 新品怎么办？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。

### 3. 促销未来可知吗？

**回答方向：** 围绕本章主线回答：系统设计题先定义 decision，再定义 forecast。模型只是其中一层，还要覆盖数据契约、回测、部署、监控、fallback 与成本函数，并落到假设、验证与工程边界。

### 4. 库存约束怎么结合？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。


### 4. 工程检查清单

- [ ] 系统设计必须覆盖数据源、feature availability、training cut-off、model registry、forecast store、monitoring、fallback。
- [ ] 把业务成本映射成 loss/quantile/service level。
- [ ] 离线评估重放线上数据到达顺序。


<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. 系统设计先定义 decision：预测对象、粒度、horizon、retraining cadence、service level 与代价，而不是先选模型。
2. 数据层需明确 event time/available time、库存 censoring、促销计划、价格、日历和外部 covariates。
3. 建模层应有 naive baseline、global model、probabilistic outputs、hierarchical reconciliation 与 fallback。
4. 上线层需 feature pipeline、forecast store、versioning、backfill、monitoring、champion-challenger。

### 2. 一条可复用的推理链

回答 **“设计一个完整的销量预测系统。”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 一开口就是 LSTM/TFT。
- **边界 2：** 只做 accuracy，不说明 forecast 如何驱动补货/排班。
- **边界 3：** 不考虑 stockout 导致观察销量低于真实需求。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

SKU-store 28 天预测，最终可能需要 lead-time P90 而不是逐日均值；这会反过来决定 loss 和 metric。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

Staff 级回答应给 failure budget：数据延迟、模型服务失败、某 SKU 无历史时分别降级到什么 baseline。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 系统设计 Checklist

- [ ] 从 decision objective 反推 forecast target
- [ ] 保证 data lineage 与 point-in-time correctness
- [ ] 设计可降级、可监控、可回放的生产链路

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 7. 可运行代码 / 伪代码

```text
Raw snapshots -> Point-in-time features -> Backtest/Train
              -> Forecast service -> Reconciliation/Quantiles
              -> Forecast store -> Inventory/Planning decision
              -> Monitoring -> Retrain/rollback/fallback
```

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** 先澄清预测粒度、horizon、更新频率、库存/补货决策和成本；再定义 point-in-time 数据集，建立 seasonal naive/ETS/GBDT baseline，做 rolling backtest，输出 quantiles，最后接入库存策略和监控。
>
> **第二层解释机制。** 高级答案会区分 demand 与 observed sales（缺货会 censor demand）、known-future promo、价格计划、商品层级，并设计 champion/challenger 与重训练机制。
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

> **结论：** 先澄清预测粒度、horizon、更新频率、库存/补货决策和成本；再定义 point-in-time 数据集，建立 seasonal naive/ETS/GBDT baseline，做 rolling backtest，输出 quantiles，最后接入库存策略和监控。  
> **原理：** 高级答案会区分 demand 与 observed sales（缺货会 censor demand）、known-future promo、价格计划、商品层级，并设计 champion/challenger 与重训练机制。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q093 生产环境为什么只监控 RMSE 不够？](../08-anomaly-drift/q093-production-monitoring-beyond-rmse.md)
- [Q095 你有 100 万个 SKU-store series，怎么建模？](../09-system-design/q095-million-sku-store-series.md)
- [Q078 如果缺货成本比库存成本高 5 倍，该用什么 loss？](../06-evaluation-probabilistic/q078-asymmetric-business-loss.md)

## 延伸阅读

- [M5 Accuracy competition paper](https://www.sciencedirect.com/science/article/pii/S0169207021001874)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
