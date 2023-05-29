from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from account.models import Profile

User = get_user_model()

class TestProfilePages(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Profile.objects.create()

    def setUp(self):
        self.user = User.objects.create(username='John')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_about_page_uses_correct_template(self):
        response = self.authorized_client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'accunt/dashboard.html')
