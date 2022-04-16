from django.db import models

# Create your models here.


class Customer(models.Model):
    SEX_CHOICES = [(1, "MALE"), (2, "FEMALE"), (3, "OTHERS")]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.PositiveSmallIntegerField(
        choices=SEX_CHOICES, help_text="Choice field where 1= male, 2=female,3=others"
    )

    def __str__(self):
        return f"{self.first_name}"  f"{self.last_name}"
