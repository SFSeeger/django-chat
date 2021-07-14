from django.urls import path

from friends.views import *

urlpatterns = [
    path('', friends_page),
    path('add/', add_friend)
]