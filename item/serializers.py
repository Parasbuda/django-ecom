from statistics import mode
from rest_framework import serializers
from .models import PackingType, PackingTypeDetail, SubCategory, Category, Item


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    category = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "active", "category"]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class PackingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingType
        fields = "__all__"


class PackingTypeDetailListSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    packing_type = PackingTypeSerializer()

    class Meta:
        model = PackingTypeDetail
        fields = ["id", "name", "active", "item", "packing_type"]
        


class PackingTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingTypeDetail
        fields = "__all__"
