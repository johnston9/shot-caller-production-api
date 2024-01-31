"""
Urls for Budgets3 App
"""
from django.urls import path
from budgets3 import views

urlpatterns = [
    path('budgets3/', views.BudgetList3.as_view()),
    path('budgets3/<int:pk>/', views.BudgetDetail3.as_view()),
]
