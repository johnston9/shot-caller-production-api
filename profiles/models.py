"""
Models for Profiles App
"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25, blank=True)
    company = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='/images/default_profile_iq2tpu'
    )
    # image = models.ImageField(
    #     upload_to='images/', default='/images/default_profile_lxlutc'
    # )

    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Function to create profile instance when a user registers
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
