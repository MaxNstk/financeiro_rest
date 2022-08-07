from rest_framework.serializers import ModelSerializer

from finances.models import SubCategory
from serializers.category_serializer import CategorySerializer

class ObjetiveSerializer(ModelSerializer):
    category = CategorySerializer

    class Meta:
        model = SubCategory
        fields= ['category', 'description']