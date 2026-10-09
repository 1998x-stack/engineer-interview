# 对应题目：Q27 为什么 decorator 通常需要 functools.wraps？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from functools import wraps

def deco(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
