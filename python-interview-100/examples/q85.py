# 对应题目：Q85 ParamSpec 为什么适合给装饰器做 typing？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from typing import Callable, ParamSpec, TypeVar
P = ParamSpec('P')
R = TypeVar('R')

def deco(fn: Callable[P, R]) -> Callable[P, R]:
    ...
