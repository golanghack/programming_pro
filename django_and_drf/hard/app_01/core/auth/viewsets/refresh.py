from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    """-> refresh viewset class"""

    permission_classes = (AllowAny,)
    http_method_names = ['post',]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serialiser(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as err:
            raise InvalidToken(e.args[0]) # BAD PRACTIC!!! Reraise
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    