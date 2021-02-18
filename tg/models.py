from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id


class TelegramToken(models.Model):
    token = models.CharField(max_length=440, null=True)

    def __str__(self):
        return self.token


class TelegramBot(models.Model):
    title = models.CharField(max_length=440)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dialog = models.CharField(max_length=440, null=True)
    tg_token = models.ForeignKey(TelegramToken, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title