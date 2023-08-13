from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Post
from api.serializers import PostSerializer

class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
