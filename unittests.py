import collections
import unittest

import point
import square
import tetromino
import utils


class TestUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(utils.tuple_add((1, -2), (-3, 4)), (-2, 2))

    def test_subtract(self):
        self.assertEqual(utils.tuple_subtract((-5, 6), (7, -8)), (-12, 14))


class TestPoint(unittest.TestCase):
    def test_x(self):
        p = point.Point((1, 0))
        self.assertEqual(p._x(), 1)

    def test_y(self):
        p = point.Point((0, -2))
        self.assertEqual(p._y(), -2)

    def test_xy(self):
        p = point.Point((-3, 4))
        self.assertEqual(p._xy(), (-3, 4))


class TestSquare(unittest.TestCase):
    def test_tuple(self):
        s = square.Square(point.Point((5, 5)))
        self.assertEqual(s.tuple(), (5, 5))

    def test_offset(self):
        s = square.Square(point.Point((9, 4)))
        s.offset(-1, 3)
        self.assertEqual(s.tuple(), (8, 7))


if __name__ == '__main__':
    unittest.main()
