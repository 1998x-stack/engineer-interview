# 第 2 章：平稳性、差分、分解与预处理

> Unit Root、ADF/KPSS、差分、Box-Cox、STL、结构突变与缺失值

## 本章学习目标

先诊断再变换。所有变换都必须回答两个问题：它改变了什么统计性质？它是否使用了未来信息？

## 题目索引

- [Q011 什么是 Unit Root？](q011-unit-root.md) - ★★★☆☆ / ★★★★★
- [Q012 ADF Test 在检验什么？](q012-adf-test.md) - ★★★☆☆ / ★★★★★
- [Q013 ADF 和 KPSS 为什么经常一起使用？](q013-adf-vs-kpss.md) - ★★★☆☆ / ★★★★★
- [Q014 为什么做 Differencing？](q014-differencing.md) - ★★☆☆☆ / ★★★★★
- [Q015 什么是 Over-differencing？](q015-over-differencing.md) - ★★★☆☆ / ★★★★★
- [Q016 Log / Box-Cox Transformation 为什么有用？](q016-log-boxcox-transform.md) - ★★☆☆☆ / ★★★★☆
- [Q017 Additive Seasonality 和 Multiplicative Seasonality 怎么判断？](q017-additive-vs-multiplicative-seasonality.md) - ★★☆☆☆ / ★★★★☆
- [Q018 STL 是什么？](q018-stl-decomposition.md) - ★★★☆☆ / ★★★★☆
- [Q019 Structural Break 会对模型造成什么影响？](q019-structural-break.md) - ★★★★☆ / ★★★★★
- [Q020 处理缺失值为什么会产生时间泄漏？](q020-missing-value-leakage.md) - ★★★★☆ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- Q001-Q010 的平稳/ACF 基础
- 随机游走与单位根直觉
- 基本假设检验语言

### 本章统一答题框架

1. 区分 deterministic/stochastic trend
2. 用互补检验和图形诊断
3. 选择最小必要变换并保留逆变换路径

### 本章综合 Case

> **同一序列 ADF 不拒绝、KPSS 拒绝，且中间有一次明显政策冲击：说明你如何区分单位根、结构突变与 near-unit-root。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 所有拟合型变换（scaler、Box-Cox 参数、插值模型）必须在训练窗内拟合。
- 同时检查 level、difference、seasonal difference 与 break；不要只看单个单位根检验。
- 记录变换后的反变换方式以及 bias correction。
