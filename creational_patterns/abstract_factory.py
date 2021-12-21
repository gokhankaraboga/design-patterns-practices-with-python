from abc import ABC, abstractmethod
from typing import Any


class Shape(ABC):
    @abstractmethod
    def draw_shape(self) -> str:
        pass


class Color(ABC):
    @abstractmethod
    def fill_color(self) -> str:
        pass


class Triangle(Shape):
    def draw_shape(self) -> str:
        return "Trinagle was drawn!"


class Square(Shape):
    def draw_shape(self) -> str:
        return "Square was drawn!"


class Red(Color):
    def fill_color(self) -> str:
        return "Filled with Red!"


class Yellow(Color):
    def fill_color(self) -> str:
        return "Filled with Yellow!"


class AbstractFactory(ABC):
    @abstractmethod
    def get_factory(self):
        pass


color_map = {"red": Red, "yellow": Yellow}
shape_map = {"triangle": Triangle, "square": Square}


class ShapeFactory:
    def __init__(self, shape_type: str) -> None:
        self.shape_type = shape_type

    def get_shape(self) -> Shape:
        return shape_map[self.shape_type]()


class ColorFactory:
    def __init__(self, color_type: str) -> None:
        self.color_type = color_type

    def get_color(self) -> Color:
        return color_map[self.color_type]()


class WholeDesignFactory(AbstractFactory):
    def __init__(self, material_typ: str) -> None:
        self.material_typ = material_typ

    def get_factory(self) -> Any:
        if self.material_typ == "shape":
            return ShapeFactory
        elif self.material_typ == "color":
            return ColorFactory


if __name__ == "__main__":
    while True:
        material_type = input("Which one do you want ? shape or color:")
        factory_cls = WholeDesignFactory(
            material_typ=material_type).get_factory()

        if material_type == "color":
            color = input("Which color do you want? red or yellow:")
            print(factory_cls(color).get_color().fill_color())
        elif material_type == "shape":
            shape = input("Which shape do you want? triangle or square:")
            print(factory_cls(shape).get_shape().draw_shape())
