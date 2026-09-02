# 第 8 章 · Hybrid Search、Neural Reranking 与 RAG

> 题目范围：Q075–Q084 · 共 10 题

## 本章目标

### 本章高级视角

Hybrid 不是 `BM25 + vector` 两个 API 调用。高质量系统需要 query routing、candidate budget、fusion、dedup、rerank、context packing 与 fallback。RAG 还应追加 answer-level evaluation，避免只优化 retrieval 指标而生成质量不升。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Hybrid & RAG 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | source recall / union oracle / rerank NDCG / context precision / answer quality |
| 白板要求 | 手写 RRF；做 retrieval→fusion→rerank→context→generation 的 stage-wise oracle。 |
| 高频失分 | 把 RAG 错误全部归因于 retriever，或直接相加 BM25/cosine。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q075 | [为什么 Hybrid Search 往往比纯 BM25 或纯 Dense 更稳？](Q075-why-hybrid-search.md) | 3/5 | S |
| Q076 | [BM25 Score 与 Dense Cosine 能直接相加吗？](Q076-bm25-dense-score-fusion.md) | 3/5 | S |
| Q077 | [什么是 Reciprocal Rank Fusion（RRF）？](Q077-reciprocal-rank-fusion.md) | 3/5 | S |
| Q078 | [SPLADE 这类 Learned Sparse Retrieval 在做什么？](Q078-splade-sparse-neural-retrieval.md) | 5/5 | A |
| Q079 | [为什么 Cross-Encoder 适合 Rerank，而不适合全库召回？](Q079-cross-encoder-reranking.md) | 3/5 | S |
| Q080 | [Dual Encoder 与 Cross-Encoder 的经典 Trade-off 是什么？](Q080-dual-vs-cross-encoder.md) | 2/5 | S |
| Q081 | [ColBERT 的 Late Interaction 为什么重要？](Q081-colbert-late-interaction.md) | 5/5 | A |
| Q082 | [RAG 的 Chunk Size 应该怎么选？](Q082-rag-chunk-size.md) | 4/5 | S |
| Q083 | [Retrieval Recall 很高，为什么 RAG 仍会答错？](Q083-high-recall-rag-still-wrong.md) | 4/5 | S |
| Q084 | [什么是 Agentic / Iterative Search？](Q084-agentic-search.md) | 5/5 | A |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
