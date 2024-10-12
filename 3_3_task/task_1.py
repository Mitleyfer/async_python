import asyncio


async def corut_1():
    await asyncio.sleep(1)
    print("Coroutine 1 is done")


async def corut_2():
    await asyncio.sleep(1)
    print("Coroutine 2 is done")


async def corut_3():
    await asyncio.sleep(1)
    print("Coroutine 3 is done")


async def main():
    tasks = [asyncio.create_task(corut_1()), asyncio.create_task(corut_2()), asyncio.create_task(corut_3())]
    await asyncio.gather(*tasks)


asyncio.run(main())
