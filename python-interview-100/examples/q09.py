# 对应题目：Q09 为什么 mutable default argument 是经典陷阱？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def bad(x, items=[]):
    items.append(x)
    return items

print(bad(1))
print(bad(2))  # [1, 2]

def good(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items
