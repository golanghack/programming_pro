from rest_framework import serializers
from django.conf import settings

from core.user.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer class""" 

    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(required=True)

    class Meta:
        model = User 
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email']
        read_only_field = ['is_active']

    
