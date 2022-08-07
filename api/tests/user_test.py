from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from api.tests.custom_API_test_case import CustomAPITestCAse


class UserTestCase(CustomAPITestCAse):

    def setUp(self):

        super(UserTestCase, self).setUp()
        User.objects.create(first_name='comum',
                        last_name='teste',
                        username='non_auth',
                        phone='1234567890123',
                        email='teste@teste.com').set_password('teste')

        admin = User.objects.create(first_name='admin',
                         last_name='admin',
                         username='admin',
                         phone='1234567890123',
                         email='admin@teste.com',
                         is_superuser=True)
        admin.set_password('testingpas123')
        admin.save()

    def test_obtain_auth_token(self):
        self.client.credentials()
        response = self.client.post(reverse('auth'), {
            "username": "admin",
            "password": "testingpas123"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        self.client.credentials()
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

    def test_update_user(self):
        user = User.objects.get(username='auth')
        auth_response = self.client.put(reverse('user-detail', kwargs={'pk': user.id}),
                                        {
                                            'first_name': 'testing',
                                            'last_name': 'testing',
                                            'username': 'testing',
                                            'phone': '1234567890123',
                                            'email': 'testado@teste.com',
                                            'password': 'adrianegay123'
                                        })
        self.assertEqual(auth_response.status_code, status.HTTP_200_OK)

    def test_update_user_not_authorized(self):
        user = User.objects.get(username='non_auth')
        auth_response = self.client.put(reverse('user-detail', kwargs={'pk': user.id}),
                                        {
                                            'first_name': 'testing',
                                            'last_name': 'testing',
                                            'username': 'testing',
                                            'phone': '1234567890123',
                                            'email': 'testado@teste.com',
                                            'password': 'adrianegay123'
                                        })
        self.assertEqual(auth_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_user_without_token(self):
        user = User.objects.get(username='auth')
        self.client.credentials()
        auth_response = self.client.put(reverse('user-detail', kwargs={'pk': user.id}),
                                        {
                                            'first_name': 'testing',
                                            'last_name': 'testing',
                                            'username': 'testing',
                                            'phone': '1234567890123',
                                            'email': 'testado@teste.com',
                                            'password': 'adrianegay123'
                                        })
        self.assertEqual(auth_response.status_code, status.HTTP_401_UNAUTHORIZED)