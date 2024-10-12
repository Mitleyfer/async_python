import asyncio


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    tasks = [read_book(*tpl) for tpl in [("Алекс", 5), ("Мария", 3), ("Иван", 4)]]
    await asyncio.gather(*tasks)


asyncio.run(main())
