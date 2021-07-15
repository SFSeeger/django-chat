import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
from login.models import User


def friends_page(request):
    user_id = request.session.get('id')
    user = User.objects.filter(id=user_id)
    if not user.exists():
        return HttpResponse("user does not exist")
    user = user[0]
    context = {
        'user': user,
    }
    print(user.id)
    return render(request, "friends/friends_index.html", context)


def add_friend(request):
    body = json.loads(request.body)
    sender = body['user']
    client = body['client']
    if sender == client:
        payload = {
            'msg': "You can not add yourself"
        }
        return JsonResponse(payload)
    sender_check = User.objects.filter(name=sender).exists()
    if not sender_check:
        return HttpResponse("User does not exist")
    sender = User.objects.filter(name=sender)[0]
    client_check = User.objects.filter(name=client).exists()
    if not client_check:
        payload = {
            "msg": "friend with name does not exist"
        }
        return JsonResponse(payload)

    client = User.objects.filter(name=client)[0]
    client.friend_requests.add(sender)
    client.save()
    print(client.friend_requests)

    sender = User.objects.filter(name=sender)[0]
    sender.friend_pending.add(client)
    sender.save()
    print(sender.friend_pending)

    payload = {
        'msg': "success in sending client should refresh the page any second"
    }
    return JsonResponse(payload)


def accept_friend(request):
    body = json.loads(request.body)
    sender = body['user']
    client = body['client']

    sender = User.objects.filter(name=sender)
    client = User.objects.filter(name=client)
    if not sender.exists():
        payload = {
            'msg': "sender does not exist"
        }
        return JsonResponse(payload)
    if not client.exists():
        payload = {
            'msg': "client does not exist"
        }
        return JsonResponse(payload)

    sender = sender[0]
    client = client[0]
    print(sender, client)

    sender.friend_pending.remove(client)
    sender.friends.add(client)
    sender.save()
    print(sender.friend_pending, sender.friends)

    client.friend_requests.remove(sender)
    client.friends.add(sender)
    client.save()
    print(client.friend_requests, client.friends)

    payload = {
        'msg': 'friend accepted'
    }
    return JsonResponse(payload)