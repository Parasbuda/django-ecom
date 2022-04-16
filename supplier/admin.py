from django.contrib import admin

from supplier.models import Supplier

# Register your models here.


class SupplierAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "address", "phone_no", "photo"]


admin.site.register(Supplier, SupplierAdmin)
