from rest_framework.viewsets import ModelViewSet

from api.serializers.user_serializer import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
