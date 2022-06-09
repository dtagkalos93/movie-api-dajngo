from django.test import Client, TestCase
from django.urls import reverse

from account.models import User


class MoviesBaseTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(username="viewer_1", password="temppass123!")
        response = self.client.post(
            reverse("login"), {"username": user.username, "password": "temppass123!"}
        )
        token = response.data["token"]
        self.client = Client(HTTP_AUTHORIZATION=f"Bearer {token}")
