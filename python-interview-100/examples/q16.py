# 对应题目：Q16 为什么实现 __eq__ 后必须认真考虑 __hash__？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class UserKey:
    def __init__(self, uid): self.uid = uid
    def __eq__(self, other):
        return isinstance(other, UserKey) and self.uid == other.uid
    def __hash__(self):
        return hash(self.uid)
