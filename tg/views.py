__author__ = '@vildan_valeev'

import telebot
from rest_framework.views import  APIView
from rest_framework.response import Response
from bot.settings import TOKEN

bot = telebot.TeleBot(TOKEN)


class UpdateBot(APIView):
    def post(self, request):
        # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return Response({'code': 200})



@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


# Webhook
# curl https://api.telegram.org/bot<KEY>/getWebhookInfo
# api.telegram.org/bot997719198:AAEi_fXpSJEhni6Lpsc5O1Q7abl5sBE7JXc/setwebhook?url=https://c425ee31.ngrok.io

