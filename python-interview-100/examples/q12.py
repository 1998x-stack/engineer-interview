# 对应题目：Q12 list.append 为什么是摊还 O(1)？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

xs = []
for i in range(1_000_000):
    xs.append(i)
