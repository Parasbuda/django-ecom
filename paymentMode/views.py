from django.shortcuts import render
from rest_framework import viewsets
from .models import PaymentMode
from .serializer import PaymentModeSerializer

# Create your views here.


class PaymentModeViewset(viewsets.ModelViewSet):
    queryset = PaymentMode.objects.all()
    serializer_class = PaymentModeSerializer
    http_method_names = ["get", "post"]
