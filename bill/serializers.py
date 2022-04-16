from dataclasses import field
from statistics import mode
from rest_framework import serializers
from order.models import OrderMain
from order.serializers import OrderMainSerializer, OrderDetailSerializer
from table.models import Table
from .models import AdditionalChargeType, BillDetail, BillMain, PaymentDetail
from additionalCharge.serializer import AdditionalChargeSerializer
from paymentMode.serializer import PaymentModeSerializer


class BillMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillMain
        fields = "__all__"


class BillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetail
        fields = "__all__"


class SaveBillDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetail
        exclude = ["bill"]


class SavePaymentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetail
        exclude = ["bill"]


class SaveAdditionalChargeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalChargeType
        exclude = ["bill"]


class SaveBillSerializer(serializers.ModelSerializer):
    bill_details = SaveBillDetailSerializer(many=True)
    payment_details = SavePaymentDetailSerializer(many=True)
    additional_charge_types = SaveAdditionalChargeTypeSerializer(many=True)

    class Meta:
        model = BillMain
        fields = [
            "id",
            "bill_no",
            "pay_type",
            "order",
            "bill_details",
            "payment_details",
            "additional_charge_types",
        ]

    def create(self, validated_data):
        bill_details = validated_data.pop("bill_details")
        payment_details = validated_data.pop("payment_details")
        additional_charge_types = validated_data.pop("additional_charge_types")
        bill_main = BillMain.objects.create(**validated_data)

        for details in bill_details:
            BillDetail.objects.create(**details, bill=bill_main)

        for details in payment_details:
            PaymentDetail.objects.create(**details, bill=bill_main)

        for types in additional_charge_types:
            AdditionalChargeType.objects.create(**types, bill=bill_main)
        return bill_main


class BillListDetailSerializer(serializers.ModelSerializer):
    order_detail = OrderDetailSerializer()

    class Meta:
        model = BillDetail
        fields = ["id", "order_detail"]


class BillListSerializer(serializers.ModelSerializer):
    bill_details = BillListDetailSerializer(many=True)
    order = OrderMainSerializer()

    class Meta:
        model = BillMain
        fields = ["id", "bill_no", "pay_type", "order", "bill_details"]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class PaymentDetailSerializer(serializers.ModelSerializer):
    payment_mode = PaymentModeSerializer()

    class Meta:
        model = PaymentDetail
        fields = ["id", "payment_mode", "amount", "remarks"]


class AdditionalChargeTypeSerializer(serializers.ModelSerializer):
    additional_charge = AdditionalChargeSerializer()

    class Meta:
        model = AdditionalChargeType
        fields = ["id", "additional_charge", "amount", "remarks"]
