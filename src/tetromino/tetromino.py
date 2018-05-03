import logging

from src.point.point import Point
from src.square.square import Square
from src.tetromino.constants import LAYOUTS, ROTATION_POINTS, SPAWN
from src.tetromino.state import State

log = logging.getLogger(__name__)


class Tetromino:
    """A tetromino is a piece which consists of exactly four squares."""

    def __init__(self, id, origin, color):
        """
        Initialize a Tetromino object.

        Args:
            id (string): The identifier of the tetromino (O, I, J, L, S, Z, T)
            origin (Point): The position of the bottom left point used as a reference for the "LAYOUTS" values
            color (list): The color of the tetromino in [R, G, B] format
        """
        log.info("Initializing Tetromino (id={}, origin=[{}][{}], color={})".format(
            id, origin.x, origin.y, color))
        self.id = id
        self.origin = origin
        self.squares = self.get_squares()
        self.state = State.ZERO
        self.color = color

    def get_squares(self):
        """
        Get the four squares that make up the tetromino.

        Returns:
            sqrs ([]Square): the four squares as a list.

        """
        squares = []
        for i in range(4):
            square_position = self.origin.add(
                Point(LAYOUTS[self.id][i][0], LAYOUTS[self.id][i][1]))
            squares.append(Square(square_position))
        return squares

    def offset(self, x, y):
        """
        Move the tetromino by the given horizontal and vertical values.

        Args:
            x (int): The number of horizontal units to move (pos = right, neg = left).
            y (int): The number of vertical units to move (pos = up, neg = down).
        """
        self.origin = self.origin.add(Point(x, y))
        for square in self.squares:
            square.offset(x, y)

    def rotate_cw(self):
        """Rotate the tetromino by 90 degrees, clockwise."""
        # the point of rotation, relative to the board origin
        abs_rotation_pt = self.origin.add(
            Point(ROTATION_POINTS[self.id][0], ROTATION_POINTS[self.id][1]))
        for i in range(len(self.squares)):
            # the square's position relative to the point of rotation
            current_square = Point(
                self.squares[i].x, self.squares[i].y).subtract(abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            btm_right = current_square.add(Point(1, 0))
            # x -> y and y -> -x for rotation about the origin
            new_point = Point(btm_right.y, -btm_right.x).add(abs_rotation_pt)
            # replace the old square with the new square
            self.squares[i] = Square(Point(int(new_point.x), int(new_point.y)))
        self.state = self.state.next()

    def rotate_ccw(self):
        """Rotate the tetromino by 90 degrees, counterclockwise."""
        # the point of rotation, relative to the board origin
        abs_rotation_pt = self.origin.add(
            Point(ROTATION_POINTS[self.id][0], ROTATION_POINTS[self.id][1]))
        for i in range(len(self.squares)):
            # the square's position relative to the point of rotation
            current_square = Point(
                self.squares[i].x, self.squares[i].y).subtract(abs_rotation_pt)
            # the square's bottom right point, which will be the new
            # square origin after the rotation
            top_left = current_square.add(Point(0, 1))
            # x -> y and y -> -x for rotation about the origin
            new_point = Point(-top_left.y, top_left.x).add(abs_rotation_pt)
            # replace the old square with the new square
            self.squares[i] = Square(Point(int(new_point.x), int(new_point.y)))
        self.state = self.state.prev()

    def reset_position(self):
        """Reset the tetromino to its original spawn position"""
        self.origin = Point(SPAWN[self.id][0], SPAWN[self.id][1])
        self.squares = self.get_squares()

    def render_tetromino(self):
        """Render the tetromino to the screen."""
        for square in self.squares:
            square.render_square(self.color)
