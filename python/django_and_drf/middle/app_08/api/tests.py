from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Post

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls: str):
        test_1 = User.objects.create_user(username='test_1', password='test123')
        test_1.save()

        test_1_post = Post.objects.create(author=test_1, title='Test 1', body='Test 1')
        test_1_post.save()

    def test_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, 'test_1')
        self.assertEqual(title, 'Test 1')
        self.assertEqual(body, 'Test 1')