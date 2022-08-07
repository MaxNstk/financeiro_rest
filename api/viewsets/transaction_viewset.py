from api.serializers.transaction_serializer import TransactionSerializer
from api.viewsets.custom_model_viewset import CustomModelViewSet
from finances.models import Transaction


class TransactionViewSet(CustomModelViewSet):
    model = Transaction
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()