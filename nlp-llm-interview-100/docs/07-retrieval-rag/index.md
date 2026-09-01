# 第 7 章 · 检索、搜索与 RAG

> **章节目标**：从召回、ANN、精排到生成，建立端到端检索系统的质量-延迟-成本模型。

## 1. 先修知识

向量相似度、BM25、基本信息检索指标。

## 2. 本章知识路线

Q075–Q078 检索模型 → Q079–Q080 ANN → Q081–Q084 Chunk/Fusion/Rerank/Eval。

## 3. 必须白板掌握

- Sparse vs Dense
- Bi vs Cross Encoder
- Hard Negative
- HNSW
- IVF-PQ
- Chunking
- RRF
- RAG 分层评估

## 4. 高频失分模式

- Dense 永远胜 BM25
- 只看 reranker 准确率
- ANN 只背名词不讲 recall-latency
- 固定 500 token chunk
- 只用 Judge 评 RAG

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q075 | [Sparse Retrieval 与 Dense Retrieval 的核心差异](Q075-sparse-vs-dense-retrieval.md) | ★★★ | ★★★★★ |
| Q076 | [Bi‑Encoder 与 Cross‑Encoder：为什么一快一准？](Q076-biencoder-vs-crossencoder.md) | ★★★ | ★★★★★ |
| Q077 | [为什么搜索系统通常是多阶段 Retrieval→Rerank？](Q077-multi-stage-retrieval.md) | ★★ | ★★★★★ |
| Q078 | [Dense Retrieval 的负样本怎么构造？](Q078-dense-retrieval-negatives.md) | ★★★★ | ★★★★★ |
| Q079 | [HNSW：为什么多层小世界图能快速 ANN？](Q079-hnsw.md) | ★★★★ | ★★★★ |
| Q080 | [IVF‑PQ：如何用聚类与乘积量化压缩十亿向量？](Q080-ivf-pq.md) | ★★★★ | ★★★★ |
| Q081 | [RAG Chunking：为什么“固定 500 tokens”不是答案？](Q081-rag-chunking.md) | ★★★★ | ★★★★★ |
| Q082 | [Hybrid Search 与 RRF：为什么排名融合常比 raw score 加权稳？](Q082-hybrid-search-rrf.md) | ★★★ | ★★★★★ |
| Q083 | [为什么 Reranker 通常比 Retriever 更准？](Q083-reranker.md) | ★★★ | ★★★★★ |
| Q084 | [如何完整评估一个 RAG 系统？](Q084-rag-evaluation.md) | ★★★★ | ★★★★★ |

## 6. 本章训练方法

1. **第一遍：60 秒回答**——每题只看“标准回答”，建立概念地图。
2. **第二遍：闭卷白板**——公式题必须从定义推导；系统题必须画数据流/资源账本。
3. **第三遍：追问链**——每题至少回答两个“为什么”和一个“不适用条件”。
4. **第四遍：工程化**——写最小代码/复杂度，或者设计一个可验证的实验。
5. **随机复习**——不要按题号形成顺序记忆，使用索引随机抽题。

## 7. 章节完成标准

- [ ] 能不看答案完成本章所有 ★★★★/★★★★★ 题的 2–3 分钟回答。
- [ ] 关键公式能从假设推到结论，而不是只背最终式。
- [ ] 每题至少能说一个边界条件、失败模式或工程 trade-off。
- [ ] 能把相邻题串成连续知识链，而不是 100 个孤立答案。
