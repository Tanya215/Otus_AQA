from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_figure_creation(create_figure):
    if isinstance(create_figure, Figure) is True:
        pass


def test_triangle_creation(create_triangle):
    if isinstance(create_triangle, Triangle) is True:
        pass


def test_rectangle_creation(create_rectangle):
    if isinstance(create_rectangle, Rectangle) is True:
        pass


def test_square_creation(create_square):
    if isinstance(create_square, Square) is True:
        pass


def test_circle_creation(create_circle):
    if isinstance(create_circle, Circle) is True:
        pass
