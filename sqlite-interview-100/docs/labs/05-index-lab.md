# 索引设计 Lab

构造至少 100k 行且具有偏斜分布的数据，比较以下索引：

```sql
CREATE INDEX idx_ab ON t(a,b);
CREATE INDEX idx_abc ON t(a,b,c);
CREATE INDEX idx_active ON t(a,b) WHERE active=1;
CREATE INDEX idx_expr ON t(lower(email));
```

对每个查询保存 `EXPLAIN QUERY PLAN`、运行时间、返回行数和数据库大小。重点验证：联合索引前缀、covering、partial predicate、expression syntax match。
