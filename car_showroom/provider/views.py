from rest_framework import viewsets

from provider.models import Car, CarPrice, Manufacturer, Provider
from user.mixins import SoftDeleteMixin, SerializerChooseMixin
from user.permissions import IsProvider

from provider.serializers import (
    CarReadSerializer,
    CarCreateSerializer,
    CarPriceSerializer,
    ManufacturerSerializer,
    ProviderReadSerializer,
    ProviderCreateSerializer,
)


class CarViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet
):
    queryset = Car.objects.all()
    default_serializer_class = CarReadSerializer
    allow_serializer_class = {
        "retrieve": CarReadSerializer,
        "update": CarCreateSerializer,
        "create": CarCreateSerializer,
        "list": CarReadSerializer,
    }


class CarPriceViewSet(
    SoftDeleteMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = CarPriceSerializer
    queryset = CarPrice.objects.all()


class ManufacturerViewSet(
    SoftDeleteMixin,
    viewsets.ModelViewSet,
):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ProviderViewSet(
    SoftDeleteMixin,
    SerializerChooseMixin,
    viewsets.ModelViewSet,
):
    permission_classes = (IsProvider,)
    queryset = Provider.objects.all()
    read_only_serializer = ProviderReadSerializer
    write_serializer = ProviderCreateSerializer

    default_serializer_class = ProviderReadSerializer
    allow_serializer_class = {
        "retrieve": ProviderReadSerializer,
        "update": ProviderCreateSerializer,
        "create": ProviderCreateSerializer,
        "list": ProviderReadSerializer,
    }
