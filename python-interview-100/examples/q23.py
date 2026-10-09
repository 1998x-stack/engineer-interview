# 对应题目：Q23 为什么说函数是一等对象？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def add1(x): return x + 1
ops = {'inc': add1}
print(ops['inc'](3))

class Multiplier:
    def __init__(self, k): self.k = k
    def __call__(self, x): return self.k * x
