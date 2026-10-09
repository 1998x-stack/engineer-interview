# 对应题目：Q83 Protocol 解决了什么问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from typing import Protocol

class Closable(Protocol):
    def close(self) -> None: ...

def shutdown(x: Closable) -> None:
    x.close()
