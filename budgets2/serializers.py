"""
Serializer for the Budgets2 App
"""
from rest_framework import serializers
from .models import Budget2


class BudgetSerializer2(serializers.ModelSerializer):
    """ Serializer class for Budget2 """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    owner_name = serializers.ReadOnlyField(source='owner.profile.name')
    company = serializers.ReadOnlyField(source='owner.profile.company')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """ Meta for Budget2 Serializer """
        model = Budget2
        fields = '__all__'
