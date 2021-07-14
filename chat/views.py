import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers


# Create your views here.
from chat.helper import check_for_chat
from chat.models import Chat
from login.models import User


def chat_main_page(request):
    id = request.session.get("id")
    if not id:
        return redirect('/login/login')
    user_list = User.objects.filter(id=id)
    if not user_list.exists():
        return HttpResponse('User id does not exist')
    user = user_list[0]
    context = {
        "user": user,
    }
    return render(request, 'chat/chat_page.html', context)


def get_chat_messages(request):
    json_request = json.loads(request.body)
    id = request.session.get("id")
    if not id:
        return redirect('/login/login')
    user = User.objects.filter(id=id)[0]
    client = json_request['client']
    chat_name = check_for_chat(user.name, client)
    chat = Chat.objects.filter(name=chat_name)
    if not chat.exists():
        payload = {
            'msg': "new chat"
        }
        return JsonResponse(payload)
    chat = chat[0]
    messages = chat.messages.all()
    messages_json = serializers.serialize('json', messages)
    return HttpResponse(messages_json, content_type='application/json')

