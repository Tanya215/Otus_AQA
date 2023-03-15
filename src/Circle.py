import math

from src.Figure import Figure


class Circle(Figure):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.name = name

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * self.radius**2
