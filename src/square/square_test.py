from src.point.point import Point
from src.square.square import Square
from src.colors import colors


def test_init():
    for i in range(10):
        for j in range(22):
            s = Square(Point(i, j), colors.ASH)
            assert s.x == i
            assert s.y == j


def test_tuple():
    for i in range(10):
        for j in range(22):
            s = Square(Point(i, j), colors.ASH)
            assert s.tuple() == (i, j)


def test_offset():
    offsets = [
        (1, 0),  # right
        (-1, 0),  # left
        (0, 1),  # up
        (0, -1),  # down
    ]
    for offset in offsets:
        for i in range(10):
            for j in range(22):
                s = Square(Point(i, j), colors.ASH)
                s.offset(offset[0], offset[1])
                assert s.x == i + offset[0]
                assert s.y == j + offset[1]
