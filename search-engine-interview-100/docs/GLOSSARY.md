# 搜索算法术语表

| 术语 | 含义 |
|---|---|
| Recall / Retrieval | 从大规模语料中产生候选集合，核心是不要过早丢失相关结果。 |
| PreRank | 用更便宜的模型把候选进一步压缩，为昂贵 Rank/Rerank 节省预算。 |
| ReRank | 对小规模候选使用更强相关性模型或规则做最终重排。 |
| Posting List | 某个 term 对应的有序文档列表，可附带 TF、position、offset 等。 |
| BM25 | 经典概率相关性词法评分，包含 IDF、TF saturation 与长度归一化。 |
| LTR | Learning to Rank，使用监督数据学习排序函数。 |
| LambdaMART | LambdaRank 风格 ranking lambdas + boosted regression trees。 |
| ANN | Approximate Nearest Neighbor，以少量召回损失换大规模向量搜索速度。 |
| IVF | Inverted File，把向量按 coarse centroid 分桶后只探测少量 buckets。 |
| PQ | Product Quantization，把向量子空间量化为紧凑 code。 |
| HNSW | 多层近邻图 ANN，主要以搜索宽度换 recall/latency。 |
| RRF | Reciprocal Rank Fusion，按 rank 而不是原始 score 融合多个结果列表。 |
| Cross-Encoder | Query 与 Document 联合编码，交互强但计算昂贵，常用于 rerank。 |
| ColBERT | Late Interaction：独立编码 q/d token，再做 MaxSim 聚合。 |
| IPS | Inverse Propensity Scoring，用曝光/观察 propensity 校正有偏反馈。 |
| NDCG | 带 graded gain 与 position discount 的排序质量指标。 |
| Oracle Recall | 假设下游排序完美时，当前候选集合能达到的相关文档覆盖上限。 |
| Query Drift | rewrite/expansion 改变了原始用户意图。 |
| Tail Latency | p95/p99 等高分位延迟，fan-out 搜索系统尤其敏感。 |
