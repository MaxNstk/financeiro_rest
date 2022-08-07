from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from finances.models import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields='__all__'

    def validate(self, data):
        if ('sub_category' in data) and ('category' not in data):
            raise ValidationError("'sub_category' must be send together with 'category'")

        if 'sub_category' in data and 'category' in data:
            if data['sub_category'].category != data['category']:
                raise ValidationError("sub_category does not reference the sent category")
        return super(TransactionSerializer, self).validate(data)