# 对应题目：Q04 Python 是 pass-by-value 还是 pass-by-reference？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def mutate(x):
    x.append(3)

def rebind(x):
    x = [100]

a = [1, 2]
mutate(a)
rebind(a)
print(a)  # [1, 2, 3]
