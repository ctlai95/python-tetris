from src.point.point import Point


def test_init():
    for i in range(10):
        for j in range(22):
            p = Point(i, j)
            assert isinstance(p, Point)
            assert p.x == i
            assert p.y == j


def test_equals():
    p1 = Point(1, 2)
    p2 = Point(1, 2)
    assert p1.equals(p2)
    p1 = Point(1, 2)
    p2 = Point(2, 1)
    assert not p1.equals(p2)


def test_add():
    add_point_list = [
        Point(-1, 0),
        Point(+1, 0),
        Point(0, -1),
        Point(0, +1),
    ]
    for i in range(10):
        for j in range(22):
            for add_point in add_point_list:
                point = Point(i, j)
                assert point.add(add_point).equals(
                    Point(i + add_point.x, j + add_point.y))


def test_subtract():
    subtract_point_list = [
        Point(-1, 0),
        Point(+1, 0),
        Point(0, -1),
        Point(0, +1),
    ]
    for i in range(10):
        for j in range(22):
            for subtract_point in subtract_point_list:
                point = Point(i, j)
                assert point.subtract(subtract_point).equals(
                    Point(i - subtract_point.x, j - subtract_point.y))
