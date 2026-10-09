# 对应题目：Q79 Semaphore 在 async 服务中解决什么问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

sem = asyncio.Semaphore(20)

async def call_upstream(x):
    async with sem:
        return await client.get(x)
