from src.point.point import Point


def test_init():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p.x == i
            assert p.y == j


def test_x():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p._x() == i


def test_y():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p._y() == j


def test_xy():
    for i in range(10):
        for j in range(22):
            p = Point((i, j))
            assert p._xy() == (i, j)
