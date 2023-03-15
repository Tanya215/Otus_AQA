import math


def test_triangle_perimeter(create_triangle):
    assert create_triangle.perimeter() == 12


def test_rectangle_perimeter(create_rectangle):
    assert create_rectangle.perimeter() == 14


def test_square_perimeter(create_square):
    assert create_square.perimeter() == 12


def test_circle_perimeter(create_circle):
    assert create_circle.perimeter() == 6 * math.pi
