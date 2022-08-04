
from django.db import models

class SubCategory(models.Model):
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=255)