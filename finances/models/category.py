from django.db import models

from finances.models.generic import GenericModel


class Category(GenericModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    objetive = models.ForeignKey('Objetive', on_delete=models.DO_NOTHING)    
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name