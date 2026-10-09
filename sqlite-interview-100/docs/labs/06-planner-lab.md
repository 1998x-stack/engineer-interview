# Query Planner Lab

```sql
.eqp on
EXPLAIN QUERY PLAN SELECT ...;
ANALYZE;
PRAGMA optimize;
SELECT * FROM sqlite_stat1;
```

准备“低基数索引 + 高基数索引 + 偏斜数据”场景，比较 ANALYZE 前后计划。对 correlated subquery 记录 outer rows × inner loops，避免只凭 SQL 外观判断。
