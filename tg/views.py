import telebot
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


class GetUpdates(APIView):
    def post(self, request, *args, **kwargs):
        """Принимаем апдейт из тг"""""
        webhook = kwargs.get('webhook', None)
        json_str = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        message = update.message
        answer_text = 'Ответ из джанги'
        chat_id = message.from_user.id
        self.send_mes(answer_text, chat_id, webhook)
        return Response()

    @staticmethod
    def send_mes(answer_text, chat_id, token):
        tg_bot = telebot.TeleBot(token)
        tg_bot.send_message(chat_id, answer_text)
