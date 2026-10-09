# 对应题目：Q06 None 到底是什么？为什么推荐 is None？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

_MISSING = object()

def f(value=_MISSING):
    if value is _MISSING:
        return 'argument not provided'
    if value is None:
        return 'explicit None'
