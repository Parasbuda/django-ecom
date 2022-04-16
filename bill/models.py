from django.db import models
from additionalCharge.models import AdditionalCharge
from order.models import OrderDetail, OrderMain
from paymentMode.models import PaymentMode

# Create your models here.


class BillMain(models.Model):
    PAY_TYPES = [(1, "Cash"), (2, "Credit")]
    order = models.ForeignKey(OrderMain, on_delete=models.PROTECT)
    bill_no = models.CharField(max_length=10, unique=True)
    pay_type = models.PositiveSmallIntegerField(choices=PAY_TYPES, default=1)

    def __str__(self):
        return self.bill_no


class BillDetail(models.Model):
    bill = models.ForeignKey(
        BillMain, on_delete=models.PROTECT, related_name="bill_details"
    )
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.PROTECT)

    def __str__(self):
        return self.bill


class PaymentDetail(models.Model):
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.PROTECT)
    amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=100)
    bill = models.ForeignKey(
        BillMain, on_delete=models.PROTECT, related_name="payment_details"
    )

    def __str__(self):
        return self.payment_mode


class AdditionalChargeType(models.Model):
    additional_charge = models.ForeignKey(AdditionalCharge, on_delete=models.PROTECT)
    amount = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    remarks = models.CharField(max_length=100)
    bill = models.ForeignKey(
        BillMain, on_delete=models.PROTECT, related_name="additional_charge_types"
    )

    def __str__(self):
        return self.additional_charge
