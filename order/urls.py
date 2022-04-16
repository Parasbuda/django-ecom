from rest_framework import routers
from .views import (
    OrderMainViewset,
    OrderDetailViewset,
    OrderSaveViewset,
    OrderListViewset,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register("order-main", OrderMainViewset, basename="order-main")
router.register("order-detail", OrderDetailViewset)
router.register("save-order", OrderSaveViewset)
router.register("order-list", OrderListViewset, basename="Order List")
urlpatterns = [] + router.urls
