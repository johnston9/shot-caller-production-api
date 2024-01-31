"""
Urls for Budgets2 App
"""
from django.urls import path
from budgets2 import views

urlpatterns = [
    path('budgets2/', views.BudgetList2.as_view()),
    path('budgets2/<int:pk>/', views.BudgetDetail2.as_view()),
]
