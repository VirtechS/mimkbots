import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
token = "(gtoken)"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

print("Бот запущен")
# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "!help":
                write_msg(event.user_id, "Команнды бота:\n!Понедельник - рассписание на понедельник\n!Вторник - рассписание на вторник\n!Среда - рассписание на среду\n!Четверг - рассписание на четверг\n!Пятница - рассписание на пятницу\n!Суббота - рассписание на субботу\n(P.S Рассписание стандартное)\n<br> !Замены число.меся.год\n Пример: !Замены 23.01.2020\n<br>!Практика1С - Методички по 1С")
            if request == "!Понедельник":
                write_msg(event.user_id, "1) Таз\n 2)БЖ\n3)Таз")
            if request == "!Вторник":
                write_msg(event.user_id, "1) Вавил\n 2)Физра\n3)Вавил")
            if request == "!Среда":
                write_msg(event.user_id, "1) Анур\n 2)Вавил\n3)Вавил")
            if request == "!Четверг":
                write_msg(event.user_id, "1) Вавил\n 2)Вавил\n3)Анур")
            if request == "!Пятница":
                write_msg(event.user_id, "1) Анур\n 2)Анур\n3)Анур")
            if request == "!Суббота":
                write_msg(event.user_id, "1) Анур\n 2)Анур\n3)Таз")
            if request == "!Практика1С":
                write_msg(event.user_id, "https://yadi.sk/d/iqsqUNoWD_rERA")
            if request == "!Практика1C":
                write_msg(event.user_id, "https://yadi.sk/d/iqsqUNoWD_rERA")
            if request == "!Замены 23.01.2020":
                write_msg(event.user_id, "Завтра на 1,2 пару идет вторая подгруппа на ВГ а первая группа спит, на 3-4 пару идет 1 группа на ВГ а 2 группа к Ануру")
