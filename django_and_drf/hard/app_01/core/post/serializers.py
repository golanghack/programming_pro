from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
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

    class Meta:
        model = Post
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated',]
        read_only_fields = ['edited']
        