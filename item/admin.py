from django.contrib import admin
from .models import Category, PackingTypeDetail, SubCategory, Item, PackingType

# Register your models here.


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]


class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "sub_category", "active"]


class PackingTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active"]


class PackingTypeDetailAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "active", "packing_type", "item"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(PackingType, PackingTypeAdmin)
admin.site.register(PackingTypeDetail, PackingTypeDetailAdmin)
