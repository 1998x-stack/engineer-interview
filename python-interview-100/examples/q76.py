# 对应题目：Q76 为什么不能随便吞 asyncio.CancelledError？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

async def worker():
    resource = await acquire()
    try:
        await run(resource)
    finally:
        await release(resource)
