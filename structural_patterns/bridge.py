from abc import ABC, abstractmethod


class AbstractColor(ABC):
    @abstractmethod
    def paint_with_color(self) -> str:
        """"""


class AbstractShape(ABC):
    @abstractmethod
    def draw_shape(self) -> str:
        """"""

    @abstractmethod
    def paint_shape(self) -> str:
        """"""


class Color(AbstractColor):
    def __init__(self, color: str) -> None:
        self.color = color

    def paint_with_color(self) -> str:
        return f"Painted with color {self.color}!"


class Shape(AbstractShape):
    def __init__(self, shape: str, color: AbstractColor) -> None:
        self.color = color
        self.shape = shape

    def draw_shape(self):
        return f"Shape {self.shape} is drawn!"

    def paint_shape(self):
        return self.color.paint_with_color()


if __name__ == "__main__":
    red = Color(color="red")
    square = Shape(color=red, shape="square")
    print(square.draw_shape())
    print(square.paint_shape())
