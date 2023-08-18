from ..models import Profile, Contact
from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class TestProfileModel(TestCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.user = User.objects.create(username="auth")
        self.profile = Profile.objects.create(user=self.user)
        self.contanct = Contact.objects.create()

    def test_models_have_correct_object_names(self):
        """testing len(__str__)"""

        error_name = "Output dont have len min 9 symbols"
        self.assertEqual(self.profile.__str__(), 9, error_name)
