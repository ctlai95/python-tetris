from src.square.square import Square
from src.point.point import Point


def test_tuple():
    s = Square(Point((5, 5)))
    assert s.tuple() == (5, 5)


def test_offset():
    s = Square(Point((9, 4)))
    s.offset(-1, 3)
    assert s.tuple() == (8, 7)
