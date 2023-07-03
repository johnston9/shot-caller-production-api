"""
Urls for Budgets App
"""
from django.urls import path
from budgets import views

urlpatterns = [
    path('budgets/', views.BudgetList.as_view()),
    path('budgets/<int:pk>/', views.BudgetDetail.as_view()),
]
