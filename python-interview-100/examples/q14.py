# 对应题目：Q14 Python dict 查找为什么平均 O(1)？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

d = {'user_id': 42}
print(d['user_id'])

class Key:
    def __hash__(self): ...
    def __eq__(self, other): ...
