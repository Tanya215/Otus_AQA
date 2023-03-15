class Figure:
    def add_area(self, figure) -> float:
        if isinstance(figure, Figure):
            return self.area() + figure.area()
        else:
            raise ValueError("It's not figure")
