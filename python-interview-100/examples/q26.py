# 对应题目：Q26 装饰器本质是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def trace(fn):
    def wrapper(*args, **kwargs):
        print('call', fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@trace
def add(a, b): return a + b
