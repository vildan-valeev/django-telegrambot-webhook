from django.urls import path
from .views import UpdateBot

app_name = 'tg'

urlpatterns = [
    path('', UpdateBot.as_view(), name='update'),
]
