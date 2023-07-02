"""
Serializer for the Accounts App
"""
from rest_framework import serializers
from .models import Account
from .models import Project
from .models import Budget


class AccountSerializer(serializers.ModelSerializer):
    """ Serializer class for Account App """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    name = serializers.ReadOnlyField(source='owner.profile.name')
    company = serializers.ReadOnlyField(source='owner.profile.company')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Account Serializer """
        model = Account
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    """ Serializer class for Project """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    owner_name = serializers.ReadOnlyField(source='owner.profile.name')
    company = serializers.ReadOnlyField(source='owner.profile.company')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Project Serializer """
        model = Project
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    """ Serializer class for Budget """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    owner_name = serializers.ReadOnlyField(source='owner.profile.name')
    company = serializers.ReadOnlyField(source='owner.profile.company')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Budget Serializer """
        model = Budget
        fields = '__all__'
