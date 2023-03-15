from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_figure_creation(create_figure):
    assert isinstance(create_figure, Figure)


def test_triangle_creation(create_triangle):
    assert isinstance(create_triangle, Triangle)
    assert create_triangle.name == 'Triangle 1'


def test_rectangle_creation(create_rectangle):
    assert isinstance(create_rectangle, Rectangle)
    assert create_rectangle.name == 'Rec 1'


def test_square_creation(create_square):
    assert isinstance(create_square, Square)
    assert create_square.name == 'Square 1'


def test_circle_creation(create_circle):
    assert isinstance(create_circle, Circle)
    assert create_circle.name == 'Circle 1'
