from django.urls import path
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .views import UpdateBot

app_name = 'tg'



urlpatterns = [
    path('{}'.format(settings.TOKEN), csrf_exempt(UpdateBot.as_view()), name='update'),

]