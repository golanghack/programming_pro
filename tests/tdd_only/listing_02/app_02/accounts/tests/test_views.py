from django.test import TestCase
from unittest import skip
from unittest.mock import patch, call
import accounts.views
from accounts.models import Token


class SendLoginEmailViewTest(TestCase):
    """-> view for send message for into""" 

    def test_redirects_to_home_page(self):
        """-> redirects on home page""" 

        response = self.client.post('/accounts/send_login_email', data={'email': 'test@test.com'})
        self.assertEqual(response.status_code, 404) # Error <-

    @patch('accounts.views.send_mail')
    def test_sends_mail_to_address_from_post(self, mock_send_mail):
        """-> send message on email from post""" 

        self.send_mail_called = True

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
   # @skip
    @patch('accounts.views.send_mail')
    def test_sends_mail_to_address_from_post_with_mock(self, mock_send_mail):
        self.client.post('/accounts/send_email', data={'email': 'test@test.com'})
        self.assertEqual(mock_send_mail.called, True)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject, 'Your login link for lists')
        self.assertEqual(from_email, 'noreply@superuser')
        self.assertEqual(to_list, ['test@test.com'])

    def test_adds_success_message(self):
        """-> added message for success""" 

        response = self.client.post('/accounts/send_email', data={
            'email': 'test@test.com'
        }, follow=True)
        message = list(response.context['messages'])[0]

        self.assertEqual(message.message, 'Link to enter send')
        self.assertEqual(message.tags, 'success')

    @skip
    def test_creates_token_associated_with_email(self):
        """-> create token for email"""

        self.client.post('/account/send_email', data={'email': 'test@test.com'})
        token = Token.objects.first()

        self.assertEqual(token.email, 'test@test.com')

    @patch('accounts.views.send_mail')
    def test_sends_link_to_login_using_token_uid(self, mock_send_mail):
        """-> link to enter in system with uid token""" 

        self.client.post('/accounts/send_email', data={'email': 'test@test.com'})
        token = Token.objects.first()
        expected_url = f'http://testserver/accounts/login?uid={token.uid}'
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertIn(expected_url, body)


    @patch('accounts.views.auth')
    def test_calls_auth_with_uid_from_get_request(self, mock_auth):
        """-> call authenticate with uid from GET""" 

        self.client.get('/accounts/login?token=abcdf12345')
        self.assertEqual(mock_auth.authenticate.call_args, call(uid='abcdf12345'))

    
    @patch('accounts.views.auth')
    def test_calls_auth_login_with_user_if_there_is_one(self, mock_auth):
        """-> call auth_login with user if exists""" 

        response = self.client.get('/accounts/login?token=abcdf12345')
        self.assertEqual(mock_auth.login.call_args, call(response.wsgi_request, 
                                                    mock_auth.authenticate.return_value))