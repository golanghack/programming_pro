from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordLessAuthenticationBackend
from accounts.models import Token

User = get_user_model()

class AuthTest(TestCase):
    """-> auth test""" 

    def test_returns_None_if_no_such_token(self):
        """-> return None if no token"""

        result = PasswordLessAuthenticationBackend().authenticate('no')
        self.assertIsNone(result)

    def test_returns_new_user_with_correct_email_if_token_exists(self):
        """-> return new user if token is correct"""

        email = 'test@test.com'
        token = Token.objects.create(email=email)
        user = PasswordLessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=email)
        self.assertEqual(user, new_user)

    def test_returns_existing_user_with_correct_email_if_token_exists(self):
        """-> return exists user with correct email""" 

        email = 'test@test.com'
        existing_user = User.objects.create(email=email)
        token = Token.objects.create(email=email)
        user = PasswordLessAuthenticationBackend().authenticate(token.uid)
        self.assertEqual(user, existing_user)