# 对应题目：Q55 为什么对象释放后进程 RSS 不一定下降？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import tracemalloc
tracemalloc.start()
# run workload
snapshot = tracemalloc.take_snapshot()
