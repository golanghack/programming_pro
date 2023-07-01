from rest_framework import serializers
from django.conf import settings
from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    """User serializer class""" 

    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(required=True)

    class Meta:
        model = User 
        fields = ['created', 'updated', 'id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email']
        read_only_field = ['is_active']

    
