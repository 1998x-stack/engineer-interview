# 对应题目：Q43 generator 与普通函数有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def read_numbers():
    for i in range(3):
        yield i

g = read_numbers()
print(next(g))
