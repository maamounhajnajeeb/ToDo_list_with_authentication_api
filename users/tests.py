from rest_framework.test import APIClient, APITestCase
from rest_framework.test import force_authenticate
from rest_framework import status

from django.contrib.auth import get_user_model, authenticate, login

# Create your tests here.

class UsersTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        
        self.signup_data = {
            "username" : "ZahraaHNajeeb",
            "email": "zahraa.h.najeeb@gmail.com",
            "password": "17AiGz48rhe",
            "phone_number": "9327153130"
        }
        self.login_data = {
            "username": "ZahraaHNajeeb",
            "password": "17AiGz48rhe"
        }
        
        self.signup_url = "/api/v1/users/signup/"
        self.login_url = "/api/v1/users/login/"
    
    def test_create_contact(self):
        data = self.signup_data
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 1)
        self.assertEqual(get_user_model().objects.first().get_username(), "ZahraaHNajeeb")
        
    def test_login_api(self):
        data = self.login_data
        self.client.login(**data)
        response = self.client.get("api/v1/users/profile")
        # self.client.
        # response = self.client.post(
        #     self.login_url, data,
        #     content_type="application/json"
        #     )
        self.assertEqual(response.status_code, status.HTTP_200_OK)