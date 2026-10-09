# Contributing

## 内容 PR 要求

1. 一个 PR 尽量只修改一个主题或少量相关题目。
2. 结论必须写清 SQLite 版本、journal mode、table 类型等前提。
3. 优先引用 `sqlite.org` 官方文档。
4. 性能结论必须提供 `EXPLAIN QUERY PLAN` 或 benchmark 依据，不写“永远更快”。
5. 新增实验应能在 sqlite3 CLI 中最小复现。
6. 修改后运行 `python scripts/validate_repo.py`。

## 单题 Markdown 结构

保持：考点 -> 30 秒回答 -> 原理 -> 深入分析 -> 实验 -> 误区 -> 追问 -> Checklist -> 相关题 -> 官方资料。
