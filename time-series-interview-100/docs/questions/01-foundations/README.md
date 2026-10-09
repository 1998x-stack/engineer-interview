# 第 1 章：时间序列基础与统计直觉

> IID、时间依赖、趋势/季节/周期、ACF/PACF 与随机过程

## 本章学习目标

把时间序列从“带时间戳的表格”提升为“带有信息集约束的随机过程”。重点是依赖、非平稳和信息可用性。

## 题目索引

- [Q001 什么是时间序列？它与普通 IID 数据最大的区别是什么？](q001-time-series-vs-iid.md) - ★★★☆☆ / ★★★★★
- [Q002 Trend、Seasonality、Cycle 有什么区别？](q002-trend-seasonality-cycle.md) - ★★☆☆☆ / ★★★★☆
- [Q003 White Noise 和 Random Walk 有什么区别？](q003-white-noise-vs-random-walk.md) - ★★★☆☆ / ★★★★★
- [Q004 什么是 Autocorrelation？](q004-autocorrelation.md) - ★★☆☆☆ / ★★★★☆
- [Q005 ACF 和 PACF 有什么区别？](q005-acf-vs-pacf.md) - ★★★☆☆ / ★★★★★
- [Q006 什么是 Lag Operator / Backshift Operator？](q006-lag-operator.md) - ★★☆☆☆ / ★★★☆☆
- [Q007 什么叫平稳？](q007-stationarity.md) - ★★★☆☆ / ★★★★★
- [Q008 Strict Stationarity 和 Weak Stationarity 有什么区别？](q008-strict-vs-weak-stationarity.md) - ★★★☆☆ / ★★★★☆
- [Q009 为什么采样频率非常重要？](q009-sampling-frequency.md) - ★★☆☆☆ / ★★★★☆
- [Q010 不规则时间序列怎么处理？](q010-irregular-time-series.md) - ★★★☆☆ / ★★★★☆

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- 概率与期望/方差/协方差
- 线性回归基本概念
- 能够区分观测时间与数据可用时间

### 本章统一答题框架

1. 先定义时间索引、频率和信息集
2. 再识别趋势/季节/依赖
3. 最后把统计性质映射到 split、feature 和 baseline

### 本章综合 Case

> **给一份两年的日销量，先不要建模：说明你会如何判断是否存在周季节、年季节、趋势、结构突变和异常，并给出最小 baseline。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 明确预测时点 $t$ 与可用信息集 $\mathcal{I}_t$。
- 绘制原序列、差分序列、ACF/PACF，并先做 Seasonal Naive baseline。
- 不要在做任何统计变换前破坏时间顺序。
