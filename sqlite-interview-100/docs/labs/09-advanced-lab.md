# 高级能力 Lab

建立同一批文档的普通表和 FTS5 表，对比 `LIKE '%term%'` 与 `MATCH`。再验证：

```sql
SELECT json_valid(payload), json_extract(payload,'$.id') FROM docs;

INSERT INTO user(id,name) VALUES(1,'A')
ON CONFLICT(id) DO UPDATE SET name=excluded.name;
```

为 REPLACE/UPSERT 配置 trigger 或 child FK，观察两种冲突处理的副作用差异。
