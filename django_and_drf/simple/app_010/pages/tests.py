from django.test import SimpleTestCase
from django.urls import reverse

class HomeTests(SimpleTestCase):
    
    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_url(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
