# 附录 B · 系统设计答题模板

1. **需求**：文档规模、QPS、TopK、p99、freshness、update rate、权限、安全、业务目标。
2. **估算**：索引大小、向量大小、网络 fan-out、模型推理次数、存储副本。
3. **数据面**：ingestion、清洗、schema、index build、version、publish、backfill。
4. **查询面**：query understanding、recall、fusion、rank、rerank、fetch。
5. **分布式**：sharding、replica、routing、timeout、partial result、hot shard。
6. **一致性**：CDC、幂等、version、delete、reconciliation。
7. **评估**：Recall/NDCG + p95/p99 + cost + A/B guardrails。
8. **降级**：model timeout、vector service down、feature miss、shard slow 的 fallback。

## 白板节奏（45 分钟）

- 0–5 分钟：澄清目标与 SLO。
- 5–10 分钟：数量级估算。
- 10–25 分钟：主链路。
- 25–35 分钟：瓶颈、数据一致性、索引更新。
- 35–42 分钟：指标、实验、回滚。
- 42–45 分钟：总结 trade-off。
