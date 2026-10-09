# 对应题目：Q36 property 是如何工作的？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class Temperature:
    def __init__(self, c): self._c = c
    @property
    def celsius(self): return self._c
    @celsius.setter
    def celsius(self, value):
        if value < -273.15: raise ValueError
        self._c = value
