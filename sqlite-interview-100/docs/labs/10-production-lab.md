# 生产压测与故障注入 Lab

不要只测 QPS。至少记录：

- transaction duration p50/p95/p99
- `SQLITE_BUSY` / `BUSY_SNAPSHOT` 次数
- WAL 文件大小与 checkpoint 结果
- top SQL 的 EQP
- DB/page/freelist 增长
- crash/restart 后完整性检查

故障注入建议：制造 2 秒长 writer、长期 reader、100 producer writer queue、百万行批量写、偏斜查询计划，并验证优化前后的指标变化。
