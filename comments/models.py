""" Comments model """
from django.db import models
from django.contrib.auth.models import User
from chat.models import Chat


class Comment(models.Model):
    """
    Comment model, related to User and Chat
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.content}'
