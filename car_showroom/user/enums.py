from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(value.name, value.value) for value in cls]


class Gender(BaseEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Role(BaseEnum):
    CUSTOMER = "customer"
    CAR_SHOWROOM = "car_showroom"
    PROVIDER = "provider"
