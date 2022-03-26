from datetime import datetime

from django.db import models


class Transaction(models.Model):

    CREDIT = 1
    EXPENSE = 2

    type_CHOICES = [(CREDIT, 'Renda'),
                    (EXPENSE, 'Despesa')]

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    type = models.IntegerField(choices=type_CHOICES, default=2)
    value = models.FloatField()
    description = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateField(default=datetime.now().date())

    def __str__(self):
        return self.description