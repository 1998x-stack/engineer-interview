# 第 6 章：回测、指标与概率预测

> Rolling CV、Leakage、MASE/RMSSE、Quantile、CRPS、预测区间与业务损失

## 本章学习目标

评估是高级时序面试的分水岭。一个没有时间正确性的高分模型，通常比一个朴素但可复现的 baseline 更危险。

## 题目索引

- [Q066 为什么不能 Random K-Fold？](q066-why-not-random-kfold.md) - ★★★★☆ / ★★★★★
- [Q067 Expanding Window 和 Sliding Window 的区别？](q067-expanding-vs-sliding-window.md) - ★★★☆☆ / ★★★★★
- [Q068 为什么必须按 Forecast Horizon 评估？](q068-evaluate-by-horizon.md) - ★★★★☆ / ★★★★★
- [Q069 常见 Data Leakage 有哪些？](q069-time-series-data-leakage.md) - ★★★★★ / ★★★★★
- [Q070 RMSE 和 MAE 有什么区别？](q070-rmse-vs-mae.md) - ★★★☆☆ / ★★★★★
- [Q071 MAPE 有什么致命问题？](q071-mape-problems.md) - ★★★☆☆ / ★★★★★
- [Q072 sMAPE 真的是完全 symmetric 吗？](q072-smape-caveats.md) - ★★★☆☆ / ★★★★☆
- [Q073 为什么 MASE 很重要？](q073-mase.md) - ★★★★☆ / ★★★★★
- [Q074 RMSSE 是什么？](q074-rmsse.md) - ★★★☆☆ / ★★★★☆
- [Q075 Quantile Loss 如何实现概率预测？](q075-quantile-pinball-loss.md) - ★★★★☆ / ★★★★★
- [Q076 CRPS 是什么？](q076-crps.md) - ★★★★★ / ★★★★☆
- [Q077 Prediction Interval 怎么评价？](q077-prediction-interval-evaluation.md) - ★★★★☆ / ★★★★★
- [Q078 如果缺货成本比库存成本高 5 倍，该用什么 loss？](q078-asymmetric-business-loss.md) - ★★★★★ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- MAE/RMSE 基础
- 时间切分
- 概率分布与分位数

### 本章统一答题框架

1. 先复刻 deployment
2. 再定义 metric 与业务损失
3. 最后做 horizon×segment×calibration 分解

### 本章综合 Case

> **离线 RMSE 提升 10%，但 P90 coverage 从 90% 降到 72%；说明该模型是否应该上线以及还需要哪些证据。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 每个 fold 内重新 fit 全部 preprocessing。
- 指标至少拆成 horizon × segment。
- 点预测与概率预测使用不同但一致的 scoring rule。
