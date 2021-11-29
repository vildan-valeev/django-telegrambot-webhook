import requests
from bot.settings import DOMAIN
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from tg.models import TelegramBot


@receiver(post_save, sender=TelegramBot)
def set_webhook(sender, instance, created, **kwargs):
    print('setWebhook')
    print(instance.id, instance.title, instance.tg_token)

    url = f"https://api.telegram.org/bot{instance.tg_token}/setwebhook?url={DOMAIN}/webhook/{instance.tg_token}/"
    response = requests.request("GET", url, )
    print(response.text)

    return response


@receiver(post_delete, sender=TelegramBot)
def delete_webhook(sender, instance, **kwargs):
    url = f"https://api.telegram.org/bot{instance.tg_token}/deleteWebhook"
    response = requests.request("GET", url, )
    print(response.text)
    return response


def getinfo_webhook():
    bot_token = ''
    url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"
    response = requests.request("GET", url, )
    print(response.text)
    return response
