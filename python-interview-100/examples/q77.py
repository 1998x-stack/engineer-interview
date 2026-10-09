# Q77 async code 中如何调用阻塞函数？
import asyncio
import time

def blocking_sdk_call(arg):
    time.sleep(0.05)
    return f"done: {arg}"

async def main():
    result = await asyncio.to_thread(blocking_sdk_call, "demo")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
