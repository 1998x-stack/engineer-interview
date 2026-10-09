# 对应题目：Q78 async 能解决 CPU-bound 吗？
# 这是书中最小实验；部分示例可能含教学用省略号/占位符，请按题目说明补全。

async def endpoint():
    result = await loop.run_in_executor(cpu_pool, heavy_compute, payload)
    return result
