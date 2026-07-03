from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import User
from django.urls import reverse

User = get_user_model()


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="k.czesko@wp.pl",
            username="czesko",
            password="czesko123"
        )

    def test_create_user(self):
        self.assertEqual(self.user.email, "k.czesko@wp.pl")
        self.assertEqual(self.user.username, "czesko")
        self.assertTrue(self.user.check_password("czesko123"))

    def test_update_user_data(self):
        logged = self.client.login(
            username="czesko",
            password="czesko123"
            )

        self.assertTrue(logged)

        response = self.client.post(
            reverse("account"),
            {
                "first_name": "Adam",
                "last_name": "Nowak",
                "username": "adam",
                "email": "adam@nowak.pl",
            }
        )

        self.assertRedirects(response, reverse("account"))

        self.user.refresh_from_db()

        self.assertEqual(self.user.first_name, "Adam")
        self.assertEqual(self.user.last_name, "Nowak")
        self.assertEqual(self.user.username, "adam")
        self.assertEqual(self.user.email, "adam@nowak.pl")

    def test_account_requires_login(self):
        response = self.client.get(reverse("account"))

        self.assertEqual(response.status_code, 302)
