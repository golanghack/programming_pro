from django.test import TestCase, Client

class StaticUrlTest(TestCase):
    """-> test for static urls"""

    def test_cart_page(self):
        """-> test cart page"""

        client = Client()
        response = client.get('/en/cart/')
        self.assertEqual(response.status_code, 200)


class TestTemplateUsed(TestCase):
    """-> test used correct template""" 

    def test_correct_template_for_cart(self):
        """-> test correct template for cart""" 

        client = Client()
        response = client.get('/en/cart/')
        self.assertTemplateUsed(response, 'cart/detail.html')