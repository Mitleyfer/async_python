import asyncio


max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counts = {
    "Counter 1": 0,
    "Counter 2": 0
}


async def counter(cnt_name, timeout):
    while counts[cnt_name] < max_counts[cnt_name]:
        counts[cnt_name] += 1
        print(f"{cnt_name}: {counts[cnt_name]}")
        await asyncio.sleep(timeout)


async def main():
    tasks = []
    for cnt_name in counts.keys():
        task = asyncio.create_task(counter(cnt_name, 1))
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())

# import asyncio
#
# max_counts = {
#     "Counter 1": 13,
#     "Counter 2": 7
# }
#
# counters = {
#     "Counter 1": 0,
#     "Counter 2": 0
# }
#
#
# async def counter(counter, t):
#     while counters[counter] != max_counts[counter]:
#         counters[counter] += 1
#         await asyncio.sleep(t)
#         print(f'{counter}: {counters[counter]}')
#
#
# async def main():
#     tasks = [asyncio.create_task(counter(i, 1)) for i in counters]
#     [await(i) for i in tasks]
#
#
# asyncio.run(main())
