import point


def test_x():
    p = point.Point((1, 0))
    assert p._x() == 1


def test_y():
    p = point.Point((0, -2))
    assert p._y() == -2


def test_xy():
    p = point.Point((-3, 4))
    assert p._xy() == (-3, 4)
