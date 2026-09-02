# 第 1 章 · 搜索引擎全局架构

> 题目范围：Q001–Q010 · 共 10 题

## 本章目标

### 本章高级视角

搜索架构题最容易被“组件罗列”拖成低分。高级回答要说明 **stage contract**：每层输入/输出候选规模、质量下界、延迟预算、失败 fallback 和观测指标。一个成熟系统还要把 index/model/feature schema 都做版本化，确保 query serving 使用兼容版本。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Search Architecture 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | Recall@K / NDCG / p99 / zero-result |
| 白板要求 | 画端到端 serving + indexing + feedback loop；给每阶段候选规模与 latency budget。 |
| 高频失分 | 只列组件，不说明候选规模、SLO 和 feedback loop。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q001 | [完整讲一下搜索引擎的端到端 Pipeline](Q001-search-engine-end-to-end-pipeline.md) | 3/5 | S |
| Q002 | [搜索系统与推荐系统的本质区别是什么？](Q002-search-vs-recommendation.md) | 2/5 | A |
| Q003 | [为什么搜索一定要有候选召回阶段？](Q003-why-candidate-retrieval.md) | 3/5 | S |
| Q004 | [召回、粗排、精排、重排分别优化什么？](Q004-recall-prerank-rank-rerank.md) | 3/5 | S |
| Q005 | [为什么不能用数据库 LIKE 代替搜索引擎？](Q005-database-like-vs-search.md) | 2/5 | A |
| Q006 | [一次搜索请求从键盘到 SERP 发生了什么？](Q006-query-to-serp-request-lifecycle.md) | 3/5 | A |
| Q007 | [为什么现代搜索几乎都是 Multi-stage Ranking？](Q007-why-multi-stage-ranking.md) | 3/5 | S |
| Q008 | [搜索系统的目标函数为什么是多目标的？](Q008-multi-objective-search-ranking.md) | 4/5 | A |
| Q009 | [为什么搜索结果不能直接按 CTR 排？](Q009-why-not-rank-by-ctr.md) | 4/5 | S |
| Q010 | [传统 Search 与 RAG Retrieval 的目标有什么不同？](Q010-search-vs-rag-retrieval.md) | 4/5 | A |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
