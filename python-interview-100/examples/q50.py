# 对应题目：Q50 contextlib.contextmanager 是如何把 generator 变成上下文管理器的？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

from contextlib import contextmanager

@contextmanager
def transaction(db):
    tx = db.begin()
    try:
        yield tx
        tx.commit()
    except:
        tx.rollback()
        raise
