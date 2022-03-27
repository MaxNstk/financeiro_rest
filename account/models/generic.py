from django.db import models
from django.db.models import Model


class GenericModel(Model):
    user = models.ForeignKey('account.User', on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True