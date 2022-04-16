from django.contrib import admin

from additionalCharge.models import AdditionalCharge

# Register your models here.


class AdditionalChargeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]


admin.site.register(AdditionalCharge, AdditionalChargeAdmin)
