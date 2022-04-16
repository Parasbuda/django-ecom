from rest_framework import routers
from .views import AdditionalChargeViewset

router = routers.DefaultRouter(trailing_slash=True)

router.register("additional-charge", AdditionalChargeViewset)

urlpatterns = [] + router.urls
