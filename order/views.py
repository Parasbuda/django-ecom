from functools import partial
from django.shortcuts import render
from rest_framework import viewsets
from .models import OrderMain, OrderDetail
from .serializers import (
    OrderListSerializer,
    OrderMainSerializer,
    OrderDetailSerializer,
    SaveOrderSerializer,
    TableSerializer,
    CustomerSerializer,
)
from django.db import transaction
from customer.models import Customer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from table.models import Table

# Create your views here.


class OrderMainViewset(viewsets.ModelViewSet):
    queryset = OrderMain.objects.all()
    serializer_class = OrderMainSerializer
    http_method_names = ["get"]


class OrderDetailViewset(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    http_method_names = ["get"]


class OrderListViewset(viewsets.ModelViewSet):
    queryset = OrderMain.objects.all()
    serializer_class = OrderListSerializer
    http_method_names = ["get"]


class OrderSaveViewset(viewsets.ModelViewSet):
    queryset = OrderMain.objects.all()
    serializer_class = SaveOrderSerializer
    http_method_names = ["post"]

    def get_customer(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            return False

    def get_table(self, pk):
        try:
            return Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            return False

    @transaction.atomic
    def create(self, request):
        count = OrderMain.objects.count() + 1
        unique_id = "O-" + "{0:0=5d}".format(count)
        request.data["order_no"] = unique_id
        currentDate = datetime.now()

        request.data["date_ad"] = currentDate.strftime("%Y-%m-%d")
        request.data["time"] = currentDate.strftime("%X")
        table = request.data.pop("table")
        table_obj = self.get_table(table)
        customer_obj = self.get_customer(request.data.pop("customer"))
        request.data["customer"] = customer_obj.id
        request.data["table"] = table_obj.id

        if not customer_obj:
            return Response(
                "Customer doesnot exist", status=status.HTTP_400_BAD_REQUEST
            )
        if not table_obj:
            return Response("Table does not exist", status=status.HTTP_400_BAD_REQUEST)

        if table_obj.status == 2 or table_obj.status == 3:
            return Response(
                "Table is either occupied or reserved",
                status=status.HTTP_400_BAD_REQUEST,
            )

        if request.data["net_amount"] <= 0:
            return Response(
                "Grand total cannot be 0 or less than 0",
                status=status.HTTP_400_BAD_REQUEST,
            )
        table_serializer = TableSerializer(table_obj, data={"status": 2}, partial=True)
        order_serializer = SaveOrderSerializer(
            data=request.data, context={"request": request}
        )
        if table_serializer.is_valid():
            if order_serializer.is_valid():
                order_serializer.save()
                table_serializer.save()
                return Response(order_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    order_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(table_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
