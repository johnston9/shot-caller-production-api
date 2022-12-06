"""
Serializer for the Accounts App
"""
from rest_framework import serializers
from .models import Account
from .models import Project


class AccountSerializer(serializers.ModelSerializer):
    """ Serializer class for Account App """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Account Serializer """
        model = Account
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer class for Project """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Project Serializer """
        model = Project
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'stripe_id',
        ]
