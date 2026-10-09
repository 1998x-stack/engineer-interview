# 对应题目：Q82 Any 和 object 有什么区别？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

def use_obj(x: object) -> str:
    return str(x)

def unsafe(x: Any):
    return x.whatever.deep.call()
