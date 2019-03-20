from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with email"""
        email = 'master@luckiest.com'
        password = 'theMaistro'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test new user email normalized"""
        email = 'master@KING.com'
        user = get_user_model().objects.create_user(email, 'tester.com')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test new user invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='testercom'
            )

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@testing.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
