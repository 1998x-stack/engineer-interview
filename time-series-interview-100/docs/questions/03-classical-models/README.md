# 第 3 章：ARIMA、ETS 与状态空间模型

> AR/MA/ARIMA、SARIMA、ARIMAX、ETS、Kalman 与残差诊断

## 本章学习目标

掌握 Box-Jenkins 不是为了背 p/d/q，而是为了建立‘识别 -> 估计 -> 诊断 -> 回测’的闭环。

## 题目索引

- [Q021 推导 AR(1) 的均值、方差和 ACF。](q021-ar1-derivation.md) - ★★★★☆ / ★★★★★
- [Q022 AR(p) 的平稳条件是什么？](q022-arp-stationarity.md) - ★★★★☆ / ★★★★☆
- [Q023 MA(q) 为什么需要 invertibility？](q023-maq-invertibility.md) - ★★★★☆ / ★★★★☆
- [Q024 AR 和 MA 最大的直觉差异是什么？](q024-ar-vs-ma.md) - ★★☆☆☆ / ★★★★★
- [Q025 解释 ARIMA(p,d,q)。](q025-arima-pdq.md) - ★★★☆☆ / ★★★★★
- [Q026 如何选择 p,d,q？](q026-select-pdq.md) - ★★★★☆ / ★★★★★
- [Q027 SARIMA 是什么？](q027-sarima.md) - ★★★☆☆ / ★★★★★
- [Q028 ARIMAX / SARIMAX 中 X 是什么？](q028-arimax-sarimax.md) - ★★★★☆ / ★★★★★
- [Q029 如何判断 ARIMA 拟合完成？](q029-arima-residual-diagnostics.md) - ★★★★☆ / ★★★★★
- [Q030 AIC、BIC 和 Forecast Accuracy 有什么区别？](q030-aic-bic-vs-forecast-accuracy.md) - ★★★☆☆ / ★★★★★
- [Q031 ETS 是什么？](q031-ets.md) - ★★★☆☆ / ★★★★★
- [Q032 Simple Exponential Smoothing 的递推公式是什么？](q032-simple-exponential-smoothing.md) - ★★☆☆☆ / ★★★★☆
- [Q033 Holt 方法解决了什么问题？](q033-holt-trend.md) - ★★☆☆☆ / ★★★★☆
- [Q034 Holt-Winters 是什么？](q034-holt-winters.md) - ★★★☆☆ / ★★★★★
- [Q035 ARIMA 和 State Space Model 什么关系？](q035-state-space-kalman.md) - ★★★★☆ / ★★★★☆

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- 平稳与差分
- ACF/PACF
- 最大似然/AIC/BIC 基础

### 本章统一答题框架

1. Identification
2. Estimation
3. Residual diagnostics
4. Rolling OOS validation

### 本章综合 Case

> **为一个 5 年月度需求序列设计 ARIMA/ETS 候选集合，并说明何时你会停止继续加阶。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- ARIMA/ETS 至少与 Naive/Seasonal Naive 比较。
- 残差诊断与 rolling backtest 缺一不可。
- 外生变量必须标注未来可用性和发布时间。
