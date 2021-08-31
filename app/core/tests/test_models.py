from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_succesful(self):
        """ Test creating a new user with an email is succesful """
        email = "test@drf.com"
        password = "Mysecurepass123"
        user = get_user_model().objects.create_user(
            email, 
            password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))