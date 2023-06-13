from django.test import TestCase

class SendLoginEmailViewTest(TestCase):
    """-> view for send message for into""" 

    def test_redirects_to_home_page(self):
        """-> redirects on home page""" 

        response = self.client.post('/accounts/send_login_email', data={'email': 'test@test.com'})
        self.assertEqual(response.status_code, 404) 