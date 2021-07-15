import json

from channels.generic.websocket import WebsocketConsumer
import channels.layers
from asgiref.sync import async_to_sync

from chat.helper import check_for_chat
from chat.models import Message, Chat
from login.models import User


#TODO:Right json implementation !!!!!
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
        )

        self.user = User.objects.filter(name=self.room_name)[0]
        print(self.user)

        if not self.user:
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    'type': 'server_message',
                    'message': 'user does not exist'
                }
            )
            return

        self.user.socket_state = 'online'
        self.user.save()
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name
        )
        self.user.socket_state = 'away'
        print(code)

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        client = text_data_json['client']
        client_class = User.objects.filter(name=client)[0]

        check = check_for_chat(name1=self.user.name, name2=client)

        if not check:
            chat_name = self.user.name + "_" + client
            chat = Chat(name=chat_name)
            chat.save()
        else:
            chat = Chat.objects.filter(name=check)[0]

        message_to_save = Message(author=self.user, client=client_class, content=message)
        message_to_save.save()

        chat.messages.add(message_to_save)
        chat.save()

        if not chat.users.all().exists():
            chat.users.add(self.user)

        async_to_sync(self.channel_layer.group_send)(
            client,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    def server_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


