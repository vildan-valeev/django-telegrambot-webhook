__author__ = '@vildan_valeev'

import telebot
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from django.http import HttpResponse
from bot.settings import TOKEN
from .models import User

bot = telebot.TeleBot(TOKEN)


# class UpdateBot(APIView):
#     def post(self, request):
#         # Сюда должны получать сообщения от телеграм и далее обрабатываться ботом
#         json_str = request.body.decode('UTF-8')
#         update = telebot.types.Update.de_json(json_str)
#         bot.process_new_updates([update])

#         return Response({'code': 200})



class UpdateBot(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Бот запущен и работает.")


    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        # if update_id != update.update_id:
        #     bot.process_new_updates([update])
        #     update_id = update.update_id
        bot.process_new_updates([update])

        return Response(b'{"ok":true,"result":[]}')





@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)




# Webhook
# curl https://api.telegram.org/bot<KEY>/getWebhookInfo
# api.telegram.org/bot997719198:AAHZmeqiXr9RHOMTjl2CBSnyFwlK9KUK3-E/setwebhook?url=https://vildan.pythonanywhere.com/api/telegram


# bot.remove_webhook()


# bot.set_webhook(url='https://vildan.pythonanywhere.com/' + TOKEN)

