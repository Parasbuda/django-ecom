from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TableSerializer, BlockSerializer
from .models import Table, Block

# Create your views here.


class BlockViewset(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer


class TableViewset(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
