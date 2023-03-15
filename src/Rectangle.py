from math import sqrt

from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, name, edge_1, edge_2):
        self.name = name
        self.edge_1 = edge_1
        self.edge_2 = edge_2

    def perimeter(self) -> int:
        return 2 * (self.edge_1 + self.edge_2)

    def area(self) -> int:
        return self.edge_1 * self.edge_2
