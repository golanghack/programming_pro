from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page 

class HomePageTest(TestCase):
    """Home page test."""

    def test_uses_base_template(self):
        """Home page with correct html"""

        response = self.client.get('/')
        self.assertTemplateUsed((response, 'base.html'))

    def test_can_save_a_POST_request(self):
        """Test -> can save a post request"""

        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())


        
