from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, UserUpdateViewSet

router = DefaultRouter()
router.register("", UserViewSet)
router.register("update", UserUpdateViewSet)

urlpatterns = router.urls
