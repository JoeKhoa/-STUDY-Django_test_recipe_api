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