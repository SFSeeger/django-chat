import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SignUp, Login
from .models import User


def redirect_to_home(request):
    return redirect('/chat/')


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'login/sign_up.html')
    else:
        form = SignUp(request.POST)
        if form.is_valid():
            search_user = User.objects.filter(name=form.cleaned_data['name'])
            if search_user.exists():
                return HttpResponse("user name already in use you can login if you are this user")
            new_user = User(name=form.cleaned_data['name'],
                            password=hashlib.md5(form.cleaned_data['password'].encode()).hexdigest(),
                            email=form.cleaned_data['email'])
            new_user.save()
            return redirect('/login/thanks')
        else:
            return HttpResponse('form invalid')


def login(request):
    if request.method == 'GET':
        user_id = request.session.get('id')
        user = User.objects.filter(id=user_id)
        if user.exists():
            context = {
                'msg': "You are already logged in"
            }
            return render(request, 'login/login.html', context)
        return render(request, 'login/login.html')
    else:
        form = Login(request.POST)
        if form.is_valid():
            user = User.objects.filter(name=form.cleaned_data['name'],
                                       password=hashlib.md5(form.cleaned_data['password'].encode()).hexdigest())
            if not user.exists():
                context = {
                    'msg': "User does not exist"
                }
                return render(request, 'login/login.html', context)

            request.session['id'] = user.first().id
            return redirect('/chat/')


def logout(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect('/login/login')


def handle_404(request, exception):
    data = {}
    return render(request, 'login/login.html', data)


def thanks(request):
    return render(request, 'thanks.html')


def test(request):
    print(request.session.get('user'))
