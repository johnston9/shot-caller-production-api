""" Chat views """
from rest_framework import generics, permissions
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer


class ChatList(generics.ListCreateAPIView):
    """ Chat views """
    serializer_class = ChatSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Chat.objects.all()


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a chat and edit or delete it if you own it.
    """
    serializer_class = ChatSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Chat.objects.all()
