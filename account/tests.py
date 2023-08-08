import json
import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()

from rest_framework.test import APITestCase
from django.urls import reverse


class UserRegistrationTestCase(APITestCase):
    url = reverse('account:register')
    url_login = reverse("token_obtain_pair")

    def test_user_registration(self):
        """
            Doğru verilerle kayıt işlemi.
        """

        data = {
            "username": "behram125",
            "password": "1111qwer"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_user_invalid_password(self):
        """
            Şifre invalid olabilir.
        """

        data = {
            "username": "behram125",
            "password": "1"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_unique_name(self):
        """
            Kullanıcı adı kullanılmış olabilir.

        """
        self.test_user_registration()
        data = {
            "username": "behram125",
            "password": "qeqwqe12"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_user_authenticated_registration(self):
        """
            session ile giriş yapmış kullanıcı sayfayı görememeli.

        """
        self.test_user_registration()
        self.client.login(username="behram125", password="1111qwer")
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    def test_user_authenticated_token_registration(self):
        """
            token ile giriş yapmış kullanıcı sayfayı görememeli.

        """
        self.test_user_registration()
        data = {
            "username": "behram125",
            "password": "1111qwer"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response_2 = self.client.get(self.url)
        self.assertEqual(403, response_2.status_code)


class UserLogin(APITestCase):
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "behram"
        self.password = "sifre1234"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_user_token(self):
        response = self.client.post(self.url_login, {"username": "behram", "password": "sifre1234"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("access" in json.loads(response.content))

    def test_user_invalid_data(self):
        response = self.client.post(self.url_login, {"username": "adasa", "password": "sifre1234"})
        self.assertEqual(401, response.status_code)

    def test_user_empty_data(self):
        response = self.client.post(self.url_login, {"username": "", "password": ""})
        self.assertEqual(400, response.status_code)


class UserPasswordChange(APITestCase):
    url = reverse("account:change-password")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "behram"
        self.password = "sifre1234"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def login_with_token(self):
        data = {
            "username": "behram",
            "password": "sifre1234"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_information(self):
        self.login_with_token()
        data = {
            "old_password": "sifre1234",
            "new_password": "1111qwer"
        }

        response = self.client.put(self.url, data)
        self.assertEqual(204, response.status_code)

    def test_with_wrong_information(self):
        self.login_with_token()
        data = {
            "old_password": "132113132fsfsa",
            "new_password": "1111qwer12"
        }

        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)

    def test_with_empty_information(self):
        self.login_with_token()
        data = {
            "old_password": "",
            "new_password": ""
        }

        response = self.client.put(self.url, data)
        self.assertEqual(400, response.status_code)


class UserProfileUpdate(APITestCase):
    url = reverse("account:me")
    url_login = reverse("token_obtain_pair")

    def setUp(self):
        self.username = "behram"
        self.password = "sifre1234"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def login_with_token(self):
        data = {
            "username": "behram",
            "password": "sifre1234"
        }
        response = self.client.post(self.url_login, data)
        self.assertEqual(200, response.status_code)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_is_authenticated_user(self):
        response = self.client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_with_valid_information(self):
        self.login_with_token()
        data = {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "",
                "twitter": "asdas"
            }
        }

        response = self.client.put(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content), data)

    def test_with_empty_information(self):
        self.login_with_token()
        data = {
            "id": 1,
            "first_name": "",
            "last_name": "",
            "profile": {
                "id": 1,
                "note": "",
                "twitter": ""
            }
        }

        response = self.client.put(self.url, data, format='json')
        self.assertEqual(200, response.status_code)
        self.assertEqual(json.loads(response.content), data)