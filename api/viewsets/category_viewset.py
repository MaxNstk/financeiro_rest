from api.serializers.category_serializer import CategorySerializer
from api.viewsets.custom_model_viewset import CustomModelViewSet
from finances.models import Category, wallet


class CategoryViewSet(CustomModelViewSet):
    model = Category
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(wallet__user=self.request.user)
