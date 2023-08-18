from rest_framework import serializers

from album.models import Singer, Song, Album

class SingerSerializer(serializers.ModelSerializer):
    """Singer serializer""" 

    class Meta:
        model =  Singer
        fields = ('id', 'name',)

class SongSerializer(serializers.ModelSerializer):
    """Song serializer""" 
    
    class Meta:
        model = Song
        fields = ('id', 'name', 'in_album', 'number_in',)

class AlbumSerializer(serializers.ModelSerializer):
    """Album serializer""" 

    class Meta:
        model = Album
        fields = ('id', 'singer', 'start',)
