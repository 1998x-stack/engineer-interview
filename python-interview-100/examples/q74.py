# 对应题目：Q74 为什么 async 函数里 time.sleep 是严重问题？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

async def bad():
    time.sleep(1)

async def good():
    await asyncio.sleep(1)
