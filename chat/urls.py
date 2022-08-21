""" Chat urls """
from django.urls import path
from chat import views

urlpatterns = [
    path('chat/', views.ChatList.as_view()),
]
