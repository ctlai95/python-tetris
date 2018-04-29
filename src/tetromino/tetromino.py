import logging
from enum import Enum

from src.point.point import Point
from src.square.square import Square
from src.tetromino.constants import LAYOUTS, ROTATION_POINTS
from src.utils.tuples import tuples

log = logging.getLogger(__name__)


class State(Enum):
    """State is used to keep track of the current Tetromino's rotation state"""
    ZERO = 0  # Initial spawn state
    ONE = 1  # 1 clockwise or 3 counterclockwise rotations from spawn state
    TWO = 2  # 2 rotations in either direction from spawn state
    THREE = 3  # 3 clockwise or 1 counterclockwise rotations from spawn state

    def next(self):
        v = (self.value + 1) % 4
        return State(v)

    def prev(self):
        v = (self.value - 1) % 4
        return State(v)


class Tetromino:
    """A tetromino is a piece which consists of exactly 4 squares"""

    def __init__(self, id, origin, color):
        """
        Initializes a Tetromino object
        Arguments:
            id (string): the identifier of the tetromino (O, I, J, L, S, Z, T)
            origin (Point): the position of the bottom left point used as a reference for the "LAYOUTS" values
            color (list): the color of the tetromino in [R, G, B] format
        """
        log.info("Initializing Tetromino (id={}, origin={}, color={})".format(
            id, origin.xy_tuple(), color))
        self.id = id
        self.origin = origin
        self.color = color
        self.sqrs = self.populate_sqrs()
        self.state = State.ZERO

    def populate_sqrs(self):
        """Returns the 4 squares as a list, according to id"""
        sqrs = []
        for i in range(4):
            point = Point(tuples.add(self.origin.xy_tuple(), LAYOUTS[self.id][i]))
            sqrs.append(Square(point, self.color))
        return sqrs

    def offset(self, x, y):
        self.origin = Point(tuples.add(
            self.origin.xy_tuple(), (x, y)))
        for s in self.sqrs:
            s.offset(x, y)

    def rotate_cw(self):
        """Rotates the tetromino by 90 degrees, clockwise"""

        # the point of rotation, relative to the board origin
        abs_rotation_pt = tuples.add(
            self.origin.xy_tuple(), ROTATION_POINTS[self.id])
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
            point = Point((int(new_point[0]), int(new_point[1])))
            self.sqrs[i] = Square(point, self.color)
        self.state = self.state.next()

    def rotate_ccw(self):
        """Rotates the tetromino by 90 degrees, counterclockwise"""

        # the point of rotation, relative to the board origin
        abs_rotation_pt = tuples.add(
            self.origin.xy_tuple(), ROTATION_POINTS[self.id])
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
            point = Point((int(new_point[0]), int(new_point[1])))
            self.sqrs[i] = Square(point, self.color)
        self.state = self.state.prev()

    def render_tetromino(self):
        """Renders the tetromino to the screen"""
        for s in self.sqrs:
            s.render_square()
