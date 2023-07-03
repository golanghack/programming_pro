from django.http.response import Http404
from rest_framework.response import Response
from rest_framework import status
from core.abstract.viewsets import AbstractViewSet
from core.comments.models import Comment
from core.comments.serializers import CommentSerializer
from core.auth.permissions import UserPermission


class CommentViewSet(AbstractViewSet):
    """Comment view""" 

    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission)
    serializer_class = CommentSerializer

    