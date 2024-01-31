"""
Urls for Budgets1 App
"""
from django.urls import path
from budgets1 import views

urlpatterns = [
    path('budgets1/', views.BudgetList1.as_view()),
    path('budgets1/<int:pk>/', views.BudgetDetail1.as_view()),
]
