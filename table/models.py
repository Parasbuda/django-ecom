from statistics import mode
from django.db import models

# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=1, blank=True)

    def __str__(self):
        return f"{self.name}"


class Table(models.Model):
    TABLE_CHOICES = [(1, "Vacant"), (2, "Occupied"), (3, "Reserved")]
    name = models.CharField(max_length=30)
    status = models.PositiveSmallIntegerField(
        choices=TABLE_CHOICES, default=1, help_text="1=vacant,2=occupied,3=reserved"
    )
    block = models.ForeignKey(Block, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"
