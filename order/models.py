from django.db import models
from customer.models import Customer
from item.models import Item
from table.models import Table

# Create your models here.


class OrderMain(models.Model):
    ORDER_STATUS = [(1, "Pending"), (2, "Billed"), (3, "Cancelled")]
    order_no = models.CharField(max_length=10, unique=True)
    status = models.PositiveSmallIntegerField(
        choices=ORDER_STATUS, default=1, help_text="1=Pending,2=Billed,3=Cancelled"
    )
    date_ad = models.DateField(blank=True)
    time = models.TimeField(blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.id}-{self.order_no}"


class OrderDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sale_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    qty = models.PositiveIntegerField()
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    order = models.ForeignKey(
        OrderMain, on_delete=models.PROTECT, related_name="order_details"
    )

    def __str__(self):
        return self.id
