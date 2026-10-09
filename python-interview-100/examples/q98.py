# 对应题目：Q98 100GB 日志不能进内存，如何处理？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from collections import Counter
counts = Counter()
with open(path, encoding='utf-8', errors='replace') as f:
    for line in f:
        counts[extract_key(line)] += 1
