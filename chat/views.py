
from chat.models import Message, Room
from rest_framework import viewsets
from chat.serializers import RoomSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
import datetime
from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer
# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, timestamp=datetime.datetime.now(),
                        room=self.request.user.current_room)
