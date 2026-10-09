# 第 7 章：多变量、协整、层级与因果

> VAR、Granger、Cointegration、ECM、Hierarchical Reconciliation 与因果

## 本章学习目标

多变量问题要区分预测相关、长期均衡、层级约束和因果效应，这四类问题经常被错误混用。

## 题目索引

- [Q079 VAR 是什么？](q079-var.md) - ★★★★☆ / ★★★★★
- [Q080 什么是 Granger Causality？](q080-granger-causality.md) - ★★★★☆ / ★★★★★
- [Q081 什么是 Cointegration？](q081-cointegration.md) - ★★★★★ / ★★★★★
- [Q082 什么是 Spurious Regression？](q082-spurious-regression.md) - ★★★★☆ / ★★★★★
- [Q083 Error Correction Model 为什么重要？](q083-error-correction-model.md) - ★★★★★ / ★★★★☆
- [Q084 Cross-correlation 有什么坑？](q084-cross-correlation-caveats.md) - ★★★★☆ / ★★★★☆
- [Q085 什么是 Hierarchical Forecasting？](q085-hierarchical-forecasting.md) - ★★★★☆ / ★★★★★
- [Q086 Bottom-up、Top-down 和 MinT 有什么区别？](q086-bottom-up-top-down-mint.md) - ★★★★★ / ★★★★★
- [Q087 一个序列同时有日、周、年周期怎么办？](q087-multiple-seasonality.md) - ★★★★☆ / ★★★★★
- [Q088 Forecasting 与 Causal Inference 有什么区别？](q088-forecasting-vs-causal-inference.md) - ★★★★★ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- 线性代数与回归
- stationarity/cointegration
- 基本因果识别概念

### 本章统一答题框架

1. 先判断问题是预测、长期均衡、层级一致还是因果
2. 再选择 VAR/VECM/reconciliation/causal method
3. 最后检查约束与可识别性

### 本章综合 Case

> **品牌总销量、区域销量、SKU 销量同时要预测且必须求和一致；解释 base forecast + MinT 的完整流程。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 先确认变量是否平稳/协整再做 VAR/回归。
- 层级系统必须检查 coherence。
- 任何因果结论都需要额外识别假设，不能由预测相关直接推出。
