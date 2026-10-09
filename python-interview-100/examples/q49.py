# 对应题目：Q49 with 为什么比手写 try/finally 更好？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from contextlib import ExitStack
with ExitStack() as stack:
    files = [stack.enter_context(open(p)) for p in paths]
    process(files)
