from dataclasses import field
from rest_framework import serializers
from .models import PaymentMode


class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = "__all__"
