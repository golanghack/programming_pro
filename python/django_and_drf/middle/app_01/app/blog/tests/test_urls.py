from django.test import TestCase, Client
from ..models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


class TestStaticPagesURL(TestCase):
    def setUp(self):
        """Don`t authorisation client."""

        super().setUpClass()
        self.guest_client = Client()

    def test_home_url_exists_at_desired_location(self):
        """Testing url /blog/"""

        response = self.guest_client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_home_url_uses_correct_template(self):
        """Testing template for url /blog/"""

        response = self.guest_client.get("/blog/")
        self.assertTemplateUsed(response, "blog/base.html")


class TestCommonURL(TestCase):
    def setUp(self):
        """Don`t authorisation client"""

        self.guest_client = Client()

    def test_home_url_exists_at_desired_location(self):
        """Page ->/<- open every user"""

        response = self.guest_client.get("/blog/")
        self.assertEqual(response.status_code, 200)

    def test_list_post_url_exists_at_desired_location(self):
        """Post feed visible every users"""

        response = self.guest_client.get("/blog/feed/")
        self.assertEqual(response.status_code, 200)

    def test_blog_search_url(self):
        response = self.guest_client.get("/blog/search/")
        self.assertEqual(response.status_code, 200)


class TestPostTemplateUsed(TestCase):
    @classmethod
    def setUpClass(cls):
        my_test_user_template = User.objects.create_user(
            username="test_user_template",
            email="test_template@test.com",
            password="pass123",
        )
        super().setUpClass()
        Post.objects.create(
            title="Test post",
            body="Test text blog",
            author=my_test_user_template,
            slug="test_slug",
        )

    def setUp(self):
        # create anonnymouse client
        self.guest_client = Client()

    def test_home_url_uses_correct_template(self):
        """home -> template base"""

        response = self.client.get("/blog/")
        self.assertTemplateUsed(response, "blog/base.html")

    def test_search_url_uses_correct_template(self):
        """List detail"""

        response = self.client.get("/blog/search/")
        self.assertTemplateUsed(response, "blog/post/search.html")
