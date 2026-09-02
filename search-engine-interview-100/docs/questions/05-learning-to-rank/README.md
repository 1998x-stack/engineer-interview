# 第 5 章 · Learning to Rank：从 RankNet 到 LambdaMART

> 题目范围：Q041–Q052 · 共 12 题

## 本章目标

### 本章高级视角

LTR 的核心资产是数据集与 feature semantics。模型只是最后一层。需要特别警惕展示位置、未来信息、query leakage、重复样本和 label policy 漂移；否则越强的 ranker 越会拟合系统偏差。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Learning to Rank 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | NDCG / feature drift / latency / calibration |
| 白板要求 | 手写 RankNet/LambdaRank 直觉；解释 LambdaMART 与 feature leakage。 |
| 高频失分 | 只背 point/pair/list 名词，不懂 label bias 和 train-serving skew。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q041 | [为什么需要 Learning to Rank？BM25 不够吗？](Q041-why-learning-to-rank.md) | 3/5 | S |
| Q042 | [Pointwise Ranking 是什么？优缺点？](Q042-pointwise-ranking.md) | 2/5 | S |
| Q043 | [Pairwise Ranking 是什么？](Q043-pairwise-ranking.md) | 3/5 | S |
| Q044 | [Listwise Ranking 是什么？为什么更贴近 NDCG？](Q044-listwise-ranking.md) | 4/5 | A |
| Q045 | [RankNet 的核心公式和直觉是什么？](Q045-ranknet.md) | 4/5 | A |
| Q046 | [LambdaRank 为什么出现？Lambda 到底是什么？](Q046-lambdarank.md) | 5/5 | S |
| Q047 | [LambdaMART 是什么？为什么经典？](Q047-lambdamart.md) | 5/5 | S |
| Q048 | [深度学习时代，为什么 LambdaMART 仍然常见？](Q048-why-lambdamart-still-used.md) | 3/5 | S |
| Q049 | [搜索 Ranker 常见特征有哪些？如何分类？](Q049-search-ranker-features.md) | 3/5 | S |
| Q050 | [什么是 Query-independent Feature？为什么有价值？](Q050-query-independent-features.md) | 2/5 | A |
| Q051 | [搜索排序中的 Feature Leakage 是什么？](Q051-feature-leakage.md) | 4/5 | S |
| Q052 | [Ranker 为什么有时需要 Calibration？](Q052-ranker-calibration.md) | 4/5 | A |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
