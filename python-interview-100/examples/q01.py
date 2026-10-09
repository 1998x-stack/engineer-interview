# 对应题目：Q01 Python 是解释型语言还是编译型语言？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import dis

def add(a, b):
    return a + b

dis.dis(add)
