# 对应题目：Q99 1 亿 URL 找 Top-K，如何设计？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

# exact, memory allows
from collections import Counter
from heapq import nlargest
counts = Counter(stream)
print(nlargest(k, counts.items(), key=lambda kv: kv[1]))
