from django import http
from rest_framework import viewsets
from item.models import Item, PackingType, PackingTypeDetail, SubCategory, Category
from .serializers import (
    SubCategorySerializer,
    CategorySerializer,
    ItemSerializer,
    PackingTypeSerializer,
    PackingTypeDetailSerializer,
    PackingTypeDetailListSerializer,
)
from rest_framework.response import Response


class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    http_method_names = ["get", "post"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ["get", "post"]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    http_method_names = ["get", "post"]


class PackingTypeViewset(viewsets.ModelViewSet):
    queryset = PackingType.objects.all()
    serializer_class = PackingTypeSerializer
    http_method_name = ["get", "post"]


class PackingTypeDetailViewset(viewsets.ModelViewSet):
    queryset = PackingTypeDetail.objects.all()
    serializer_class = PackingTypeDetailSerializer
    http_method_names = ["get", "post"]

    def list(self, request):
        queryset = PackingTypeDetail.objects.all()
        serializer = PackingTypeDetailListSerializer(queryset, many=True)
        return Response(serializer.data)
