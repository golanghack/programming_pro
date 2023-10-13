from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment
from model_bakery import baker


class PostTest(TestCase):
    def test_creating_object(self):
        user_one = User.objects.create()
        title_post = Post.objects.create(title="second", author=user_one)
        self.assertEqual(title_post.title, "second")
        self.assertEqual(Post.objects.count(), 2)

    @classmethod
    def setUpClass(cls):
        my_test_user = User.objects.create_user(
            username="test_user", email="test@test.com", password="pass123"
        )

        super().setUpClass()
        cls.post = Post.objects.create(
            title="one post 1",
            body="one post",
            slug="one_blog",
            author=my_test_user,
            status="Published",
        )

    def test_title(self):
        """test verbose name"""

        post = PostTest.post
        verbose = post._meta.get_field("title").verbose_name

        self.assertEqual(verbose, "Title")

    def test_object_name_is_title_fild(self):
        """testing __str__ -> post.title"""

        post = PostTest.post
        excpected_object_name = post.title

        self.assertEqual(excpected_object_name, str(post))

    # subtesting
    def test_verbose_naming(self):
        post = PostTest.post
        field_verboses = {
            "title": "Title",
            "body": "Enter text",
            "slug": "slug",
        }

        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_value
                )

    def test_text_to_slug_convertion(self):
        """From title to slug"""

        post = PostTest.post
        slug = post.slug
        self.assertEqual(slug, "one_blog")

    def test_text_slug_max_lenght_not_exceed(self):
        """Long slug breaking and dont more max_lenght"""

        post = PostTest.post
        max_length_slug = post._meta.get_field("slug").max_length
        lenght_slug = len(post.slug) * 37.5
        self.assertEqual(max_length_slug, lenght_slug)
