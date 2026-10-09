# WAL 与 Checkpoint Lab

```sql
PRAGMA journal_mode=WAL;
PRAGMA wal_autocheckpoint;
PRAGMA wal_checkpoint(PASSIVE);
```

保持连接 A 的 read transaction 不提交，让连接 B 连续批量写入。周期记录 `db-wal` 大小，并执行 `PRAGMA wal_checkpoint(PASSIVE);`。关闭 A 后再次 checkpoint，观察可回写 frame 的变化。
