from django.urls import path
from .views import *

urlpatterns = [
    path('thanks', thanks, name="thanks"),
    path('signUp', sign_up, name="sign_up"),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('test', test, name="test")
]