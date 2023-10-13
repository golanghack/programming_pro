from django.test import TestCase
from django.contrib.auth import get_user_model

class MyUserTest(TestCase):
    def test_create_user(self):
        """Testing funcionality for creating user"""

        User = get_user_model()
        user = User.objects.create_user(username='test', 
                                    email='test@test.com', 
                                    password='test123')

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Creating superuser"""

        User = get_user_model()
        admin = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@admin.com',
            password='test123'
        )
        self.assertEqual(admin.username, 'superadmin')
        self.assertEqual(admin.email, 'superadmin@admin.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

