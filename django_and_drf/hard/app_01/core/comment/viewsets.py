from django.http.response import Http404
from rest_framework.response import Response 
from rest_framework import status
from core.abstract.viewsets import AbstractViewSet
from core.comment.models import Comment
from core.comment.serializers import CommentSerializer
from core.post.viewsets import UserPermission


class CommentViewSet(AbstractViewSet):
    """-> comment view set"""

    http_method_names = ['post', 'get', 'delete', 'put']
    permission_classes = (UserPermission, )
    serializer_class = CommentSerializer