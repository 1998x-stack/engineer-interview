# 第 10 章 · 综合系统设计与 0→1 方法论

> 题目范围：Q095–Q100 · 共 6 题

## 本章目标

### 本章高级视角

系统设计最终看优先级。最好的答案会先用 oracle/error analysis 找瓶颈，然后选择最低成本的改动，并定义 rollout、guardrail、rollback。不要把“上更大模型”当默认方案。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | System Design 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | quality + SLO + cost + freshness + availability |
| 白板要求 | 先报规模假设，再画 indexing/serving；给容量估算、降级、灰度、回滚。 |
| 高频失分 | 架构图是组件拼图，没有数字、优先级与失败策略。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q095 | [系统设计：从 0 设计一个 Google-like Web Search](Q095-system-design-web-search.md) | 5/5 | S |
| Q096 | [系统设计：淘宝 / Amazon 商品搜索](Q096-system-design-ecommerce-search.md) | 5/5 | S |
| Q097 | [系统设计：亿级 Query Autocomplete](Q097-system-design-query-autocomplete.md) | 5/5 | A |
| Q098 | [系统设计：10 亿文档 Semantic Search](Q098-system-design-billion-vector-search.md) | 5/5 | S |
| Q099 | [系统设计：现代 Hybrid Search Engine](Q099-system-design-hybrid-search.md) | 5/5 | S |
| Q100 | [终极题：如果让你从 0 到 1 提升一个搜索引擎，你会怎么做？](Q100-zero-to-one-search-improvement.md) | 5/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
