from django.test import TestCase, Client

class TestStaticURL(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        
        response = self.client.get('')
        self.assertEqual(response.status_code, 302)
