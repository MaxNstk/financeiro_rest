from datetime import datetime

from django.db import models

from account.models.generic import GenericModel
from django.core.validators import MinValueValidator



class Transaction(GenericModel):

    CREDIT = 1
    EXPENSE = 2

    WEEKLY = 1
    BIWEEKLY = 2
    MONTHLY = 3
    BI_MONTHLY = 4
    SEMIANUALLY = 5
    YEARLY = 6


    type_CHOICES = [(CREDIT, 'Renda'),
                    (EXPENSE, 'Despesa')]

    recurrence_CHOICES = [
        (WEEKLY, 'Semanalmente'),
        (BIWEEKLY, 'Bimestralmente'),
        (MONTHLY, 'Mensalmente'),
        (BI_MONTHLY, 'Bimestralmente'),
        (SEMIANUALLY, 'Semestralmente'),
        (YEARLY, 'Anualmente'),
    ]

    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    sub_category = models.ForeignKey('SubCategory', on_delete=models.DO_NOTHING, null=True, blank=True)
    type = models.IntegerField(choices=type_CHOICES, default=2)
    value = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.TextField(max_length=255, null=True, blank=True)
    date = models.DateField(default=datetime.today)
    recurrence_type = models.IntegerField(choices=recurrence_CHOICES)

    def save(self, *args, **kwargs):
        if self.recurrence_type:
            self.create_recurrence_instances()
        return super(Transaction, self).save(*args, **kwargs)


        match self.recurrence_type:
            case self.WEEKLY:
                pass
            case self.BIWEEKLY:
                pass
            case self.MONTHLY:
                pass
            case self.BI_MONTHLY:
                pass
            case self.SEMIANUALLY
                pass
            case self.YEARLY:
                pass

    def __str__(self):
        return self.description