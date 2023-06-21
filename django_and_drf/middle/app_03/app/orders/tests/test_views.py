from django.test import Client, TestCase
from django.urls import reverse

class TestPageCart(TestCase):
    """-> test page of cart""" 

    def test_detail_page_uses_correct_template(self):
        """-> page of cart with correct template""" 

        client = Client()
        response = client.get(reverse('cart:cart_detail'))
        self.assertTemplateUsed(response, 'cart/detail.html')