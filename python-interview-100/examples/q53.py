# 对应题目：Q53 什么是 reference cycle？循环 GC 为什么需要它？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

a = []
b = []
a.append(b)
b.append(a)
del a, b
# cyclic GC 可发现不可达环
