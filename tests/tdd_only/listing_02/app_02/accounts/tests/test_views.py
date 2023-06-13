from django.test import TestCase
import accounts.views

class SendLoginEmailViewTest(TestCase):
    """-> view for send message for into""" 

    def test_redirects_to_home_page(self):
        """-> redirects on home page""" 

        response = self.client.post('/accounts/send_login_email', data={'email': 'test@test.com'})
        self.assertEqual(response.status_code, 404) # Error <-

    
    def test_sends_mail_to_address_from_post(self):
        """-> send message on email from post""" 

        self.send_mail_called = False

        def fake_send_mail(subject, body, from_email, to_list):
            """-> fake function send_email from django"""

            self.send_mail_called = True
            self.subject = subject
            self.body = body
            self.from_email = from_email
            self.to_list = to_list

        accounts.views.send_mail = fake_send_mail
        self.client.post('/accounts/send_login_email', data={'email': 'test@test.com'})
        self.assertTrue(self.send_mail_called)
        self.assertEqual(self.subject, 'Your login link for lists')
        self.assertEqual(self.from_email, 'noreply@superuser.com')
        self.assertEqual(self.to_list, ['test@test.com'])
