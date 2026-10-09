# 对应题目：Q47 为什么 generator/iterator 通常只能消费一次？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

g = (x for x in range(3))
print(list(g))
print(list(g))  # []
