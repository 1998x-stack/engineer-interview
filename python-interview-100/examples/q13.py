# 对应题目：Q13 为什么 list.insert(0, x) / pop(0) 慢？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from collections import deque
q = deque()
q.append(1)
q.appendleft(0)
q.popleft()
