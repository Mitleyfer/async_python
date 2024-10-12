import asyncio


max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

counts = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}


async def counter(cnt_name):
    while counts[cnt_name] < max_counts[cnt_name]:
        counts[cnt_name] += 1
        print(f"{cnt_name}: {counts[cnt_name]}")
        await asyncio.sleep(delays[cnt_name])


async def main():
    tasks = [counter(cnt_name) for cnt_name in counts.keys()]
    await asyncio.gather(*tasks)


asyncio.run(main())
