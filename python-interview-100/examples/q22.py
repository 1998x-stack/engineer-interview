# 对应题目：Q22 positional-only 与 keyword-only 参数解决什么问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def connect(host, /, port=443, *, timeout=5, verify=True):
    ...

connect('example.com', timeout=2)
