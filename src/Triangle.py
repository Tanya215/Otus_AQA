from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, edge_1, edge_2, edge_3):
        self.name = name
        self.edge_1 = edge_1
        self.edge_2 = edge_2
        self.edge_3 = edge_3
        if not Triangle.is_triangle_exist:
            raise ValueError("Impossible to create a triangle")

    def perimeter(self) -> int:
        return self.edge_1 + self.edge_2 + self.edge_3

    def area(self) -> float:
        half_perimeter = self.perimeter() / 2
        area_calc: float = sqrt(half_perimeter * (half_perimeter - self.edge_1) * (half_perimeter - self.edge_2) * (
                half_perimeter - self.edge_3))
        return area_calc

    @property
    def is_triangle_exist(self):
        return (self.edge_1 < self.edge_2 + self.edge_3) and (self.edge_1 + self.edge_3 > self.edge_2) and (
                    self.edge_3 < self.edge_2 + self.edge_1)
