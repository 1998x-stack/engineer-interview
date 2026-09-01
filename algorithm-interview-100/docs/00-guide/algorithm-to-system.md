# 从 LeetCode 到算法系统

| LeetCode 母题 | 工程约束变化 | 算法岗升级方向 |
|---|---|---|
| LC215 / LC347 Top-K | 数据量 > 内存 | 分片 Local Top-K -> Global Merge，外部排序 |
| LC295 Median Stream | 无限流 / 滑窗 | 双堆 + lazy deletion；近似分位数 sketch |
| LC146 LRU | 线上缓存 | TTL、并发、LFU、分布式一致性、KV Cache 驱逐 |
| LC208 Trie | 搜索提示 | prefix top-k、Radix Tree、FST、热门前缀缓存 |
| LC973 K Closest | 高维向量 | 精确扫描 -> ANN，HNSW/IVF 权衡 |
| LC528 / LC470 Sampling | 训练采样 | alias table、reservoir、importance sampling |
| LC207 Topological | 特征/任务依赖 | DAG 调度、Pipeline、循环依赖检测 |
| LC721 Union-Find | 实体归并 | Entity Resolution、离线批处理、增量合并 |
