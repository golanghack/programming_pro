from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveAPIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from main.models import News, Comment
from api.serializers import NewsSerializer, NewsDetailSerializer, CommentSerializer

@api_view(['GET'])
def news(request: str) -> Response:
    if request.method == 'GET':
        # first 10 news
        news = News.objects.filter(is_active=True)[:10]
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsDetailSerializer


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def comments(request: str, pk: int) -> Response:
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        comments = Comment.objects.filter(is_active=True, news=pk)
        serializer = CommentSerializer(comments, mant=True)
        return Response(serializer.data)