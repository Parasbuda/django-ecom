from django.contrib import admin

from paymentMode.models import PaymentMode

# Register your models here.


class PaymentModeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]


admin.site.register(PaymentMode, PaymentModeAdmin)
