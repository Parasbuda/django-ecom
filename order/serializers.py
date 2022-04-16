from dataclasses import field
from rest_framework import serializers
from customer.models import Customer

from table.models import Table
from .models import OrderMain, OrderDetail


class OrderMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMain
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = "__all__"


class OrderListSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True)

    class Meta:
        model = OrderMain
        fields = [
            "id",
            "order_no",
            "status",
            "customer",
            "net_amount",
            "date_ad",
            "time",
            "table",
            "order_details",
        ]


class SaveOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = ["order"]


class SaveOrderSerializer(serializers.ModelSerializer):
    order_details = SaveOrderDetailSerializer(many=True)

    class Meta:
        model = OrderMain
        fields = [
            "id",
            "order_no",
            "status",
            "customer",
            "net_amount",
            "date_ad",
            "time",
            "table",
            "order_details",
        ]

    def create(self, validated_data):
        order_details = validated_data.pop("order_details")
        order_main = OrderMain.objects.create(**validated_data)
        for detail in order_details:
            OrderDetail.objects.create(**detail, order=order_main)

        return order_main


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        field = "__all__"
