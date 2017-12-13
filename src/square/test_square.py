import point
import square


def test_tuple():
    s = square.Square(point.Point((5, 5)))
    assert s.tuple() == (5, 5)


def test_offset():
    s = square.Square(point.Point((9, 4)))
    s.offset(-1, 3)
    assert s.tuple() == (8, 7)
