from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('users.User', related_name="owned_rooms", on_delete=models.CASCADE)
    members = models.ManyToManyField('users.User', related_name="member_rooms")


class Message(models.Model):
    text = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('users.User', related_name="sent_messages", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)
