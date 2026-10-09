# 对应题目：Q56 sys.getsizeof 为什么不是对象“总内存”？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import sys
xs = [b'x' * 1000 for _ in range(100)]
print(sys.getsizeof(xs))  # 主要是 list 自身，不含所有 bytes 内容
