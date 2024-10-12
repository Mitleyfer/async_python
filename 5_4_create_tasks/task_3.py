import asyncio

news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
    "Разработчики анонсировали новую игру в жанре RPG",
    "Исследователи описали новый вид насекомых"
]


async def analyze_news(keyword, news_list, delay):
    for header in news_list:
        if keyword in header:
            print(f"Найдено соответствие для '{keyword}': {header}")
            await asyncio.sleep(delay)


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news('COVID-19', news_list, 1))
    task2 = asyncio.create_task(analyze_news('игр', news_list, 1))
    task3 = asyncio.create_task(analyze_news('новый вид', news_list, 1))

    # Ожидаем выполнения всех задач
    await asyncio.gather(*[task1, task2, task3])


asyncio.run(main())
