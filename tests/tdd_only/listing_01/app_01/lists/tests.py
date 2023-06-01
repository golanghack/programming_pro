
from django.test import TestCase

class HomeTest(TestCase):
    """Home page test"""

    def test_uses_home_template(self):
        """-> used home template""" 

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
