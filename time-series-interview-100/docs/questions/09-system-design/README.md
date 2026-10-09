# 第 9 章：工业系统设计题

> 销量预测系统、百万序列、离线好线上差的系统化诊断

## 本章学习目标

系统设计题先定义 decision，再定义 forecast。模型只是其中一层，还要覆盖数据契约、回测、部署、监控、fallback 与成本函数。

## 题目索引

- [Q094 设计一个完整的销量预测系统。](q094-sales-forecasting-system-design.md) - ★★★★★ / ★★★★★
- [Q095 你有 100 万个 SKU-store series，怎么建模？](q095-million-sku-store-series.md) - ★★★★★ / ★★★★★
- [Q096 如何 Debug 一个“离线 RMSE 极好，上线完全失效”的 forecasting pipeline？](q096-debug-offline-good-online-bad.md) - ★★★★★ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- 前 8 章核心概念
- 基本 ML platform / feature store / model registry
- 业务损失与 SLA

### 本章统一答题框架

1. Decision → Target → Data contract → Backtest → Model → Serving → Monitoring → Fallback

### 本章综合 Case

> **从零设计一个日级补货预测平台：要求支持百万序列、概率输出、节假日、促销、冷启动和模型回滚。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 系统设计必须覆盖数据源、feature availability、training cut-off、model registry、forecast store、monitoring、fallback。
- 把业务成本映射成 loss/quantile/service level。
- 离线评估重放线上数据到达顺序。
