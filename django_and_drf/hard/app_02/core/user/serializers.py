from rest_framework import serializers
from django.conf import settings
from core.abstract.serializers import AbstractSerializer
from core.user.models import User


class UserSerializer(AbstractSerializer):
    """User serializer class""" 

    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(required=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AUTO_FIELD
            return representation
        if settings.DEBUG:
            request = self.context.get('request')
            representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        return representation
    class Meta:
        model = User 
        fields = ['created', 'updated', 'id', 'username', 'first_name', 'last_name', 'bio', 'avatar', 'email']
        read_only_field = ['is_active']

    
