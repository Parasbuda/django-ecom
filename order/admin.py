from django.contrib import admin

from order.models import OrderDetail, OrderMain

# Register your models here.
class OrderMainAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order_no",
        "customer",
        "date_ad",
        "time",
        "status",
        "net_amount",
    ]


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "order",
        "item",
        "purchase_cost",
        "sale_cost",
        "qty",
        "grand_total",
    ]


admin.site.register(OrderMain, OrderMainAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
