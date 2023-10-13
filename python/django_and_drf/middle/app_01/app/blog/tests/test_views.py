'''from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from django import forms

from ..models import Post

User = get_user_model()

class TestPostViews(TestCase):
    @classmethod
    def setUpClass(cls):
        my_test_user_views = User.objects.create_user(username='test_user_views', 
                                            email='test_views@test.com',
                                            password='pass123')
        super().setUpClass()

        Post.objects.create(
            title='Views test',
            body='Test views',
            slug='test_slug',
            author=my_test_user_views
        )

    def setUp(self):
         super().setUpClass()
         self.client = Client()
    
    def test_home_page_show_correct_context(self):
        """Correect context"""

        response = self.client.get(reverse('blog:post_list'))
DONT WORK POSRTGRES UTILS IN DJANGO
'''
