# 对应题目：Q38 super() 为什么不是“调用父类”？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class A:
    def f(self): print('A')
class B(A):
    def f(self):
        print('B')
        super().f()
