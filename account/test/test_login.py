from django.test.testcases import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from account.models import User


class LoginTestCase(TestCase):
    def test_should_return_invalid_method_when_request_with_wrong_method(self):
        response = self.client.get(
            reverse("login"), {"username": "user_1", "password": "pass1234!"}
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.data["detail"], 'Method "GET" not allowed.')

    def test_should_return_invalid_credentials_when_no_user_exist(self):
        response = self.client.post(
            reverse("login"), {"username": "user_1", "password": "pass1234!"}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["message"], "Invalid Credentials. Try again.")

    def test_should_return_invalid_credentials_when_wrong_username_given(self):
        User.objects.create_user(username="user_1", password="pass1234!")

        response = self.client.post(
            reverse("login"), {"username": "user_2", "password": "pass1234!"}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["message"], "Invalid Credentials. Try again.")

    def test_should_return_invalid_credentials_when_wrong_password_given(self):
        User.objects.create_user(username="user_1", password="pass123!")

        response = self.client.post(
            reverse("login"), {"username": "user_1", "password": "pass1234!"}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data["message"], "Invalid Credentials. Try again.")

    def test_should_return_success_when_correct_credentials_given(self):
        User.objects.create_user(username="user_1", password="pass1234!")
        response = self.client.post(
            reverse("login"), {"username": "user_1", "password": "pass1234!"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "user_1")
        self.assertIn("token", response.data)
