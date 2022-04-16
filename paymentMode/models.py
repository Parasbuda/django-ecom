from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class PaymentMode(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
