# 对应题目：Q54 weakref 适合解决什么问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

import weakref
class Item: pass
x = Item()
r = weakref.ref(x)
assert r() is x
del x
# r() 之后可能为 None
