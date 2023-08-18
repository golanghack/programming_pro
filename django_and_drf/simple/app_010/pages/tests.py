from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pages.views import HomeView 


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

    def test_homeview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomeView.as_view().__name__)

