import asyncio


async def countdown(name, seconds):
    while seconds:
        if name == 'Квест на поиск сокровищ':
            print(f"{name}: Осталось {seconds} сек. Найди скрытые сокровища!")
        elif name == 'Побег от дракона':
            print(f"{name}: Осталось {seconds} сек. Беги быстрее, дракон на хвосте!")
        await asyncio.sleep(1)
        seconds -= 1
    print(f"{name}: Задание выполнено! Что дальше?")


# async def main():
#     treasure_hunt = asyncio.create_task(countdown('Квест на поиск сокровищ', 10))
#     dragon_escape = asyncio.create_task(countdown('Побег от дракона', 5))
#     await asyncio.gather(*[treasure_hunt, dragon_escape])
#
#
# asyncio.run(main())
# 
# import asyncio
#
# quests = [
#     {'name': 'Квест на поиск сокровищ', 'seconds': 10, 'text': 'Найди скрытые сокровища!'},
#     {'name': 'Побег от дракона', 'seconds': 5, 'text': f'Беги быстрее, дракон на хвосте!'}
# ]
#
#
# async def countdown(name, seconds, text):
#     for i in range(seconds, 0, -1):
#         print(f'{name}: Осталось {i} сек. {text}')
#         await asyncio.sleep(1)
#
#     print(f"{name}: Задание выполнено! Что дальше?")
