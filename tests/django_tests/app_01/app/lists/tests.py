from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from .views import home_page 

class HomePageTest(TestCase):
    """Home page test."""

    def test_root_url_resolves_to_home_page_view(self):
        """Root url test"""

        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        """Home page with correct html"""

        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do</title>', html)
        self.assertTrue(html.endswith('</html>'))



        
