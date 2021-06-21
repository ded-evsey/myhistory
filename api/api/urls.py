from django.urls import path
from api.views import ImgMessageSendAPI, TextMessageSendAPI
urlpatterns = [
    path('text-data/', TextMessageSendAPI.as_view()),
    path('file-data', ImgMessageSendAPI.as_view())
]