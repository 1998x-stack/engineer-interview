# 系统设计答题路线

回答 Memcached 系统设计题时按固定顺序：

1. **Workload**：QPS、GET/SET 比、item 平均/P99 大小、TTL、热点偏斜。
2. **Working set**：真正需要留在 Cache 的 unique hot items 数量。
3. **Capacity**：分别计算 RAM、CPU、Network、P99 四个下界。
4. **Routing**：client-side hashing 还是 built-in proxy；如何发布 membership。
5. **Origin**：hit 下降 1%、单节点故障、全量 cold start 时 DB/API 能否承受。
6. **Resilience**：coalescing、stale、L1、rate limit、circuit breaker、warmup。
7. **Observability**：hit/miss、per-slab evictions、connections、P99、origin QPS。
8. **Change safety**：扩缩容、rolling deploy、Hash Ring 变更和回滚。

核心公式不是一个固定数字，而是：

```text
nodes_required = max(nodes_by_RAM, nodes_by_CPU, nodes_by_network, nodes_by_P99)
```

之后再乘以故障与运营 headroom。
