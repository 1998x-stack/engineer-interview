# 对应题目：Q94 如何系统定位 Python memory leak？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

tracemalloc.start()
before = tracemalloc.take_snapshot()
run_workload()
after = tracemalloc.take_snapshot()
for stat in after.compare_to(before, 'lineno')[:20]:
    print(stat)
