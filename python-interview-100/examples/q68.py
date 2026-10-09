# 对应题目：Q68 fork、spawn、forkserver 有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import multiprocessing as mp
print(mp.get_start_method())
# 必要时显式选择 context，而不是假定全平台相同
