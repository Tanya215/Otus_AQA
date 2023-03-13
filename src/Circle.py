import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def add_area(self, figure) -> float:
        if isinstance(figure, Figure):
            return Circle.area(self) + figure.area()
        else:
            raise ValueError("It's not figure")
