from django.contrib import admin
from .models import Block, Table

# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "display_order", "active"]


class TableAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "status", "block", "active"]


admin.site.register(Block, BlockAdmin)
admin.site.register(Table, TableAdmin)
