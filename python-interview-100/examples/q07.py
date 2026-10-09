# 对应题目：Q07 Python 的 truthy / falsy 规则是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class Bag:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)

print(bool(Bag([])))  # False
