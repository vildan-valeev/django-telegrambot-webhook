from django.contrib import admin
from .models import User, TelegramToken, TelegramBot

admin.site.register(User)


class TelegramTokenAdmin(admin.ModelAdmin):
    list_display = ('id', 'token',)
    list_display_links = ('id', 'token',)


admin.site.register(TelegramToken, TelegramTokenAdmin)
admin.site.register(TelegramBot)
