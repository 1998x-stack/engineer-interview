# 第 5 章｜流水线、预测与乱序执行

> **本章目标**：现代高性能 CPU 的目标不是让单条指令“神奇地更快”，而是在保持架构语义的前提下同时容纳更多 in-flight work，挖掘 ILP 并隐藏长延迟。

## 能力阶梯

| 层级 | 你应该做到什么 |
|---|---|
| L1 定义 | 30 秒说清术语和目标 |
| L2 机制 | 能画出最小硬件/执行链 |
| L3 定量 | 能用公式、数量级或 PMU 指标分析 |
| L4 边界 | 能指出架构保证与微架构差异 |
| L5 工程 | 能设计 benchmark / profiling 验证假设 |

## 本章核心指标

关注 IPC、backend/frontend stall、branch-miss、ROB/RS/LSQ occupancy、依赖链与执行端口利用率。

```mermaid
flowchart LR
F[Fetch] --> D[Decode]
D --> R[Rename]
R --> Q[Dispatch/Issue]
Q --> E[Execute]
E --> C[Complete]
C --> ROB[ROB]
ROB --> T[In-order Retire]
B[Branch Predictor] --> F
```

## 题目索引

| 题号 | 题目 | 难度 | 频率 | PDF 页 |
|---|---|---|---|---:|
| [Q041](q041-question.md) | 流水线冒险有哪些类型？ | ★★★★★ | 必考 | 52 |
| [Q042](q042-raw-war-waw.md) | RAW、WAR、WAW 分别是什么？哪些是真依赖？ | ★★★★★ | 必考 | 53 |
| [Q043](q043-forwarding-bypassing.md) | Forwarding/Bypassing 如何减少流水线停顿？ | ★★★★★ | 必考 | 54 |
| [Q044](q044-load-use-hazard.md) | Load-Use Hazard 为何特别难处理？ | ★★★★★ | 高频 | 55 |
| [Q045](q045-control-hazard.md) | 分支为什么会造成 Control Hazard？ | ★★★★★ | 必考 | 56 |
| [Q046](q046-question.md) | 分支预测器通常预测哪些东西？ | ★★★★★ | 高频 | 57 |
| [Q047](q047-question.md) | 分支预测失败为何代价高？ | ★★★★★ | 必考 | 58 |
| [Q048](q048-out-of-order-execution.md) | 什么是乱序执行（Out-of-Order Execution）？ | ★★★★★ | 必考 | 59 |
| [Q049](q049-register-renaming-war-waw.md) | Register Renaming 为何能消除 WAR/WAW？ | ★★★★★ | 必考 | 60 |
| [Q050](q050-rob-reorder-buffer.md) | ROB（Reorder Buffer）的核心作用是什么？ | ★★★★★ | 必考 | 61 |

## 学习要求

建议每题完成三轮：

1. **30 秒**：只答结论、机制、边界；
2. **2 分钟**：加入一个公式/最小例子；
3. **5 分钟**：加入架构差异、工程指标与反例。

完成本章后，不应只“认识名词”，而应能把 10 道题连接成一条因果链。
