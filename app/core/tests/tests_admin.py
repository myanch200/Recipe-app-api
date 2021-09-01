from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """Assigning the test client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@drf.com',
            password='pass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@drf.com',
            password='pass123',
            name="John Smith"
        )

    def test_users_listed(self):
        """Tests that users are listed in admin page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)