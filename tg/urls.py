from django.urls import path
from .views import GetUpdates

app_name = 'tg'


urlpatterns = [
    path('<webhook>/', GetUpdates.as_view(), name='update'),
]