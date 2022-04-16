from statistics import mode
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = "SubCategories"

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="category"
    )
    name = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class Item(models.Model):
    class Meta:
        verbose_name_plural = "Items"

    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    active = models.BooleanField()

    def __str__(self):
        return self.name


class PackingType(models.Model):
    name = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PackingTypeDetail(models.Model):
    name = models.CharField(max_length=30)
    pack_qty = models.PositiveSmallIntegerField()
    active = models.BooleanField(default=True)
    packing_type = models.ForeignKey(
        PackingType, on_delete=models.PROTECT, related_name="packing_type"
    )
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name="item")

    def __str__(self):
        return self.name
