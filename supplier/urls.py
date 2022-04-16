from rest_framework import routers
from .views import SupplierViewset

router = routers.DefaultRouter(trailing_slash=False)

router.register("supplier", SupplierViewset)

urlpatterns = [] + router.urls
