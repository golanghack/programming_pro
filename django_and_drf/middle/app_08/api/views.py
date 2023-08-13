from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.models import Post
from api.permissions import IsAuthorOrReadOnly
from api.serializers import UserSerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    