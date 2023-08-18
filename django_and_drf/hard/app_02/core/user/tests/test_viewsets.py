import pytest
from rest_framework import status
from core.fixtures.user import user
from core.fixtures.post import post
from core.fixtures.comment import comment


class TestUserViewSet:

    endpoint = '/api/user/'
    user = user
    post = post
    comment = comment   

    