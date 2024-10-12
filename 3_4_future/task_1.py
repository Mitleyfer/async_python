import asyncio


async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    future = asyncio.Future()
    if not future.done():
        print("Состояние Task до выполнения: Ожидание")
    else:
        print("Состояние Task после выполнения: Ожидание")
    print("Задача запущена, ожидаем завершения...")
    result = await set_future_result("Успех", 2)
    future.set_result(result)
    if future.done():
        print("Состояние Task после выполнения: Завершено")
    else:
        print("Состояние Task после выполнения: Ожидание")
    return future.result()


async def main():
    result = await create_and_use_future()
    print("Результат из Task:", result)


asyncio.run(main())
