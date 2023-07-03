"""
Models for Accounts App
"""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Account(models.Model):
    """
    Account model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s Account"


def create_account(sender, instance, created, **kwargs):
    """
    Function to create account instance when a user registers
    """
    if created:
        Account.objects.create(owner=instance)


post_save.connect(create_account, sender=User)


class Project(models.Model):
    """
    Project model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, blank=True)
    url = models.CharField(max_length=25, blank=True)
    stripe_id = models.CharField(max_length=25, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} "
