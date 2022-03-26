from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from api.serializers.category_serializer import CategorySerializer
from finances.models import Category


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]