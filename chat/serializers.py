from rest_framework import serializers
from rest_framework import permissions
from users.models import User
from chat.models import Message, Room
from django.conf import settings


class RoomSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Room
        fields = ('id', 'name', 'owner', 'members')


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    chat = serializers.ReadOnlyField(source='chat.name')

    class Meta:
        model = Message
        fields = ['id', 'text', 'timestamp', 'author', 'chat']
