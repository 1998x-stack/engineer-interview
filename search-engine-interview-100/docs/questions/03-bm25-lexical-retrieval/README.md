# 第 3 章 · TF-IDF、BM25 与词法检索

> 题目范围：Q021–Q030 · 共 10 题

## 本章目标

### 本章高级视角

词法检索不是“过时 baseline”。它提供稀有词、实体、标识符和精确短语的强证据，也是 hybrid search 的稳定锚点。生产优化时应把 analyzer、fielding、boost、BM25 参数、query rewrite 与 retrieval depth 当成一个整体，而不是只调 `k1/b`。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Lexical Retrieval 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | NDCG / exact-match recall / postings visited |
| 白板要求 | 从 TF-IDF 推到 BM25；画 TF saturation；解释 k1/b 和 multi-field。 |
| 高频失分 | 只背 BM25 公式，不会做极限检查或 failure taxonomy。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q021 | [TF-IDF 的核心直觉是什么？](Q021-tf-idf-intuition.md) | 2/5 | S |
| Q022 | [为什么 IDF 能衡量一个词的“辨识度”？](Q022-idf-discriminativeness.md) | 2/5 | A |
| Q023 | [TF-IDF 的主要问题是什么？](Q023-tf-idf-limitations.md) | 3/5 | S |
| Q024 | [写出 BM25，并解释每一项的意义](Q024-bm25-formula.md) | 4/5 | S |
| Q025 | [BM25 相比 TF-IDF 到底改进了什么？](Q025-bm25-vs-tf-idf.md) | 3/5 | S |
| Q026 | [BM25 中 k1 控制什么？如何调？](Q026-bm25-k1.md) | 3/5 | A |
| Q027 | [BM25 中 b 控制什么？如何理解 b=0 和 b=1？](Q027-bm25-b.md) | 3/5 | A |
| Q028 | [Title 和 Body 应该如何联合打分？什么是 BM25F 思想？](Q028-bm25f-title-body.md) | 4/5 | A |
| Q029 | [BM25 会在哪些场景失败？](Q029-bm25-failure-modes.md) | 3/5 | S |
| Q030 | [为什么 BM25 在 2026 年仍然非常强？](Q030-why-bm25-still-strong.md) | 3/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
