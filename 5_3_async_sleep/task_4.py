import asyncio
import random

# Не менять.
random.seed(1)


class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


# Тут пишите ваш код
async def check_mail(server):
    response = await server.check_for_new_mail()
    if response == "Ошибка при проверке новых писем.":
        print(response)
        return False
    elif response:
        new_mail = await server.fetch_new_mail()
        print(new_mail)
    elif not response:
        print("Новых писем нет.")
    await asyncio.sleep(1)
    return True


async def main():
    server = MailServer()
    while True:
        result = await check_mail(server)
        if not result:
            break


asyncio.run(main())



# import asyncio
# import random
# 
# # Не менять.
# random.seed(1)
#
#
# class MailServer:
#     def __init__(self):
#         self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]
#
#     async def check_for_new_mail(self):
#         if random.random() < 0.1:
#             return "Ошибка при проверке новых писем."
#         return random.choice([True, False])
#
#     async def fetch_new_mail(self):
#         mail = random.choice(self.mailbox)
#         return f"Новое письмо: {mail}"
#
#
# # Тут пишите ваш код
# async def check_mail(server):
#     while (test := await server.check_for_new_mail()) in [True, False]:
#         print(await server.fetch_new_mail() if test else 'Новых писем нет.')
#         await asyncio.sleep(1)
#     print("Ошибка при проверке новых писем.")
#
#
# async def main():
#     await check_mail(MailServer())
#
#
# asyncio.run(main())
