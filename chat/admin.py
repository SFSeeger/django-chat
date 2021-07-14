from django.contrib import admin

# Register your models here.
from chat.models import Message, Chat

admin.site.register(Message)
admin.site.register(Chat)