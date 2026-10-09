# 对应题目：Q25 late binding closure 为什么会得到 [2,2,2]？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]

funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])  # [0, 1, 2]
