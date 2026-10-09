# 对应题目：Q60 monkey patching 什么时候有用，为什么危险？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from unittest.mock import patch

with patch('myapp.service.time.time', return_value=0):
    assert deterministic_result()
