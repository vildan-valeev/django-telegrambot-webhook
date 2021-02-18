from django.urls import path
from .views import UpdateBot

app_name = 'tg'


urlpatterns = [
    path('<hook_id>/', UpdateBot.as_view(), name='update'),
]