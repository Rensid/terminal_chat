
from django.urls import path, re_path
from chat import consumers

websocket_urlpatterns = [
    # path("ws/", consumers.UserConsumer.as_asgi()),
    path("ws/chat/", consumers.RoomConsumer.as_asgi()),
    # re_path(r'ws/chat/room/$', consumers.RoomConsumer.as_asgi()),
]
