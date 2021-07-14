from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
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
        "user":user,
    }
    return render(request, 'chat/chat_page.html', context)
