# 对应题目：Q18 dict.get、setdefault、defaultdict 如何选择？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from collections import defaultdict
index = defaultdict(list)
for word, doc_id in pairs:
    index[word].append(doc_id)
