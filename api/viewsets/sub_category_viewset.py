from api.serializers.objective_serializer import ObjetiveSerializer
from api.viewsets.custom_model_viewset import CustomModelViewSet
from finances.models import SubCategory


class SubCategoryViewSet(CustomModelViewSet):
    model = SubCategory
    serializer_class = ObjetiveSerializer
    queryset = SubCategory.objects.all()