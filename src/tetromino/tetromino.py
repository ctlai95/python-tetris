from enum import Enum

from src import config
from src.point.point import Point
from src.square.square import Square
from src.utils.tuples import tuples


class State(Enum):
    """State is used to keep track of the current Tetromino's rotation state"""
    ZERO = 0  # Initial spawn state
    ONE = 1  # 1 clockwise or 3 counter-clockwise rotations from spawn state
    TWO = 2  # 2 rotations in either direction from spawn state
    THREE = 3  # 3 clockwise or 1 counter-clockwise rotations from spawn state

    def next(self):
        v = (self.value + 1) % 4
        return State(v)

    def prev(self):
        v = (self.value - 1) % 4
        return State(v)


class Tetromino:
    """A tetromino is a piece which consists of exactly 4 squares"""

    def __init__(self, name, location, color):
        self.name = name
        self.loc = location  # of the bottomleft-most piece
        self.sqrs = self.populate_sqrs()
        self.state = State.ZERO
        self.color = color

    def populate_sqrs(self):
        """Returns the 4 squares as a list, according to name"""
        sqrs = []
        for i in range(4):
            sqrs.append(
                Square(Point(tuples.add(self.loc._xy(),
                                        config.LAYOUTS[self.name][i]))))
        return sqrs

    def offset(self, x, y):
        self.loc = Point(tuples.add(self.loc._xy(), (x, y)))
        for s in self.sqrs:
            s.offset(x, y)

    def rotate_cw(self):
        """Rotates the tetromino by 90 degrees, clockwise"""

        # the point of rotation, relative to the board origin
        abs_rotation_pt = tuples.add(
            self.loc._xy(), config.ROTATION_POINTS[self.name])
        for i in range(len(self.sqrs)):
            # the square's position relative to the point of rotation
            current_square = tuples.subtract(
                self.sqrs[i].tuple(), abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            btm_right = tuples.add(
                current_square, (1, 0))
            # x -> y and y -> -x for rotation about the origin
            new_point = tuples.add(
                (btm_right[1], -btm_right[0]), abs_rotation_pt)
            # replace the old square with the new square
            self.sqrs[i] = Square(
                Point((int(new_point[0]), int(new_point[1]))))
        self.state = self.state.next()

    def rotate_ccw(self):
        """Rotates the tetromino by 90 degrees, counter-clockwise"""

        # the point of rotation, relative to the board origin
        abs_rotation_pt = tuples.add(
            self.loc._xy(), config.ROTATION_POINTS[self.name])
        for i in range(len(self.sqrs)):
            # the square's position relative to the point of rotation
            current_square = tuples.subtract(
                self.sqrs[i].tuple(), abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            top_left = tuples.add(
                current_square, (0, 1))
            # x -> y and y -> -x for rotation about the origin
            new_point = tuples.add(
                (-top_left[1], top_left[0]), abs_rotation_pt)

            # replace the old square with the new square
            self.sqrs[i] = Square(
                Point((int(new_point[0]), int(new_point[1]))))
        self.state = self.state.prev()

    def render_tetromino(self):
        """Renders the tetromino to the screen"""
        for s in self.sqrs:
            s.render_square(self.color)
