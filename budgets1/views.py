""" Views for the Budgets1 app """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Budget1
from .serializers import BudgetSerializer1


class BudgetList1(generics.ListCreateAPIView):
    """
    List all Budget1
    """
    serializer_class = BudgetSerializer1
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Budget1.objects.all().order_by('-created_at')
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


class BudgetDetail1(generics.RetrieveUpdateAPIView):
    """
    Budget1 detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BudgetSerializer1
    queryset = Budget1.objects.all().order_by('-created_at')
