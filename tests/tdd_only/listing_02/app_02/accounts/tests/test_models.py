from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Token

User = get_user_model()

class UserModelTest(TestCase):
    """-> model user test""" 

    def test_user_is_valid_with_email_only(self):
        """-> user with only email""" 

        user = User(email='test@test.com')
        user.full_clean()

    def test_email_is_primary_key(self):
        """-> email is primary key"""

        user = User(email='test@test.com')
        self.assertEqual(user.pk, 'test@test.com')

class TokenModelTest(TestCase):
    """-> Token model test""" 

    def test_links_user_with_auto_generated_uid(self):
        """-> user networking eith auto id""" 

        token1 = Token.objects.create(email='test@test.com')
        token2 = Token.objects.create(email='test@test.com')
        self.assertNotEqual(token1.uid, token2.uid)
