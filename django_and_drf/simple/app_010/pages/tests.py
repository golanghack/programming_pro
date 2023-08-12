from django.test import SimpleTestCase
from django.urls import reverse

class HomeTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_contains_correct(self):
        self.assertContains(self.response, 'Home')

    def test_home_incorrect(self):
        self.assertNotContains(self.response, 'Hi')
        
