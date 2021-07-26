from rest_framework.routers import DefaultRouter

from showroom.views import (
    ShowroomPurchaseHistoryViewSet,
    ShowroomSaleHistoryViewSet,
    AvailableCarsViewSet,
    ShowroomViewSet,
    LocationViewSet,
)

router = DefaultRouter()
router.register("sale-history", ShowroomSaleHistoryViewSet)
router.register("available-cars", AvailableCarsViewSet)
router.register("buy-history", ShowroomPurchaseHistoryViewSet)
router.register("location", LocationViewSet)
router.register("", ShowroomViewSet)

urlpatterns = router.urls
