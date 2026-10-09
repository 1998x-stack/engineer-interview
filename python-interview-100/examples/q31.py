# 对应题目：Q31 __new__ 和 __init__ 有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class PositiveInt(int):
    def __new__(cls, value):
        value = max(0, int(value))
        return super().__new__(cls, value)
