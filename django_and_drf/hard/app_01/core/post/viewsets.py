from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.abstract.viewsets import AbstractViewSet
from core.post.models import Post
from core.post.serializers import PostSerializer

class PostViewSet(AbstractViewSet):
    """-> create post view set"""

    http_method_names = ['post', 'get', ]
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer

    def get_queryset(self):
        """-> query set"""

        return Post.objects.all()

    def get_object(self):
        """-> get object""" 

        obj = Post.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj 

    def create(self, request, *args, **kwargs):
        """-> create Response"""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserPermission(BasePermission):
    """-> user permission"""

    def has_object_permission(self, request, view, obj):
        if request.user.is_annonymous:
            return request.method in SAFE_METHODS
        if view.basename in ['post']:
            return bool(request.user and request.user.is_authenticated)
        return False

    def has_permission(self, request, view):
        if view.basename in ['post']:
            if request.user.is_annonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False