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


class Budget(models.Model):
    """
    Budget model
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=25, blank=True)
    series = models.CharField(max_length=25, blank=True)
    prodco = models.CharField(max_length=25, blank=True)
    format = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    dated = models.CharField(max_length=25, blank=True)
    research = models.IntegerField(blank=True)
    prep = models.IntegerField(blank=True)
    shoot = models.IntegerField(blank=True)
    wrap = models.IntegerField(blank=True)
    post = models.IntegerField(blank=True)
    length_total = models.IntegerField(blank=True)
    story_rights = models.IntegerField(blank=True)
    miscellaneous = models.IntegerField(blank=True)
    rights_total = models.IntegerField(blank=True)

    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} "
