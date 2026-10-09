# 对应题目：Q37 MRO 是什么？C3 linearization 解决什么问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print(D.__mro__)
