from django.urls import path
from .views import UpdateBot

app_name = 'tg'

urlpatterns = [
    path('1627048801:AAEUbgX0wnaH3-97GH4TE-2WVpeqI6hDl4I/', UpdateBot.as_view(), name='update'),
    path('1668462979:AAG9TCoWzriJEWULw1K8hzztlIvJyGQiRBA/', UpdateBot.as_view(), name='update'),
]
