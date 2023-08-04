from rest_framework.response import Response
from rest_framework.decorators import api_view

from main.models import News
from api.serializers import NewsSerializer

@api_view(['GET'])
def news(request: str) -> Response:
    if request.method == 'GET':
        # first 10 news
        news = News.objects.filter(is_active=True)[:10]
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)
        