from  django.test import TestCase, Client

class TestStaticPagesURL(TestCase):
    def setUp(self):
        """Don`t authorisation client."""

        super().setUpClass()
        self.guest_client = Client()

    
    def test_home_url_exists_at_desired_location(self):
        """Testing url /blog/"""

        response = self.guest_client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_home_url_uses_correct_template(self):
        """Testing template for url /blog/"""

        response = self.guest_client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/base.html')


class TestCommonURL(TestCase):
    def setUp(self):
        """Don`t authorisation client"""

        self.guest_client = Client()

    def test_home_url_exists_at_desired_location(self):
        """Page ->/<- open every user"""

        response = self.guest_client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_list_post_url_exists_at_desired_location(self):
        """Post feed visible every users"""

        response = self.guest_client.get('/blog/feed/')
        self.assertEqual(response.status_code, 200)

        
    def test_blog_search_url(self):
        response = self.guest_client.get('/blog/search/')
        self.assertEqual(response.status_code, 200)