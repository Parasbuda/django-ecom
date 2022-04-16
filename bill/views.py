from functools import partial
from django import http
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from bill.models import BillDetail, BillMain, PaymentDetail, AdditionalChargeType
from bill.serializers import TableSerializer
from table.models import Table
from .serializers import (
    BillListSerializer,
    BillMainSerializer,
    BillDetailSerializer,
    SaveBillSerializer,
    PaymentDetailSerializer,
    AdditionalChargeTypeSerializer,
)
from django.db import transaction
from order.models import OrderMain

# Create your views here.
class PaymentDetailViewset(viewsets.ModelViewSet):
    queryset = PaymentDetail.objects.all()
    serializer_class = PaymentDetailSerializer
    http_method_names = ["get"]


class AdditionalChargeTypeViewset(viewsets.ModelViewSet):
    queryset = AdditionalChargeType.objects.all()
    serializer_class = AdditionalChargeTypeSerializer
    http_method_names = ["get"]


class BillMainViewset(viewsets.ModelViewSet):
    queryset = BillMain.objects.all()
    serializer_class = BillMainSerializer
    http_method_names = ["get"]


class BillDetailViewset(viewsets.ModelViewSet):
    queryset = BillDetail.objects.all()
    serializer_class = BillDetailSerializer
    http_method_names = ["get"]


class SaveBillViewset(viewsets.ModelViewSet):
    queryset = BillMain.objects.all()
    serializer_class = SaveBillSerializer
    http_method_names = ["post"]

    def get_order(self, pk):
        try:
            return OrderMain.objects.get(pk=pk)
        except OrderMain.DoesNotExist:
            return False

    def get_table(self, pk):
        try:
            return Table.objects.get(pk=pk)
        except Table.DoesNotExist:
            return False

    @transaction.atomic
    def create(self, request):

        bill_count = BillMain.objects.count() + 1
        unique_bill = "B-" + "{0:0=5d}".format(bill_count)
        request.data["bill_no"] = unique_bill
        order = request.data.pop("order")
        order_obj = self.get_order(order)
        request.data["order"] = order_obj.id
        if not order_obj:
            return Response("Order doesnot exist", status=status.HTTP_400_BAD_REQUEST)

        if order_obj.status == 2 or order_obj.status == 3:
            return Response(
                "Order is either billed or cancelled",
                status=status.HTTP_400_BAD_REQUEST,
            )
        table = order_obj.table
        table_obj = self.get_table(table.id)

        if not table_obj:
            return Response("Table does not exist", status=status.HTTP_400_BAD_REQUEST)

        if table_obj.status == 1 or table_obj.status == 3:
            return Response(
                "Table is either vacant or reserved ",
                status=status.HTTP_400_BAD_REQUEST,
            )
        table_serializer = TableSerializer(table_obj, data={"status": 1}, partial=True)
        bill_serializer = SaveBillSerializer(
            data=request.data, context={"request": request}
        )
        if table_serializer.is_valid():
            if bill_serializer.is_valid():
                bill_serializer.save()
                table_serializer.save()
                return Response(bill_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    bill_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(table_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillListViewset(viewsets.ModelViewSet):
    queryset = BillMain.objects.all()
    serializer_class = BillListSerializer
    http_method_names = ["get"]
