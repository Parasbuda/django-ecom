from django.urls import URLPattern
from rest_framework import routers
from .views import PaymentModeViewset

router = routers.DefaultRouter(trailing_slash=True)
router.register("payment-mode", PaymentModeViewset)

urlpatterns = [] + router.urls
