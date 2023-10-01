from django.contrib.auth import get_user_model 
from django.test import Client, TestCase
from django.urls import reverse
from .models import Post 

class BlogTests(TestCase):
    
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username = 'testuser', 
            email = 'test@email.com',
            password = 'secret',
        )
        
        self.post = Post.objects.create(
            title = 'A',
            body = 'BBB',
            author = self.user
        )
        
    def test_string_representation(self):
        """Return repr form."""
        
        post = Post(title='A')
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'BBB')
        
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'BBB')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_body_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEquals(self.post.get_absolute_url(), 'post/1/')
        
    
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text', 
            'author': self.user,
        })
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')
        
    def tedt_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title', 
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
        
    def test_post_detail_view(self):
        response = self.client.get(
            reverse('post_delete', args='1')
        )
        self.assertEqual(response.status_code, 200)