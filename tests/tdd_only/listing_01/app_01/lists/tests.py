from django.urls import resolve
from django.test import TestCase
from lists.views import home

class HomeTest(TestCase):
    """Home page test"""

    def test_root_url_resolves_to_home_page_view(self):
        """-> root url to view for home page""" 

        found = resolve('/')
        self.assertEqual(found.func, home_page)