from rest_framework import serializers

from provider.serializers import CarReadSerializer, ProviderCreateSerializer
from user.serializers import UserSerializer

from showroom.models import (
    ShowroomPurchaseHistory,
    ShowroomSaleHistory,
    AvailableCars,
    Showroom,
    Location,
)


class AvailableCarsSerializer(serializers.ModelSerializer):
    car = CarReadSerializer(read_only=True)

    class Meta:
        model = AvailableCars


class ShowroomReadSerializer(serializers.ModelSerializer):
    cars = AvailableCarsSerializer(read_only=True, many=True)

    class Meta:
        model = Showroom
        fields = '__all__'


class ShowroomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = '__all__'


class ShowroomPurchaseHistorySerializer(serializers.ModelSerializer):
    showroom = ShowroomCreateSerializer(read_only=True)
    provider = ProviderCreateSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta:
        model = ShowroomPurchaseHistory
        fields = '__all__'


class ShowroomSaleHistorySerializer(serializers.ModelSerializer):
    showroom = ShowroomCreateSerializer(read_only=True)
    customer = UserSerializer(read_only=True)
    car = CarReadSerializer(read_only=True)

    class Meta:
        model = ShowroomSaleHistory
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
