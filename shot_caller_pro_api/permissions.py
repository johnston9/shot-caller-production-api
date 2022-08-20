""" permissions
"""
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ permissions
    """
    def has_object_permission(self, request, view, obj):
        """ permissions function
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
