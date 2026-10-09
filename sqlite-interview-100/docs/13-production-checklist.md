# 生产排障 Checklist

- **database is locked**：记录事务开始/结束；找最长 read/write transaction；检查网络 I/O 是否在事务内。
- **WAL 过大**：找长期 reader；确认 statement/cursor 是否及时结束；检查 checkpoint 策略。
- **查询突然变慢**：`EXPLAIN QUERY PLAN`；检查统计新鲜度；`PRAGMA optimize`；确认数据分布是否变化。
- **索引没使用**：确认 expression/partial predicate 是否匹配；检查选择性、affinity、排序与覆盖。
- **批量写慢**：显式 transaction + prepared statement reuse + batching；评估 index/trigger/synchronous 成本。
- **数据库异常**：先复制现场；不要随意删除 `-wal`/`-journal`；再运行 `quick_check` / `integrity_check` / `foreign_key_check`。
- **Schema migration**：逐版本升级；在真实旧版本库回放；检查 feature compatibility。
- **FTS 搜索异常**：检查 tokenizer、external content 同步、rebuild/trigger 与 SQLite 构建能力。
