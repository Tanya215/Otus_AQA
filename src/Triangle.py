from math import sqrt

from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, name, edge_1, edge_2, edge_3):
        super().__init__(name)
        self.edge_1 = edge_1
        self.edge_2 = edge_2
        self.edge_3 = edge_3
        if not Triangle.is_triangle_exist:
            raise ValueError("Impossible to create a triangle")

    def perimeter(self) -> int:
        return self.edge_1 + self.edge_2 + self.edge_3

    def area(self) -> float:
        half_perimeter = Triangle.perimeter(self) / 2
        area_calc: float = sqrt(half_perimeter * (half_perimeter - self.edge_1) * (half_perimeter - self.edge_2) * (
                half_perimeter - self.edge_3))
        return area_calc

    @property
    def is_triangle_exist(self):
        assert isinstance(self.edge_1, object)
        return (self.edge_1 < self.edge_2 + self.edge_3) and (self.edge_1 + self.edge_3 > self.edge_2) and (
                    self.edge_3 < self.edge_2 + self.edge_1)

    def add_area(self, figure) -> float:
        if isinstance(figure, Figure):
            return Triangle.area(self) + figure.area()
        else:
            raise ValueError("It's not figure")
