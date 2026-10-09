# Contributing

1. 一题一个 Markdown；不要改变 Q 编号。
2. 新增事实应注明来源；PDF 原始内容与新增内容保持分区。
3. 所有代码示例优先保证 point-in-time correctness。
4. 新模型结论必须与强 baseline 在相同 backtest 协议下比较。
5. 提交前运行 `pytest -q` 与 `python scripts/validate_repo.py`。
