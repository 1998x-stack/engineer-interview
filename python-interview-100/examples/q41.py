# 对应题目：Q41 iterable 和 iterator 有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

xs = [10, 20]
it = iter(xs)
print(next(it))
print(next(it))
# next(it) -> StopIteration
