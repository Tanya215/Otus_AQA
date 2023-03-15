import pytest
from src.Circle import Circle
from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.fixture(scope='module')
def create_figure():
    figure_1 = Figure()
    yield figure_1


@pytest.fixture(scope='module')
def create_triangle():
    triangle_1 = Triangle('Triangle 1', 3, 4, 5)
    yield triangle_1


@pytest.fixture(scope='module')
def create_not_triangle():
    triangle_2 = Triangle('Triangle 2', 3, 4, 10)
    yield triangle_2


@pytest.fixture(scope='module')
def create_rectangle():
    rectangle_1 = Rectangle('Rec 1', 3, 4)
    yield rectangle_1


@pytest.fixture(scope='module')
def create_square():
    square_1 = Square('Square 1', 3)
    yield square_1


@pytest.fixture(scope='module')
def create_circle():
    circle_1 = Circle('Circle 1', 3)
    yield circle_1
