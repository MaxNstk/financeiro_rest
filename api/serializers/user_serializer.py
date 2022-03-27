from rest_framework.serializers import ModelSerializer

from account.models.user import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'phone', 'email', 'password']