from django.test import TestCase
from e_learn.models import Mode
from django.urls import reverse


class UserTest(TestCase):

    def setUp(self):
        self.mode = Mode.objects.create(
            name="próba",
            image="e_learn/home.png",
            url="probka",
            order=4
        )

    def test_create_mode(self):
        self.assertEqual(self.mode.name, "próba")
        self.assertEqual(self.mode.image, "e_learn/home.png")
        self.assertEqual(self.mode.url, "probka")
        self.assertEqual(self.mode.order, 4)

    def test_mode_page_load(self):
        response = self.client.get(
            reverse("home")
        )
        self.assertEqual(response.status_code, 200)
