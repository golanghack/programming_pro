from rest_framework import serializers

from main.models import News

class NewsSerializer(serializers.ModelSerializer):
    """News serialization"""

    class Meta:
        model = News
        fields = ('id', 'title', 'content', 'weight', 'created_at', 'source')