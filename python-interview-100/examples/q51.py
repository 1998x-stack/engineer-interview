# 对应题目：Q51 CPython 如何管理对象生命周期？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import gc, sys
x = []
print(sys.getrefcount(x))  # 注意调用本身会临时增加引用
print(gc.is_tracked(x))
