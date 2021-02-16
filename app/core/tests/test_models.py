from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""
        email = 'test@dev.com'
        password = 'test@pw'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        # check_password is DJ-built-in

    # nomalize email then test
    def test_new_user_email_normalize(self):
        """test the email for a new user is normalize"""
        email = 'test@dev.COM'
        user = get_user_model().objects.create_user(email, 'pass@word')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass@word')

    def test_create_new_super_user(self):
        """Test create a super user with an email """
        email = 'test_super_user@dev.com'
        password = 'test@pw'
        user = get_user_model().objects.create_super_user(
            email=email,
            password=password
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
