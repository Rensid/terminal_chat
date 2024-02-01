from django.db import models
from users.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_rooms')
    users = models.ManyToManyField(User, related_name='rooms')


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
