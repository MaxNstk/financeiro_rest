
from django.db import models

class Wallet(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.user = self.request.user
        return super(Wallet, self).save(*args, **kwargs)