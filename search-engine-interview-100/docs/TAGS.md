# 标签索引

## `ab-testing`

- [Q053 · Precision@K 与 Recall@K 分别衡量什么？](questions/06-evaluation-click-ab/Q053-precision-recall-at-k.md)
- [Q054 · MRR 是什么？适合什么场景？](questions/06-evaluation-click-ab/Q054-mrr.md)
- [Q055 · MAP 是什么？与 MRR 有何不同？](questions/06-evaluation-click-ab/Q055-map-average-precision.md)
- [Q056 · NDCG 是什么？为什么是搜索面试必考？](questions/06-evaluation-click-ab/Q056-ndcg.md)
- [Q057 · 为什么 NDCG 比 Accuracy 更适合 Search？](questions/06-evaluation-click-ab/Q057-why-ndcg-not-accuracy.md)
- [Q058 · Recall@1000 提升但 NDCG@10 下降，怎么解释？](questions/06-evaluation-click-ab/Q058-recall-up-ndcg-down.md)
- [Q059 · 为什么 Click 不能直接当 Relevance Label？](questions/06-evaluation-click-ab/Q059-clicks-vs-relevance-labels.md)
- [Q060 · 如何处理 Position Bias？什么是 IPS？](questions/06-evaluation-click-ab/Q060-position-bias-ips.md)
- [Q061 · Offline 指标涨了，Online CTR/满意度为什么可能下降？](questions/06-evaluation-click-ab/Q061-offline-up-online-down.md)
- [Q062 · 搜索 A/B Test 应如何设计？](questions/06-evaluation-click-ab/Q062-search-ab-testing.md)

## `agentic-search`

- [Q084 · 什么是 Agentic / Iterative Search？](questions/08-hybrid-rag-rerank/Q084-agentic-search.md)

## `ann`

- [Q063 · Dense Retrieval 与 BM25 的本质区别是什么？](questions/07-dense-retrieval-ann/Q063-dense-retrieval-vs-bm25.md)
- [Q064 · 为什么 Dual Encoder 适合召回？](questions/07-dense-retrieval-ann/Q064-dual-encoder-retrieval.md)
- [Q065 · 双塔检索模型通常怎么训练？](questions/07-dense-retrieval-ann/Q065-dual-encoder-training.md)
- [Q066 · 为什么 Hard Negative 对 Dense Retrieval 至关重要？](questions/07-dense-retrieval-ann/Q066-hard-negatives.md)
- [Q067 · 什么是 In-batch Negative？有什么坑？](questions/07-dense-retrieval-ann/Q067-in-batch-negatives.md)
- [Q068 · Cosine、Inner Product、L2 在归一化向量下有什么关系？](questions/07-dense-retrieval-ann/Q068-cosine-dot-l2.md)
- [Q069 · 为什么十亿向量不能直接暴力扫描？如何算量？](questions/07-dense-retrieval-ann/Q069-why-ann-not-bruteforce.md)
- [Q070 · IVF 的原理是什么？nlist 与 nprobe 如何影响效果？](questions/07-dense-retrieval-ann/Q070-ivf-index.md)
- [Q071 · Product Quantization（PQ）是什么？](questions/07-dense-retrieval-ann/Q071-product-quantization.md)
- [Q072 · HNSW 的原理是什么？为什么分层？](questions/07-dense-retrieval-ann/Q072-hnsw-principles.md)
- [Q073 · HNSW 的 M、efConstruction、efSearch 分别控制什么？](questions/07-dense-retrieval-ann/Q073-hnsw-parameters.md)
- [Q074 · HNSW 与 IVF-PQ 如何选？](questions/07-dense-retrieval-ann/Q074-hnsw-vs-ivf-pq.md)

## `autocomplete`

- [Q018 · Trie 为什么适合做 Search Autocomplete？](questions/02-inverted-index-lucene/Q018-trie-autocomplete.md)
- [Q040 · 如何设计 Search Autocomplete / Query Suggest？](questions/04-query-understanding/Q040-search-autocomplete-query-suggest.md)
- [Q097 · 系统设计：亿级 Query Autocomplete](questions/10-system-design/Q097-system-design-query-autocomplete.md)

## `bm25`

- [Q021 · TF-IDF 的核心直觉是什么？](questions/03-bm25-lexical-retrieval/Q021-tf-idf-intuition.md)
- [Q022 · 为什么 IDF 能衡量一个词的“辨识度”？](questions/03-bm25-lexical-retrieval/Q022-idf-discriminativeness.md)
- [Q023 · TF-IDF 的主要问题是什么？](questions/03-bm25-lexical-retrieval/Q023-tf-idf-limitations.md)
- [Q024 · 写出 BM25，并解释每一项的意义](questions/03-bm25-lexical-retrieval/Q024-bm25-formula.md)
- [Q025 · BM25 相比 TF-IDF 到底改进了什么？](questions/03-bm25-lexical-retrieval/Q025-bm25-vs-tf-idf.md)
- [Q026 · BM25 中 k1 控制什么？如何调？](questions/03-bm25-lexical-retrieval/Q026-bm25-k1.md)
- [Q027 · BM25 中 b 控制什么？如何理解 b=0 和 b=1？](questions/03-bm25-lexical-retrieval/Q027-bm25-b.md)
- [Q028 · Title 和 Body 应该如何联合打分？什么是 BM25F 思想？](questions/03-bm25-lexical-retrieval/Q028-bm25f-title-body.md)
- [Q029 · BM25 会在哪些场景失败？](questions/03-bm25-lexical-retrieval/Q029-bm25-failure-modes.md)
- [Q030 · 为什么 BM25 在 2026 年仍然非常强？](questions/03-bm25-lexical-retrieval/Q030-why-bm25-still-strong.md)
- [Q041 · 为什么需要 Learning to Rank？BM25 不够吗？](questions/05-learning-to-rank/Q041-why-learning-to-rank.md)
- [Q063 · Dense Retrieval 与 BM25 的本质区别是什么？](questions/07-dense-retrieval-ann/Q063-dense-retrieval-vs-bm25.md)
- [Q075 · 为什么 Hybrid Search 往往比纯 BM25 或纯 Dense 更稳？](questions/08-hybrid-rag-rerank/Q075-why-hybrid-search.md)
- [Q076 · BM25 Score 与 Dense Cosine 能直接相加吗？](questions/08-hybrid-rag-rerank/Q076-bm25-dense-score-fusion.md)

## `cache`

- [Q093 · 搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？](questions/09-search-infrastructure/Q093-search-caching.md)

## `click-bias`

- [Q053 · Precision@K 与 Recall@K 分别衡量什么？](questions/06-evaluation-click-ab/Q053-precision-recall-at-k.md)
- [Q054 · MRR 是什么？适合什么场景？](questions/06-evaluation-click-ab/Q054-mrr.md)
- [Q055 · MAP 是什么？与 MRR 有何不同？](questions/06-evaluation-click-ab/Q055-map-average-precision.md)
- [Q056 · NDCG 是什么？为什么是搜索面试必考？](questions/06-evaluation-click-ab/Q056-ndcg.md)
- [Q057 · 为什么 NDCG 比 Accuracy 更适合 Search？](questions/06-evaluation-click-ab/Q057-why-ndcg-not-accuracy.md)
- [Q058 · Recall@1000 提升但 NDCG@10 下降，怎么解释？](questions/06-evaluation-click-ab/Q058-recall-up-ndcg-down.md)
- [Q059 · 为什么 Click 不能直接当 Relevance Label？](questions/06-evaluation-click-ab/Q059-clicks-vs-relevance-labels.md)
- [Q060 · 如何处理 Position Bias？什么是 IPS？](questions/06-evaluation-click-ab/Q060-position-bias-ips.md)
- [Q061 · Offline 指标涨了，Online CTR/满意度为什么可能下降？](questions/06-evaluation-click-ab/Q061-offline-up-online-down.md)
- [Q062 · 搜索 A/B Test 应如何设计？](questions/06-evaluation-click-ab/Q062-search-ab-testing.md)

## `colbert`

- [Q081 · ColBERT 的 Late Interaction 为什么重要？](questions/08-hybrid-rag-rerank/Q081-colbert-late-interaction.md)

## `dense-retrieval`

- [Q063 · Dense Retrieval 与 BM25 的本质区别是什么？](questions/07-dense-retrieval-ann/Q063-dense-retrieval-vs-bm25.md)
- [Q064 · 为什么 Dual Encoder 适合召回？](questions/07-dense-retrieval-ann/Q064-dual-encoder-retrieval.md)
- [Q065 · 双塔检索模型通常怎么训练？](questions/07-dense-retrieval-ann/Q065-dual-encoder-training.md)
- [Q066 · 为什么 Hard Negative 对 Dense Retrieval 至关重要？](questions/07-dense-retrieval-ann/Q066-hard-negatives.md)
- [Q067 · 什么是 In-batch Negative？有什么坑？](questions/07-dense-retrieval-ann/Q067-in-batch-negatives.md)
- [Q068 · Cosine、Inner Product、L2 在归一化向量下有什么关系？](questions/07-dense-retrieval-ann/Q068-cosine-dot-l2.md)
- [Q069 · 为什么十亿向量不能直接暴力扫描？如何算量？](questions/07-dense-retrieval-ann/Q069-why-ann-not-bruteforce.md)
- [Q070 · IVF 的原理是什么？nlist 与 nprobe 如何影响效果？](questions/07-dense-retrieval-ann/Q070-ivf-index.md)
- [Q071 · Product Quantization（PQ）是什么？](questions/07-dense-retrieval-ann/Q071-product-quantization.md)
- [Q072 · HNSW 的原理是什么？为什么分层？](questions/07-dense-retrieval-ann/Q072-hnsw-principles.md)
- [Q073 · HNSW 的 M、efConstruction、efSearch 分别控制什么？](questions/07-dense-retrieval-ann/Q073-hnsw-parameters.md)
- [Q074 · HNSW 与 IVF-PQ 如何选？](questions/07-dense-retrieval-ann/Q074-hnsw-vs-ivf-pq.md)
- [Q075 · 为什么 Hybrid Search 往往比纯 BM25 或纯 Dense 更稳？](questions/08-hybrid-rag-rerank/Q075-why-hybrid-search.md)
- [Q076 · BM25 Score 与 Dense Cosine 能直接相加吗？](questions/08-hybrid-rag-rerank/Q076-bm25-dense-score-fusion.md)

## `distributed-search`

- [Q085 · 为什么 Search Index 要做 Sharding？](questions/09-search-infrastructure/Q085-search-index-sharding.md)
- [Q086 · 分布式 Search Query 的 Scatter-Gather 怎么工作？](questions/09-search-infrastructure/Q086-scatter-gather-search.md)
- [Q087 · 为什么每个 Shard 只返回 Local TopK 可能有问题？](questions/09-search-infrastructure/Q087-distributed-topk-pitfalls.md)
- [Q088 · Primary Shard 与 Replica 的区别是什么？](questions/09-search-infrastructure/Q088-primary-vs-replica-shard.md)
- [Q089 · Shard 越多是不是查询越快？什么是 Over-sharding？](questions/09-search-infrastructure/Q089-over-sharding.md)
- [Q090 · 什么是 Near Real-Time（NRT）Search？](questions/09-search-infrastructure/Q090-near-real-time-search.md)
- [Q091 · Refresh Interval 为什么存在 Freshness-Throughput Trade-off？](questions/09-search-infrastructure/Q091-refresh-interval-tradeoff.md)
- [Q092 · 搜索索引如何与 MySQL/业务数据库保持同步？](questions/09-search-infrastructure/Q092-mysql-search-cdc-sync.md)
- [Q093 · 搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？](questions/09-search-infrastructure/Q093-search-caching.md)
- [Q094 · 搜索延迟从 50ms 突然变成 2s，怎么系统排查？](questions/09-search-infrastructure/Q094-search-tail-latency-debugging.md)

## `dual-encoder`

- [Q064 · 为什么 Dual Encoder 适合召回？](questions/07-dense-retrieval-ann/Q064-dual-encoder-retrieval.md)
- [Q080 · Dual Encoder 与 Cross-Encoder 的经典 Trade-off 是什么？](questions/08-hybrid-rag-rerank/Q080-dual-vs-cross-encoder.md)

## `evaluation`

- [Q053 · Precision@K 与 Recall@K 分别衡量什么？](questions/06-evaluation-click-ab/Q053-precision-recall-at-k.md)
- [Q054 · MRR 是什么？适合什么场景？](questions/06-evaluation-click-ab/Q054-mrr.md)
- [Q055 · MAP 是什么？与 MRR 有何不同？](questions/06-evaluation-click-ab/Q055-map-average-precision.md)
- [Q056 · NDCG 是什么？为什么是搜索面试必考？](questions/06-evaluation-click-ab/Q056-ndcg.md)
- [Q057 · 为什么 NDCG 比 Accuracy 更适合 Search？](questions/06-evaluation-click-ab/Q057-why-ndcg-not-accuracy.md)
- [Q058 · Recall@1000 提升但 NDCG@10 下降，怎么解释？](questions/06-evaluation-click-ab/Q058-recall-up-ndcg-down.md)
- [Q059 · 为什么 Click 不能直接当 Relevance Label？](questions/06-evaluation-click-ab/Q059-clicks-vs-relevance-labels.md)
- [Q060 · 如何处理 Position Bias？什么是 IPS？](questions/06-evaluation-click-ab/Q060-position-bias-ips.md)
- [Q061 · Offline 指标涨了，Online CTR/满意度为什么可能下降？](questions/06-evaluation-click-ab/Q061-offline-up-online-down.md)
- [Q062 · 搜索 A/B Test 应如何设计？](questions/06-evaluation-click-ab/Q062-search-ab-testing.md)

## `fst`

- [Q017 · Term Dictionary 为什么常用 FST，而不只是 HashMap？](questions/02-inverted-index-lucene/Q017-term-dictionary-fst.md)

## `hard-negative`

- [Q066 · 为什么 Hard Negative 对 Dense Retrieval 至关重要？](questions/07-dense-retrieval-ann/Q066-hard-negatives.md)

## `hnsw`

- [Q072 · HNSW 的原理是什么？为什么分层？](questions/07-dense-retrieval-ann/Q072-hnsw-principles.md)
- [Q073 · HNSW 的 M、efConstruction、efSearch 分别控制什么？](questions/07-dense-retrieval-ann/Q073-hnsw-parameters.md)
- [Q074 · HNSW 与 IVF-PQ 如何选？](questions/07-dense-retrieval-ann/Q074-hnsw-vs-ivf-pq.md)

## `hybrid-search`

- [Q075 · 为什么 Hybrid Search 往往比纯 BM25 或纯 Dense 更稳？](questions/08-hybrid-rag-rerank/Q075-why-hybrid-search.md)
- [Q076 · BM25 Score 与 Dense Cosine 能直接相加吗？](questions/08-hybrid-rag-rerank/Q076-bm25-dense-score-fusion.md)
- [Q077 · 什么是 Reciprocal Rank Fusion（RRF）？](questions/08-hybrid-rag-rerank/Q077-reciprocal-rank-fusion.md)
- [Q078 · SPLADE 这类 Learned Sparse Retrieval 在做什么？](questions/08-hybrid-rag-rerank/Q078-splade-sparse-neural-retrieval.md)
- [Q079 · 为什么 Cross-Encoder 适合 Rerank，而不适合全库召回？](questions/08-hybrid-rag-rerank/Q079-cross-encoder-reranking.md)
- [Q080 · Dual Encoder 与 Cross-Encoder 的经典 Trade-off 是什么？](questions/08-hybrid-rag-rerank/Q080-dual-vs-cross-encoder.md)
- [Q081 · ColBERT 的 Late Interaction 为什么重要？](questions/08-hybrid-rag-rerank/Q081-colbert-late-interaction.md)
- [Q082 · RAG 的 Chunk Size 应该怎么选？](questions/08-hybrid-rag-rerank/Q082-rag-chunk-size.md)
- [Q083 · Retrieval Recall 很高，为什么 RAG 仍会答错？](questions/08-hybrid-rag-rerank/Q083-high-recall-rag-still-wrong.md)
- [Q084 · 什么是 Agentic / Iterative Search？](questions/08-hybrid-rag-rerank/Q084-agentic-search.md)
- [Q099 · 系统设计：现代 Hybrid Search Engine](questions/10-system-design/Q099-system-design-hybrid-search.md)

## `indexing`

- [Q011 · 什么是倒排索引？](questions/02-inverted-index-lucene/Q011-inverted-index.md)
- [Q012 · 为什么叫“倒排”？正排索引还有什么用？](questions/02-inverted-index-lucene/Q012-inverted-vs-forward-index.md)
- [Q013 · Posting List 中一般存哪些信息？](questions/02-inverted-index-lucene/Q013-posting-list-contents.md)
- [Q014 · 两个有序 Posting List 的 AND 查询怎么做？](questions/02-inverted-index-lucene/Q014-posting-list-intersection.md)
- [Q015 · Posting List 很长时，WAND / Block-Max WAND 在做什么？](questions/02-inverted-index-lucene/Q015-wand-block-max-wand.md)
- [Q016 · 为什么 DocID 常用 gap/delta 编码？](questions/02-inverted-index-lucene/Q016-docid-gap-delta-encoding.md)
- [Q017 · Term Dictionary 为什么常用 FST，而不只是 HashMap？](questions/02-inverted-index-lucene/Q017-term-dictionary-fst.md)
- [Q018 · Trie 为什么适合做 Search Autocomplete？](questions/02-inverted-index-lucene/Q018-trie-autocomplete.md)
- [Q019 · Lucene Segment 为什么设计成 immutable？](questions/02-inverted-index-lucene/Q019-lucene-immutable-segment.md)
- [Q020 · Segment Merge 为什么既重要又危险？](questions/02-inverted-index-lucene/Q020-segment-merge-tradeoffs.md)

## `information-retrieval`

- [Q021 · TF-IDF 的核心直觉是什么？](questions/03-bm25-lexical-retrieval/Q021-tf-idf-intuition.md)
- [Q022 · 为什么 IDF 能衡量一个词的“辨识度”？](questions/03-bm25-lexical-retrieval/Q022-idf-discriminativeness.md)
- [Q023 · TF-IDF 的主要问题是什么？](questions/03-bm25-lexical-retrieval/Q023-tf-idf-limitations.md)
- [Q024 · 写出 BM25，并解释每一项的意义](questions/03-bm25-lexical-retrieval/Q024-bm25-formula.md)
- [Q025 · BM25 相比 TF-IDF 到底改进了什么？](questions/03-bm25-lexical-retrieval/Q025-bm25-vs-tf-idf.md)
- [Q026 · BM25 中 k1 控制什么？如何调？](questions/03-bm25-lexical-retrieval/Q026-bm25-k1.md)
- [Q027 · BM25 中 b 控制什么？如何理解 b=0 和 b=1？](questions/03-bm25-lexical-retrieval/Q027-bm25-b.md)
- [Q028 · Title 和 Body 应该如何联合打分？什么是 BM25F 思想？](questions/03-bm25-lexical-retrieval/Q028-bm25f-title-body.md)
- [Q029 · BM25 会在哪些场景失败？](questions/03-bm25-lexical-retrieval/Q029-bm25-failure-modes.md)
- [Q030 · 为什么 BM25 在 2026 年仍然非常强？](questions/03-bm25-lexical-retrieval/Q030-why-bm25-still-strong.md)

## `infra`

- [Q085 · 为什么 Search Index 要做 Sharding？](questions/09-search-infrastructure/Q085-search-index-sharding.md)
- [Q086 · 分布式 Search Query 的 Scatter-Gather 怎么工作？](questions/09-search-infrastructure/Q086-scatter-gather-search.md)
- [Q087 · 为什么每个 Shard 只返回 Local TopK 可能有问题？](questions/09-search-infrastructure/Q087-distributed-topk-pitfalls.md)
- [Q088 · Primary Shard 与 Replica 的区别是什么？](questions/09-search-infrastructure/Q088-primary-vs-replica-shard.md)
- [Q089 · Shard 越多是不是查询越快？什么是 Over-sharding？](questions/09-search-infrastructure/Q089-over-sharding.md)
- [Q090 · 什么是 Near Real-Time（NRT）Search？](questions/09-search-infrastructure/Q090-near-real-time-search.md)
- [Q091 · Refresh Interval 为什么存在 Freshness-Throughput Trade-off？](questions/09-search-infrastructure/Q091-refresh-interval-tradeoff.md)
- [Q092 · 搜索索引如何与 MySQL/业务数据库保持同步？](questions/09-search-infrastructure/Q092-mysql-search-cdc-sync.md)
- [Q093 · 搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？](questions/09-search-infrastructure/Q093-search-caching.md)
- [Q094 · 搜索延迟从 50ms 突然变成 2s，怎么系统排查？](questions/09-search-infrastructure/Q094-search-tail-latency-debugging.md)

## `inverted-index`

- [Q011 · 什么是倒排索引？](questions/02-inverted-index-lucene/Q011-inverted-index.md)
- [Q012 · 为什么叫“倒排”？正排索引还有什么用？](questions/02-inverted-index-lucene/Q012-inverted-vs-forward-index.md)
- [Q013 · Posting List 中一般存哪些信息？](questions/02-inverted-index-lucene/Q013-posting-list-contents.md)
- [Q014 · 两个有序 Posting List 的 AND 查询怎么做？](questions/02-inverted-index-lucene/Q014-posting-list-intersection.md)
- [Q015 · Posting List 很长时，WAND / Block-Max WAND 在做什么？](questions/02-inverted-index-lucene/Q015-wand-block-max-wand.md)
- [Q016 · 为什么 DocID 常用 gap/delta 编码？](questions/02-inverted-index-lucene/Q016-docid-gap-delta-encoding.md)
- [Q017 · Term Dictionary 为什么常用 FST，而不只是 HashMap？](questions/02-inverted-index-lucene/Q017-term-dictionary-fst.md)
- [Q018 · Trie 为什么适合做 Search Autocomplete？](questions/02-inverted-index-lucene/Q018-trie-autocomplete.md)
- [Q019 · Lucene Segment 为什么设计成 immutable？](questions/02-inverted-index-lucene/Q019-lucene-immutable-segment.md)
- [Q020 · Segment Merge 为什么既重要又危险？](questions/02-inverted-index-lucene/Q020-segment-merge-tradeoffs.md)

## `ips`

- [Q060 · 如何处理 Position Bias？什么是 IPS？](questions/06-evaluation-click-ab/Q060-position-bias-ips.md)

## `ivf`

- [Q070 · IVF 的原理是什么？nlist 与 nprobe 如何影响效果？](questions/07-dense-retrieval-ann/Q070-ivf-index.md)
- [Q074 · HNSW 与 IVF-PQ 如何选？](questions/07-dense-retrieval-ann/Q074-hnsw-vs-ivf-pq.md)

## `lambdamart`

- [Q041 · 为什么需要 Learning to Rank？BM25 不够吗？](questions/05-learning-to-rank/Q041-why-learning-to-rank.md)
- [Q042 · Pointwise Ranking 是什么？优缺点？](questions/05-learning-to-rank/Q042-pointwise-ranking.md)
- [Q043 · Pairwise Ranking 是什么？](questions/05-learning-to-rank/Q043-pairwise-ranking.md)
- [Q044 · Listwise Ranking 是什么？为什么更贴近 NDCG？](questions/05-learning-to-rank/Q044-listwise-ranking.md)
- [Q045 · RankNet 的核心公式和直觉是什么？](questions/05-learning-to-rank/Q045-ranknet.md)
- [Q046 · LambdaRank 为什么出现？Lambda 到底是什么？](questions/05-learning-to-rank/Q046-lambdarank.md)
- [Q047 · LambdaMART 是什么？为什么经典？](questions/05-learning-to-rank/Q047-lambdamart.md)
- [Q048 · 深度学习时代，为什么 LambdaMART 仍然常见？](questions/05-learning-to-rank/Q048-why-lambdamart-still-used.md)
- [Q049 · 搜索 Ranker 常见特征有哪些？如何分类？](questions/05-learning-to-rank/Q049-search-ranker-features.md)
- [Q050 · 什么是 Query-independent Feature？为什么有价值？](questions/05-learning-to-rank/Q050-query-independent-features.md)
- [Q051 · 搜索排序中的 Feature Leakage 是什么？](questions/05-learning-to-rank/Q051-feature-leakage.md)
- [Q052 · Ranker 为什么有时需要 Calibration？](questions/05-learning-to-rank/Q052-ranker-calibration.md)

## `lambdarank`

- [Q046 · LambdaRank 为什么出现？Lambda 到底是什么？](questions/05-learning-to-rank/Q046-lambdarank.md)

## `latency`

- [Q085 · 为什么 Search Index 要做 Sharding？](questions/09-search-infrastructure/Q085-search-index-sharding.md)
- [Q086 · 分布式 Search Query 的 Scatter-Gather 怎么工作？](questions/09-search-infrastructure/Q086-scatter-gather-search.md)
- [Q087 · 为什么每个 Shard 只返回 Local TopK 可能有问题？](questions/09-search-infrastructure/Q087-distributed-topk-pitfalls.md)
- [Q088 · Primary Shard 与 Replica 的区别是什么？](questions/09-search-infrastructure/Q088-primary-vs-replica-shard.md)
- [Q089 · Shard 越多是不是查询越快？什么是 Over-sharding？](questions/09-search-infrastructure/Q089-over-sharding.md)
- [Q090 · 什么是 Near Real-Time（NRT）Search？](questions/09-search-infrastructure/Q090-near-real-time-search.md)
- [Q091 · Refresh Interval 为什么存在 Freshness-Throughput Trade-off？](questions/09-search-infrastructure/Q091-refresh-interval-tradeoff.md)
- [Q092 · 搜索索引如何与 MySQL/业务数据库保持同步？](questions/09-search-infrastructure/Q092-mysql-search-cdc-sync.md)
- [Q093 · 搜索系统有哪些 Cache？为什么 Query Result Cache 不一定有效？](questions/09-search-infrastructure/Q093-search-caching.md)
- [Q094 · 搜索延迟从 50ms 突然变成 2s，怎么系统排查？](questions/09-search-infrastructure/Q094-search-tail-latency-debugging.md)

## `learning-to-rank`

- [Q041 · 为什么需要 Learning to Rank？BM25 不够吗？](questions/05-learning-to-rank/Q041-why-learning-to-rank.md)
- [Q042 · Pointwise Ranking 是什么？优缺点？](questions/05-learning-to-rank/Q042-pointwise-ranking.md)
- [Q043 · Pairwise Ranking 是什么？](questions/05-learning-to-rank/Q043-pairwise-ranking.md)
- [Q044 · Listwise Ranking 是什么？为什么更贴近 NDCG？](questions/05-learning-to-rank/Q044-listwise-ranking.md)
- [Q045 · RankNet 的核心公式和直觉是什么？](questions/05-learning-to-rank/Q045-ranknet.md)
- [Q046 · LambdaRank 为什么出现？Lambda 到底是什么？](questions/05-learning-to-rank/Q046-lambdarank.md)
- [Q047 · LambdaMART 是什么？为什么经典？](questions/05-learning-to-rank/Q047-lambdamart.md)
- [Q048 · 深度学习时代，为什么 LambdaMART 仍然常见？](questions/05-learning-to-rank/Q048-why-lambdamart-still-used.md)
- [Q049 · 搜索 Ranker 常见特征有哪些？如何分类？](questions/05-learning-to-rank/Q049-search-ranker-features.md)
- [Q050 · 什么是 Query-independent Feature？为什么有价值？](questions/05-learning-to-rank/Q050-query-independent-features.md)
- [Q051 · 搜索排序中的 Feature Leakage 是什么？](questions/05-learning-to-rank/Q051-feature-leakage.md)
- [Q052 · Ranker 为什么有时需要 Calibration？](questions/05-learning-to-rank/Q052-ranker-calibration.md)

## `lexical-retrieval`

- [Q021 · TF-IDF 的核心直觉是什么？](questions/03-bm25-lexical-retrieval/Q021-tf-idf-intuition.md)
- [Q022 · 为什么 IDF 能衡量一个词的“辨识度”？](questions/03-bm25-lexical-retrieval/Q022-idf-discriminativeness.md)
- [Q023 · TF-IDF 的主要问题是什么？](questions/03-bm25-lexical-retrieval/Q023-tf-idf-limitations.md)
- [Q024 · 写出 BM25，并解释每一项的意义](questions/03-bm25-lexical-retrieval/Q024-bm25-formula.md)
- [Q025 · BM25 相比 TF-IDF 到底改进了什么？](questions/03-bm25-lexical-retrieval/Q025-bm25-vs-tf-idf.md)
- [Q026 · BM25 中 k1 控制什么？如何调？](questions/03-bm25-lexical-retrieval/Q026-bm25-k1.md)
- [Q027 · BM25 中 b 控制什么？如何理解 b=0 和 b=1？](questions/03-bm25-lexical-retrieval/Q027-bm25-b.md)
- [Q028 · Title 和 Body 应该如何联合打分？什么是 BM25F 思想？](questions/03-bm25-lexical-retrieval/Q028-bm25f-title-body.md)
- [Q029 · BM25 会在哪些场景失败？](questions/03-bm25-lexical-retrieval/Q029-bm25-failure-modes.md)
- [Q030 · 为什么 BM25 在 2026 年仍然非常强？](questions/03-bm25-lexical-retrieval/Q030-why-bm25-still-strong.md)

## `lucene`

- [Q011 · 什么是倒排索引？](questions/02-inverted-index-lucene/Q011-inverted-index.md)
- [Q012 · 为什么叫“倒排”？正排索引还有什么用？](questions/02-inverted-index-lucene/Q012-inverted-vs-forward-index.md)
- [Q013 · Posting List 中一般存哪些信息？](questions/02-inverted-index-lucene/Q013-posting-list-contents.md)
- [Q014 · 两个有序 Posting List 的 AND 查询怎么做？](questions/02-inverted-index-lucene/Q014-posting-list-intersection.md)
- [Q015 · Posting List 很长时，WAND / Block-Max WAND 在做什么？](questions/02-inverted-index-lucene/Q015-wand-block-max-wand.md)
- [Q016 · 为什么 DocID 常用 gap/delta 编码？](questions/02-inverted-index-lucene/Q016-docid-gap-delta-encoding.md)
- [Q017 · Term Dictionary 为什么常用 FST，而不只是 HashMap？](questions/02-inverted-index-lucene/Q017-term-dictionary-fst.md)
- [Q018 · Trie 为什么适合做 Search Autocomplete？](questions/02-inverted-index-lucene/Q018-trie-autocomplete.md)
- [Q019 · Lucene Segment 为什么设计成 immutable？](questions/02-inverted-index-lucene/Q019-lucene-immutable-segment.md)
- [Q020 · Segment Merge 为什么既重要又危险？](questions/02-inverted-index-lucene/Q020-segment-merge-tradeoffs.md)

## `map`

- [Q017 · Term Dictionary 为什么常用 FST，而不只是 HashMap？](questions/02-inverted-index-lucene/Q017-term-dictionary-fst.md)
- [Q055 · MAP 是什么？与 MRR 有何不同？](questions/06-evaluation-click-ab/Q055-map-average-precision.md)

## `mrr`

- [Q054 · MRR 是什么？适合什么场景？](questions/06-evaluation-click-ab/Q054-mrr.md)
- [Q055 · MAP 是什么？与 MRR 有何不同？](questions/06-evaluation-click-ab/Q055-map-average-precision.md)

## `ndcg`

- [Q044 · Listwise Ranking 是什么？为什么更贴近 NDCG？](questions/05-learning-to-rank/Q044-listwise-ranking.md)
- [Q056 · NDCG 是什么？为什么是搜索面试必考？](questions/06-evaluation-click-ab/Q056-ndcg.md)
- [Q057 · 为什么 NDCG 比 Accuracy 更适合 Search？](questions/06-evaluation-click-ab/Q057-why-ndcg-not-accuracy.md)
- [Q058 · Recall@1000 提升但 NDCG@10 下降，怎么解释？](questions/06-evaluation-click-ab/Q058-recall-up-ndcg-down.md)

## `nlp`

- [Q031 · Query Understanding 通常包括哪些任务？](questions/04-query-understanding/Q031-query-understanding-tasks.md)
- [Q032 · 中文搜索分词为什么比英文更难？](questions/04-query-understanding/Q032-chinese-tokenization.md)
- [Q033 · 搜索分词是不是越细越好？](questions/04-query-understanding/Q033-search-tokenization-granularity.md)
- [Q034 · 拼写纠错如何设计 Candidate Generation 与 Ranking？](questions/04-query-understanding/Q034-spelling-correction-candidate-ranking.md)
- [Q035 · “苹果”这样的 Query 为什么难？如何做意图消歧？](questions/04-query-understanding/Q035-query-intent-disambiguation-apple.md)
- [Q036 · 什么是 Query Expansion？为什么会同时提升 Recall 和伤害 Precision？](questions/04-query-understanding/Q036-query-expansion-recall-precision.md)
- [Q037 · Synonym、Query Rewrite、Query Expansion 有什么区别？](questions/04-query-understanding/Q037-synonym-rewrite-expansion.md)
- [Q038 · LLM 如何用于 Query Rewrite？](questions/04-query-understanding/Q038-llm-query-rewrite.md)
- [Q039 · LLM Query Rewrite 最大的风险是什么？](questions/04-query-understanding/Q039-llm-query-rewrite-risks.md)
- [Q040 · 如何设计 Search Autocomplete / Query Suggest？](questions/04-query-understanding/Q040-search-autocomplete-query-suggest.md)

## `posting-list`

- [Q013 · Posting List 中一般存哪些信息？](questions/02-inverted-index-lucene/Q013-posting-list-contents.md)
- [Q014 · 两个有序 Posting List 的 AND 查询怎么做？](questions/02-inverted-index-lucene/Q014-posting-list-intersection.md)
- [Q015 · Posting List 很长时，WAND / Block-Max WAND 在做什么？](questions/02-inverted-index-lucene/Q015-wand-block-max-wand.md)

## `pq`

- [Q071 · Product Quantization（PQ）是什么？](questions/07-dense-retrieval-ann/Q071-product-quantization.md)

## `query-rewrite`

- [Q031 · Query Understanding 通常包括哪些任务？](questions/04-query-understanding/Q031-query-understanding-tasks.md)
- [Q032 · 中文搜索分词为什么比英文更难？](questions/04-query-understanding/Q032-chinese-tokenization.md)
- [Q033 · 搜索分词是不是越细越好？](questions/04-query-understanding/Q033-search-tokenization-granularity.md)
- [Q034 · 拼写纠错如何设计 Candidate Generation 与 Ranking？](questions/04-query-understanding/Q034-spelling-correction-candidate-ranking.md)
- [Q035 · “苹果”这样的 Query 为什么难？如何做意图消歧？](questions/04-query-understanding/Q035-query-intent-disambiguation-apple.md)
- [Q036 · 什么是 Query Expansion？为什么会同时提升 Recall 和伤害 Precision？](questions/04-query-understanding/Q036-query-expansion-recall-precision.md)
- [Q037 · Synonym、Query Rewrite、Query Expansion 有什么区别？](questions/04-query-understanding/Q037-synonym-rewrite-expansion.md)
- [Q038 · LLM 如何用于 Query Rewrite？](questions/04-query-understanding/Q038-llm-query-rewrite.md)
- [Q039 · LLM Query Rewrite 最大的风险是什么？](questions/04-query-understanding/Q039-llm-query-rewrite-risks.md)
- [Q040 · 如何设计 Search Autocomplete / Query Suggest？](questions/04-query-understanding/Q040-search-autocomplete-query-suggest.md)

## `query-understanding`

- [Q031 · Query Understanding 通常包括哪些任务？](questions/04-query-understanding/Q031-query-understanding-tasks.md)
- [Q032 · 中文搜索分词为什么比英文更难？](questions/04-query-understanding/Q032-chinese-tokenization.md)
- [Q033 · 搜索分词是不是越细越好？](questions/04-query-understanding/Q033-search-tokenization-granularity.md)
- [Q034 · 拼写纠错如何设计 Candidate Generation 与 Ranking？](questions/04-query-understanding/Q034-spelling-correction-candidate-ranking.md)
- [Q035 · “苹果”这样的 Query 为什么难？如何做意图消歧？](questions/04-query-understanding/Q035-query-intent-disambiguation-apple.md)
- [Q036 · 什么是 Query Expansion？为什么会同时提升 Recall 和伤害 Precision？](questions/04-query-understanding/Q036-query-expansion-recall-precision.md)
- [Q037 · Synonym、Query Rewrite、Query Expansion 有什么区别？](questions/04-query-understanding/Q037-synonym-rewrite-expansion.md)
- [Q038 · LLM 如何用于 Query Rewrite？](questions/04-query-understanding/Q038-llm-query-rewrite.md)
- [Q039 · LLM Query Rewrite 最大的风险是什么？](questions/04-query-understanding/Q039-llm-query-rewrite-risks.md)
- [Q040 · 如何设计 Search Autocomplete / Query Suggest？](questions/04-query-understanding/Q040-search-autocomplete-query-suggest.md)

## `rag`

- [Q010 · 传统 Search 与 RAG Retrieval 的目标有什么不同？](questions/01-search-architecture/Q010-search-vs-rag-retrieval.md)
- [Q075 · 为什么 Hybrid Search 往往比纯 BM25 或纯 Dense 更稳？](questions/08-hybrid-rag-rerank/Q075-why-hybrid-search.md)
- [Q076 · BM25 Score 与 Dense Cosine 能直接相加吗？](questions/08-hybrid-rag-rerank/Q076-bm25-dense-score-fusion.md)
- [Q077 · 什么是 Reciprocal Rank Fusion（RRF）？](questions/08-hybrid-rag-rerank/Q077-reciprocal-rank-fusion.md)
- [Q078 · SPLADE 这类 Learned Sparse Retrieval 在做什么？](questions/08-hybrid-rag-rerank/Q078-splade-sparse-neural-retrieval.md)
- [Q079 · 为什么 Cross-Encoder 适合 Rerank，而不适合全库召回？](questions/08-hybrid-rag-rerank/Q079-cross-encoder-reranking.md)
- [Q080 · Dual Encoder 与 Cross-Encoder 的经典 Trade-off 是什么？](questions/08-hybrid-rag-rerank/Q080-dual-vs-cross-encoder.md)
- [Q081 · ColBERT 的 Late Interaction 为什么重要？](questions/08-hybrid-rag-rerank/Q081-colbert-late-interaction.md)
- [Q082 · RAG 的 Chunk Size 应该怎么选？](questions/08-hybrid-rag-rerank/Q082-rag-chunk-size.md)
- [Q083 · Retrieval Recall 很高，为什么 RAG 仍会答错？](questions/08-hybrid-rag-rerank/Q083-high-recall-rag-still-wrong.md)
- [Q084 · 什么是 Agentic / Iterative Search？](questions/08-hybrid-rag-rerank/Q084-agentic-search.md)

## `ranking`

- [Q001 · 完整讲一下搜索引擎的端到端 Pipeline](questions/01-search-architecture/Q001-search-engine-end-to-end-pipeline.md)
- [Q002 · 搜索系统与推荐系统的本质区别是什么？](questions/01-search-architecture/Q002-search-vs-recommendation.md)
- [Q003 · 为什么搜索一定要有候选召回阶段？](questions/01-search-architecture/Q003-why-candidate-retrieval.md)
- [Q004 · 召回、粗排、精排、重排分别优化什么？](questions/01-search-architecture/Q004-recall-prerank-rank-rerank.md)
- [Q005 · 为什么不能用数据库 LIKE 代替搜索引擎？](questions/01-search-architecture/Q005-database-like-vs-search.md)
- [Q006 · 一次搜索请求从键盘到 SERP 发生了什么？](questions/01-search-architecture/Q006-query-to-serp-request-lifecycle.md)
- [Q007 · 为什么现代搜索几乎都是 Multi-stage Ranking？](questions/01-search-architecture/Q007-why-multi-stage-ranking.md)
- [Q008 · 搜索系统的目标函数为什么是多目标的？](questions/01-search-architecture/Q008-multi-objective-search-ranking.md)
- [Q009 · 为什么搜索结果不能直接按 CTR 排？](questions/01-search-architecture/Q009-why-not-rank-by-ctr.md)
- [Q010 · 传统 Search 与 RAG Retrieval 的目标有什么不同？](questions/01-search-architecture/Q010-search-vs-rag-retrieval.md)
- [Q041 · 为什么需要 Learning to Rank？BM25 不够吗？](questions/05-learning-to-rank/Q041-why-learning-to-rank.md)
- [Q042 · Pointwise Ranking 是什么？优缺点？](questions/05-learning-to-rank/Q042-pointwise-ranking.md)
- [Q043 · Pairwise Ranking 是什么？](questions/05-learning-to-rank/Q043-pairwise-ranking.md)
- [Q044 · Listwise Ranking 是什么？为什么更贴近 NDCG？](questions/05-learning-to-rank/Q044-listwise-ranking.md)
- [Q045 · RankNet 的核心公式和直觉是什么？](questions/05-learning-to-rank/Q045-ranknet.md)
- [Q046 · LambdaRank 为什么出现？Lambda 到底是什么？](questions/05-learning-to-rank/Q046-lambdarank.md)
- [Q047 · LambdaMART 是什么？为什么经典？](questions/05-learning-to-rank/Q047-lambdamart.md)
- [Q048 · 深度学习时代，为什么 LambdaMART 仍然常见？](questions/05-learning-to-rank/Q048-why-lambdamart-still-used.md)
- [Q049 · 搜索 Ranker 常见特征有哪些？如何分类？](questions/05-learning-to-rank/Q049-search-ranker-features.md)
- [Q050 · 什么是 Query-independent Feature？为什么有价值？](questions/05-learning-to-rank/Q050-query-independent-features.md)
- [Q051 · 搜索排序中的 Feature Leakage 是什么？](questions/05-learning-to-rank/Q051-feature-leakage.md)
- [Q052 · Ranker 为什么有时需要 Calibration？](questions/05-learning-to-rank/Q052-ranker-calibration.md)

## `ranknet`

- [Q045 · RankNet 的核心公式和直觉是什么？](questions/05-learning-to-rank/Q045-ranknet.md)

## `reranking`

- [Q075 · 为什么 Hybrid Search 往往比纯 BM25 或纯 Dense 更稳？](questions/08-hybrid-rag-rerank/Q075-why-hybrid-search.md)
- [Q076 · BM25 Score 与 Dense Cosine 能直接相加吗？](questions/08-hybrid-rag-rerank/Q076-bm25-dense-score-fusion.md)
- [Q077 · 什么是 Reciprocal Rank Fusion（RRF）？](questions/08-hybrid-rag-rerank/Q077-reciprocal-rank-fusion.md)
- [Q078 · SPLADE 这类 Learned Sparse Retrieval 在做什么？](questions/08-hybrid-rag-rerank/Q078-splade-sparse-neural-retrieval.md)
- [Q079 · 为什么 Cross-Encoder 适合 Rerank，而不适合全库召回？](questions/08-hybrid-rag-rerank/Q079-cross-encoder-reranking.md)
- [Q080 · Dual Encoder 与 Cross-Encoder 的经典 Trade-off 是什么？](questions/08-hybrid-rag-rerank/Q080-dual-vs-cross-encoder.md)
- [Q081 · ColBERT 的 Late Interaction 为什么重要？](questions/08-hybrid-rag-rerank/Q081-colbert-late-interaction.md)
- [Q082 · RAG 的 Chunk Size 应该怎么选？](questions/08-hybrid-rag-rerank/Q082-rag-chunk-size.md)
- [Q083 · Retrieval Recall 很高，为什么 RAG 仍会答错？](questions/08-hybrid-rag-rerank/Q083-high-recall-rag-still-wrong.md)
- [Q084 · 什么是 Agentic / Iterative Search？](questions/08-hybrid-rag-rerank/Q084-agentic-search.md)

## `retrieval`

- [Q001 · 完整讲一下搜索引擎的端到端 Pipeline](questions/01-search-architecture/Q001-search-engine-end-to-end-pipeline.md)
- [Q002 · 搜索系统与推荐系统的本质区别是什么？](questions/01-search-architecture/Q002-search-vs-recommendation.md)
- [Q003 · 为什么搜索一定要有候选召回阶段？](questions/01-search-architecture/Q003-why-candidate-retrieval.md)
- [Q004 · 召回、粗排、精排、重排分别优化什么？](questions/01-search-architecture/Q004-recall-prerank-rank-rerank.md)
- [Q005 · 为什么不能用数据库 LIKE 代替搜索引擎？](questions/01-search-architecture/Q005-database-like-vs-search.md)
- [Q006 · 一次搜索请求从键盘到 SERP 发生了什么？](questions/01-search-architecture/Q006-query-to-serp-request-lifecycle.md)
- [Q007 · 为什么现代搜索几乎都是 Multi-stage Ranking？](questions/01-search-architecture/Q007-why-multi-stage-ranking.md)
- [Q008 · 搜索系统的目标函数为什么是多目标的？](questions/01-search-architecture/Q008-multi-objective-search-ranking.md)
- [Q009 · 为什么搜索结果不能直接按 CTR 排？](questions/01-search-architecture/Q009-why-not-rank-by-ctr.md)
- [Q010 · 传统 Search 与 RAG Retrieval 的目标有什么不同？](questions/01-search-architecture/Q010-search-vs-rag-retrieval.md)

## `rrf`

- [Q077 · 什么是 Reciprocal Rank Fusion（RRF）？](questions/08-hybrid-rag-rerank/Q077-reciprocal-rank-fusion.md)

## `search-architecture`

- [Q001 · 完整讲一下搜索引擎的端到端 Pipeline](questions/01-search-architecture/Q001-search-engine-end-to-end-pipeline.md)
- [Q002 · 搜索系统与推荐系统的本质区别是什么？](questions/01-search-architecture/Q002-search-vs-recommendation.md)
- [Q003 · 为什么搜索一定要有候选召回阶段？](questions/01-search-architecture/Q003-why-candidate-retrieval.md)
- [Q004 · 召回、粗排、精排、重排分别优化什么？](questions/01-search-architecture/Q004-recall-prerank-rank-rerank.md)
- [Q005 · 为什么不能用数据库 LIKE 代替搜索引擎？](questions/01-search-architecture/Q005-database-like-vs-search.md)
- [Q006 · 一次搜索请求从键盘到 SERP 发生了什么？](questions/01-search-architecture/Q006-query-to-serp-request-lifecycle.md)
- [Q007 · 为什么现代搜索几乎都是 Multi-stage Ranking？](questions/01-search-architecture/Q007-why-multi-stage-ranking.md)
- [Q008 · 搜索系统的目标函数为什么是多目标的？](questions/01-search-architecture/Q008-multi-objective-search-ranking.md)
- [Q009 · 为什么搜索结果不能直接按 CTR 排？](questions/01-search-architecture/Q009-why-not-rank-by-ctr.md)
- [Q010 · 传统 Search 与 RAG Retrieval 的目标有什么不同？](questions/01-search-architecture/Q010-search-vs-rag-retrieval.md)
- [Q095 · 系统设计：从 0 设计一个 Google-like Web Search](questions/10-system-design/Q095-system-design-web-search.md)
- [Q096 · 系统设计：淘宝 / Amazon 商品搜索](questions/10-system-design/Q096-system-design-ecommerce-search.md)
- [Q097 · 系统设计：亿级 Query Autocomplete](questions/10-system-design/Q097-system-design-query-autocomplete.md)
- [Q098 · 系统设计：10 亿文档 Semantic Search](questions/10-system-design/Q098-system-design-billion-vector-search.md)
- [Q099 · 系统设计：现代 Hybrid Search Engine](questions/10-system-design/Q099-system-design-hybrid-search.md)
- [Q100 · 终极题：如果让你从 0 到 1 提升一个搜索引擎，你会怎么做？](questions/10-system-design/Q100-zero-to-one-search-improvement.md)

## `semantic-search`

- [Q098 · 系统设计：10 亿文档 Semantic Search](questions/10-system-design/Q098-system-design-billion-vector-search.md)

## `sharding`

- [Q085 · 为什么 Search Index 要做 Sharding？](questions/09-search-infrastructure/Q085-search-index-sharding.md)
- [Q087 · 为什么每个 Shard 只返回 Local TopK 可能有问题？](questions/09-search-infrastructure/Q087-distributed-topk-pitfalls.md)
- [Q088 · Primary Shard 与 Replica 的区别是什么？](questions/09-search-infrastructure/Q088-primary-vs-replica-shard.md)
- [Q089 · Shard 越多是不是查询越快？什么是 Over-sharding？](questions/09-search-infrastructure/Q089-over-sharding.md)

## `splade`

- [Q078 · SPLADE 这类 Learned Sparse Retrieval 在做什么？](questions/08-hybrid-rag-rerank/Q078-splade-sparse-neural-retrieval.md)

## `staff-interview`

- [Q095 · 系统设计：从 0 设计一个 Google-like Web Search](questions/10-system-design/Q095-system-design-web-search.md)
- [Q096 · 系统设计：淘宝 / Amazon 商品搜索](questions/10-system-design/Q096-system-design-ecommerce-search.md)
- [Q097 · 系统设计：亿级 Query Autocomplete](questions/10-system-design/Q097-system-design-query-autocomplete.md)
- [Q098 · 系统设计：10 亿文档 Semantic Search](questions/10-system-design/Q098-system-design-billion-vector-search.md)
- [Q099 · 系统设计：现代 Hybrid Search Engine](questions/10-system-design/Q099-system-design-hybrid-search.md)
- [Q100 · 终极题：如果让你从 0 到 1 提升一个搜索引擎，你会怎么做？](questions/10-system-design/Q100-zero-to-one-search-improvement.md)

## `system-design`

- [Q095 · 系统设计：从 0 设计一个 Google-like Web Search](questions/10-system-design/Q095-system-design-web-search.md)
- [Q096 · 系统设计：淘宝 / Amazon 商品搜索](questions/10-system-design/Q096-system-design-ecommerce-search.md)
- [Q097 · 系统设计：亿级 Query Autocomplete](questions/10-system-design/Q097-system-design-query-autocomplete.md)
- [Q098 · 系统设计：10 亿文档 Semantic Search](questions/10-system-design/Q098-system-design-billion-vector-search.md)
- [Q099 · 系统设计：现代 Hybrid Search Engine](questions/10-system-design/Q099-system-design-hybrid-search.md)
- [Q100 · 终极题：如果让你从 0 到 1 提升一个搜索引擎，你会怎么做？](questions/10-system-design/Q100-zero-to-one-search-improvement.md)

## `tf-idf`

- [Q021 · TF-IDF 的核心直觉是什么？](questions/03-bm25-lexical-retrieval/Q021-tf-idf-intuition.md)
- [Q023 · TF-IDF 的主要问题是什么？](questions/03-bm25-lexical-retrieval/Q023-tf-idf-limitations.md)
- [Q025 · BM25 相比 TF-IDF 到底改进了什么？](questions/03-bm25-lexical-retrieval/Q025-bm25-vs-tf-idf.md)

## `trie`

- [Q010 · 传统 Search 与 RAG Retrieval 的目标有什么不同？](questions/01-search-architecture/Q010-search-vs-rag-retrieval.md)
- [Q018 · Trie 为什么适合做 Search Autocomplete？](questions/02-inverted-index-lucene/Q018-trie-autocomplete.md)
- [Q063 · Dense Retrieval 与 BM25 的本质区别是什么？](questions/07-dense-retrieval-ann/Q063-dense-retrieval-vs-bm25.md)
- [Q066 · 为什么 Hard Negative 对 Dense Retrieval 至关重要？](questions/07-dense-retrieval-ann/Q066-hard-negatives.md)
- [Q078 · SPLADE 这类 Learned Sparse Retrieval 在做什么？](questions/08-hybrid-rag-rerank/Q078-splade-sparse-neural-retrieval.md)
- [Q083 · Retrieval Recall 很高，为什么 RAG 仍会答错？](questions/08-hybrid-rag-rerank/Q083-high-recall-rag-still-wrong.md)

## `vector-search`

- [Q063 · Dense Retrieval 与 BM25 的本质区别是什么？](questions/07-dense-retrieval-ann/Q063-dense-retrieval-vs-bm25.md)
- [Q064 · 为什么 Dual Encoder 适合召回？](questions/07-dense-retrieval-ann/Q064-dual-encoder-retrieval.md)
- [Q065 · 双塔检索模型通常怎么训练？](questions/07-dense-retrieval-ann/Q065-dual-encoder-training.md)
- [Q066 · 为什么 Hard Negative 对 Dense Retrieval 至关重要？](questions/07-dense-retrieval-ann/Q066-hard-negatives.md)
- [Q067 · 什么是 In-batch Negative？有什么坑？](questions/07-dense-retrieval-ann/Q067-in-batch-negatives.md)
- [Q068 · Cosine、Inner Product、L2 在归一化向量下有什么关系？](questions/07-dense-retrieval-ann/Q068-cosine-dot-l2.md)
- [Q069 · 为什么十亿向量不能直接暴力扫描？如何算量？](questions/07-dense-retrieval-ann/Q069-why-ann-not-bruteforce.md)
- [Q070 · IVF 的原理是什么？nlist 与 nprobe 如何影响效果？](questions/07-dense-retrieval-ann/Q070-ivf-index.md)
- [Q071 · Product Quantization（PQ）是什么？](questions/07-dense-retrieval-ann/Q071-product-quantization.md)
- [Q072 · HNSW 的原理是什么？为什么分层？](questions/07-dense-retrieval-ann/Q072-hnsw-principles.md)
- [Q073 · HNSW 的 M、efConstruction、efSearch 分别控制什么？](questions/07-dense-retrieval-ann/Q073-hnsw-parameters.md)
- [Q074 · HNSW 与 IVF-PQ 如何选？](questions/07-dense-retrieval-ann/Q074-hnsw-vs-ivf-pq.md)
