# 对应题目：Q46 yield from 不只是语法糖吗？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def child():
    yield 1
    return 99

def parent():
    result = yield from child()
    print('child returned', result)
