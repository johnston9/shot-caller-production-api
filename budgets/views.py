""" Views for the Budgets app """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Budget1
from .models import Budget2
from .models import Budget3
from .serializers import BudgetSerializer1
from .serializers import BudgetSerializer2
from .serializers import BudgetSerializer3


class BudgetList(generics.ListCreateAPIView):
    """
    List all Budgets
    """
    serializer_class = BudgetSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Budget.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'project',
    ]
    search_fields = [
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BudgetDetail(generics.RetrieveUpdateAPIView):
    """
    Budget detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BudgetSerializer
    queryset = Budget.objects.all().order_by('-created_at')
