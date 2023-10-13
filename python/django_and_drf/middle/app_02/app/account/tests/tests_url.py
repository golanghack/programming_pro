from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from account.models import Profile, Contact

User = get_user_model()


class TestStaticURL(TestCase):
    def setUp(self):
        self.client = Client()

    def test_urls_correct_template_used(self) -> None:
        templates_url: dict = {
            "": "/account/login.html",
        }

        for address, template in templates_url.items():
            with self.subTest(address=address):
                response = self.client.get(address)
                error_name: str = f"Error -> {address} waiting template {template}"

                self.assertTemplateNotUsed(response, template, error_name)


class TestAccountURL(TestCase):
    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username="auth")
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.profile = Profile.objects.create(user=self.user)
        self.contact = Contact.objects.create(
            user_from=self.user,
            user_to=self.user,
        )

    def test_urls_quest_client(self):
        """NON AUTHORIZED USER PERMISSION"""

        pages = ("", "/users/", "/users/follow/")

        for page in pages:
            response = self.guest_client.get(page)
            error_name = f"Error -> permission diened for {page}"
            self.assertEqual(response.status_code, 302, error_name)

    def test_register_page_status_200(self):
        """Register page displays for guest user"""

        register_page = "/register/"
        response = self.guest_client.get(register_page)
        error_name = f"Error -> dont show  {register_page}"
        self.assertEqual(response.status_code, 200, error_name)

    def test_edit_page_status_301(self):
        """Register page displays for guest user"""

        edit_page = "/edit"
        response = self.guest_client.get(edit_page)
        error_name = f"Error -> dont use  {edit_page}"
        self.assertEqual(response.status_code, 301, error_name)

    def test_redirect_non_auth_user(self):
        url_one = "/login/?next=/"
        url_two = "/login/?next=/"
        pages = {"": url_one, "": url_two}
        for page, value in pages.items():
            response = self.guest_client.get(page)
            self.assertRedirects(response, value)
