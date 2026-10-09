# 对应题目：Q08 and / or 为什么不一定返回 bool？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

timeout = user_timeout or 30  # 若 0 是合法值，这可能是 bug

timeout = 30 if user_timeout is None else user_timeout
