# 对应题目：Q63 Python 3.14 free-threaded CPython 改变了什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import sys
if hasattr(sys, '_is_gil_enabled'):
    print('GIL enabled:', sys._is_gil_enabled())
