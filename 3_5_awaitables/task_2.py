import asyncio

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}


async def study_course(student, course, steps, speed):
    reading_time = round(steps/speed, 2)
    print(f"{student} начал проходить курс {course}.")
    await asyncio.sleep(int(reading_time))
    print(f"{student} прошел курс {course} за {reading_time} ч.")


async def main():
    # Создание задач с помощью asyncio.create_task для каждого студента
    tasks_1 = asyncio.create_task(study_course("Алекс", **students["Алекс"]))
    tasks_2 = asyncio.create_task(study_course("Мария", **students["Мария"]))
    tasks_3 = asyncio.create_task(study_course("Иван", **students["Иван"]))

    # Ожидание завершения каждой задачи индивидуально
    await tasks_1
    await tasks_2
    await tasks_3


asyncio.run(main())


# import asyncio
#
#
# async def study_course(student, course, step, speed):
#     print(f"{student} начал проходить курс {course}.")
#     time = round(step / speed, 2)
#     await asyncio.sleep(time)
#     print(f"{student} прошел курс {course} за {time} ч.")
#
#
# async def main():
#     tasks = [asyncio.create_task(study_course(k, *v.values())) for k, v in students.items()]
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())
