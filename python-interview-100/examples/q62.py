# 对应题目：Q62 “有 GIL 所以不需要锁”为什么是错的？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

lock = threading.Lock()
with lock:
    if key not in cache:
        cache[key] = build()
