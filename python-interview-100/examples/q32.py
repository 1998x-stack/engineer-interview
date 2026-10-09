# 对应题目：Q32 实例方法、classmethod、staticmethod 如何选择？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class User:
    def __init__(self, name): self.name = name

    @classmethod
    def from_email(cls, email):
        return cls(email.split('@')[0])

    @staticmethod
    def valid_name(name):
        return bool(name.strip())
