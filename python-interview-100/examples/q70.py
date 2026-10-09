# 对应题目：Q70 Python 3.14 InterpreterPoolExecutor 是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from concurrent.futures import InterpreterPoolExecutor

def cpu(x):
    return sum(i * i for i in range(x))

with InterpreterPoolExecutor() as ex:
    print(list(ex.map(cpu, [10000, 20000])))
