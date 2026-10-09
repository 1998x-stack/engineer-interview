# Q75 asyncio.gather 与 TaskGroup 怎么选？
import asyncio

async def job1():
    await asyncio.sleep(0.01)
    return "job1"

async def job2():
    await asyncio.sleep(0.01)
    return "job2"

async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(job1())
        t2 = tg.create_task(job2())
    print(t1.result(), t2.result())

if __name__ == "__main__":
    asyncio.run(main())
