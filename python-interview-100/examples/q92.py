# 对应题目：Q92 list comprehension 为什么经常比显式 for 更快？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

result = [x * 2 for x in xs if x > 0]
# 清晰时使用；复杂分支请展开为普通循环
