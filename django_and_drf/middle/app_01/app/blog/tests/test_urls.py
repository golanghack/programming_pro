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
        