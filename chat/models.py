from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Room(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('users.User', related_name="owned_rooms", on_delete=models.CASCADE, )
    members = models.ManyToManyField('users.User', related_name="member_rooms", blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Room)
def add_owner_as_member(sender, instance, created, **kwargs):
    if created:
        instance.members.add(instance.owner)


class Message(models.Model):
    text = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey('users.User', related_name="sent_messages", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return self.text
