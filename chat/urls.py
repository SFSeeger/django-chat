from django.urls import path

from .views import *
urlpatterns = [
    path('', chat_main_page, name="chat_main_page")
]