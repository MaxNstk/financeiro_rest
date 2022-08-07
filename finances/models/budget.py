from finances.models.generic import GenericModel
from django.db.models import CharField, FloatField
from django.core.validators import MinValueValidator 

class Budget(GenericModel):
    name = CharField(max_length=255)
    spending_ceiling = FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self) -> str:
        return self.name