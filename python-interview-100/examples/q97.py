# 对应题目：Q97 手写 LRU Cache，为什么常用 HashMap + Doubly Linked List？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

# node: key, value, prev, next
# map[key] -> node
# get: lookup + move_to_front
# put: update/insert + evict_tail
