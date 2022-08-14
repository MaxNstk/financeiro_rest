from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from finances.models import Transaction, Category
from datetime import datetime
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import status


class CategoryBalance(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        try:
            now = datetime.now()
            initial_date = self.request.query_params.get('initial_date', now - timedelta(days=30))
            final_date = self.request.query_params.get('final_date', now)
            type = self.request.query_params.get('initial_date', Transaction.EXPENSE)
            transaction_qs = Transaction.objects.filter(type=type, date__gte=initial_date, date__lte=final_date)

            total_value = transaction_qs.aggregate(Sum('value'))['value__sum']

            categories_balance = {
                'total_value': total_value,
                'transaction_amount': len(transaction_qs),
                'categories': {}}

            for category in Category.objects.filter(active=True):
                filtered_transaction_qs = transaction_qs.filter(category=category)
                category_value = filtered_transaction_qs.aggregate(Sum('value'))['value__sum']

                categories_balance['categories'][category.name] = {}
                categories_balance['categories'][category.name]['transaction_amount'] = len(filtered_transaction_qs)
                categories_balance['categories'][category.name]['value'] = category_value
                categories_balance['categories'][category.name]['percentage'] = (category_value / total_value) * 100

            return Response(categories_balance, status=status.HTTP_200_OK)

        except Exception as e:
            # TODO implements a good treatment for exceptions
            return Response({'invalid' : 'there are errors'}, status=status.HTTP_400_BAD_REQUEST)


class MockedCategoryBalance(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):

        categories_balance = {'total_value': 444.0, 'transaction_amount': 4, 'categories': {'comida': {'transaction_amount': 2, 'value': 165.5, 'percentage': 37.27477477477478}, 'casa': {'transaction_amount': 2, 'value': 278.5, 'percentage': 62.72522522522522}}}

        return Response(categories_balance, status=status.HTTP_200_OK)