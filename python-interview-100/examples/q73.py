# 对应题目：Q73 await 的核心语义是什么？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

async def fetch_all(client, urls):
    tasks = [asyncio.create_task(client.get(u)) for u in urls]
    return await asyncio.gather(*tasks)
