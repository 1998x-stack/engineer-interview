# 对应题目：Q48 context manager 的核心协议是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

class LockCtx:
    def __enter__(self):
        self.lock.acquire(); return self
    def __exit__(self, exc_type, exc, tb):
        self.lock.release()
