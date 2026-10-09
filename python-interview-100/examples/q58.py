# 对应题目：Q58 circular import 为什么会产生 partially initialized module？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

# a.py: from b import B
# b.py: from a import A
# 两个模块在初始化阶段互相要求对方已经完成定义
