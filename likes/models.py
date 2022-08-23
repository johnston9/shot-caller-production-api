""" Likes model """
from django.db import models
from django.contrib.auth.models import User
from chat.models import Chat


class Like(models.Model):
    """
    Like model, related to 'owner' and 'chat'.
    'unique_together' makes sure a user can't like the same chat twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    chatmessage = models.ForeignKey(
        Chat, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'chatmessage']

    def __str__(self):
        return f'{self.owner}'
