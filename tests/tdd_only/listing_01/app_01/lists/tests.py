
from django.test import TestCase

class HomeTest(TestCase):
    """Home page test"""

    def test_uses_home_template(self):
        """-> used home template""" 

        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """-> may be save post-request?""" 
        
        member = 'A new list item'
        response = self.client.post('/', data={'item_text': 'A new list item'})
        container = response.content.decode()

        self.assertIn(member, container)
        self.assertTemplateUsed(response, 'home.html')
