from rest_framework import viewsets

from user.mixins import SoftDeleteMixin, SerializerChooseMixin
from user.permissions import IsShowroom

from showroom.models import (
    ShowroomPurchaseHistory,
    ShowroomSaleHistory,
    AvailableCars,
    Showroom,
    Location,
)

from showroom.serializers import (
    ShowroomPurchaseHistorySerializer,
    ShowroomSaleHistorySerializer,
    ShowroomCreateSerializer,
    AvailableCarsSerializer,
    ShowroomReadSerializer,
    LocationSerializer,
)


class AvailableCarsViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = AvailableCarsSerializer
    queryset = AvailableCars.objects.all()


class ShowroomViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    permission_classes = (IsShowroom,)
    queryset = Showroom.objects.all()
    default_serializer_class = ShowroomReadSerializer
    allow_serializer_class = {
        "retrieve": ShowroomReadSerializer,
        "update": ShowroomCreateSerializer,
        "create": ShowroomCreateSerializer,
        "list": ShowroomReadSerializer,
    }


class ShowroomPurchaseHistoryViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = ShowroomPurchaseHistorySerializer
    queryset = ShowroomPurchaseHistory.objects.all()


class ShowroomSaleHistoryViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet
):
    serializer_class = ShowroomSaleHistorySerializer
    queryset = ShowroomSaleHistory.objects.all()


class LocationViewSet(
    viewsets.ModelViewSet,
):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
