from rest_framework import serializers
from rest_framework import permissions
from users.models import User
from chat.models import Message, Room
from chat.serializers import RoomSerializer


class UserSerializer(serializers.ModelSerializer):
    # rooms = serializers.PrimaryKeyRelatedField(many=True, queryset=Room.objects.all(), allow_null=True, required=False)
    rooms = RoomSerializer(many=True, read_only=True)
    current_room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all(), allow_null=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'rooms', 'current_room']

# class SnippetSerializer(serializers.HyperlinkedModelSerializer):

#     owner = serializers.ReadOnlyField(source='owner.username')
#     highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

#     class Meta:
#         model = Snippet
#         fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'linenos', 'language', 'style']


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'snippets']
