"""
Models for Budgets App
"""
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Project


class Budget(models.Model):
    """
    Budget model
    """
    project = models.CharField(max_length=25, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=25, blank=True)
    series = models.CharField(max_length=25, blank=True)
    prodco = models.CharField(max_length=25, blank=True)
    format = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    dated = models.CharField(max_length=25, blank=True)
    research = models.CharField(max_length=25, blank=True)
    prep = models.CharField(max_length=25, blank=True)
    shoot = models.CharField(max_length=25, blank=True)
    wrap = models.CharField(max_length=25, blank=True)
    post = models.CharField(max_length=25, blank=True)
    length_total = models.CharField(max_length=25, blank=True)
    story_rights = models.CharField(max_length=25, blank=True)
    miscellaneous = models.CharField(max_length=25, blank=True)
    rights_total = models.CharField(max_length=25, blank=True)

    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} "
