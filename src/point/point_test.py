from src.point.point import Point


def test_init():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p.x == i
            assert p.y == j


def test_x_value():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p.x_value() == i


def test_y():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p.y_value() == j


def test_xy():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p.xy_tuple() == (i, j)
