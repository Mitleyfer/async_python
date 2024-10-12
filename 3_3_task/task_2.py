import asyncio


async def print_with_delay(num):
    print(f'Coroutine {num} is done')
    await asyncio.sleep(1)


async def main():
    tasks = [asyncio.create_task(print_with_delay(i)) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
