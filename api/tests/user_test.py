from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User


class UserTestCase(APITestCase):

    def setUp(self):
         common = User.objects.create(first_name='comum',
                            last_name='teste',
                            username='comum',
                            phone='1234567890123',
                            email='teste@teste.com').set_password('teste')
         token = Token.objects.get(user=common)
         self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

         admin = User.objects.create(first_name='admin',
                             last_name='admin',
                             username='admin',
                             phone='1234567890123',
                             email='admin@teste.com',
                             is_superuser=True).set_password('admin')

    def test_obtain_auth_token(self):
        response = self.client.post(reverse('user-list'),
                                    {
                                        "first_name": "usuario",
                                        "last_name": "test",
                                        "username": "teste",
                                        "phone": "1234567890123",
                                        "email": "teste@teste.com",
                                        "password": "testingpas123"
                                    })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('auth'), {
            "username": "teste",
            "password": "testingpas123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
