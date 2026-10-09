# 对应题目：Q20 浅拷贝和深拷贝有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import copy
a = [[1], [2]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0].append(9)
print(b)  # [[1, 9], [2]]
print(c)  # [[1], [2]]
