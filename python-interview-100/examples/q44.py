# 对应题目：Q44 为什么 generator 通常更省内存？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

squares = (x * x for x in range(10_000_000))
for x in squares:
    consume(x)
