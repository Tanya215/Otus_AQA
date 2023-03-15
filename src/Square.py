from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, name, edge):
        super().__init__(name, edge_1=edge, edge_2=edge)

