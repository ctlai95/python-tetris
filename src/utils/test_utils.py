import utils


def test_add():
    assert utils.tuple_add((1, -2), (-3, 4)) == (-2, 2)


def test_subtract():
    assert utils.tuple_subtract((-5, 6), (7, -8)) == (-12, 14)
