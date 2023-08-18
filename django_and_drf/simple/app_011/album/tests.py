from django.test import TestCase
import warnings
warnings.filterwarnings(action="ignore")
from album.models import Album, Singer, Song 

class MySimpleTests(TestCase):

    def test_singer(self):
        singer = Singer.objects.create(name='Eminem')
    
        self.assertEqual(singer.name, 'Eminem')

    def test_song(self):
        singer = Singer.objects.create(name='Eminem')
        album = Album.objects.create( singer=singer, start='1998-01-01')
        song = Song.objects.create(name='Infinity', in_album=album, number_in=2)

        self.assertEqual(song.name, 'Infinity')
        self.assertEqual(song.in_album, album)
        self.assertEqual(song.number_in, 2)

    def test_album(self):
        singer = Singer.objects.create(name='Eminem')
        album = Album.objects.create(singer=singer, start='1998-01-01')
        
        self.assertEqual(album.start, '1998-01-01')
