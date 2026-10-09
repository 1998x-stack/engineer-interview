# Contributing

## 内容修改原则

1. 不把二手面经包装成官方真题。
2. 任何时点数据必须包含日期与一手来源。
3. 修改某题时保持 Question Schema 的 11 个主章节。
4. 公式必须解释变量与成立条件。
5. 提交前运行 `python scripts/validate_repo.py`。

## PR 建议

- 一个 PR 尽量只处理一个主题（例如 Q021-Q030 的图形一致性）。
- 在 PR 描述中写明：问题、修改、证据、可能影响的关联题。
- 涉及政策数据更新时，同时修改 `data/sources.json` 与热点题。
