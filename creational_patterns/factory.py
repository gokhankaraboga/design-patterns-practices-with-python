"""
# We want do define classes for the Toyota vehicle factory.
# The factory assembles different types of vehicles.
# You may have many models of cars made by Toyota.
# Vehicles have various components.
# Some components are commonly re-used in multiple car models.
# For example, the  Camry and Corolla cars use the same engine, but the Prius uses a different one.
# Please represent this relationship with code so we can make lots of cars.

different types of vehicles
different models of cars
different components in a vehicle


# We want do define classes for the Toyota vehicle factory.
# The factory assembles different types of vehicles.
# You may have many models of cars made by Toyota.
# Vehicles have various components.
# Some components are commonly re-used in multiple car models.
# For example, the  Camry and Corolla cars use the same engine, but the Prius uses a different one.
# Please represent this relationship with code so we can make lots of cars.

"""

from abc import abstractmethod, ABC


class Engine(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass


class Car(ABC):
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    @abstractmethod
    def start_car(self) -> str:
        pass


class XEngine(Engine):
    name = "Xengine"

    def start_engine(self) -> str:
        return f"{self.name} engine started!"


class YEngine(Engine):
    name = "Yengine"

    def start_engine(self) -> str:
        return f"{self.name} engine started!"


class Corolla(Car):
    name = "Corolla"

    def start_car(self) -> str:
        return self.engine.start_engine() + "\n" + f"{self.name} car started!"


class Cambry(Car):
    name = "Cambry"

    def start_car(self) -> str:
        return self.engine.start_engine() + "\n" + f"{self.name} car started!"


car_map = {
    "corolla": Corolla,
    "cambry": Cambry,
}

engine_map = {
    "xengine": XEngine,
    "yengine": YEngine,
}


class WholeCarExporter:
    def __init__(self, car_typ: str, engine_typ: str) -> None:
        self.car_type = car_typ
        self.engine_type = engine_typ

    def get_engine(self) -> Engine:
        return engine_map[self.engine_type]()

    def get_car(self) -> Car:
        return car_map[self.car_type](engine=self.get_engine())


if __name__ == "__main__":
    while True:
        car_type = input(f"Please enter a car type{list(car_map.keys())}:")
        engine_type = input(
            f"Please enter an engine type{list(engine_map.keys())}:")

        car = WholeCarExporter(car_type, engine_type).get_car()
        print(car.start_car())
