# 第 4 章：机器学习与大规模 Global Forecasting

> Lag/Rolling、GBDT、Global Model、冷启动、间歇需求与集成

## 本章学习目标

机器学习预测的核心不是换模型，而是构造 point-in-time 正确的监督学习样本，并决定 local/global、多步策略与业务 covariates。

## 题目索引

- [Q036 如何把时间序列转换成监督学习问题？](q036-time-series-to-supervised-learning.md) - ★★☆☆☆ / ★★★★★
- [Q037 Lag Features 怎么选择？](q037-lag-feature-selection.md) - ★★★☆☆ / ★★★★★
- [Q038 Rolling Features 最大的 leakage trap 是什么？](q038-rolling-feature-leakage.md) - ★★★★☆ / ★★★★★
- [Q039 Calendar Features 有哪些？](q039-calendar-features.md) - ★★☆☆☆ / ★★★★☆
- [Q040 如何编码周期性时间特征？](q040-cyclical-feature-encoding.md) - ★★☆☆☆ / ★★★★☆
- [Q041 什么是 Known Future Covariate？](q041-known-future-covariates.md) - ★★★☆☆ / ★★★★★
- [Q042 Recursive、Direct、MIMO 多步预测有什么区别？](q042-recursive-direct-mimo.md) - ★★★★☆ / ★★★★★
- [Q043 Random Forest 和 ARIMA 做趋势外推时有什么区别？](q043-random-forest-vs-arima-extrapolation.md) - ★★★★☆ / ★★★★★
- [Q044 LightGBM 做时间序列为什么如此常见？](q044-lightgbm-for-time-series.md) - ★★★☆☆ / ★★★★★
- [Q045 Local Model 和 Global Model 有什么区别？](q045-local-vs-global-model.md) - ★★★★☆ / ★★★★★
- [Q046 Global Model 怎么告诉模型“这是哪个商品”？](q046-series-identity-embedding.md) - ★★☆☆☆ / ★★★★☆
- [Q047 Cold Start 怎么解决？](q047-cold-start.md) - ★★★★☆ / ★★★★★
- [Q048 Intermittent Demand 怎么预测？](q048-intermittent-demand.md) - ★★★★☆ / ★★★★★
- [Q049 Promotion / Cannibalization 怎么建模？](q049-promotion-cannibalization.md) - ★★★★☆ / ★★★★☆
- [Q050 为什么 Ensemble 经常有效？](q050-forecast-ensembles.md) - ★★★☆☆ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- 监督学习与树模型
- 时间正确的切分
- lag/rolling 的 timestamp 语义

### 本章统一答题框架

1. 定义 horizon 和 label
2. 构造 point-in-time features
3. 选择 local/global 与 multi-step strategy
4. 按 segment/horizon 回测

### 本章综合 Case

> **50 万 SKU-store、28 天 horizon、促销提前两周确定：设计一个 LightGBM global baseline 的训练表。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 特征构造统一遵循 point-in-time contract。
- 对每个 horizon 说明 recursive/direct/MIMO 策略。
- Global model 要评估跨实体泛化、cold start 与 scale normalization。
