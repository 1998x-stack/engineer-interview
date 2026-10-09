# 对应题目：Q34 __getattribute__ 和 __getattr__ 有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class Proxy:
    def __init__(self, target):
        object.__setattr__(self, '_target', target)

    def __getattr__(self, name):
        return getattr(self._target, name)
