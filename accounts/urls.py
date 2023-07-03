"""
Urls for Accounts App
"""
from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.AccountList.as_view()),
    path('accounts/<int:pk>/', views.AccountDetail.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
]
