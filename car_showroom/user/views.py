from rest_framework import viewsets, mixins

from user.mixins import SoftDeleteMixin
from user.models import User
from user.permissions import IsUser
from user.serializers import UserSerializer


class UserViewSet(
    SoftDeleteMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateViewSet(
    SoftDeleteMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    permission_classes = (IsUser,)
    serializer_class = UserSerializer
    queryset = User.objects.all()
