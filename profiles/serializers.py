"""
Serializer for Profiles App
"""
from rest_framework import serializers
from followers.models import Follower
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """ Serializer class for Profiles App """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    chats_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """ Meta for Profiles Serializer """
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'company', 'content', 'image', 'is_owner',
            'following_id', 'chats_count', 'followers_count', 
            'following_count',
        ]
