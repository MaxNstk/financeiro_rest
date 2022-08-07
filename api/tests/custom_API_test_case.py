from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import User
from finances.models import Wallet


class CustomAPITestCAse(APITestCase):

    def setUp(self):
        auth_user = User.objects.create(first_name='autorizado',
                                        last_name='teste',
                                        username='auth',
                                        phone='1234567890123',
                                        email='teste@teste.com')
        auth_user.set_password('teste')
        auth_user.save()
        self.wallet = Wallet.objects.create(user=auth_user, name='test')

        self.payload = {'wallet': self.wallet.id}

        self.token = Token.objects.create(user=auth_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
