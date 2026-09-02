# 第 4 章 · Query Understanding 与 Query Rewrite

> 题目范围：Q031–Q040 · 共 10 题

## 本章目标

### 本章高级视角

Query 模型的收益通常取决于 error taxonomy，而不是模型参数量。先分清 typo、segmentation、entity、intent、attribute extraction、rewrite drift，再给每类设计独立 metric 和 fallback。LLM 引入后，最重要的新问题是可控性、稳定性、成本与 hallucinated constraints。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Query Understanding 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | rewrite gain / drift rate / zero-result / intent accuracy |
| 白板要求 | 给一个歧义 query 完整走 spell→entity→intent→rewrite→recall。 |
| 高频失分 | 默认所有 query 都用 LLM，忽略 drift、cost 和 fallback。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q031 | [Query Understanding 通常包括哪些任务？](Q031-query-understanding-tasks.md) | 3/5 | S |
| Q032 | [中文搜索分词为什么比英文更难？](Q032-chinese-tokenization.md) | 2/5 | A |
| Q033 | [搜索分词是不是越细越好？](Q033-search-tokenization-granularity.md) | 3/5 | A |
| Q034 | [拼写纠错如何设计 Candidate Generation 与 Ranking？](Q034-spelling-correction-candidate-ranking.md) | 4/5 | A |
| Q035 | [“苹果”这样的 Query 为什么难？如何做意图消歧？](Q035-query-intent-disambiguation-apple.md) | 3/5 | A |
| Q036 | [什么是 Query Expansion？为什么会同时提升 Recall 和伤害 Precision？](Q036-query-expansion-recall-precision.md) | 3/5 | A |
| Q037 | [Synonym、Query Rewrite、Query Expansion 有什么区别？](Q037-synonym-rewrite-expansion.md) | 2/5 | A |
| Q038 | [LLM 如何用于 Query Rewrite？](Q038-llm-query-rewrite.md) | 4/5 | A |
| Q039 | [LLM Query Rewrite 最大的风险是什么？](Q039-llm-query-rewrite-risks.md) | 4/5 | S |
| Q040 | [如何设计 Search Autocomplete / Query Suggest？](Q040-search-autocomplete-query-suggest.md) | 4/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
