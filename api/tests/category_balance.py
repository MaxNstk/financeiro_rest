from django.urls import reverse
from rest_framework import status

from api.tests.custom_API_test_case import CustomAPITestCAse
from finances.models import Transaction, Category, SubCategory
from datetime import datetime, timedelta


class CategoryBalance(CustomAPITestCAse):

    def setUp(self):
        super(CategoryBalance, self).setUp()
        self.food_category = Category.objects.create(name='comida', wallet=self.wallet)
        self.house_category = Category.objects.create(name='casa',wallet=self.wallet)

        Transaction.objects.create(description='carne no mercado',
                                    category=self.food_category, 
                                    type=Transaction.EXPENSE,
                                    value=100,
                                    wallet=self.wallet
                                )
        Transaction.objects.create(description='pizza',
                                    category=self.food_category, 
                                    type=Transaction.EXPENSE,
                                    value=65.50,
                                    wallet=self.wallet
                                )
        Transaction.objects.create(description='reboco',
                                    category=self.house_category, 
                                    type=Transaction.EXPENSE,
                                    value=45,
                                   wallet=self.wallet

                                   )
        Transaction.objects.create(description='furadeira',
                                    category=self.house_category, 
                                    type=Transaction.EXPENSE,
                                    value=233.50,
                                    wallet=self.wallet
                                )
        Transaction.objects.create(description='rancho do mês',
                                    category=self.food_category, 
                                    type=Transaction.EXPENSE,
                                    value=750,
                                    date=datetime.now() - timedelta(days=31),
                                    wallet=self.wallet
                                )
        Transaction.objects.create(description='vendi a casa',
                                    category=self.food_category, 
                                    type=Transaction.CREDIT,
                                    value=400000,
                                    wallet=self.wallet
                                   )

    def test_categories_balance(self):
        response = self.client.get(reverse('category_balance'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categories_balance_unauthorized(self):
        self.client.credentials()
        response = self.client.get(reverse('category_balance'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)