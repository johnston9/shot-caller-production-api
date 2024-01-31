""" Views for the Budgets app """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Budget2
from .serializers import BudgetSerializer2


class BudgetList2(generics.ListCreateAPIView):
    """
    List all Budget2
    """
    serializer_class = BudgetSerializer2
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Budget2.objects.all().order_by('-created_at')
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


class BudgetDetail2(generics.RetrieveUpdateAPIView):
    """
    Budget2 detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = BudgetSerializer2
    queryset = Budget2.objects.all().order_by('-created_at')
