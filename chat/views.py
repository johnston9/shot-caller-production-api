""" Chat views """
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from shot_caller_pro_api.permissions import IsOwnerOrReadOnly
from .models import Chat
from .serializers import ChatSerializer


class ChatList(APIView):
    """ Chat views """
    serializer_class = ChatSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        """ get """
        chats = Chat.objects.all()
        serializer = ChatSerializer(
            chats, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        """ post """
        serializer = ChatSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ChatDetail(APIView):
    """ Chat views """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ChatSerializer

    def get_object(self, pk):
        """ get """
        try:
            chatmessage = Chat.objects.get(pk=pk)
            self.check_object_permissions(self.request, chatmessage)
            return chatmessage
        except Chat.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """ get """
        chatmessage = self.get_object(pk)
        serializer = ChatSerializer(
            chatmessage, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        chatmessage = self.get_object(pk)
        serializer = ChatSerializer(
            chatmessage, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        """ delete """
        chatmessage = self.get_object(pk)
        chatmessage.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
