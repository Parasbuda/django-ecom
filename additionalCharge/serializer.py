from rest_framework import serializers
from .models import AdditionalCharge


class AdditionalChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalCharge
        fields = "__all__"
