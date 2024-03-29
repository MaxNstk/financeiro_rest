from finances.models.generic import GenericModel
from finances.models.generic import GenericModel
from django.db.models import CharField, FloatField
from django.core.validators import MinValueValidator 

class Goal(GenericModel):
    name = CharField(max_length=255)
    goal_value = FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self) -> str:
        return self.name