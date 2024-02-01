""" Views for the Budgets3 app """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Budget3
from .serializers import BudgetSerializer3


class BudgetList3(generics.ListCreateAPIView):
    """
    List all Budget3
    """
    serializer_class = BudgetSerializer3
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Budget3.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'project',
        'budget_number',
    ]
    search_fields = [
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BudgetDetail3(generics.RetrieveUpdateAPIView):
    """
    Budget3 detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BudgetSerializer3
    queryset = Budget3.objects.all().order_by('-created_at')
