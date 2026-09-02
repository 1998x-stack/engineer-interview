# 第 7 章 · Dense Retrieval 与 ANN

> 题目范围：Q063–Q074 · 共 12 题

## 本章目标

### 本章高级视角

Dense/ANN 要端到端看：encoder、negative mining、vector normalization、ANN、metadata filter、index update、quantization、reranker。离线 embedding cosine 很高不等于线上 retrieval 就好，ANN 与 filtering 常会吞掉模型收益。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Dense Retrieval & ANN 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | exact Recall@K / latency / memory/vector / index age |
| 白板要求 | 写 InfoNCE；算 1B×768 内存；画 HNSW/IVF recall-latency 曲线。 |
| 高频失分 | 只会说“向量语义更好”，不会算 ANN 成本和 hard negative。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q063 | [Dense Retrieval 与 BM25 的本质区别是什么？](Q063-dense-retrieval-vs-bm25.md) | 3/5 | S |
| Q064 | [为什么 Dual Encoder 适合召回？](Q064-dual-encoder-retrieval.md) | 3/5 | S |
| Q065 | [双塔检索模型通常怎么训练？](Q065-dual-encoder-training.md) | 4/5 | S |
| Q066 | [为什么 Hard Negative 对 Dense Retrieval 至关重要？](Q066-hard-negatives.md) | 4/5 | S |
| Q067 | [什么是 In-batch Negative？有什么坑？](Q067-in-batch-negatives.md) | 3/5 | S |
| Q068 | [Cosine、Inner Product、L2 在归一化向量下有什么关系？](Q068-cosine-dot-l2.md) | 3/5 | A |
| Q069 | [为什么十亿向量不能直接暴力扫描？如何算量？](Q069-why-ann-not-bruteforce.md) | 3/5 | S |
| Q070 | [IVF 的原理是什么？nlist 与 nprobe 如何影响效果？](Q070-ivf-index.md) | 4/5 | S |
| Q071 | [Product Quantization（PQ）是什么？](Q071-product-quantization.md) | 5/5 | S |
| Q072 | [HNSW 的原理是什么？为什么分层？](Q072-hnsw-principles.md) | 5/5 | S |
| Q073 | [HNSW 的 M、efConstruction、efSearch 分别控制什么？](Q073-hnsw-parameters.md) | 4/5 | S |
| Q074 | [HNSW 与 IVF-PQ 如何选？](Q074-hnsw-vs-ivf-pq.md) | 5/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
