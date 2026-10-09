# 对应题目：Q10 global 和 nonlocal 有什么区别？LEGB 如何工作？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

x = 1

def outer():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc
