import requests
from bot.settings import DOMAIN
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from tg.models import TelegramBot


@receiver(post_save, sender=TelegramBot)
def setWebhook(sender, instance, created, **kwargs):
    print('setWebhook')
    print(instance.id, instance.title, instance.tg_token)
    if created:
        url = f"http://api.telegram.org/bot{instance.tg_token}/setwebhook?url={DOMAIN}"
        print(url)
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

        return response


@receiver(post_save, sender=TelegramBot)
def updateWebhook(sender, instance, created, **kwargs):
    print('updateWebhook')
    if created == False:
        url = f"http://api.telegram.org/bot{instance.tg_token}/setwebhook?url={DOMAIN}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

        return response


@receiver(post_delete, sender=TelegramBot)
def deleteWebhook(sender, instance, **kwargs):
    payload = {}
    headers = {}
    url = f"https://api.telegram.org/bot{instance.tg_token}/deleteWebhook"
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return response


def getinfoWebhook():
    bot_token = '1577812306:AAESS6a5ge3-sDkaKSz8VgJz2g_I8LeTzSE'
    url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return response
