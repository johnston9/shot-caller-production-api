""" Views for the Account app """
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Account
from .serializers import AccountSerializer
from .models import Project
from .serializers import ProjectSerializer
from .models import Budget
from .serializers import BudgetSerializer


class AccountList(generics.ListAPIView):
    """
    List all Accounts
    Account creation handled by django signals
    """
    queryset = Account.objects.all().order_by('-created_at')
    serializer_class = AccountSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
    ]


class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    Account detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AccountSerializer
    queryset = Account.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]


class ProjectList(generics.ListCreateAPIView):
    """
    List all Projects
    """
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Project.objects.all().order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
    ]
    search_fields = [
        'name',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProjectDetail(generics.RetrieveUpdateAPIView):
    """
    Project detail view
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('-created_at')


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
