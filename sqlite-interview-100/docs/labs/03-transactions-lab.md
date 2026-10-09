# 事务与并发双连接 Lab

必须开两个终端 A/B 连接同一数据库。

A：
```sql
BEGIN;
SELECT * FROM demo WHERE id=1;
```

B：
```sql
BEGIN IMMEDIATE;
UPDATE demo SET value=value+1 WHERE id=1;
COMMIT;
```

回 A 尝试 UPDATE，并分别在 rollback/WAL 下观察错误码与可见性。再把 A 改成 `BEGIN IMMEDIATE`，比较“竞争发生在事务入口还是升级阶段”。
