# 对应题目：Q21 *args 和 **kwargs 的本质是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def f(a, *args, **kwargs):
    print(a, args, kwargs)

params = {'debug': True}
f(1, 2, 3, **params)
