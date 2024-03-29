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


class RoomConsumer(GenericAsyncAPIConsumer):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'pk'

    @action()
    async def join_room(self, pk):
        self.room_subscribe = pk
        await self.add_user_to_room(pk)

    @action()
    async def leave_room(self, pk):
        await self.remove_user_from_room(pk)

    @database_sync_to_async
    def add_user_to_room(self, pk):
        user: User = self.scope["user"]
        if not User.current_room.filter(pk=self.room_subscribe).exists():
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
