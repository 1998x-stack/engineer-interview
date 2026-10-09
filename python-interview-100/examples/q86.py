# 对应题目：Q86 dataclass 解决了什么？有哪些陷阱？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from dataclasses import dataclass, field

@dataclass(slots=True)
class User:
    name: str
    tags: list[str] = field(default_factory=list)
