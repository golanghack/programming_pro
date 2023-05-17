from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from model_bakery import baker 

class PostTest(TestCase):

    def test_creating_object(self):
        user_one = User.objects.create()
        title_post = Post.objects.create(title='one', author=user_one)
        self.assertEqual(title_post.title, 'one')
        self.assertEqual(Post.objects.count(), 1)


    def test_fields_of_model_post(self):

        post = baker.make(Post, title='First post')
        self.assertEqual(str(post), 'First post')


class TestForm(TestCase):
    def test_cant_send_form_user(self):
        """Testing forms."""

        
        