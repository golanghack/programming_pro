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


        
