from django.urls import reverse
from rest_framework import status

from api.tests.custom_API_test_case import CustomAPITestCAse
from finances.models import Transaction, Category, SubCategory


class TransactionTestCase(CustomAPITestCAse):


    def setUp(self):
        super(TransactionTestCase, self).setUp()
        self.category1 = Category.objects.create(name='test1', wallet=self.wallet)
        self.category2 = Category.objects.create(name='test2',wallet=self.wallet)
        self.subcategory1 = SubCategory.objects.create(category=self.category1, description='test1')
        self.subcategory2 = SubCategory.objects.create(category=self.category2, description='test2')

    def test_create_transaction(self):

        self.payload.update({'description': 'testing',
                            'type': Transaction.EXPENSE,
                            'category': self.category1.id,
                            'sub_category': self.subcategory1.id,
                            'value':100,
        })
        response = self.client.post(reverse('transaction-list'),
                                    data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # sub_categories should reference the right category
    def test_create_transaction_with_invalid_category(self):
        self.payload.update(({'description': 'testing',
                            'type': Transaction.EXPENSE,
                            'category': self.category1.id,
                            'sub_category': self.subcategory2.id,
                            'value':100,
        }))
        response = self.client.post(reverse('transaction-list'),
                                    data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_transaction_without_category(self):
        self.payload.update(({'description': 'testing',
                            'type': Transaction.EXPENSE,
                            'sub_category': self.subcategory2.id,
                            'value':100,
        }))
        response = self.client.post(reverse('transaction-list'),
                                    data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unauthorized_category_request(self):
        self.client.credentials()
        self.payload.update({'description': 'testing',
                             'type': Transaction.EXPENSE,
                             'category': self.category1.id,
                             'sub_category': self.subcategory1.id,
                             'value': 100,
                             })
        response = self.client.post(reverse('transaction-list'),
                                    data=self.payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)