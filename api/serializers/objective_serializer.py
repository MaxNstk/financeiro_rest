from rest_framework.serializers import ModelSerializer

from finances.models import Objective

class ObjetiveSerializer(ModelSerializer):
    class Meta:
        model = Objective
        fields= ['objetive_types','type','name','goal_value']