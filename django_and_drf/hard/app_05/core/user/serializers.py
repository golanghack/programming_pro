from rest_framework import serializers
from django.conf import settings
from core.abstract.serializers import AbstractSerializer
from core.user.models import User

class UserSerializer(AbstractSerializer):
    """User Serializer""" 

    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance) -> int:
        return instance.post_st.all().count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AVATAR_URL 
        
        if settings.DEBUG:
            request = self.context.get('request')
            representation['avatar'] = request.build_absolute_uri(
                            representation['avatar']
                            )
        return representation
    
    class Meta:
        model = User 
        fields = [
            'id',
            'username',
            'name',
            'first_name',
            'last_name',
            'bio', 
            'avatar', 
            'email',
            'is_active', 
            'created', 
            'updated', 
            'posts_count',
        ]
        read_only_fields = ['is_active']
