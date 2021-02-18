__author__ = '@vildan_valeev'

import telebot
from rest_framework.views import APIView
from rest_framework.response import Response
# from bot.settings import TOKEN

# bot = telebot.TeleBot(TOKEN)


class UpdateBot(APIView):
    def post(self, request):

        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        # bot.process_new_updates([update])
        print(update)
        return Response({'code': 200})


# @bot.message_handler(commands=['start'])
# def start(message):
#     # автоответ на команду
#     bot.reply_to(message, f'Привет, ' + message.from_user.first_name + ' это сообщение из джанго проекта.')
#

# # обработчик будет вызван при команде /voice
# @dp.message_handler(commands=['voice'])
# async def process_voice_command(message: types.Message):
#     text = "Чо надо?"
#     await message.answer(text=text)