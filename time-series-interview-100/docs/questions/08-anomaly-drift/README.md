# 第 8 章：异常检测、变化点与漂移

> Point/Contextual/Collective anomaly、change point、concept drift 与线上监控

## 本章学习目标

线上时序系统必须区分偶发异常、永久机制变化和渐进漂移；三者对应的告警、重训和业务动作不同。

## 题目索引

- [Q089 Point、Contextual 和 Collective Anomaly 有何区别？](q089-anomaly-types.md) - ★★★☆☆ / ★★★★☆
- [Q090 如何利用 STL 做异常检测？](q090-stl-anomaly-detection.md) - ★★★☆☆ / ★★★★☆
- [Q091 Change Point Detection 和 Anomaly Detection 有何不同？](q091-change-point-vs-anomaly.md) - ★★★★☆ / ★★★★★
- [Q092 Concept Drift 怎么处理？](q092-concept-drift.md) - ★★★★☆ / ★★★★★
- [Q093 生产环境为什么只监控 RMSE 不够？](q093-production-monitoring-beyond-rmse.md) - ★★★★☆ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- STL/残差
- 分类评估指标
- 线上监控基本概念

### 本章统一答题框架

1. 先定义异常类型和业务后果
2. 再选择 detector/threshold
3. 最后设计持续漂移后的模型动作

### 本章综合 Case

> **某传感器从一次尖峰变成持续偏高：如何让系统从 anomaly alert 转为 change-point/regime handling。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 区分数据质量故障、异常、change point 与 drift。
- 告警应带 severity、segment、horizon 和业务影响。
- 重训不是唯一动作：还可 fallback、缩短窗口、切换 regime model。
