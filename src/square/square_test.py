from src.point.point import Point
from src.square.square import Square
from src.utils.tuples import tuples


def test_init():
    for i in range(10):
        for j in range(22):
            s = Square(Point(i, j))
            assert s.x == i
            assert s.y == j


def test_tuple():
    for i in range(10):
        for j in range(22):
            s = Square(Point(i, j))
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
                s = Square(Point(i, j))
                s.offset(offset[0], offset[1])
                assert s.tuple() == tuples.add((i, j), offset)
