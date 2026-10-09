# 对应题目：Q45 generator.send() 有什么语义？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def accumulator():
    total = 0
    while True:
        x = yield total
        total += x

g = accumulator()
next(g)
print(g.send(5))  # 5
