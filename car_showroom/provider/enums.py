from user.enums import BaseEnum


class Carcase(BaseEnum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    COUPE = "coupe"
    CABRIOLET = "cabriolet"
    LIMOUSINE = "limousine"
    JEEP = "JEEP"


class State(BaseEnum):
    NEW = "new"
    WITH_MILEAGE = "with mileage"
    BROKEN = "broken"
    TOTAL = "total"


class Engine(BaseEnum):
    PETROL_ENGINE = "petrol engine"
    DIESEL_ENGINE = "diesel engine"
    GAS_ENGINE = "gas engine"
    ELECTRIC_ENGINE = "electric engine"
