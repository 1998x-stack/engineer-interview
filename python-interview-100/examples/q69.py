# 对应题目：Q69 什么是 race condition？如何系统治理？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

# check-then-act race
if order.status == 'pending':
    charge(order)
    order.status = 'paid'
# 多 worker 下需要更强的一致性机制
