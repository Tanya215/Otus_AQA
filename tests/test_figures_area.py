import math


def test_triangle_area(create_triangle):
    assert create_triangle.area() == 6


def test_rectangle_area(create_rectangle):
    assert create_rectangle.area() == 12


def test_square_area(create_square):
    assert create_square.area() == 9


def test_circle_area(create_circle):
    assert create_circle.area() == 9 * math.pi
