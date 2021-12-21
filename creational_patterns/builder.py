from abc import ABC, abstractmethod


class AbstractBuilder(ABC):
    @abstractmethod
    def manufacture_first_phase(self) -> None:
        pass

    @abstractmethod
    def add_some_necessary_infrastructure(self) -> None:
        pass

    @abstractmethod
    def make_it_luxurious(self) -> None:
        pass


class House:
    house_parts = list()

    def add_parts(self, items) -> None:
        self.house_parts.extend(items)

    def get_house_building_process(self) -> str:
        return f"House was build so far with the parts " \
               f"{self.house_parts}."


class HouseBuilder(AbstractBuilder):
    # highly coupled structure, composition
    house = House()

    def manufacture_first_phase(self) -> None:
        self.house.add_parts(["Walls", "Roof", "Windows"])

    def add_some_necessary_infrastructure(self) -> None:
        self.house.add_parts(["Sink", "Toilets", "Electricity"])

    def make_it_luxurious(self) -> None:
        self.house.add_parts(["Fireplace", "Internet Infra.", "Cable Tv"])


class HouseConstructor:
    def __init__(self, buildr: AbstractBuilder) -> None:
        self.builder = buildr

    def build_empty_house(self) -> None:
        self.builder.manufacture_first_phase()

    def build_house_completely(self) -> None:
        self.builder.manufacture_first_phase()
        self.builder.add_some_necessary_infrastructure()
        self.builder.make_it_luxurious()


if __name__ == "__main__":
    # builder can be obtained with factory pattern here, just to note !
    builder = HouseBuilder()
    director = HouseConstructor(buildr=builder)
    director.build_empty_house()
    print(builder.house.get_house_building_process())

    director.build_house_completely()
    print(builder.house.get_house_building_process())
