# 对应题目：Q35 什么是 descriptor？为什么它如此重要？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class Positive:
    def __set_name__(self, owner, name):
        self.name = '_' + name
    def __get__(self, obj, owner=None):
        if obj is None: return self
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value < 0: raise ValueError('must be >= 0')
        setattr(obj, self.name, value)
