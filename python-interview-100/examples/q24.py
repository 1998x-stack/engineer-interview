# 对应题目：Q24 什么是闭包？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def make_multiplier(k):
    def mul(x):
        return k * x
    return mul

times3 = make_multiplier(3)
print(times3(10))
