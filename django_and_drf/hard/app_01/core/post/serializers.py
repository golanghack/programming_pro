from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.user.serializers import UserSerializer
from core.post.models import Post
from core.user.models import User


class PostSerializer(AbstractSerializer):
    """-> create post serializer""" 

    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

    def validation_author(self, value):
        """-> validation author field""" 

        if self.context['request'].user != value:
            raise ValidationError('You will not create a post for another user')
        return value 

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data
        return rep


    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance, validated_data)
        return instance

    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    def get_liked(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_annonymous:
            return False
        return request.user.has_liked(instance)

    def get_likes_count(self, instance):
        return instance.liked_by.count()
        
    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 
                    'liked', 'likes_count', 'created', 'updated',]
        read_only_fields = ['edited']
        