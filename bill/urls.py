from rest_framework import routers
from .views import (
    AdditionalChargeTypeViewset,
    BillListViewset,
    BillMainViewset,
    BillDetailViewset,
    PaymentDetailViewset,
    SaveBillViewset,
)

router = routers.DefaultRouter(trailing_slash=False)

router.register("bill-main", BillMainViewset, basename="Bill Main")
router.register("bill-detail", BillDetailViewset)
router.register("save-bill", SaveBillViewset)
router.register("bill-list", BillListViewset, basename="Bill List")
router.register("payment-detail", PaymentDetailViewset)
router.register("additional-charge-type",AdditionalChargeTypeViewset)

urlpatterns = [] + router.urls
