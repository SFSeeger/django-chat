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
    sender_check = User.objects.filter(name=sender).exists()
    if not sender_check:
        HttpResponse("User does not exist")
    sender = User.objects.filter(name=sender)[0]
    client_check = User.objects.filter(name=client).exists()
    if not client_check:
        payload = {
            'msg': "friend with name does not exist"
        }
        json_response = json.dumps(payload)
        return JsonResponse(json_response)

    client = User.objects.filter(name=client)[0]
    client.friend_requests.add(sender)
    client.save()

    return JsonResponse("success in sending client should refresh the page any second")

def accept_friend(request):
    