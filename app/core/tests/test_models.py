"""Import some modules."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models
from unittest.mock import patch


def sample_user(email='test@gmail.com', password='testpass'):
    """Create a sample user."""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test different case for user."""

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful."""
        email = 'test@gmail.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized_email(self):
        """Test the email for a new user is normalized."""
        email = 'test@GMAIL.cOm'
        user = get_user_model().objects.create_user(
            email, 'testpass'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')

    def test_new_superuser(self):
        """Test creating a new superuser."""
        user = get_user_model().objects.create_superuser(
            'test@admin.com',
            'admintest'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
