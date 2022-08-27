""" Chat views """
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer


class ChatList(generics.ListCreateAPIView):
    """ Chat views """
    serializer_class = ChatSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Chat.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]
    search_fields = [
        'owner__username',
        'owner__profile__company',
        'title',
    ]


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a chat and edit or delete it if you own it.
    """
    serializer_class = ChatSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Chat.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
