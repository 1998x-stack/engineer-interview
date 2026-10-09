# 对应题目：Q93 为什么 NumPy 往往比 Python for loop 快很多？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import numpy as np
a = np.arange(1_000_000, dtype=np.float64)
b = a * 2 + 1
