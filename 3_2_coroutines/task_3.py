import asyncio


async def generate(number):
    print(f"Корутина generate с аргументом {number}")


async def main():
    tasks = [generate(i) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
