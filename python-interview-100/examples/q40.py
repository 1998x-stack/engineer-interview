# 对应题目：Q40 __slots__ 有什么用？有哪些坑？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y
