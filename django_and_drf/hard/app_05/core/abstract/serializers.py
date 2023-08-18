from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
    """Abstract Serializer""" 

    id: int = serializers.UUIDField(source='public_id',
                                    read_only=True, 
                                    format='hex')
    created: str = serializers.DateTimeField(read_only=True)
    updated: str = serializers.DateTimeField(read_only=True)