# 对应题目：Q84 TypeVar / 新泛型语法解决什么问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from collections.abc import Sequence

def first[T](xs: Sequence[T]) -> T:
    return xs[0]
