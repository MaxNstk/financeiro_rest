from django.db import models
from django.db.models import Model

class GenericModel(Model):
    wallet = models.ForeignKey('finances.Wallet', on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True