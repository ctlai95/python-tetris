from src.utils import tuples


def test_add():
    assert tuples.add((1, -2), (-3, 4)) == (-2, 2)


def test_subtract():
    assert tuples.subtract((-5, 6), (7, -8)) == (-12, 14)
