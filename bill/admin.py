from django.contrib import admin

from bill.models import AdditionalChargeType, BillDetail, BillMain, PaymentDetail

# Register your models here.
class BillMainAdmin(admin.ModelAdmin):
    list_display = ["id", "bill_no", "pay_type"]


class BillDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "bill", "order_detail"]


class PaymentDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "payment_mode", "amount", "remarks", "bill"]


class AdditionalChargeTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "additional_charge", "amount", "remarks", "bill"]


admin.site.register(BillMain, BillMainAdmin)
admin.site.register(BillDetail, BillDetailAdmin)
admin.site.register(PaymentDetail, PaymentDetailAdmin)
admin.site.register(AdditionalChargeType, AdditionalChargeTypeAdmin)
