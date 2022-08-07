
from rest_framework import serializers
from api.serializers.objective_serializer import ObjetiveSerializer

from finances.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    objetive = ObjetiveSerializer
    
    class Meta:
        model = Category
        fields = '__all__'