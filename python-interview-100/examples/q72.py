# 对应题目：Q72 coroutine、Task、Future 分别是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

async def work(): return 42

async def main():
    coro = work()
    task = asyncio.create_task(coro)
    print(await task)
