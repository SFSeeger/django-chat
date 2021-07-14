from django.db import models

# Create your models here.
from login.models import User


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="author")
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="client")
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class Chat(models.Model):
    messages = models.ManyToManyField(Message)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=61)
    users = models.ManyToManyField(User)