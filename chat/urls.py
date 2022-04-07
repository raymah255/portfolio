from django.urls import path

from .views import chat_room, list_chat_room


urlpatterns = [
    path('', list_chat_room),
    path('<str:username>', chat_room),
]
