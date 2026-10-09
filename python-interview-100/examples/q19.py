# 对应题目：Q19 set 为什么能高效查重？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def has_duplicate(xs):
    seen = set()
    for x in xs:
        if x in seen:
            return True
        seen.add(x)
    return False
