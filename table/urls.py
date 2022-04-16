from rest_framework import routers
from .views import BlockViewset, TableViewset

router = routers.DefaultRouter(trailing_slash=False)
router.register("block", BlockViewset)
router.register("table", TableViewset)

urlpatterns = [] + router.urls
