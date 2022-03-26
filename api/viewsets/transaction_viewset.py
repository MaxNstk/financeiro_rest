from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers.transaction_serializer import TransactionSerializer
from finances.models import Transaction


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = [permissions.AllowAny]