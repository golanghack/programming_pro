from rest_framework import serializers

from main.models import News, Comment

class NewsSerializer(serializers.ModelSerializer):
    """News serialization"""

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'weight', 'created_at', 'source')


class NewsDetailSerializer(serializers.ModelSerializer):
    """Detail for News model""" 

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'weight', 'created_at', 'source', 'image')


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer""" 

    class Meta:
        model = Comment
        fields = ('new','author', 'content')