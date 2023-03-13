import math


def test_triangle_add_area_triangle(create_triangle):
    assert create_triangle.add_area(create_triangle) == 12


def test_triangle_add_area_rectangle(create_triangle, create_rectangle):
    assert create_triangle.add_area(create_rectangle) == 18


def test_triangle_add_area_square(create_triangle, create_square):
    assert create_triangle.add_area(create_square) == 15


def test_triangle_add_area_circle(create_triangle, create_circle):
    assert create_triangle.add_area(create_circle) == 6 + 9 * math.pi


def test_rectangle_add_area_triangle(create_rectangle, create_triangle):
    assert create_rectangle.add_area(create_triangle) == 18


def test_rectangle_add_area_rectangle(create_rectangle):
    assert create_rectangle.add_area(create_rectangle) == 24


def test_rectangle_add_area_square(create_rectangle, create_square):
    assert create_rectangle.add_area(create_square) == 21


def test_rectangle_add_area_circle(create_rectangle, create_circle):
    assert create_rectangle.add_area(create_circle) == 12 + 9 * math.pi


def test_square_add_area_triangle(create_square, create_triangle):
    assert create_square.add_area(create_triangle) == 15


def test_square_add_area_rectangle(create_square, create_rectangle):
    assert create_square.add_area(create_rectangle) == 21


def test_square_add_area_square(create_square):
    assert create_square.add_area(create_square) == 18


def test_square_add_area_circle(create_square, create_circle):
    assert create_square.add_area(create_circle) == 9 + 9 * math.pi


def test_circle_add_area_triangle(create_circle, create_triangle):
    assert create_circle.add_area(create_triangle) == 6 + 9 * math.pi


def test_circle_add_area_rectangle(create_circle, create_rectangle):
    assert create_circle.add_area(create_rectangle) == 12 + 9 * math.pi


def test_circle_add_area_square(create_circle, create_square):
    assert create_circle.add_area(create_square) == 9 + 9 * math.pi


def test_circle_add_area_circle(create_circle):
    assert create_circle.add_area(create_circle) == 18 * math.pi
