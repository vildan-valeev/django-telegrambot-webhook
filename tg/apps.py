from django.apps import AppConfig


class TgConfig(AppConfig):
    name = 'tg'

    def ready(self):
        import tg.signals