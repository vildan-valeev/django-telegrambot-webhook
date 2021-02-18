__author__ = '@vildan_valeev'

import requests
import telebot
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# from bot.settings import TOKEN
TOKEN = None


class GetUpdates(CreateAPIView):
    def post(self, request, *args, **kwargs):
        # TODO: enable logging
        # print(f'{args=}')
        # print(f'{kwargs=}')
        # print(f'{type(request.data)} {request.data=}')
        # print(request.data['message']['from']['id'])
        # print(f'{request.path=}')
        webhook = kwargs.get('webhook', None)
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        message = update.message
        # # bot.process_new_updates([update])
        #
        # print(f'{message.from_user.id}')
        # print(f'{type(webhook)} {webhook=}')
        # # chat_id = request.data['message']['from']['id']
        #
        #
        # print(f'{type(json_str)} {json_str=}')
        # print(f'{type(update)} {update=}')
        #
        #
        # # TODO: send_message as json response
        answer_text = 'Ответ из джанги'
        chat_id = message.from_user.id
        # print(chat_id, type(chat_id))
        self.send_mes(answer_text, chat_id, webhook)

        return Response({'code': 200})

    @staticmethod
    def send_mes(answer_text, chat_id, token):
        tg_bot = telebot.TeleBot(token)
        r = tg_bot.send_message(chat_id, answer_text)
        print(r)

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
