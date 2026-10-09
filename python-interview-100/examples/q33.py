# 对应题目：Q33 Python 的“private”是怎么实现的？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class A:
    def __init__(self):
        self._internal = 1
        self.__mangled = 2

a = A()
print(a._A__mangled)
