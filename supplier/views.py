from django.shortcuts import render
from rest_framework import viewsets

from supplier.models import Supplier
from .serializers import SupplierSerializer

# Create your views here.


class SupplierViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    http_method_name = ["get", "post"]
