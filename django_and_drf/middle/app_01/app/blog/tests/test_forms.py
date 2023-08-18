from ..forms import CommentForm
from ..models import Comment
from django.conf import settings
from django.test import Client, TestCase, override_settings
from django.urls import reverse


class TestFormComment(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
