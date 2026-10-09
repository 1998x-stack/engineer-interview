# 对应题目：Q96 FastAPI async def endpoint 为什么仍可能很慢？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

@app.get('/x')
async def x():
    data = await async_client.get(...)  # 真正 async
    return data
