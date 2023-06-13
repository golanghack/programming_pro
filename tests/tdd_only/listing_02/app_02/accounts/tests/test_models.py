from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    """-> model user test""" 

    def test_user_is_valid_with_email_only(self):
        """-> user with only email""" 

        user = User(email='test@test.com')
        user.full_clean()
