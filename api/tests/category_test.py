from django.urls import reverse
from rest_framework import status

from api.tests.custom_API_test_case import CustomAPITestCAse


class CategoryTestCase(CustomAPITestCAse):

    def test_create_category(self):
        self.payload.update({
                            'name': 'test_category',
                            'description': 'testing',
                            'objetive': None,
                         })
        response = self.client.post(reverse('category-list'),
                         data=self.payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_create_not_auth_category(self):
        self.client.credentials()
        response = self.client.post(reverse('category-list'),
                         data={
                            'name': 'test_category',
                            'description': 'testing',
                            'objetive': None,
                         })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)