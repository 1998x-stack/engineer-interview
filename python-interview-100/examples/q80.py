# 对应题目：Q80 如何设计一个生产级 asyncio worker？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

async def worker(queue):
    while True:
        item = await queue.get()
        try:
            async with asyncio.timeout(10):
                await handle(item)
        finally:
            queue.task_done()
