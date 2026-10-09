# 对应题目：Q29 lambda 与普通 def 的区别是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

users = [{'name': 'a', 'score': 9}, {'name': 'b', 'score': 7}]
users.sort(key=lambda u: u['score'], reverse=True)
