
from django.urls import path
from chat import consumers

websocket_urlpatterns = [
    path("ws/", consumers.UserConsumer.as_asgi()),
    path("ws/chat/", consumers.RoomConsumer.as_asgi()),
]
