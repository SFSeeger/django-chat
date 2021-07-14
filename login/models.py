import datetime

from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=44)
    date = models.DateTimeField(default=datetime.datetime.now())
    socket_state = models.CharField(max_length=60, default="away")
    chats = models.ManyToManyField("chat.Chat")
    friends = models.ManyToManyField("login.User")
    friend_requests = models.ManyToManyField("login.User", related_name="requests")

    def __str__(self):
        return self.name


