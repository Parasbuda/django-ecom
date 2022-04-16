

from django.urls import path

from item.models import PackingType
from .views import SubcategoryViewSet, CategoryViewSet,ItemViewSet,PackingTypeViewset,PackingTypeDetailViewset
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

router.register('subcategory', SubcategoryViewSet )

router.register('Category', CategoryViewSet)
router.register('item', ItemViewSet )
router.register("PackingType",PackingTypeViewset)
router.register("PackingTypeDetail",PackingTypeDetailViewset)
urlpatterns = [
    # path('api/',views.BoardViewSet),
    

]+router.urls