from rest_framework.routers import DefaultRouter

from provider.views import (
    ManufacturerViewSet,
    CarPriceViewSet,
    ProviderViewSet,
    CarViewSet,
)

router = DefaultRouter()
router.register("cars", CarViewSet)
router.register("car-price", CarPriceViewSet)
router.register("manufacturer", ManufacturerViewSet)
router.register("provider", ProviderViewSet)

urlpatterns = router.urls
