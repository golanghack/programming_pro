from django.urls import path
from rest_framework.routers import SimpleRouter
from album.views import SongList, SingerList, AlbumList

router = SimpleRouter()
router.register('song', SongList, basename='song')
router.register('singer', SingerList, basename='singer')
router.register('album', AlbumList, basename='album')

urlpatterns = router.urls