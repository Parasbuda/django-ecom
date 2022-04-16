from django.shortcuts import render
from rest_framework import viewsets

from additionalCharge.models import AdditionalCharge
from .serializer import AdditionalChargeSerializer

# Create your views here.


class AdditionalChargeViewset(viewsets.ModelViewSet):
    queryset = AdditionalCharge.objects.all()
    serializer_class = AdditionalChargeSerializer
    http_method_names = ["get", "post"]
