from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView

from main.models import News
from api.serializers import NewsSerializer, NewsDetailSerializer

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