from rest_framework.viewsets import ModelViewSet
from album.models import Singer, Song, Album
from album.serializers import (SongSerializer, 
                                SingerSerializer, 
                                AlbumSerializer)

class SongList(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SingerList(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class AlbumList(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer