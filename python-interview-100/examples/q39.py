# 对应题目：Q39 什么是 metaclass？什么时候真的需要？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class Registry(type):
    classes = {}
    def __new__(mcls, name, bases, ns):
        cls = super().__new__(mcls, name, bases, ns)
        mcls.classes[name] = cls
        return cls
