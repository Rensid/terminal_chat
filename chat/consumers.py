import json
from channels.generic.websocket import AsyncWebsocketConsumer
from users.models import User
from chat.models import Room, Message
from channels.db import database_sync_to_async
from djangochannelsrestframework.observer.generics import action
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from chat.serializers import RoomSerializer
from users.serializers import UserSerializer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)


# на будущее себе
# в случае если в функции есть запрос в базу данных, то прописывается database_sync_to_async
# сама функция при этом синхронная
# если запроса нет, то можно делать функцию асинхронной

# class RoomConsumer(GenericAsyncAPIConsumer):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer
#     lookup_field = 'pk'

#     def send_message(self, message):
#         print(f'message is "{message}"')

class RoomConsumer(GenericAsyncAPIConsumer):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'pk'

    # присоединение к комнате чвта
    @action()
    async def connect_to_room(self, pk, **kwargs):
        self.room_subscribe = pk
        await self.add_user_to_room(pk)

    @action()
    async def disconnect_room(self, pk):
        await self.remove_user_from_room(pk)

        # def add_user_to_room_list_member(self, pk):
        #     User = self.scope['user']
        #     if not User.me

    @database_sync_to_async
    def add_user_to_room(self, pk):
        user: User = self.scope["user"]
        print('User')
        if not User.current_room.get(id=self.pk).exists():
            user.current_room.add(Room.objects.get(pk=pk))

    @database_sync_to_async
    def remove_user_from_room(self, pk):
        user: User = self.scope["user"]
        user.current_room.remove()

    @action()
    async def send_message(self, text):
        user: User = self.scope["user"]
        room: Room = await self.get_room(pk=self.room_subscribe)
        await database_sync_to_async(Message.objects.create)(
            text=text,
            sender=user,
            room=room,
        )

    @database_sync_to_async
    def get_room(self, pk):
        return Room.objects.get(pk=pk)


class UserConsumer(
        ListModelMixin,
        RetrieveModelMixin,
        PatchModelMixin,
        UpdateModelMixin,
        CreateModelMixin,
        DeleteModelMixin,
        GenericAsyncAPIConsumer,
):

    queryset = User.objects.all()
    serializer_class = UserSerializer
