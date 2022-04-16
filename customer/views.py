from django import http
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CustomerSerializer
from customer.models import Customer
# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    http_methods_names=["get","post"]