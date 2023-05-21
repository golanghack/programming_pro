from django.test import TestCase, Client

class TestStaticURL(TestCase):
    
    def test_home(self):
        client = Client()
        response = client.get('/account/login')
        self.assertEqual(response.status_code, 301)
