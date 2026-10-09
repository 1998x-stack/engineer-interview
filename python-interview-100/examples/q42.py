# 对应题目：Q42 iter(x) 实际发生了什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class CountDown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0: raise StopIteration
        self.n -= 1
        return self.n + 1
