from finances.models.generic import GenericModel
from finances.models.generic import GenericModel
from django.db.models import IntegerField, CharField, FloatField
from django.core.validators import MinValueValidator 

class Objective(GenericModel):

    GOAL = 1
    BUDGET = 2 

    objetive_types = [(GOAL, "Meta"),(BUDGET, "Orçamento")]
    type = IntegerField(choices=objetive_types)
    name = CharField(max_length=255)
    goal_value = FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self) -> str:
        return self.name