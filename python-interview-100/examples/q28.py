# 对应题目：Q28 如何实现带参数装饰器？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from functools import wraps

def retry(times):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last = e
            raise last
        return wrapper
    return deco
