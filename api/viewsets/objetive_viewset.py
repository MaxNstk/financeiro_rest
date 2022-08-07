from api.serializers.objective_serializer import ObjetiveSerializer
from api.viewsets.custom_model_viewset import CustomModelViewSet
from finances.models import Objective


class ObjectiveViewSet(CustomModelViewSet):
    model = Objective
    serializer_class = ObjetiveSerializer
    queryset = Objective.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(wallet__user=self.request.user)