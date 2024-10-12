import asyncio


async def async_operation():
    print("Начало асинхронной операции.")
    try:
        await asyncio.sleep(2)
        print("Асинхронная операция успешно завершилась.")
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise


async def main():
    print("Главная корутина запущена.")
    task = asyncio.create_task(async_operation())
    try:
        await asyncio.sleep(0.1)
        print("Попытка отмены Task.")
        task.cancel()
        result = await task
        print("Результат Task:", result)
    except asyncio.CancelledError:
        print("Обработка исключения: Task был отменен.")
    if task.cancelled():
        print("Проверка: Task был отменен.")
    else:
        print("Проверка: Task не был отменен.")
    print("Главная корутина завершена.")

asyncio.run(main())


# import asyncio
#
#
# async def async_operation():
#     print("Начало асинхронной операции.")
#     try:
#         # Имитация асинхронной операции с задержкой
#         await asyncio.sleep(2)
#         print("Асинхронная операция успешно завершилась.")
#         return "success"
#     except asyncio.CancelledError:
#         print("Асинхронная операция была отменена в процессе выполнения.")
#         raise
#

# async def main():
#     print("Главная корутина запущена.")
#     # Создаем Future с помощью ensure_future, обернув асинхронную операцию
#     future = asyncio.ensure_future(async_operation())
#
#     # Даём немного времени на старт асинхронной операции
#     await asyncio.sleep(0.1)
#     print("Попытка отмены Future.")
#
#     # Отменяем Future до его завершения
#     future.cancel()
#
#     try:
#         # Пытаемся получить результат Future
#         result = await future
#         print("Результат Future:", result)
#     except asyncio.CancelledError:
#         # Обработка исключения, возникающего при отмене Future
#         print("Обработка исключения: Future был отменен.")
#
#     # Проверяем, отменился ли Future
#     if future.cancelled():
#         print("Проверка: Future был отменен.")
#     else:
#         print("Проверка: Future не был отменен.")
#
#     print("Главная корутина завершена.")
#
#
# asyncio.run(main())


# import asyncio
#
#
# async def async_operation(delay: int) -> str:
#     try:
#         print("Начало асинхронной операции.")
#         await asyncio.sleep(delay)
#         print("Асинхронная операция успешно завершилась.")
#         return True
#     except asyncio.CancelledError:
#         print("Асинхронная операция была отменена в процессе выполнения.")
#         raise
#
#
# async def cancel_future(future: asyncio.Future) -> str:
#     await asyncio.sleep(0.1)
#     print("Попытка отмены Future.")
#     future.cancel()
#
#
# async def main():
#     print("Главная корутина запущена.")
#     future = asyncio.ensure_future(async_operation(delay=5))
#     try:
#         task_cancel = asyncio.create_task(cancel_future(future))
#         result = await asyncio.gather(*[future, task_cancel])
#     except asyncio.CancelledError:
#         print("Обработка исключения: Future был отменен.")
#     if future.cancelled():
#         print("Проверка: Future был отменен.")
#     print("Главная корутина завершена.")
#
#
# asyncio.run(main())
